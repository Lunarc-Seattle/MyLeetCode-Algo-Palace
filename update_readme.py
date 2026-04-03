import requests
import json
import re
import os

def fetch_leetcode_data(username):
    url = "https://leetcode.com/graphql"
    payload = {
        "query": "query userProfile($username: String!) { matchedUser(username: $username) { languageProblemCount { languageName problemsSolved } skillTags { name problemsSolved } } }",
        "variables": {"username": Lunarc-Seattle}
    }
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("data", {}).get("matchedUser", {})
    return None

def main():
    username = "Lunarc-Seattle"
    user_info = fetch_leetcode_data(username)
    
    if not user_info:
        print("未能获取到 LeetCode 数据")
        return

    # 生成 Markdown 格式的字符串
    md_content = "### 💻 编程语言统计\n"
    for lang in user_info.get("languageProblemCount", []):
        md_content += f"* **{lang['languageName']}**: {lang['problemsSolved']} 题\n"
        
    md_content += "\n### 🧩 刷题类型统计\n"
    for skill in user_info.get("skillTags", []):
        md_content += f"* **{skill['name']}**: {skill['problemsSolved']} 题\n"

    # 读取现有的 README.md
    with open("README.md", "r", encoding="utf-8") as file:
        readme_text = file.read()

    # 使用正则表达式替换 START 和 END 之间的内容
    pattern = r"(\n).*?(\n)"
    # 注意这里要保证首尾的注释标签还在，方便下次继续替换
    replacement = rf"\1{md_content}\2"
    new_readme = re.sub(pattern, replacement, readme_text, flags=re.DOTALL)

    # 将新内容写回 README.md
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(new_readme)
        
    print("README.md 更新成功！")

if __name__ == "__main__":
    main()
