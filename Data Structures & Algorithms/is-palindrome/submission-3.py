class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < len(s) and j >= 0:
            left = s[i].lower()
            right = s[j].lower()

            if not left.isalnum():
                
                i += 1
                continue

            
            if not right.isalnum():
                j -= 1
                continue

            print(f"{left} != {right}")

            if left != right:
                return False

            i += 1
            j -= 1


 
        return True




