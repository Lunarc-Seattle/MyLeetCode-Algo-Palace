class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = [0]*26
        count2 = [0]*26
        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')] += 1
            count2[ord(s2[i])-ord('a')] += 1

        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1
        l = 0
        for r in range((len(s1)),len(s2)):
            # print(f"Checking window: {s2[r-len(s1)+1 : r+1]}, matches: {matches}") # 打印当前窗口和匹配数
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            count2[index] += 1
            
            if count1[index] == count2[index]:
                matches += 1
            elif count1[index]+1 == count2[index]:
                matches -= 1
            
            index = ord(s2[l])- ord('a')
            count2[index] -= 1
            if count1[index] == count2[index]:
                matches += 1
            elif count1[index]-1 == count2[index]:
                matches -= 1
            l += 1
        return matches == 26
                
        #时间复杂度	O(n) gengxiao
        #空间复杂度	O(1)（固定26）
