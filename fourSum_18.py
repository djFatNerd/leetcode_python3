'''
# naive version(correct though)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        r = []
        l = len(nums)
        if l < 4 or 4 * nums[l-1] < target: return r
        i = 0
        while i < l - 3 and 4 * nums[i] <= target:
            # avoid i duplicates
            if (i > 0 and nums[i] == nums[i-1]) or (3 * nums[l-1] < target - nums[i]):
                i+=1
                continue
            
            j = i + 1
            while j < l - 2 and 3 * nums[j] <= target - nums[i]:
                # avoid j duplicates
                if j > i + 1 and nums[j] == nums[j-1]:
                    j+=1
                    continue
                              
                k = j + 1
                m = l - 1
                while k < m:
                    foursum = nums[i] + nums[j] + nums[k] + nums[m]
                    if foursum == target:
                        r.append([nums[i], nums[j], nums[k], nums[m]])
                        k+=1
                        m-=1
                        # avoid k, m duplicates
                        while k<m and nums[k] == nums[k-1]: k+=1
                        while k<m and nums[m] == nums[m+1]: m-=1
                    elif foursum < target:
                        k+= 1
                    else:
                        m-= 1
                
                j+=1
            i+=1
        return r  
'''

# cleaner general version
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    
        def kSum(nums, target, k):
            result = []

            # base case 0, no possible solution
            if len(nums) < k or k * nums[0] > target or k * nums[-1] < target:
                return result

            # base case 1, k = 2
            if k == 2:
                return twoSum(nums, target)

            # recursive case
            for i in range(len(nums) - k + 1):
                # avoid duplicates at start
                if i == 0 or nums[i] != nums[i-1]:
                    # result for k-1 sum
                    k_minus_1_sum = kSum(nums[i+1:], target - nums[i], k-1)
    
                    for l in k_minus_1_sum:
                        # result for k sum
                        result.append([nums[i]] + l)
                    
            return result

        # base case
        def twoSum(nums, target):
            result = []
            i = 0
            j = len(nums) - 1
            while i < j:
                twosum = nums[i] + nums[j]
                # approach target from left || avoid i duplicate
                if twosum < target or (i > 0 and nums[i] == nums[i-1]):
                    i+=1
                # approach target from right || avoid j duplicate
                elif twosum > target or (j < len(nums) -1 and nums[j] == nums[j+1]):
                    j-=1

                # twosum == target
                else:
                    result.append([nums[i], nums[j]])
                    i+=1
                    j-=1
                
            return result
        
        
        nums.sort()
        return kSum(nums, target, 4)
