import requests
import json
import sys

def fetch_leetcode_data(username):
    url = "https://leetcode.com/graphql"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/{username}/",
        "Origin": "https://leetcode.com"
    }
    
    query = """
    query userProfile($username: String!) {
      matchedUser(username: $username) {
        languageProblemCount { languageName problemsSolved }
        tagProblemCounts {
          advanced { tagName problemsSolved }
          intermediate { tagName problemsSolved }
          fundamental { tagName problemsSolved }
        }
      }
    }
    """
    payload = {"query": query, "variables": {"username": username}}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        if response.status_code == 200:
            return response.json().get("data", {}).get("matchedUser")
    except Exception as e:
        print(f"Error: {e}")
    return None

def main():
    username = "JietheBig" 
    user_info = fetch_leetcode_data(username)
    
    if not user_info:
        print("未能获取数据，脚本终止执行。")
        sys.exit(1)

    # 生成 Markdown 内容
    md_content = "\n### 💻 编程语言统计\n"
    langs = user_info.get("languageProblemCount", [])
    if langs:
        for lang in langs:
            md_content += f"* **{lang['languageName']}**: {lang['problemsSolved']} 题\n"
    else:
        md_content += "* 暂无数据\n"
        
    md_content += "\n### 🧩 刷题类型统计\n"
    tags_data = user_info.get("tagProblemCounts", {})
    all_tags = []
    for level in ["advanced", "intermediate", "fundamental"]:
        if tags_data.get(level):
            all_tags.extend(tags_data[level])
            
    if all_tags:
        all_tags.sort(key=lambda x: x['problemsSolved'], reverse=True)
        for skill in all_tags[:15]: 
            md_content += f"* **{skill['tagName']}**: {skill['problemsSolved']} 题\n"
    else:
        md_content += "* 暂无数据\n"

    # 【终极防重复写入逻辑：一刀切】
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = ""
    end_marker = ""

    # 找第一个开始标志
    start_idx = content.find(start_marker)
    # 找最后一个结束标志 (即使中间套娃了无数个，也全被包围在内)
    end_idx = content.rfind(end_marker)

    if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
        # 截取头部和尾部，中间全部塞入最新的、唯一的数据
        before_content = content[:start_idx + len(start_marker)]
        after_content = content[end_idx:]
        
        new_content = before_content + "\n" + md_content + "\n" + after_content
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("✅ README.md 更新成功（已彻底清除历史嵌套垃圾）！")
    else:
        print("❌ 错误：在 README.md 中找不到对应的隐藏标签。")

if __name__ == "__main__":
    main()
