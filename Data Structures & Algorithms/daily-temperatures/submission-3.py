class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_day = stack[-1][1]
                res[prev_day] = i - prev_day
                stack.pop()
            stack.append([temp,i])
        return res

        