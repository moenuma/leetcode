class Solution:
    # Time: O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                last = stack.pop()
                last2 = stack.pop()
                if token == "+":
                    stack.append(last + last2)
                elif token == "-":
                    stack.append(last2 - last)
                elif token == "*":
                    stack.append(last * last2)
                else:
                    stack.append(int(last2 / last))
            else:
                stack.append(int(token))

        return stack[0]