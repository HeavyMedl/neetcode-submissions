class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, res, _set = 0, 0, 0, set()

        while r < len(s):
            while s[r] in _set:
                _set.remove(s[l])
                l += 1
            _set.add(s[r])
            res = max(res, (r - l)+ 1)
            r += 1 
        
        return res
