class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                if not stack:
                    # heights = [5,4,3,2,1]一直在pop就会pop空
                    w = i
                else:
                    w = i -stack[-1]-1
                maxArea = max(maxArea, h*w)
            stack.append(i)
        return maxArea


        