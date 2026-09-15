class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freqs = defaultdict(int)

        for i,num in enumerate(nums):
            missing = target - num
            if missing in freqs.keys():
                return [freqs[missing] , i]
            freqs[num] = i
        return []
            
        