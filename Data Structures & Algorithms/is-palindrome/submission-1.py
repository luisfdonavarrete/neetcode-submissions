class Solution:
    def isPalindrome(self, s: str) -> bool:


        a_code = ord('a')
        z_code = ord('z')

        code_0 = ord('0')
        code_9 = ord('9')
        
        normalize_s = ""
        
        for c in s:
            lower = c.lower()
            if (ord(lower) >= a_code and ord(lower) <= z_code) or (ord(lower) >= code_0 and ord(lower) <= code_9):
                normalize_s += lower

        i, j = 0, len(normalize_s) - 1

        while i < len(normalize_s):
            if normalize_s[i] != normalize_s[j]: 
                return False
            i += 1
            j -=1
 
        return True




