def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
 if y== 0:
    return "Error: Division by zero."
 else:
    return x / y

def main():
    while True:
       print("\n###########\nCalculator!\n###########\n")
       print("Select Operation:")
       print("1. Add")
       print("2. Subtract")
       print("3. Multiply")
       print("4. Divide")

       choice = input("Enter Choice (1/2/3/4): ")
       print("###########\n")

       if choice in ('1', '2', '3', '4'):
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero.")
                else:
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
       else:
           print("Invalid Input")

           another_calculation = input("Do you want to perform another calculation? (yes/no): ")
           if another_calculation.lower() != "yes":
               break
if __name__ == "__main__":
  main()