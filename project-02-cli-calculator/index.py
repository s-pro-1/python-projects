def calculate(expression):
    operator = None

    # Find the operator
    for op in ["+", "-", "*", "/"]:
        if op in expression:
            operator = op
            break

    if operator is None:
        print("Invalid operator.")
        return

    try:
        # Split the expression
        left, right = expression.split(operator)

        # Convert strings to numbers
        left = float(left)
        right = float(right)

        # Perform calculation
        if operator == "+":
            result = left + right
        elif operator == "-":
            result = left - right
        elif operator == "*":
            result = left * right
        elif operator == "/":
            if right == 0:
                print("Cannot divide by zero.")
                return
            result = left / right

        print(f"Result: {result}")

    except ValueError:
        print("Invalid number. Please enter an expression like 25+13.")


def main():
    print("=== CLI Calculator ===")

    while True:
        expression = input("\nEnter calculation (or 'q' to quit): ").strip()

        if expression.lower() == "q":
            print("Goodbye!")
            break

        calculate(expression)


if __name__ == "__main__":
    main()