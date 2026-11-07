class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for num in nums:
            if visited.get(num) is not None:
                return True 
            else:
                visited[num] = True;

        return False;
        
            