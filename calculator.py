
def calculate(a: float, operator: str, b: float) -> float | str:
    """Perform basic arithmetic on two numbers.

    Args:
        a: The first number.
        operator: The operation, one of +, -, *, /.
        b: The second number.
    """
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Unsupported operator"
