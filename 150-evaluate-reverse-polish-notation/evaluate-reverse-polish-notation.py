class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        possible_operations=['+', '-', '*', '/']
        for token in tokens:
            if token not in possible_operations:
                stack.append(int(token))
            else:
                operand2 = stack.pop(-1)
                operand1 = stack.pop(-1)
                if token == '+':
                    stack.append(operand1+operand2)
                elif token == '-':
                    stack.append(operand1-operand2)
                elif token == '*':
                    stack.append(operand1*operand2)
                else:
                    stack.append(int(operand1/operand2))
        return stack[-1]