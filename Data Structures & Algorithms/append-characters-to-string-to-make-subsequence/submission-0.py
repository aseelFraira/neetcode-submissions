class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n1 = len(t)
        n2 = len(s) 
        left = 0
        
        for right in range(n2):
            if left < n1 and s[right] == t[left]:
                left += 1
        
        return n1 - left
