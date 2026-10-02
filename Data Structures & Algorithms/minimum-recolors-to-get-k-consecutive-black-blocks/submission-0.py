class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        curr_recolor = 0

        for right in range(k):
            if blocks[right] == 'W':
                curr_recolor += 1

        left = 0
        min_recolor = curr_recolor
        for right in range(k,n):
            if blocks[right] == 'W':
                curr_recolor += 1
            if blocks[left] == 'W':
                curr_recolor -= 1
            left += 1
            min_recolor = min(min_recolor,curr_recolor)
        return min_recolor
            




        