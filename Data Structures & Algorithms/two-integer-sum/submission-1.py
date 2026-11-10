class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        previous = {} # val : index
        i = 0

        for j, num in enumerate(nums):
            
            diff = target - num

            if diff in previous:
                i = previous[diff]
                break

            previous[num] = j


        return [i, j]