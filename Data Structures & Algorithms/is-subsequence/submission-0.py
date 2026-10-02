class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t) 
        left = 0
        
        for right in range(n2):
            if left < n1 and t[right] == s[left]:
                left += 1
        
        return left == n1
            
        
      
      
        
        