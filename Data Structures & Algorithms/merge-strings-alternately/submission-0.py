class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        write = 0
        res = [''] * (n1 + n2)
        p1 = 0
        p2 = 0

        while p1 < n1 and p2 < n2:
            res[write] = word1[p1]
            res[write + 1] = word2[p2]

            p1 += 1
            p2 += 1
            write += 2

        while p1 < n1:
            res[write] = word1[p1]
            p1 += 1
            write += 1
        while p2 < n2:
            res[write] = word2[p2]
            p2 += 1
            write += 1

        return "".join(res)

        


        