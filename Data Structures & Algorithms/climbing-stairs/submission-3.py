class Solution:
    def climbStairs(self, n: int) -> int:    
        if n == 1 or n == 2:
            return n
        helper = [0] * (n + 1)
        helper[1] = 1
        helper[2] = 2


        for i in range(3,n + 1):
            print(i)
            helper[i] = helper[i - 1] + helper[i-2]


        return helper[-1]
            



        