class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> hashSet;
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            if (hashSet.count(num)) {
                return true;
            }
            hashSet.insert(num);
        }
        return false;
    }
};
