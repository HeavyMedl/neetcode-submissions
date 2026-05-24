class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # formula:
        #   size of window - max frequency <= k 

        # count = {X: 1}

        # X Y Y X
        # l
        #   r

        res = 0
        left = 0
        count = defaultdict(int)
        for right in range(len(s)):
            count[s[right]] += 1

            while (right - left) + 1 - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, (right - left) + 1)
        
        return res