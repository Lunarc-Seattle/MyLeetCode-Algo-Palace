class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #edge case
        if not s or not t:
            return ""
        countT , window = {}, {}
        #get t's count
        for c in t:
            countT[c] = 1 + countT.get( c, 0 )
        
        have, need = 0 , len(countT)
        res, resLen = [-1,-1] , float("infinity")
        l = 0 
        for r in range(len(s)):
            c = s[r] 
            window [c] = 1+window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r-l+1)< resLen:
                    resLen = r-l+1
                    res = [l,r]
                
                window[s[l]] -= 1
                #不写这一句，程序会以为“还满足条件”，就会继续乱缩窗口，最后答案就错了 ❌
                if s[l] in countT and window[s[l]]< countT[s[l]]:
                    have -= 1
                l += 1
        l, r =res
        return s[l:r+1] if resLen != float("infinity") else""