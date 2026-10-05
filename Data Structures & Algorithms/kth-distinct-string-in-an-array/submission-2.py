class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = Counter(arr)
        distincts = {ch for ch,val in seen.items() if val == 1}
        turn = 0
        for ch in arr:
            if ch in distincts:
                turn += 1
            if turn == k:
                return ch
        return ""
        

        