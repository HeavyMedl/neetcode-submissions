class Solution:
    def isValid(self, s: str) -> bool:
        # this solution involves creating a hash map to
        # map open parens/brackets and squirlies to closed ones

        # we must also create a "stack", which we'll use a standard
        # dynamic array/list for
        charMap = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []

        for char in s:
            # char can be an opening paren/bracket/squiggly, close paren/bracket/squiggles, 
            # or something else
            if char in charMap: # we are open
                stack.append(char)
            elif char == ')' or char == '}' or char == ']':
                # pop top of stack to see if we have a
                # matching open paren

                # if the stack is empty at this point return false
                if len(stack) == 0: return False
                topOpen = stack.pop()
                if charMap[topOpen] != char:
                    return False
        
        return len(stack) == 0