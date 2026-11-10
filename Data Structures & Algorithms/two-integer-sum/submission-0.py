class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indixes_by_number = {}
        i = 0
        j = 0
        for k in range(len(nums)):

            num = target - nums[k]

            if num in indixes_by_number:
                i = indixes_by_number[num]
                j = k
                pass

            indixes_by_number[nums[k]] = k
            
       
        return [i, j]