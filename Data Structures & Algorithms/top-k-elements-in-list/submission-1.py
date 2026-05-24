class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first add buckets. The maximum number of any k is the
        # length of the input nums
        buckets = [[] for _ in range(len(nums) + 1)]

        # Now we count the occurences of each number
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1

        # print(buckets)
        # print(frequency)
        
        # now each value in the frequency dict maps to the index
        # of each bucket
        for num, freq in frequency.items():
            buckets[freq].append(num)

        result = []
        count = k

        for bucket in reversed(buckets):
            for num in bucket:
                if count == 0:
                    return result
                result.append(num)
                count -= 1
        
        return result


        