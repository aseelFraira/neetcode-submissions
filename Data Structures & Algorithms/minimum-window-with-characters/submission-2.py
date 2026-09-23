class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = right = 0
        letters2 = Counter(t)
        letters1 = defaultdict(int)
        n = len(s)
        min_len = n
        min_r = -1
        min_l = -1


        while right < n:
            letters1[s[right]] += 1
            while self.contains(letters1,letters2):
                if (right - left + 1) <= min_len:
                    min_len = right - left + 1
                    min_r = right
                    min_l = left
                letters1[s[left]] -= 1
                left += 1
            right += 1
        return s[min_l:min_r+1]
    
    def contains(self,letters1,letters2):
        for letter in letters2.keys():
            if letters2[letter] > letters1[letter]:
                return False
        return True


        