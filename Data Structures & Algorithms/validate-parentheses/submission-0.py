class Solution:
    def isValid(self, s: str) -> bool:
        # maps close -> open
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in pairs:                       # it's a closing bracket
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:                                # it's an opening bracket
                stack.append(c)

        return not stack 