# Check if choice is one of the valid options
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")

    elif choice == '2':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")

    elif choice == '3':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")

    elif choice == '4':
        # Handle division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")

else:
    print("Invalid Input: Please select a valid option (1, 2, 3, or 4).")'''
