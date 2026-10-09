class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1,n):
                store = set()
                curr_targ = target - nums[i] - nums[j]
                for k in range(j + 1,n):
                    if curr_targ - nums[k] in store:
                        res.add(tuple(sorted([nums[i],nums[j],nums[k],curr_targ - nums[k]])))
                    store.add(nums[k])
        return [list(t) for t in res]

                


        