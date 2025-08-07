def max_of_three(a, b, c):
    """Return the maximum of three numbers by comparison."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == "__main__":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        result = max_of_three(num1, num2, num3)
        print(f"The maximum of the three numbers is: {result}")
    except ValueError:
        print("Please enter valid numbers.")

