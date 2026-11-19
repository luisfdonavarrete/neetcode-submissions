class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for n, c in counter.items():
            buckets[c].append(n)

        res = []

        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res

