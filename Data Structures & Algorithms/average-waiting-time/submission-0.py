class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        finish_time = [0] * n
        for i,pair in enumerate(customers):
            finish_time[i] += max(finish_time[i - 1],pair[0]) + pair[1]
        wait_time = sum([finish - p[0] for finish,p in zip(finish_time,customers)])
        print(wait_time)
        return wait_time/n




            
            


        