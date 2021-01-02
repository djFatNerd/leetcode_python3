class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # sign of dividend / divisor
        pos = (dividend <= 0) == (divisor <= 0)
        
        a = abs(dividend)
        b = abs(divisor)
        
        res = 0
        while a >= b:
            x = 0
            while a >= (b << 1 << x):
                x +=1
            
            res += (1 << x)
            a -= (b << x) 
        
        
        return min(res if pos else -res, 2147483647)