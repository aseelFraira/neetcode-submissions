class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = n - 1
        curr_sum = 0
        curr_len = n + 1
        for right in range(n):
            curr_sum += nums[right]
            while curr_sum >= target:
                curr_len = min(right - left + 1,curr_len)
                curr_sum -= nums[left]
                left += 1

        return curr_len if curr_len != n + 1 else 0





        
        