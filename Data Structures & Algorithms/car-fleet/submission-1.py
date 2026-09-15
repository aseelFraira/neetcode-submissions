class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for pos, pace in zip(position, speed):
            cars.append([pos,pace])
        cars.sort()

        fleets = []

        for pos,pace in reversed(cars): #start from the bigger postion
            arrival_time = (target - pos)/pace
            if not fleets or fleets[-1] < arrival_time:
                fleets.append(arrival_time)

        return len(fleets)



        