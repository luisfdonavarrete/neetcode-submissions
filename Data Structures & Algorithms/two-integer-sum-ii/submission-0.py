class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        lookup = {}
        for i in range(len(numbers)):
            d = target - numbers[i]
            if d in lookup:
                return [lookup[d], i + 1]
            
            lookup[numbers[i]] = i + 1
            