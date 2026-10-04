class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size =len(flowerbed)
        helper = [0] + flowerbed + [0]
        for i in range(1,size +1 ):
            if helper[i] == 0 and helper[i - 1] == 0 and helper[i + 1] == 0:   
                helper[i] = 1
                n -= 1
        
        return n <= 0

        