def addOp(*args):
    return sum(args)

def subOp(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def mulOp(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divOp(*args):
    try:
        result = args[0]
        for num in args[1:]:
            result /= num
        return result
    except ZeroDivisionError:
        return "Error: Division by zero."

def remOp(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a - b * (a // b)

def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input, please enter a numeric value.")

def main():
    operations = {'1': addOp, '2': subOp, '3': mulOp, '4': divOp, '5': remOp}
    while True:
        try:
            print("\nChoose an operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Remainder\n6. Exit")
            choice = input("Enter your choice (1-6): ")
            if choice == '6':
                break

            if choice in ['1', '2', '3', '4']:
                nums = list(map(float, input("Enter numbers separated by space: ").split()))
                result = operations[choice](*nums)
            elif choice == '5':
                a = get_numeric_input("Enter the first number: ")
                b = get_numeric_input("Enter the second number: ")
                result = operations[choice](a, b)
            else:
                print("Invalid choice. Please select a valid option.")
                continue

            print("Result:", result)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            continue

if __name__ == "__main__":
    main()
