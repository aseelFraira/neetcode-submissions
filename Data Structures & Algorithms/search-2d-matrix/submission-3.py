class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first we find the correct row to search in
        high = len(matrix) - 1
        low = 0

        while low < high:
            mid = int((low + high)/2)
            if matrix[mid][0] <= target <= matrix[mid][-1] :
                low = mid
                break
            elif matrix[mid][0] < target :
                low = mid + 1
            else:
                high = mid - 1
        
        left = 0
        right = len(matrix[low]) - 1

        while left <= right:
            mid = int((left + right)/2)
            if matrix[low][mid] == target:
                return True
            elif matrix[low][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

        
        