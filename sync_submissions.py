import requests
import sys
import os
import re
import time
from pathlib import Path

# ── 配置 ──────────────────────────────────────────────────────────────────────
SYNC_FOLDER = "action-sync"

LEETCODE_SESSION   = os.environ.get("LEETCODE_SESSION", "")
LEETCODE_CSRF_TOKEN = os.environ.get("LEETCODE_CSRF_TOKEN", "")

LANG_EXT = {
    "python":     "py",
    "python3":    "py",
    "java":       "java",
    "cpp":        "cpp",
    "c":          "c",
    "javascript": "js",
    "typescript": "ts",
    "go":         "go",
    "rust":       "rs",
    "kotlin":     "kt",
    "swift":      "swift",
    "scala":      "scala",
    "ruby":       "rb",
    "mysql":      "sql",
    "mssql":      "sql",
    "oraclesql":  "sql",
    "bash":       "sh",
}

# ── HTTP 会话 ─────────────────────────────────────────────────────────────────
def make_session():
    s = requests.Session()
    s.headers.update({
        "User-Agent":   "Mozilla/5.0",
        "Content-Type": "application/json",
        "Referer":      "https://leetcode.com",
        "Origin":       "https://leetcode.com",
        "x-csrftoken":  LEETCODE_CSRF_TOKEN,
    })
    s.cookies.set("LEETCODE_SESSION",  LEETCODE_SESSION,   domain="leetcode.com")
    s.cookies.set("csrftoken",         LEETCODE_CSRF_TOKEN, domain="leetcode.com")
    return s


# ── 拉取 submissions（分页） ──────────────────────────────────────────────────
SUBMISSION_LIST_QUERY = """
query submissionList($offset: Int!, $limit: Int!, $lastKey: String) {
  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey) {
    lastKey
    hasNext
    submissions {
      id
      titleSlug
      title
      lang
      statusDisplay
      timestamp
      code
    }
  }
}
"""

def fetch_all_accepted(session):
    """返回 {titleSlug: submission_dict} 每题只保留最新 AC"""
    url     = "https://leetcode.com/graphql"
    best    = {}          # titleSlug -> submission
    last_key = None
    offset   = 0
    limit    = 20

    while True:
        variables = {"offset": offset, "limit": limit, "lastKey": last_key}
        try:
            resp = session.post(url, json={"query": SUBMISSION_LIST_QUERY,
                                           "variables": variables}, timeout=20)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            print(f"❌ 请求失败: {e}")
            sys.exit(1)

        if data.get("errors"):
            print(f"❌ GraphQL 错误: {data['errors']}")
            sys.exit(1)

        sl = data["data"]["submissionList"]
        submissions = sl.get("submissions") or []

        for sub in submissions:
            if sub["statusDisplay"] != "Accepted":
                continue
            slug = sub["titleSlug"]
            # 只保留 timestamp 最大（最新）的一条
            if slug not in best or int(sub["timestamp"]) > int(best[slug]["timestamp"]):
                best[slug] = sub

        if not sl.get("hasNext"):
            break

        last_key = sl.get("lastKey")
        offset  += limit
        time.sleep(0.3)   # 避免频率过高

    print(f"✅ 共获取到 {len(best)} 道已 AC 题目")
    return best


# ── 拉取题目元数据（题号） ────────────────────────────────────────────────────
QUESTION_META_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    titleSlug
    difficulty
  }
}
"""

def fetch_question_meta(session, title_slug):
    url = "https://leetcode.com/graphql"
    try:
        resp = session.post(url, json={"query": QUESTION_META_QUERY,
                                       "variables": {"titleSlug": title_slug}}, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        return data["data"]["question"]
    except Exception as e:
        print(f"  ⚠️  获取题目元数据失败 ({title_slug}): {e}")
        return None


# ── 文件名工具 ────────────────────────────────────────────────────────────────
def slug_to_folder_name(frontend_id, title_slug):
    """e.g. 0001-two-sum"""
    num = str(frontend_id).zfill(4)
    return f"{num}-{title_slug}"


def get_existing_slugs(sync_folder):
    """返回已同步的 titleSlug 集合（从文件夹名解析）"""
    folder = Path(sync_folder)
    if not folder.exists():
        return set()
    existing = set()
    for item in folder.iterdir():
        if item.is_dir():
            # 格式: 0001-two-sum  → two-sum
            parts = item.name.split("-", 1)
            if len(parts) == 2 and parts[0].isdigit():
                existing.add(parts[1])
    return existing


# ── 写入文件 ──────────────────────────────────────────────────────────────────
def write_submission(sync_folder, folder_name, sub, meta):
    target = Path(sync_folder) / folder_name
    target.mkdir(parents=True, exist_ok=True)

    lang     = sub["lang"].lower()
    ext      = LANG_EXT.get(lang, "txt")
    filename = f"solution.{ext}"
    filepath = target / filename

    # 文件头注释
    header_lines = [
        f"# {meta['questionFrontendId']}. {meta['title']}",
        f"# Difficulty: {meta['difficulty']}",
        f"# https://leetcode.com/problems/{meta['titleSlug']}/",
        "",
    ]
    if ext in ("py", "sh"):
        header = "\n".join(f"# {l}" if l else "" for l in header_lines)
    elif ext in ("sql",):
        header = "\n".join(f"-- {l}" if l else "" for l in header_lines)
    else:
        header = "/*\n" + "\n".join(f" * {l}" if l else " *" for l in header_lines) + "\n */\n"

    code = sub.get("code", "")
    filepath.write_text(header + "\n" + code, encoding="utf-8")
    print(f"  ✍️  写入: {folder_name}/{filename}")


# ── 主流程 ────────────────────────────────────────────────────────────────────
def main():
    if not LEETCODE_SESSION or not LEETCODE_CSRF_TOKEN:
        print("❌ 缺少环境变量 LEETCODE_SESSION / LEETCODE_CSRF_TOKEN")
        sys.exit(1)

    session  = make_session()
    accepted = fetch_all_accepted(session)   # {slug: sub}
    existing = get_existing_slugs(SYNC_FOLDER)

    new_slugs = set(accepted.keys()) - existing
    print(f"📦 新增题目: {len(new_slugs)} 道（已跳过已存在的 {len(existing)} 道）")

    if not new_slugs:
        print("✅ 无新题目，跳过。")
        return

    for i, slug in enumerate(sorted(new_slugs), 1):
        sub  = accepted[slug]
        meta = fetch_question_meta(session, slug)
        if meta is None:
            print(f"  ⚠️  跳过 {slug}（无法获取题号）")
            continue

        folder_name = slug_to_folder_name(meta["questionFrontendId"], slug)
        print(f"[{i}/{len(new_slugs)}] {folder_name}")
        write_submission(SYNC_FOLDER, folder_name, sub, meta)
        time.sleep(0.2)

    print(f"\n🎉 同步完成，共写入 {len(new_slugs)} 道新题目。")


if __name__ == "__main__":
    main()
