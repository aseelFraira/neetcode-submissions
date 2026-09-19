class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        biggest_pile = max(piles)
        curr_pace = 0
        left = 1
        right = biggest_pile

        while left <= right:
            mid = int((left+right)/2)
            if self.finish_piles(piles,mid) <= h:
                print(mid)
                curr_pace = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if self.finish_piles(piles,curr_pace) <= h:
            return curr_pace
        return -1

    def finish_piles(self,piles,pace):
        hours = 0
        for pile in piles:
            if pace:
                hours += math.ceil(pile/pace)
        return hours

            


        
        