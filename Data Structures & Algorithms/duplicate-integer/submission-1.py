class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a dict that whose keys represent wht we've seen before
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = True
        return False