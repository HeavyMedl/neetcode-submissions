class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
          // we need to create a signature for each string so that we
  // can correctly group each anagram according to its signature
  // wihin a hashmap, where each key represents the signature,
  // and each value is the array of anagrams.

  // start with the hashmap we'll use for grouping
  unordered_map<string, vector<string>> anagramGroups;

  // now we loop through the strings
  for (const auto& str : strs) {
    // Here is the signature [0,0,...,0]
    vector<int> signature(26, 0);

    // count the frequency.
    for (char c : str) {
      // use the ascii value of each char to define the
      // signature which will end up as the key
      signature[c - 'a']++;
    }

    // Convert the vector to the signature key string
    // for hashing
    string signatureKey;
    for (const auto& count : signature) {
      signatureKey += to_string(count) += '#';
    }

    anagramGroups[signatureKey].push_back(str);
  }

  // iterate through the values of the map,

  vector<vector<string>> result;
  result.reserve(anagramGroups.size());  // Preallocate space

  for (const auto& pair : anagramGroups) {
    result.push_back(pair.second);
  }

  return result;
    }
};
