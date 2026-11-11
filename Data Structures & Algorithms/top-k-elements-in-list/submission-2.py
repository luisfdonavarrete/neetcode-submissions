class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = [[] for _ in range(len(nums) + 1)]         
        counter = {}
    
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
            
        for n, c in counter.items():
            groups[c].append(n)
            
        res = []
        
        for i in range(len(groups) - 1, 0, -1):
            for num in groups[i]:
                res.append(num)
                if len(res) >= k:
                    return res
        