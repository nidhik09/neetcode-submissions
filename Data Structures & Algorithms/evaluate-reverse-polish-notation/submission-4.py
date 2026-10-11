# class Solution:
#     def evalRPN(self, tokens):
#         def helper(i):
#             # returns (value, index of last consumed token)
#             if tokens[i] not in {"+", "-", "*", "/"}:
#                 return int(tokens[i]), i - 1
#             right, j = helper(i - 1)
#             left, k = helper(j)
#             if tokens[i] == "+":
#                 val = left + right
#             elif tokens[i] == "-":
#                 val = left - right
#             elif tokens[i] == "*":
#                 val = left * right
#             else:
#                 val = int(left / right)  # truncate toward zero
#             return val, k

#         return helper(len(tokens) - 1)[0]
class Solution:
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                right = stack.pop()
                left = stack.pop()
                stack.append((t, left, right))
            else:
                stack.append(int(t))

        def evaluate(node):
            if isinstance(node, int):
                return node
            op, left, right = node
            l, r = evaluate(left), evaluate(right)
            if op == "+":
                return l + r
            if op == "-":
                return l - r
            if op == "*":
                return l * r
            return int(l / r)  # truncate toward zero

        return evaluate(stack[0])