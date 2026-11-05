class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = defaultdict(int)
        curr_sum = 0
        curr_count = 0
        prefixes[0] = 1

        for num in nums:
            curr_sum += num
            curr_count += prefixes[curr_sum - k]
            prefixes[curr_sum] += 1
        return curr_count 
             
        