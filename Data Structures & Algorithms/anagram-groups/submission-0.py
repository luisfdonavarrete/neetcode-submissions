class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = {}
        for word in strs: 
            arr = [0] * 26
            for letter in word:
                i = ord(letter) - ord('a')
                arr[i] = 1 + arr[i]
            key = tuple(arr)
            if key in hashMap:
                hashMap[key].append(word)
            else:
                hashMap[key] = [word]
        
        return [*hashMap.values()]