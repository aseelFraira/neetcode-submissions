class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freqs = [0] * (ord('z') - ord('a') + 1)
        max_substring = 0
        right = left = 0
        n = len(s)

        while right < n:
            freqs[ord(s[right]) - ord('Z')] += 1
            if self.diff_letters(freqs) <= k:
                max_substring = max(right - left + 1,max_substring)
            else:
                while self.diff_letters(freqs) > k:
                    freqs[ord(s[left]) - ord('Z')] -= 1
                    left += 1
            right += 1
        
        return max_substring

    def diff_letters(self,freqs):
        return (sum(freqs) - max(freqs))





        