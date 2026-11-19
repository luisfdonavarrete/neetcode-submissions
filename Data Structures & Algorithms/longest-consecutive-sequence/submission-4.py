class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        d = {}

        for num in nums:
            d[num] = num
        
        res = 0
        for num in nums:
            if (num - 1) not in d:            
                c = 0
                b = num
                while b in d:
                    c = c + 1
                    b = b + 1
                if c > res:
                    res = c

        return res