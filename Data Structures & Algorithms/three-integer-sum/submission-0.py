class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for right in range(len(nums)):
            target = -1 * nums[right]
            seen = set()
            for left in range(right + 1,len(nums)):
                missing = target - nums[left]
                if missing in seen:
                    res.add(tuple(sorted([nums[right], nums[left], missing])))
                seen.add(nums[left])
        return [list(x) for x in res]




        