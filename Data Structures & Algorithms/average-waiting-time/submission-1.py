class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        curr_finish = 0
        prev_finish = 0
        wait_time = 0
        for i,pair in enumerate(customers):
            curr_finish = max(prev_finish,pair[0]) + pair[1]

            wait_time += curr_finish - pair[0]
            prev_finish = curr_finish

        return wait_time/n




            
            


        