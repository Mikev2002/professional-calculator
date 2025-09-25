# main.py

from app.operation import operations
from app.calculator.calculator import Calculator

def print_help():
    print("""
Available commands:
  add, subtract, multiply, divide
  history  - show all previous calculations
  help     - show this message
  exit     - quit the calculator
""")

def main():
    print("Welcome to the Professional Calculator!")
    print_help()

    while True:
        try:
            command = input("\nEnter command: ").strip().lower()

            if command == "exit":
                print("Goodbye!")
                break
            elif command == "help":
                print_help()
            elif command == "history":
                for i, calc in enumerate(Calculator.get_history(), 1):
                    print(f"{i}: {calc.a} {calc.operation_func.__name__} {calc.b} = {calc.get_result()}")
            elif command in ["add", "subtract", "multiply", "divide"]:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                operation_map = {
                    "add": operations.add,
                    "subtract": operations.subtract,
                    "multiply": operations.multiply,
                    "divide": operations.divide
                }

                calc = Calculator.create_calculation(a, b, operation_map[command])
                print(f"Result: {calc.get_result()}")

            else:
                print("Invalid command. Type 'help' to see available commands.")
        except ValueError as ve:
            print(f"Error: {ve}")  # e.g., invalid number, divide by zero
        except Exception as e:
            print(f"Unexpected error: {e}")  # catch-all

if __name__ == "__main__":
    main()