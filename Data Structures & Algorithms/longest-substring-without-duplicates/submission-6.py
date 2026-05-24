class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set z x y
        # z x y z x y z
        # l
        #       r

        left = 0
        charSet = set()
        result = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            result = max(result, (right - left) + 1)

        return result