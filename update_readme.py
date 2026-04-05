import requests
import json
import sys

def generate_bar(count, max_count, total_bar_length=25):
    """根据数量生成比例进度条"""
    if max_count == 0: return ""
    filled_length = int(total_bar_length * count // max_count)
    bar = '█' * filled_length
    return bar

def get_proficiency(count):
    """根据刷题数量动态返回星级评价"""
    if count >= 50: return "count + ⭐⭐⭐⭐⭐"
    elif count >= 30: return "count + ⭐⭐⭐⭐"
    elif count >= 15: return "count + ⭐⭐⭐"
    elif count >= 5: return "count + ⭐⭐"
    else: return "count + ⭐"

def fetch_leetcode_data(username):
    url = "https://leetcode.com/graphql"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/{username}/",
        "Origin": "https://leetcode.com"
    }
    
    # 重点：查询语句中增加了 submitStatsGlobal 获取难度数据
    query = """
    query userProfile($username: String!) {
      matchedUser(username: $username) {
        submitStatsGlobal {
          acSubmissionNum { difficulty count }
        }
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
            data = response.json()
            return data.get("data", {}).get("matchedUser")
    except Exception as e:
        print(f"❌ 发生异常: {e}")
    return None

def main():
    username = "jiefia" 
    user_info = fetch_leetcode_data(username)
    
    if not user_info:
        print("数据同步失败，脚本已退出。")
        sys.exit(1)

    md_content = ""

    # ==========================================
    # 0. 生成 题目难度分布 (新增部分！)
    # ==========================================
    submit_stats = user_info.get("submitStatsGlobal", {}).get("acSubmissionNum", [])
    diff_counts = {"Easy": 0, "Medium": 0, "Hard": 0, "All": 0}
    for stat in submit_stats:
        diff_counts[stat['difficulty']] = stat['count']
        
    total = diff_counts["All"]
    if total > 0:
        md_content += "\n### 📈 题目难度分布\n\n"
        md_content += f"**总计解决**: {total} 题\n\n"
        
        md_content += "```text\n"
        easy_c, med_c, hard_c = diff_counts["Easy"], diff_counts["Medium"], diff_counts["Hard"]
        
        # 为了进度条好看，以总题数为满格
        md_content += f"Easy   {generate_bar(easy_c, total, 25):<25} {easy_c:>3} 题 ({easy_c/total*100:.1f}%)\n"
        md_content += f"Medium {generate_bar(med_c, total, 25):<25} {med_c:>3} 题 ({med_c/total*100:.1f}%)\n"
        md_content += f"Hard   {generate_bar(hard_c, total, 25):<25} {hard_c:>3} 题 ({hard_c/total*100:.1f}%)\n"
        md_content += "```\n"

    # ==========================================
    # 1. 生成 编程语言分布 (星级表格)
    # ==========================================
    md_content += "\n### 📊 编程语言分布\n\n"
    md_content += "| 语言 | 题数 | 熟练度 |\n"
    md_content += "| :--- | :--- | :--- |\n"
    langs = user_info.get("languageProblemCount", [])
    if langs:
        langs.sort(key=lambda x: x['problemsSolved'], reverse=True)
        for lang in langs:
            md_content += f"| **{lang['languageName']}** | {lang['problemsSolved']} | {get_proficiency(lang['problemsSolved'])} |\n"
    else:
        md_content += "| 暂无 | 0 | - |\n"
            
    # ==========================================
    # 2. 生成 刷题类型统计 (代码块进度条)
    # ==========================================
    md_content += "\n### 🧩 刷题类型统计\n\n"
    md_content += "| 类型 | 题目数 | 进度图 |\n"
    md_content += "| :--- | :---: | :--- |\n"
    
    if all_tags:
        all_tags.sort(key=lambda x: x['problemsSolved'], reverse=True)
        max_problems = all_tags[0]['problemsSolved']
        
        for skill in all_tags[:15]:
            tag_name = skill['tagName']
            count = skill['problemsSolved']
            # 建议缩短进度条长度，在表格中更美观（如 15 或 20）
            bar = generate_bar(count, max_problems, total_bar_length=15)
            # 使用 Markdown 表格行格式
            md_content += f"| {tag_name} | `{count}` | `{bar}` |\n"

    # ==========================================
    # 3. 写入 README.md
    # ==========================================
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = ""
    end_marker = ""
    start_idx = content.find(start_marker)
    end_idx = content.rfind(end_marker)

    if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
        before_content = content[:start_idx + len(start_marker)]
        after_content = content[end_idx:]
        new_content = before_content + "\n" + md_content + "\n" + after_content
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("🎉 任务完成！带有难度分布的战绩已更新！")
    else:
        print("❌ README 标记丢失。")

if __name__ == "__main__":
    main()
