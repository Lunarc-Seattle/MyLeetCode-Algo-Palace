class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for s in range(1,len(strs)):
            i = 0
            while i < min(len(res) , len(strs[s])):
                if res[i] != strs[s][i]:
                    break
                i += 1
            res = res[:i]
        return res



        
