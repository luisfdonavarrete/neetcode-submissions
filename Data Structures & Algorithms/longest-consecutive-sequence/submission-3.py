class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        starts = [];
        d = {}

        for num in nums:
            d[num] = num
        
        for num in nums:
            if (num - 1) not in d:
                starts.append(num)

        res = 0
        for s in starts:
            c = 0
            while s in d:
                c = c + 1
                s = s + 1
            if c > res:
                res = c

        return res