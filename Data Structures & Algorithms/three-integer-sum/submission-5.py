class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []        
        added = set()
        for i in range(len(nums)):
            l, r = 0, len(nums) - 1
            target = -1 * (nums[i])
            while l < r:
                if l == i:
                    l = l + 1
                elif r == i:
                    r = r - 1
                else:                    
                    twoSum = nums[l] + nums[r]
                    if twoSum > target:
                        r = r - 1
                    elif twoSum < target:
                        l = l + 1
                    else:
                        key = tuple(sorted([nums[i], nums[l] , nums[r]]))
                        if key not in added:
                            res.append([nums[i], nums[l] , nums[r]])
                            added.add(key)                        
                        r = r - 1
                        l = l + 1

        return res