class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            target = -1 * (nums[i])
            while j < k:     
                twoSum = nums[j] + nums[k]
                if twoSum > target:
                    k = k - 1
                elif twoSum < target:
                    j = j + 1
                else:
                    y = nums[j]
                    z = nums[k]
                    res.append([nums[i], nums[j] , nums[k]])            
                    
                    while j < k and y == nums[j] and z == nums[k]:
                        j = j + 1    

                    while j < k and y == nums[j] and z == nums[k]:
                        k = k - 1                
        return res