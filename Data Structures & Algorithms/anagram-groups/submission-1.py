class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        res = []

        for s in strs:
            letters = [0] * (ord('z') - ord('a') + 1)
            for ch in s:
                letters[ord(ch) - ord('a')] += 1
            groups[tuple(letters)].append(s)

        for group_key in groups.keys():
            res.append(groups[group_key])
        return res

        
        