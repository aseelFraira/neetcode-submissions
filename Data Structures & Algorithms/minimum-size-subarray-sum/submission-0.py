class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix_sums = [0] * (n + 1)
        prefix = 0

        for right in range(n):
            prefix_sums[right] = prefix
            prefix += nums[right]
        prefix_sums[-1] = prefix
        print(prefix_sums)

        left = 0
        right = n - 1
        curr_len = n
        for right in range(n):
            while prefix_sums[right + 1] - prefix_sums[left] >= target:
                curr_len = min(right - left + 1,curr_len)
                left += 1
        if prefix_sums[-1] <target:
            return 0
        return curr_len





        
        