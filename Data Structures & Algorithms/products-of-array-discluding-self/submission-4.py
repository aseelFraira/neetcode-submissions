class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        left_side = 1
        for i in range(n):
            res[i] *= left_side
            left_side *= nums[i]

        right_side = 1
        for i in range(n - 1,-1,-1):
            res[i] *=  right_side
            right_side *=nums[i]
        return res


        