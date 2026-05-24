class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        prevNum = None
        length = len(nums) - 1
        for i in range(length):
            num = nums[i]
            if num != prevNum:
                # two sum 2.. 
                # input: [-2,0,0,2,2]
                #          n l     r
                l, r = i + 1, length
                while l < r:
                    if nums[l] + nums[r] + num > 0:
                        r -= 1
                    elif nums[l] + nums[r] + num < 0:
                        l += 1
                    else:
                        result.append([num, nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1

            prevNum = num
        return result

