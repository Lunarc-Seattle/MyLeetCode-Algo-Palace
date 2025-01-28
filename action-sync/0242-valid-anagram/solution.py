class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ansS, ansT = {}, {}
        for i in range(len(s)):
            ansS[s[i]] = 1+ ansS.get(s[i],0)
            ansT[t[i]] = 1+ ansT.get(t[i],0)
        return ansS == ansT
