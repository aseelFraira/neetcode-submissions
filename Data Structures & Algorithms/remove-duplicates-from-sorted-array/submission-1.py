class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        write = 1

        for right in range(n):
            if nums[right] != nums[write - 1]:
                nums[write] = nums[right]
                write += 1
            
        return write
            

        