class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # initialize a dict
        char_count = {}
        
        # iterate through S, for each char in S, increment count to char_count
        # in the same block, decrement each char in the char_count

        for i, _ in enumerate(s):
            # char_count[char] = char_count.get(char, 0) + 1
            # char_count[char] = char_count.get(char, 0) + 1
            char_count[s[i]] = char_count.get(s[i], 0) + 1
            char_count[t[i]] = char_count.get(t[i], 0) - 1

        for val in char_count.values():
            if val != 0:
                return False

        return True