class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)

        if n % 2 != 0:
            return False
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
    
        # Time Complexity: O(n) - We traverse the string once.
        # Space Complexity: O(n) - In the worst case, we might push all opening
        # brackets onto the stack.
        # n is the length of the input string s.
        # The algorithm uses a stack to keep track of opening brackets and
        # ensures that they are properly closed in the correct order.