class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        curr = 0
        for d in num:
            curr *= 10
            curr += d

        curr += k
        while curr:
            res.append(curr%10)
            curr //= 10
        res = res[::-1]
        return res
