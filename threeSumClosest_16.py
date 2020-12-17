class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 0
        diff = inf
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                threesum = nums[i] + nums[j] + nums[k]
                new_diff = threesum - target
                
                if new_diff == 0:
                    return target
                # 3sum < target, only increasing 3sum can decrease diff
                elif new_diff < 0:
                    j+=1
                # 3sum > target, only decreasing 3sum can increase diff
                else:
                    k-=1
                
                # update diff               
                if abs(new_diff) < abs(diff):
                    diff = new_diff
            
            # break early, smallest sum > target
            if nums[i] + nums[i+1] + nums[i+2] > target: break
            i+=1
        
        return diff + target