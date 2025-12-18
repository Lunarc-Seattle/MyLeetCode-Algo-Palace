class Solution:
    def maxArea(self, height: List[int]) -> int:
        current = 0
        left, right = 0, len(height)-1

        while left< right:
            area = (right-left)* min(height[left] ,height[right])
            current = max(current, area)
            
            # 关键步骤：移动高度较小的那个指针
            if height[left]< height[right]:
                left += 1
            else:
                right  -= 1
        return current

        
