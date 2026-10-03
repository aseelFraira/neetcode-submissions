class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            print(i)
            print(haystack[i:m])
            if needle == haystack[i:i + m]:
                return i
        return -1

        