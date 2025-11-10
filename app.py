# app.py
# Simple Python application for Git practice

def greet_user(name):
    """Function to greet the user."""
    return f"Hello, {name}! Welcome to Git practice."

def add_numbers(a, b):
    """Function that returns the sum of two numbers."""
    return a + b

def main():
    print("=== Python Git Demo ===")
    name = input("Enter your name: ")
    print(greet_user(name))

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The sum is: {add_numbers(num1, num2)}")

if __name__ == "__main__":
    main()

