class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggest = -1
        n = len(arr)

        for i in range(n - 1,-1,-1):
            tmp = arr[i]
            arr[i] = biggest
            biggest = max(biggest,tmp)
        return arr

        