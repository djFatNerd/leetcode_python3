class Solution:
    def reverse(self, x: int) -> int:
        # flag indicate sign of x
        neg = 0
        if x<0:
            x = -x
            neg = 1
        
        result = 0
        while x > 0:
            result *= 10
            result += x%10
            x //= 10
        
        # return 0 if overflow
        if (neg and result > 2**31) or ((not neg) and result > 2**31-1):
            return 0
        
        # return result
        if neg: result *= -1
        return result