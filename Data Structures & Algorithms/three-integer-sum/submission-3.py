class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)

        for i,target in enumerate(nums):
            left = i + 1
            right = n - 1
            while left < right:
                curr_sum = nums[left] + nums[right] +target
                if curr_sum == 0:
                    res.add((target,nums[left],nums[right]))
                    right -= 1
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else: 
                    left += 1
        return [list(tup) for tup in res]



        