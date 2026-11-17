class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # edge case: 
        if s[0] in ")]}":
            return False
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif char == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif char == "]":
                if not stack or stack.pop() != "[":
                    return False
        return not stack
        