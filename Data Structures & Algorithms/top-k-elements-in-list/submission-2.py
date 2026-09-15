class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter ={}
        
        for num in nums:
            counter[num] = counter.get(num,0) + 1
        
        frequncies = defaultdict(list)

        for num,freq in counter.items():
            frequncies[freq].append(num)

        res = []

        for i in range(n, -1 , - 1):
            for num in frequncies[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res


        