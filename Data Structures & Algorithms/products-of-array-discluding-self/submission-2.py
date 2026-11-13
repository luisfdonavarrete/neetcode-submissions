class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        suffixes = [1] * len(nums)
        
        acc = 1
        for i in range(0, len(nums)):
            acc = acc * nums[i]
            prefixes.append(acc)

        acc = 1
        for i in range(len(nums) - 1, 0, -1):
            acc = acc * nums[i]
            suffixes[i] = acc

        res = []
        for i in range(len(nums)):
            pre = 1 if i - 1 < 0 else prefixes[i - 1]
            post = 1 if i + 1 >= len(nums) else suffixes[i + 1]
            res.append(pre * post)
        
        return res;
         