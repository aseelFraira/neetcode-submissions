class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        res = num[::-1] 
        carry = 0
        for i in range(n):
            curr_sum = res[i] + k%10 + carry
            res[i] = curr_sum % 10 
            carry = curr_sum // 10
            k = k // 10
        k += carry
        while k > 0: 
            res.append(k % 10)
            k //= 10
        res.reverse()
        return res

        
            
            



        return res