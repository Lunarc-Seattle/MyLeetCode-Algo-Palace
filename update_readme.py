import requests
import json
import sys
import re

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
        print(f"正在抓取真实用户数据: {username} ...")
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            user_info = data.get("data", {}).get("matchedUser")
            if user_info:
                print("✅ 身份确认成功，正在同步数据...")
                return user_info
            else:
                print(f"❌ 错误：在 LeetCode(US) 库中未找到 ID 为 '{username}' 的用户。")
                print(f"API 返回内容: {json.dumps(data)}")
        else:
            print(f"❌ 网络请求失败，状态码: {response.status_code}")
    except Exception as e:
        print(f"❌ 发生异常: {e}")
    return None

def main():
    # 修正后的唯一 ID
    username = "jiefia" 
    user_info = fetch_leetcode_data(username)
    
    if not user_info:
        print("数据同步失败，脚本已安全退出。")
        sys.exit(1)

    # 1. 语言统计
    md_content = "\n### 💻 编程语言统计\n"
    langs = user_info.get("languageProblemCount", [])
    if langs:
        for lang in langs:
            md_content += f"* **{lang['languageName']}**: {lang['problemsSolved']} 题\n"
            
    # 2. 题型标签统计
    md_content += "\n### 🧩 刷题类型统计\n"
    tags_data = user_info.get("tagProblemCounts", {})
    all_tags = []
    for level in ["advanced", "intermediate", "fundamental"]:
        if tags_data.get(level):
            all_tags.extend(tags_data[level])
            
    if all_tags:
        all_tags.sort(key=lambda x: x['problemsSolved'], reverse=True)
        # 展示前 15 类，涵盖你的主要刷题领域
        for skill in all_tags[:15]: 
            md_content += f"* **{skill['tagName']}**: {skill['problemsSolved']} 题\n"

    # 3. 写入文件（防套娃逻辑）
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
        print(f"🎉 任务完成！{username} 的战绩已更新至主页。")
    else:
        print("❌ README 标记丢失，请检查是否包含 ")

if __name__ == "__main__":
    main()
