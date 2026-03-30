class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0]*26
        res = 0
        maxCount = 0
        left = 0

        # tradeoff 如果题目明确是 A-Z：优先数组
        # 如果字符不确定：用 dict
        for right in range(len(s)):
            count[ord(s[right])-ord('A')] += 1
            maxCount = max(maxCount, count[ord(s[right])-ord('A')])
            #Q：为什么要看现在right所在的位置的字母？直接找count里最大的就好了，因为已经更新了
            #A；虽然看 26 个字母的数组很快，但在计算机底层：直接找 count 里的最大值：你需要遍历一遍长度为 26 的数组。复杂度是 O(26)。只看 right 字母：只需要一次加法和一次比较。复杂度是 O(1)。在滑动窗口移动 n 次的过程中，这种累积的差异会让代码跑得更“优雅”
            while(right-left+1)-maxCount > k:
                count[ord(s[left])-ord('A')] -= 1
                left += 1
            res = max(res, right-left+1)
        return res