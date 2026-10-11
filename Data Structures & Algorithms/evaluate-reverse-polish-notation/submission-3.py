class Solution:
    def evalRPN(self, tokens):
        def helper(i):
            # returns (value, index of last consumed token)
            if tokens[i] not in {"+", "-", "*", "/"}:
                return int(tokens[i]), i - 1
            right, j = helper(i - 1)
            left, k = helper(j)
            if tokens[i] == "+":
                val = left + right
            elif tokens[i] == "-":
                val = left - right
            elif tokens[i] == "*":
                val = left * right
            else:
                val = int(left / right)  # truncate toward zero
            return val, k

        return helper(len(tokens) - 1)[0]