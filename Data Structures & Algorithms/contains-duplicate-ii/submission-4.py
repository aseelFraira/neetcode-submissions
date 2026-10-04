class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        write = 0
        seen = set()
        
        for i in range(n):
            if nums[i] in seen:
                return True
            seen.add(nums[i])            
            if i - k >= 0 and nums[i - k] in seen:
                seen.remove(nums[i - k])
        return False

        