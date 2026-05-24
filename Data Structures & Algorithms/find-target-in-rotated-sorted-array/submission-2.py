class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l, r = 0, len(nums) - 1

        # [3,4,5,6,1,2] t = 2
        #.       l
        #.           r 
        #.         m 

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # determine the left/right portions relative to M
            if nums[l] <= nums[m]:
                # left sorted portion
                if target > nums[m]:
                    l = m + 1
                elif target < nums[l]:
                    l = m + 1 
                else:
                    r = m - 1
            else:
                # right sorted portion
                if target < nums[m]:
                    r = m - 1
                elif target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return res
