class Solution {
public:
vector<int> topKFrequent(vector<int>& nums, int k) {
  // Input: nums = [1,2,2,3,3,3], k = 2
  // Output: [2,3]
  // Input: nums = [7,7], k = 1
  // Output: [7]

  // we need a freq count
  unordered_map<int, int> freqCount;
  for (int num : nums) {
    freqCount[num]++;
  }
  // {1: 1, 2: 2, 3: 3 }
  // Now, we intiialize our buckets using the nums vector
  // size, since we can only have up to len(nums) count for
  // any x in nums.
  vector<vector<int>> buckets(nums.size() + 1);
  // Iterate through entries in the freq count map. We'll use
  // the count as the index that we'll insert into.
  for (const auto& pair : freqCount) {
    buckets[pair.second].push_back(pair.first);
  }
  // [[], [1], [2], [3], [], []]
  vector<int> result;
  // interate from the back of buckets, as the last index
  // would represent the largest count.
  for (int i = buckets.size() - 1; i >= 0; --i) {
    vector<int> bucket = buckets[i];
    for (int num : bucket) {
      if (result.size() == k) {
        return result;
      }
      result.push_back(num);
    }
  }

  return result;
}
};
