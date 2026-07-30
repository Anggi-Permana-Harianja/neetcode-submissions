class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', ']': '[', '}': "{"}
        opening_brackets = ['(', '[', '{']
        stack = []

        for bracket in s:
            if bracket in opening_brackets:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                last_opening_bracket = stack.pop()
                if brackets[bracket] != last_opening_bracket:
                    return False
        return not stack