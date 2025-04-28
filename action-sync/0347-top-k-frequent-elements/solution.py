#Bucket Sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequence = [ [] for i in range(len(nums)+1)] 
        ### 创建nested 的方法!!! 

        for num in nums:
            count[num] = 1+count.get(num,0)
        for num, cnt in count.items():
            frequence[cnt].append(num)
        
        res =[]

        for i in range(len(frequence)-1,0,-1):
            for n in frequence[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
