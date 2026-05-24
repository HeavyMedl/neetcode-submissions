class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # <--1,2,3,4--100--200-->
        # first convert list to set, so we have a o(1) lookup for
        # left and right neighbors
        numSet = set(nums)

        # We'll iterate through the list
        # [2,20,4,10,3,4,5]
        #  ^

        longestConsecutiveSeq = 0
        for num in nums:
            seq = 0
            # is this num the start of seq?
            # check if the previous number exists in the numSet
            if num - 1 not in numSet:
                # its the start of a seq
                seq = 1
                n = num + 1
                while n in numSet:
                    seq += 1
                    n += 1

            longestConsecutiveSeq = max(longestConsecutiveSeq, seq)

        return longestConsecutiveSeq
