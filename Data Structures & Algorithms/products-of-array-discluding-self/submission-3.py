class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        right = nums[-1]
        for i in range(1,n):
            res[i] = nums[i - 1] * res[i - 1]

        for i in range(n - 2, -1 ,-1):
            res[i] = res[i] *right
            right *= nums[i]

        return res

        