class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramMap;

        for (int i = 0; i < strs.size(); ++i) {
            string sortedStr = strs[i];
            sort(sortedStr.begin(), sortedStr.end());
            anagramMap[sortedStr].push_back(strs[i]);
        }

        vector<vector<string>> groupedAnagrams;
        for (const auto& pair : anagramMap) {
            groupedAnagrams.push_back(pair.second);
        }

        return groupedAnagrams;
    }
};
