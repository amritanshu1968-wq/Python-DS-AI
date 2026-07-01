try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    # attempt division
    result = numerator / denominator
    print("The result of the division is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
finally:
    print("BYE BYE")

