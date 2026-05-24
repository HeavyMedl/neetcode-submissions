class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s)-1

        while left < right:
            while left < right and not self.isAlphaNum(s[left]):
                left += 1
            while right > left and not self.isAlphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left, right = left + 1, right - 1

        return True


    def isAlphaNum(self, c) -> bool:
        return (
            'A' <= c <= 'Z' or
            'a' <= c <= 'z' or
            '0' <= c <= '9'
        )
