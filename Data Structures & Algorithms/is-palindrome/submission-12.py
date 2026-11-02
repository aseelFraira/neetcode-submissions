class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.isPalindrome_aux(s,0,len(s) - 1)   

    def isPalindrome_aux(self, s: str,left,right) -> bool:
        if right <= left:
            return True
        if not s[left].isalnum():
            return self.isPalindrome_aux(s,left + 1,right)
        elif not s[right].isalnum():
            return self.isPalindrome_aux(s,left,right - 1)
        elif s[left].lower() != s[right].lower():
            return False
        else:
            return self.isPalindrome_aux(s,left + 1,right - 1)







        