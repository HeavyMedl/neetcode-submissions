class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = nums[0]

        # [3,4,5,6,1,2]
        #.         l
        #.         r
        #.         m

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            # compute middle
            m = (right + left) // 2 
            res = min(res, nums[m])

            if nums[m] >= nums[left]:
                left = m + 1
            else:
                right = m - 1
        
        return res;
