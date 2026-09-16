class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(s)
        left = 0 
        right = len(s) - 1

        while left < right:
            
            while left < right and  not (s[left].isalpha() or s[left].isdigit()):
                left += 1
            while left < right and not (s[right].isalpha() or s[right].isdigit()):
                right -= 1

            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True



        