class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # holds (temperature, index) pairs, decreasing temps

        for i, t in enumerate(temperatures):
            # Current day is warmer than days sitting on top of the stack
            while stack and t > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                res[stack_index] = i - stack_index
            stack.append((t, i))

        return res