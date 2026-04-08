# Part 1: Simple Calculator

print("\n=== Part 1: Simple Calculator ===")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\nChoose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid choice")


# -----------------------------
# Part 2: Average Calculator
# -----------------------------
print("\n=== Part 2: Average Calculator ===")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

average = (num1 + num2)

print("The average is:", (average,))


# -----------------------------
# Part 3: Grade Evaluator
# -----------------------------
print("\n=== Part 3: Grade Evaluator ===")

grade = float(input("Enter your grade: "))

if grade >= 75:
    print("Result: Pass")
else:
    print("Result: Fail")

print("\n===== END OF PROGRAM =====")
