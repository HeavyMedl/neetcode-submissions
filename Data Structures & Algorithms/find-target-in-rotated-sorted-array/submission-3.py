class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, res = 0, len(nums) - 1, -1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # |6| |1,2,3,4,5| target = 1
            #  l
            #              r
            #.       m

            # with a rotated array, we have 2 sorted sections
            # we need to determine what portion of the
            # array we're in, left or right, relative to m

            if nums[l] <= nums[m]: # we're in the left sorted section
                # now we need to compare the values of m and l against the target
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # we need to compare the values of m and r against the target
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return res
