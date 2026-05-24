class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nLen = len(nums)
        ans = [0] * (2 * nLen)
        for i in range(nLen):
            ans[i] = ans[i + nLen] = nums[i]
        return ans