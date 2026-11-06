# Simple Calculator
# Author: Mohammed Akbar Kittur

print("=== MY CALCULATOR ===")
print("Type 'exit' to stop")

while True:
    print("\nChoose: +  -  *  / %")
    choice = input("Enter operation (+,-,*,/,%) or exit: ")

    if choice == "exit":
        print("Thanks for using my calculator! Bye!")
        break

    if choice not in ["+", "-", "*", "/", "%"]:
        print("Invalid! Please enter + - * / %")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "+":
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == "-":
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == "*":
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == "/":
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
    elif choice == "%":
            if num2 == 0:
                print("Cannot do % by zero!")
            else:
                print(f"Result: {num1} % {num2} = {num1 % num2}")        