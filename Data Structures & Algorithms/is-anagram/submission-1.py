class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = [0] * (ord('z') - ord('a') + 1)

        for ch1,ch2 in zip(s,t):
            letters[ord(ch1) - ord('a')] += 1
            letters[ord(ch2) - ord('a')] -= 1
        
        for letter in letters:
            if letter != 0:
                return False
        return True


        
        