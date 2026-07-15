import datetime
import time
import math
import random
import uuid

def create_file(filename):
    try:
        with open(filename, 'w') as f:
            pass
        return "File created successfully!"
    except Exception as e:
        return f"Error: {e}"

def write_to_file(filename, data):
    try:
        with open(filename, 'w') as f:
            f.write(data)
        return "Data written successfully!"
    except Exception as e:
        return f"Error: {e}"

def read_from_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {e}"

def append_to_file(filename, data):
    try:
        with open(filename, 'a') as f:
            f.write("\n" + data)
        return "Data appended successfully!"
    except Exception as e:
        return f"Error: {e}"

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def datetime_menu():
    while True:
        print("\n" + "="*30)
        print("Datetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        print("="*30)
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            now = datetime.datetime.now()
            print(f"\nCurrent Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        
        elif choice == '2':
            try:
                d1_str = input("Enter the first date (YYYY-MM-DD): ")
                d2_str = input("Enter the second date (YYYY-MM-DD): ")
                d1 = datetime.datetime.strptime(d1_str, "%Y-%m-%d")
                d2 = datetime.datetime.strptime(d2_str, "%Y-%m-%d")
                diff = abs((d2 - d1).days)
                print(f"Difference: {diff} days")
            except ValueError:
                print("Invalid date format! Use YYYY-MM-DD.")
                
        elif choice == '3':
            try:
                d_str = input("Enter date (YYYY-MM-DD): ")
                d = datetime.datetime.strptime(d_str, "%Y-%m-%d")
                print("Custom Formats:")
                print(f"Format 1 (DD/MM/YYYY): {d.strftime('%d/%m/%Y')}")
                print(f"Format 2 (Month Day, Year): {d.strftime('%B %d, %Y')}")
            except ValueError:
                print("Invalid date format!")
                
        elif choice == '4':
            input("Press Enter to START the stopwatch...")
            start_time = time.time()
            input("Press Enter to STOP the stopwatch...")
            end_time = time.time()
            print(f"Elapsed Time: {round(end_time - start_time, 2)} seconds")
            
        elif choice == '5':
            try:
                seconds = int(input("Enter countdown time in seconds: "))
                print("Starting countdown...")
                for i in range(seconds, 0, -1):
                    print(f"{i}...", end="\r", flush=True)
                    time.sleep(1)
                print("Time's up!")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == '6':
            break
        else:
            print("Invalid Choice!")


def math_menu():
    while True:
        print("\n" + "="*30)
        print("Mathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        print("="*30)
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                num = int(input("Enter a number: "))
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print(f"Factorial: {math.factorial(num)}")
            except ValueError:
                print("Please enter a valid integer.")
                
        elif choice == '2':
            try:
                p = float(input("Enter principal amount: "))
                r = float(input("Enter rate of interest (in %): "))
                t = float(input("Enter time (in years): "))
                n = int(input("Number of times interest compounded per year (e.g., 1, 4, 12): "))
                amount = p * math.pow((1 + (r / (100 * n))), n * t)
                print(f"Total Accumulated Amount: {round(amount, 2)}")
                print(f"Compound Interest: {round(amount - p, 2)}")
            except ValueError:
                print("Invalid input values.")
                
        elif choice == '3':
            try:
                deg = float(input("Enter angle in degrees: "))
                rad = math.radians(deg)
                print(f"Sine: {round(math.sin(rad), 4)}")
                print(f"Cosine: {round(math.cos(rad), 4)}")
                print(f"Tangent: {round(math.tan(rad), 4)}")
            except ValueError:
                print("Invalid input.")
                
        elif choice == '4':
            print("Select Shape:\n1. Circle\n2. Rectangle")
            shape = input("Choice: ")
            if shape == '1':
                r = float(input("Enter radius: "))
                print(f"Area of Circle: {round(math.pi * r * r, 2)}")
            elif shape == '2':
                l = float(input("Enter length: "))
                w = float(input("Enter width: "))
                print(f"Area of Rectangle: {l * w}")
                
        elif choice == '5':
            break
        else:
            print("Invalid Choice!")


def random_menu():
    while True:
        print("\n" + "="*30)
        print("Random Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        print("="*30)
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            low = int(input("Enter lower bound: "))
            high = int(input("Enter upper bound: "))
            print(f"Random Int: {random.randint(low, high)}")
            
        elif choice == '2':
            size = int(input("List size: "))
            print(f"Generated List: {[random.randint(1, 100) for _ in range(size)]}")
            
        elif choice == '3':
            length = int(input("Enter password length: "))
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
            pwd = "".join(random.choice(chars) for _ in range(length))
            print(f"Generated Password: {pwd}")
            
        elif choice == '4':
            otp = "".join(random.choice("0123456789") for _ in range(6))
            print(f"Generated 6-Digit OTP: {otp}")
            
        elif choice == '5':
            break
        else:
            print("Invalid Choice!")


def file_ops_menu():
    while True:
        print("\n" + "="*30)
        print("File Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        print("="*30)
        
        choice = input("Enter your choice: ")
        if choice in ['1', '2', '3', '4']:
            fname = input("Enter file name: ")
            
            if choice == '1':
                print(create_file(fname))
            elif choice == '2':
                data = input("Enter data to write: ")
                print(write_to_file(fname, data))
            elif choice == '3':
                print("\nFile Content:")
                print(read_from_file(fname))
            elif choice == '4':
                data = input("Enter data to append: ")
                print(append_to_file(fname, data))
        elif choice == '5':
            break
        else:
            print("Invalid Choice!")


def main():
    while True:
        print("\n" + "="*30)
        print("Welcome to Multi-Utility Toolkit")
        print("="*30)
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations(Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("="*30)
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            datetime_menu()
        elif choice == '2':
            math_menu()
        elif choice == '3':
            random_menu()
        elif choice == '4':
            print(f"\nGenerated UUID v4: {uuid.uuid4()}")
        elif choice == '5':
            file_ops_menu()
        elif choice == '6':
            mod_name = input("Enter module name to explore (e.g., math, random, datetime, uuid, time): ").strip()
            if mod_name in ['math', 'random', 'datetime', 'uuid', 'time']:
                try:
                    target_mod = __import__(mod_name)
                    print(f"\nAvailable Attributes in '{mod_name}' module:")
                    print(dir(target_mod))
                except Exception as e:
                    print(f"Error checking attributes: {e}")
            else:
                print("Module must be a standard imported module to check attributes.")
        elif choice == '7':
            print("\n" + "="*30)
            print("Thank you for using the Multi-Utility Toolkit!")
            print("="*30)
            break
        else:
            print("Invalid selection. Try again.")


if __name__ == '__main__':
    main()