class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredS = ''.join(ch for ch in s if ch.isalnum()).lower()
        i = 0
        j = len(filteredS) - 1

        print(filteredS)
        while i < j:
            if filteredS[i] != filteredS[j]:
                return False
            i += 1
            j -= 1

        return True