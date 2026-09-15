class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freqs = {}

        for i,num in enumerate(nums):
            missing = target - num
            if missing in freqs:
                return [freqs[missing] , i]
            freqs[num] = i
        return []
            
        