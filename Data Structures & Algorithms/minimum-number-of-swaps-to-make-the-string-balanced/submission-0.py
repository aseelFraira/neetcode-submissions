class Solution:
    def minSwaps(self, s: str) -> int:
        left = 0
        n = len(s) 
        res = 0

        open_brackets = 0


        while left < n:
            if s[left] == ']' and open_brackets == 0:
                res += 1
                open_brackets += 1
            elif s[left] == ']' and open_brackets > 0 :
                open_brackets -= 1
            if s[left] == '[':
                open_brackets += 1
            left += 1
        return res





        