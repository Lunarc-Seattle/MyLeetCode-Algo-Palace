class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(subs):
            return subs == subs[::-1]

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # 尝试删除左边或右边一个字符
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
            left += 1
            right -= 1
        return True

