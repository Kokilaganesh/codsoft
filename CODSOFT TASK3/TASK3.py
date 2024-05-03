def calculator() -> None:
    """A simple calculator for addition, subtraction, multiplication, and division."""
    print("Simple Calculator")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    print("\nSelect Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if choice not in [1, 2, 3, 4]:
        print("Invalid choice. Please enter a number between 1 and 4.")
        return

    if choice == 1:
        result = num1 + num2
        operation = "+"
    elif choice == 2:
        result = num1 - num2
        operation = "-"
    elif choice == 3:
        result = num1 * num2
        operation = "*"
    else:
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = round(num1 / num2, 2)
        operation = "/"

    print("\nResult:")
    print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()