class Solution:
    def isValid(self, s: str) -> bool:
        parenDict = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []

        for char in s:            
            if len(stack) > 0 and (char == '}' or char == ']' or char == ')'):
                openParen = stack.pop()

                if parenDict[char] != openParen:
                    return False

            else:
                stack.append(char)
        
        return len(stack) == 0