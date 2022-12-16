class PostfixCalculator:

    @staticmethod
    def compute(string: str) -> int:
        stack = []
        for e in string.split():
            match e:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
                case '/':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a // b)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case _:
                    stack.append(int(e))
        return stack[0]


