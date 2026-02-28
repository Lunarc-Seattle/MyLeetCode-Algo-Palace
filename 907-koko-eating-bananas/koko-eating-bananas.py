class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low < high:
            mid = low+(high-low)//2

            total = 0
            for p in piles:
                total = total + (p+mid-1)//mid
                #这里是重点 p//mid 往上加一个就是（p+mid-1）//mid
                # (p + mid - 1) // mid 就是程序员版的“向上取整”函数
                # 在 Python 中，// 符号是“地板除”（向下取整）。
            
            if total <= h:
                high = mid
                #如果会排出正确答案的话，就不能mid-1
            else:
                low = mid+1
        return low
        