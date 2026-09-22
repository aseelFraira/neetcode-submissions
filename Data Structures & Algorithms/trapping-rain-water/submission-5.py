class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        trapped = 0
        curr_left_max = 0
        curr_right_max = 0

        while left <= right:
            if curr_left_max >= curr_right_max:
                trapped += max(0,curr_right_max - height[right])
                curr_right_max = max(curr_right_max,height[right])

                right -= 1
            else:
                trapped += max(0,curr_left_max - height[left])
                curr_left_max = max(curr_left_max,height[left])
                left += 1
        return trapped



            

        