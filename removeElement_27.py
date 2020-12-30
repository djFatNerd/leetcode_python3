'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
            
            j +=1
        
        return i

'''

# in case 1 we were doing unnecessary modifications to the array, for example:
# [4, 1, 2, 3, 5], 4
# we end up relocating all the elements

# in place means: no extra storage
# stable: maintains order
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        l = len(nums)
        while i < l:
            if nums[i] == val:
                nums[i] = nums[l-1]
                l-=1
            
            # can't directly i++ here becuz after swapping its still possible that new nums[i] = val
            # need to test nums[i] again
            else:
                i+=1
            
        return l