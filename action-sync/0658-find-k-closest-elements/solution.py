class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
         # 第一步：按照离 x 的距离来排序，如果距离一样就按数值大小排
        sorted_arr = sorted(arr, key=lambda num: (abs(num - x), num))
        
        # 第二步：取前 k 个最近的
        closest_k = sorted_arr[:k]
        
        # 第三步：按从小到大排序
        return sorted(closest_k)
        
