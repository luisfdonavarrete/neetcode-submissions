class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sLetterCounts = {}
        tLetterCounts = {}

        for i in range(0, len(s)):
            if sLetterCounts.get(s[i]) is None: 
                sLetterCounts[s[i]] = 0
            sLetterCounts[s[i]] += 1

            if tLetterCounts.get(t[i]) is None: 
                tLetterCounts[t[i]] = 0
            tLetterCounts[t[i]] += 1

        for key, value in sLetterCounts.items():
            if key not in tLetterCounts or tLetterCounts[key] != value:
                return False

        return True