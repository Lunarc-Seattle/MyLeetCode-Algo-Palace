import requests
import json
import re
import sys

def fetch_leetcode_data(username):
    url = "https://leetcode.com/graphql"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/{username}/",
        "Origin": "https://leetcode.com"
    }
    
    # 【重点修复】使用了最新的 LeetCode API 字段 tagProblemCounts
    query = """
    query userProfile($username: String!) {
      matchedUser(username: $username) {
        languageProblemCount {
          languageName
          problemsSolved
        }
        tagProblemCounts {
          advanced {
            tagName
            problemsSolved
          }
          intermediate {
            tagName
            problemsSolved
          }
          fundamental {
            tagName
            problemsSolved
          }
        }
      }
    }
    """
    
    payload = {
        "query": query,
        "variables": {"username": username}
    }

    try:
        print(f"正在尝试抓取用户 {username} 的数据...")
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        
        print(f"服务器返回状态码: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if "errors" in data:
                print(f"❌ API 返回错误: {data['errors']}")
                return None
                
            user_info = data.get("data", {}).get("matchedUser")
            if not user_info:
                print(f"❌ 错误：未能找到用户 '{username}'。")
                return None
            
            print("✅ 成功获取数据！")
            return user_info
        else:
            print(f"❌ 错误：请求失败，内容如下: {response.text[:200]}")
            
    except Exception as e:
        print(f"❌ 发生异常: {e}")
    
    return None

def main():
    username = "Lunarc-Seattle" 
    user_info = fetch_leetcode_data(username)
    
    if not user_info:
        print("由于未能获取数据，脚本终止执行。")
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
    
    # 【重点修复】合并 advanced, intermediate, fundamental 三个难度的标签
    tags_data = user_info.get("tagProblemCounts", {})
    all_tags = []
    
    # 将不同难度的标签汇总到一个大列表里
    for level in ["advanced", "intermediate", "fundamental"]:
        level_tags = tags_data.get(level)
        if level_tags: # 如果该难度下有数据
            all_tags.extend(level_tags)
            
    if all_tags:
        # 按照做题数量从多到少排序
        all_tags.sort(key=lambda x: x['problemsSolved'], reverse=True)
        
        # 只展示前 15 个最常练习的类型，防止列表过长
        for skill in all_tags[:15]: 
            md_content += f"* **{skill['tagName']}**: {skill['problemsSolved']} 题\n"
    else:
        md_content += "* 暂无数据\n"

    # 读取并替换 README 内容
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r"().*?()"
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, f"\\1\n{md_content}\n\\2", content, flags=re.DOTALL)
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("✅ README.md 已成功更新！")
    else:
        print("❌ 错误：在 README.md 中找不到 标签！")

if __name__ == "__main__":
    main()
