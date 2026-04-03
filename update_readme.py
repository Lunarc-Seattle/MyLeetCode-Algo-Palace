import requests
import json
import re
import sys

def fetch_leetcode_data(username):
    url = "https://leetcode.com/graphql"
    
    # 模拟更加真实的浏览器请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/{username}/",
        "Origin": "https://leetcode.com"
    }
    
    query = """
    query userProfile($username: String!) {
      matchedUser(username: $username) {
        languageProblemCount {
          languageName
          problemsSolved
        }
        skillTags {
          name
          problemsSolved
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
        
        # 打印状态码，方便定位问题
        print(f"服务器返回状态码: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if "errors" in data:
                print(f"❌ API 返回错误: {data['errors']}")
                return None
                
            user_info = data.get("data", {}).get("matchedUser")
            if not user_info:
                print(f"❌ 错误：未能找到用户 '{username}'。请检查用户名是否拼写正确，或账号是否为国际服。")
                return None
            
            print("✅ 成功获取数据！")
            return user_info
        elif response.status_code == 403:
            print("❌ 错误：请求被 LeetCode 防火墙拦截 (403 Forbidden)。")
        else:
            print(f"❌ 错误：请求失败，内容如下: {response.text[:200]}")
            
    except Exception as e:
        print(f"❌ 发生异常: {e}")
    
    return None

def main():
    # 请确保这里的用户名和你 LeetCode 主页 URL 里的完全一致
    # 例如：https://leetcode.com/Lunarc-Seattle/
    username = "Lunarc-Seattle" 
    user_info = fetch_leetcode_data(username)
    
    if not user_info:
        print("由于未能获取数据，脚本终止执行。")
        sys.exit(1) # 告诉 GitHub Action 这一步运行失败了

    # 生成 Markdown 内容
    md_content = "\n### 💻 编程语言统计\n"
    langs = user_info.get("languageProblemCount", [])
    if langs:
        for lang in langs:
            md_content += f"* **{lang['languageName']}**: {lang['problemsSolved']} 题\n"
    else:
        md_content += "* 暂无数据\n"
        
    md_content += "\n### 🧩 刷题类型统计\n"
    skills = user_info.get("skillTags", [])
    if skills:
        # 只展示前 15 个最常练习的类型，防止列表过长
        for skill in skills[:15]: 
            md_content += f"* **{skill['name']}**: {skill['problemsSolved']} 题\n"
    else:
        md_content += "* 暂无数据\n"

    # 读取并替换 README 内容
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r"().*?()"
    if re.search(pattern, content, re.DOTALL):
        # 保持注释标签，只替换中间内容
        new_content = re.sub(pattern, f"\\1\n{md_content}\n\\2", content, flags=re.DOTALL)
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("✅ README.md 已成功更新！")
    else:
        print("❌ 错误：在 README.md 中找不到 标签！")

if __name__ == "__main__":
    main()
