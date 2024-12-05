def calculator(expression: str) -> float:
    def evaluate(ops, nums):
        """Helper function to apply an operator to the top two numbers."""
        operator = ops.pop()
        b = nums.pop()
        a = nums.pop()
        if operator == '+':
            nums.append(a + b)
        elif operator == '-':
            nums.append(a - b)
        elif operator == '*':
            nums.append(a * b)
        elif operator == '/':
            nums.append(a / b)

    def precedence(op):
        """Helper function to define operator precedence."""
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    nums = []  # Stack for numbers
    ops = []   # Stack for operators
    i = 0      # Index to traverse the expression

    while i < len(expression):
        char = expression[i]

        if char.isdigit():
            # Parse multi-digit numbers
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            nums.append(num)
            continue

        elif char == '(':
            # Push open parenthesis
            ops.append(char)

        elif char == ')':
            # Solve everything inside parentheses
            while ops and ops[-1] != '(':
                evaluate(ops, nums)
            ops.pop()  # Remove the '('

        elif char in '+-*/':
            # Process current operator based on precedence
            while ops and precedence(ops[-1]) >= precedence(char):
                evaluate(ops, nums)
            ops.append(char)

        i += 1

    # Final evaluation of remaining operators
    while ops:
        evaluate(ops, nums)

    return nums[0]

# Example Usage
expression = "3+(2*2)-5/(1+1)"
result = calculator(expression)
print(f"The result of '{expression}' is: {result}")
