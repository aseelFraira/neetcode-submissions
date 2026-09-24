class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return 0
        if n == 2:
            return min(cost[0],cost[-1])
        pay = [0] * (n + 1)
        
        for i in range(2 ,n + 1):
            pay[i] = min(pay[i - 1] + cost[i - 1],pay[i - 2] + cost[i - 2])
        return pay[-1]


        