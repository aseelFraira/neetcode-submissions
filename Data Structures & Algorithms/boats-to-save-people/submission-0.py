class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0 
        n = len(people)
        right = n - 1
        num_boats = 0

        while left <= right:
            curr_weight = people[left] + people[right]
            if curr_weight <= limit:
                left += 1
            right -= 1
            num_boats += 1
        return num_boats

        