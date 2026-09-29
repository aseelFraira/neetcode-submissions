class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        counter = [0] * (n + 1)
        ans = [0] * len(queries)

        vowels = {'a','e','i','o','u'}
        
        for i,word in enumerate(words):
            counter[i] = counter[i - 1]
            if word[0] in vowels and word[-1] in vowels:
                counter[i] += 1
        
        for i,query in enumerate(queries):
            li = query[0] - 1 

            ri = query[-1]
            ans[i] = counter[ri] - counter[li]
        return ans