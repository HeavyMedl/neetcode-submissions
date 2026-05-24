class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // initialize an hash, compliment to index.
        unordered_map<int, int> complimentToIndex;

        // iterate through the array
        for (int i = 0; i < nums.size(); ++i) {
            // First compute the compliment
            int compliment = target - nums[i];
            // if we have the compliment stored in the map,
            // we're done, return the current index and the
            // found index from the map
            if (complimentToIndex.count(compliment)) { 
                // return 
                return {complimentToIndex[compliment], i};
            } else {
                // if we don't have the compiment, add it 
                // and the index at which it lives
                complimentToIndex.emplace(nums[i], i);
            }
        }

        return {};
    }
};
