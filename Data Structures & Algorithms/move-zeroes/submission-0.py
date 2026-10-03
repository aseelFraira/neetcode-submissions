class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        write = 0

        for read in range(n):
            if nums[read] != 0:
                nums[write],nums[read]  = nums[read] , nums[write]
                write += 1
        
        """
        Do not return anything, modify nums in-place instead.
        """
        