class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we want large numbers at front
        # 1 2 6 4 2 -> 1 4 2 2 6 -> 1 4 2 6 2 -> 1 4 6 2 2 - > 1 6 2 2 4...
        
        targetIdx = len(nums) - 2
        while targetIdx >= 0 and nums[targetIdx] >= nums[targetIdx + 1]: targetIdx -= 1
        
        # nums is sorted in descending order, return smallets permutation
        # based on the fact we knew it's already sorted in descending order, we can just reverse it to save time
        if targetIdx == -1: return nums.reverse()
    
    
        # find swapIdx that nums[swapIdx] is larger than nums[targetIdx] and closest to it
        swapIdx = targetIdx + 1
        
        while ((swapIdx + 1) < len(nums)) and (nums[swapIdx+1] > nums[targetIdx]): swapIdx +=1
        
        # swap
        nums[swapIdx], nums[targetIdx] = nums[targetIdx], nums[swapIdx]
        
        # sort in ascending order after targetIdx
        # based on the fact we knew it's already sorted in descending order, we can just reverse it to save time
        # ** because when we swap we guranteed everything after tagetIdx is smaller than nums[targetIdx] and in descending order
        # reverse is much faster than sorting
        nums[targetIdx+1:] = reversed(nums[targetIdx+1:])
        # nums[targetIdx+1:] = sorted(nums[targetIdx+1:])