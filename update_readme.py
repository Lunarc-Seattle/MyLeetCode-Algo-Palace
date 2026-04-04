import requests
import json
import sys
import re

def generate_bar(count, max_count, total_bar_length=25):
    """根据数量生成比例进度条"""
    if max_count == 0: return ""
    filled_length = int(total_bar_length * count // max_count)
    bar = '█' * filled_length
    return bar

def get_proficiency(count):
    """根据刷题数量动态返回星级评价"""
    if count >= 50:
        return "⭐⭐⭐⭐⭐"
    elif count >= 30:
        return "⭐⭐⭐⭐"
    elif count >= 15:
        return "⭐⭐⭐"
    elif count >= 5:
        return "⭐⭐"
    else:
        return "🏗️ 施工中"

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

    # ==========================================
    # 1. 生成 编程语言分布 (星级表格)
    # ==========================================
    md_content = "\n### 📊 编程语言分布\n\n"
    md_content += "| 语言 | 题数 | 熟练度 |\n"
    md_content += "| :--- | :--- | :--- |\n"
    
    langs = user_info.get("languageProblemCount", [])
    if langs:
        # 按题数从高到低排序
        langs.sort(key=lambda x: x['problemsSolved'], reverse=True)
        for lang in langs:
            lang_name = lang['languageName']
            count = lang['problemsSolved']
            proficiency = get_proficiency(count)
            md_content += f"| **{lang_name}** | {count} | {proficiency} |\n"
    else:
        md_content += "| 暂无 | 0 | - |\n"
            
    # ==========================================
    # 2. 生成 刷题类型统计 (代码块进度条)
    # ==========================================
    md_content += "\n### 🧩 刷题类型统计\n"
    tags_data = user_info.get("tagProblemCounts", {})
    all_tags = []
    for level in ["advanced", "intermediate", "fundamental"]:
        if tags_data.get(level):
            all_tags.extend(tags_data[level])
            
    if all_tags:
        all_tags.sort(key=lambda x: x['problemsSolved'], reverse=True)
        max_problems = all_tags[0]['problemsSolved']
        
        md_content += "\n```text\n"
        for skill in all_tags[:15]: 
            tag_name = skill['tagName']
            count = skill['problemsSolved']
            bar = generate_bar(count, max_problems, total_bar_length=25)
            md_content += f"{tag_name:<16} {bar} {count}\n"
        md_content += "```\n"
        md_content += "\n*(And others... keep climbing!)*\n"

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
        print("🎉 任务完成！带有星级表格和进度条的战绩已更新！")
    else:
        print("❌ README 标记丢失，请检查是否包含 ")

if __name__ == "__main__":
    main()
