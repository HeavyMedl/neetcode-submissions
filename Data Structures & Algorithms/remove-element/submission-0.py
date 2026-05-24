class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            nums[left] = nums[right]
            if nums[right] != val:
                left += 1
        
        return left