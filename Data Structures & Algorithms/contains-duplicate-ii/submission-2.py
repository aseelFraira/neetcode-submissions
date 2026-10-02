class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(int)

        for i,num in enumerate(nums):
            if num in seen:
                if i - seen[num] <= k:
                    return True
            if i - k - 1  >= 0:
                del seen[nums[i - k - 1]]
            seen[num] = i
        return False

        