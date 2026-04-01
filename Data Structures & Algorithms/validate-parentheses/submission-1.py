class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            bracket = s[i]
            if bracket == '(' or bracket == '[' or bracket == '{':
                stack.append(bracket)
            else:
                if not stack:
                    return False

                top = stack.pop()
                if bracket == ')' and top != '(':
                    return False
                elif bracket == ']' and top != '[':
                    return False
                elif bracket == '}' and top != '{':
                    return False

        return not stack