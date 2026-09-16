class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            curr_area = min(heights[left],heights[right]) * (right - left)
            if heights[left] < heights[right]:
                curr_area = heights[left] * (right - left)
                left += 1
            else:
                curr_area = heights[right] * (right - left)
                right -= 1
            max_area = max(curr_area,max_area)
        return max_area
        