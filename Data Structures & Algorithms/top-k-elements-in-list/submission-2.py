from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToCount = defaultdict(int)

        for n in nums:
            numToCount[n] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for n, c in numToCount.items():
            buckets[c].append(n)
        
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                if k > 0:
                    result.append(n)
                    k -= 1
                    if k == 0:
                        return result
        
        return result