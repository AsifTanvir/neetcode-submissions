class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left = 0
        right = len(heights) - 1
        
        while left < right:
            diff = right - left
            if heights[left] < heights[right]:
                area = diff * heights[left]
                left += 1
            else:
                area = diff * heights[right]
                right -= 1
            result = max(result, area)
        
        return result
        