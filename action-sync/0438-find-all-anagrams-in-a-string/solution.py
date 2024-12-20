class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_count = {}
        s_count = {}
        for char in p:
            p_count[char] = p_count.get(char,0) + 1
        l = 0 
        r = 0 
        for r in range(len(s)):
            s_count[s[r]] = s_count.get(s[r] , 0 ) + 1 
            if r-l+1 > len(p):
                if s_count[s[l]] == 1:
                    del s_count[s[l]]
                else:
                    s_count[s[l]] -= 1
                l += 1
            if s_count == p_count:
                res.append(l)           
        
        return res


        
