class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)

        for i,target in enumerate(nums):
            seen = set()
            for left in range(i + 1,n):
                search = -target -nums[left] 
                if search in seen:
                    res.add(tuple(sorted([target,nums[left],search])))
                seen.add(nums[left])

        return [list(tup) for tup in res]



        