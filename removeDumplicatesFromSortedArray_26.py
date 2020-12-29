class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        i = 0
        j = 1
        while j < l:
            if nums[j] != nums[i]:
                i+=1
                nums[i] = nums[j]
            
            j+=1
        
        return i+1 