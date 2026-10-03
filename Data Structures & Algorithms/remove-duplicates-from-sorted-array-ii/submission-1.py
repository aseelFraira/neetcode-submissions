class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n - 2):
            if nums[i] == nums[i + 2]:
                nums[i] = '_'
                cnt += 1
        left = 0
        right = 0
        print(nums)
        while left < n:
            if nums[left] == '_':
                i = 1
                while left + i < n and nums[left + i] == '_':
                    i += 1
                if left + i < n:
                    nums[left] , nums[left + i] = nums[left + i] ,nums[left]
            left += 1
        return n - cnt

            
        