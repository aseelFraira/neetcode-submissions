class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        left = 0
        curr_min = nums[-1]
        for right in range(k -1,len(nums)):
            print(nums[right])
            diff = nums[right] - nums[left] 
            if diff < curr_min:
                curr_min = diff
            left += 1
        return curr_min

        