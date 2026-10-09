class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[left] > nums[mid] and target >= nums[left]:
                right = mid - 1
            elif nums[left] > nums[mid] and target <= nums[left] and target < nums[mid]:
                right = mid - 1
            elif nums[left] > nums[mid] and target <= nums[left] and target > nums[mid]:
                left = mid + 1
            elif nums[left] < nums[mid] and nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            

            

        return -1
            
        