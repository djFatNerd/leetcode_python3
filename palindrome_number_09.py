'''
# solution 1, reversed all x to see if r(x) = x
# naive, need to checked overflow
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        return x == self.reverse(x)
    
    def reverse(self, x:int) -> int:
        result = 0
        while(x>0):
            result *= 10
            result += x%10
            x //= 10
        
        if x>2**31: return -1
        return result
    
'''    
# solution 2, reverse half part of x to see if x_first_half = x_second half_reverse
# smart, no need to check overflow
class Solution:
    def isPalindrome(self, x:int) -> bool:
        if x <0: return False
        
        # N0000...
        if x%10==0 and x>0:
            return False
        
        x_reversed = 0
        while x > x_reversed:
            x_reversed *= 10
            x_reversed += x%10
            x //= 10
            
        #     "1221"              "12321"
        return x == x_reversed or x == x_reversed // 10
        # but this will fail the "N0000000.." case, so add this to the base case