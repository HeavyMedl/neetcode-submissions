class Solution {
public:
    bool isAnagram(string s, string t) {
        // if s and t have different amount of chars,
        // we can't be an anagram
        if (s.size() != t.size()) return false;
        
        // set up a map to count occurences of each char
        unordered_map<char, int> umap;

        // We count occurences of each char
        for (int i = 0; i < s.size(); ++i) {
            // increment the count of the current char in the map
            // if the char is not in the map yet, the count is initialized to 1
            umap[s[i]]++;
            umap[t[i]]--;
        }

        for (const auto& pair : umap) {
            if (pair.second != 0) return false;
        }

        return true;
    }
};
