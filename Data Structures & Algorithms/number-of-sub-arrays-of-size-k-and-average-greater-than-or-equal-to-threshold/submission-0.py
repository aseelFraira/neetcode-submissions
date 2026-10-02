class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = sum(arr[:k])
        n = len(arr)
        left = 0
        res = 0
        if curr_sum >= threshold*k:
            res += 1

        for right in range(k,n):
            curr_sum += arr[right]
            curr_sum -= arr[left]
            if curr_sum >= threshold*k:
                res += 1
            left+= 1

        return res
        