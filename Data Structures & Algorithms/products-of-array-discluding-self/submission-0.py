class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # compute prefix list
        # prefix will store our previous product. Initialize it to 1
        prefix = 1
        for i, num in enumerate(nums):
            result[i] = prefix
            prefix *= num

        # now we set result[i] = result[i] * suffix
        # and then set suffix *= nums[i]
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result