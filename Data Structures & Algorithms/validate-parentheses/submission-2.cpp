class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> parenMap = {
            {'(', ')'},
            {'{', '}'},
            {'[', ']'}
        };
        vector<char> stack;
        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push_back(c);
            } else if (!stack.empty() && parenMap[stack.back()] == c) {
                stack.pop_back();
            } else {
                return false;
            }
        }
        return stack.size() == 0;
    }
};
