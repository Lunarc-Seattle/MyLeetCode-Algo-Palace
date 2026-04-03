# My LeetCode Journey 🚀


欢迎来到我的 LeetCode 解题笔记库！这里记录了我刷题的过程、思路总结以及不同最优解的实现。
{
    "query": "query userProfile($username: String!) { matchedUser(username: $username) { languageProblemCount { languageName problemsSolved } skillTags { name problemsSolved } } }",
    "variables": {
        "username": "Lunarc-Seattle"
    }
}

### 🛠 技术栈与工具
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LeetCode](https://img.shields.io/badge/LeetCode-000000?style=for-the-badge&logo=LeetCode&logoColor=#d16c00)

---

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Lunarc-Seattle&layout=compact&theme=radical" alt="Top Langs" />
  </div>

---
## 📚 题目分类索引

这里的内容之后会被脚本自动替换掉，你现在留空也没关系。
### 基础数据结构



# My LeetCode Journey 🚀

欢迎来到我的 LeetCode 解题笔记库！这里记录了我刷题的过程、思路总结以及不同最优解的实现。

## 🛠 语言与工具
* **编程语言**: Python 3
* **解题策略**: 栈、双指针、动态规划、广度/深度优先搜索等

## 📚 题目分类索引

### 基础数据结构
* [0020. 有效的括号](./path/to/valid_parentheses.py) - 栈的应用
* [0001. 两数之和](./path/to/two_sum.py) - 哈希表

### 进阶算法
* (待补充...)

## 📝 学习笔记示例：有效的括号 (20. Valid Parentheses)

在处理这类题目时，核心逻辑如下：
1. **左括号入栈**：遇到 `(`、`[`、`{` 时放入栈中。
2. **右括号匹配**：
   * 检查栈是否为空（预防开头就是右括号的情况）。
   * 弹出栈顶元素，对比是否为对应的左括号。
3. **最终检查**：遍历结束后，栈必须为空才算完全匹配。

> **注意语法陷阱**：
> 在 Python 中，`elif` 必须紧跟在 `if` 块之后。中间不能插入像 `temp = stack.pop()` 这样的独立赋值语句，否则会报 `SyntaxError`。

---
*坚持刷题，保持手感。*
