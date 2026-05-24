class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> menu({{'}', '{'}, {']', '['}, {')', '('}});
        stack<char> kitchenBench;

        for (char item : s) {      // 1. start processing items from the conveyor belt
            if (menu.count(item)) {  // 2. Is it a suchi piece?
            if (!kitchenBench.empty() && kitchenBench.top() == menu[item]) {
                // 3. Check that we have at least one plate and that the style matches
                // the what the sushi piece requires. If it does, we can remove the
                // plate and serve the sushi
                kitchenBench.pop();
            } else {
                // We don't have the right plate for the sushi piece
                return false;
            }
            } else {  // 4. Put the dish on the kitchen bench
            kitchenBench.push(item);
            }
        }
        // 5. All orders are processed, the kitchen bench must be empty!
        return kitchenBench.empty();
    }
};
