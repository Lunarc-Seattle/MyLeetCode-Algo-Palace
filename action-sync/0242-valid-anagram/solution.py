class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = [0]*26
        list2 = [0]*26

        for chara in s:
            list1[ord(chara)-ord('a')] += 1
        for chara in t:
            list2[ord(chara)-ord('a')] += 1
        return list1 == list2
        
            


        
