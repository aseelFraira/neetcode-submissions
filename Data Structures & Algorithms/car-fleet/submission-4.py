class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[pos,speed] for pos,speed in zip(position,speed)]
        cars.sort()

        stack = []
        for car in cars:
            #can the car coming from behind move faster from the one already moving? we need 
            while stack and car[1] < stack[-1][1] and (car[0] + car[1]*((car[0] - stack[-1][0])/(stack[-1][1] - car[1]))) <= target:
                stack.pop()

            stack.append(car)
        return len(stack)



            
                







        