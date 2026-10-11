class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def helper(i):
        # tokens[i] is the operand/operator to evaluate
          if tokens[i] not in {"+", "-", "*", "/"}:
            return int(tokens[i]), i - 1
        # operator: its right operand is at i-1, then recurse for the left
          right, j = helper(i - 1)
          left, k = helper(j)
          if tokens[i] == "+":
             val = left + right
          elif tokens[i] == "-":
             val = left - right
          elif tokens[i] == "*":
             val = left * right
          else:
             val = int(left / right)   # truncate toward zero
          return val, k
        return helper(len(tokens) - 1)[0]
        