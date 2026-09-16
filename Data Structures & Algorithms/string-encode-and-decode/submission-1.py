class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        return res
            
        

    def decode(self, s: str) -> List[str]:
        res = []
        left = 0
        right = 0
        n = len(s)
        while left < n:
            right = left
            while s[right] != '#':
                right += 1
            length = int(s[left:right])
            left = right + 1 + length
            res.append(s[right + 1: right + 1 + length])
        return res



