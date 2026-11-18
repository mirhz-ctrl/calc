def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y

def calculator():
    operations = {'1': ('+', add), '2': ('-', subtract), '3': ('*', multiply), '4': ('/', divide)}
    while True:
        choice = input("\n1. Add, 2. Subtract, 3. Multiply, 4. Divide, 5. Exit: ")
        if choice == '5': break
        if choice in operations:
            try:
                n1, n2 = float(input("First number: ")), float(input("Second number: "))
                symbol, func = operations[choice]
                print(f"{n1} {symbol} {n2} = {func(n1, n2)}")
            except ValueError:
                print("Invalid numeric input.")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    calculator()
