# 17. Letter Combinations of a Phone Number
# Difficulty: Medium
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
        res = []

        def backtrack (i,path):
            if i == len(digits):
                res.append(path)
                return
            for ch in phone[digits[i]]:
                backtrack(i+1,path+ch)
            
        backtrack(0,"")
        return res
