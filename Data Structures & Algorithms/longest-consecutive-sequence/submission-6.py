class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        d = {}

        for num in nums:
            d[num] = num
        
        res = 0
        for num in nums:
            if (num - 1) not in d:            
                counter = 0
                next_number = num
                while next_number in d:
                    counter = counter + 1
                    next_number = next_number + 1
                if counter > res:
                    res = counter

        return res