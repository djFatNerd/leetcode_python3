# first pass multiply everything b4
# second pass multiply everything after

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]
        for i in range(1, len(nums)):
            out.append(nums[i-1] * out[-1])
            
        
        p = 1
        
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= p
            p*= nums[i]

            
        return out