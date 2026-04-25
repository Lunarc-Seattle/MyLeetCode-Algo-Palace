class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        dp = [False]*(len(s)+1)
        #1 1. 数组开太小 (越界)
        #错误： 你只开了 n 个位置，但 DP 需要 n+1 个位置来存“前 $n$ 个字符”的结果。口诀： 有 n 个字母，就开 n+1 个坑（索引 0 到 n）
        dp[0] = True

        for i in range(1,len(s)+1):
            #2. 循环走不到头 (漏算)
            #错误： range(1, len(s)) 会在倒数第二个字符就停下。口诀： 范围必须加 1
            #用 range(1, n + 1) 才能确保算到整个字符串的终点
            for j in range(i):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break
                #dp 数组存的是“结果”（能不能跳到这），而 s[j:i] 提取的是“内容”（这一块是什么单词）
        return dp[len(s)]
        
