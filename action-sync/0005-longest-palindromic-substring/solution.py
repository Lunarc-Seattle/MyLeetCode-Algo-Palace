class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        for i in range(len(s)):
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if len(res)<r-l+1:
                    res = s[l:r+1]
                l -= 1
                r += 1

            l = i 
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if len(res) < r-l+1:
                    res = s[l:r+1]
                l -= 1
                r += 1

        return res
