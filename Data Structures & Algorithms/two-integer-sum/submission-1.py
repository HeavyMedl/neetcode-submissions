class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i, num in enumerate(nums):
            compliment = target - num
            # If the compliment is within the numToIndex
            if compliment in numToIndex:
                return [numToIndex[compliment], i]
            else:
                numToIndex[num] = i
                
        return []