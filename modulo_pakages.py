import os
import sys
import math
import time
import uuid
import random
import string
from datetime import datetime
import pandas as pd

# ==========================================
# 1. DATETIME AND TIME OPERATIONS
# ==========================================
def datetime_operations():
    while True:
        print("\n------------------------------------")
        print("Datetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        print("------------------------------------")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            now = datetime.now()
            print(f"\nCurrent Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            
        elif choice == '2':
            try:
                d1_str = input("Enter the first date (YYYY-MM-DD): ").strip()
                d2_str = input("Enter the second date (YYYY-MM-DD): ").strip()
                d1 = datetime.strptime(d1_str, "%Y-%m-%d")
                d2 = datetime.strptime(d2_str, "%Y-%m-%d")
                diff = abs((d2 - d1).days)
                print(f"Difference: {diff} days")
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD.")
                
        elif choice == '3':
            try:
                fmt = input("Enter format pattern (e.g., %d-%m-%Y, %B %d, %Y): ").strip()
                now = datetime.now()
                print(f"Formatted Date: {now.strftime(fmt)}")
            except Exception as e:
                print(f"Error formatting date: {e}")
                
        elif choice == '4':
            input("Press Enter to START stopwatch...")
            start_time = time.time()
            input("Press Enter to STOP stopwatch...")
            elapsed = time.time() - start_time
            print(f"Elapsed Time: {elapsed:.2f} seconds")
            
        elif choice == '5':
            try:
                seconds = int(input("Enter countdown time in seconds: ").strip())
                print("Starting countdown...")
                while seconds > 0:
                    print(f"Time left: {seconds}s", end="\r")
                    time.sleep(1)
                    seconds -= 1
                print("\nTime's up!")
            except ValueError:
                print("Please enter a valid integer.")
                
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please select 1-6.")


# ==========================================
# 2. MATHEMATICAL OPERATIONS
# ==========================================
def mathematical_operations():
    while True:
        print("\n------------------------------------")
        print("Mathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        print("------------------------------------")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            try:
                num = int(input("Enter a number: ").strip())
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print(f"Factorial: {math.factorial(num)}")
            except ValueError:
                print("Please enter a valid integer.")
                
        elif choice == '2':
            try:
                p = float(input("Enter principal amount: ").strip())
                r = float(input("Enter rate of interest (in %): ").strip())
                t = float(input("Enter time (in years): ").strip())
                # Formula: A = P * (1 + r/100)^t
                amount = p * math.pow((1 + (r / 100)), t)
                print(f"Compound Interest: {amount:.2f}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                
        elif choice == '3':
            try:
                angle_deg = float(input("Enter angle in degrees: ").strip())
                rad = math.radians(angle_deg)
                print(f"sin({angle_deg}) = {math.sin(rad):.4f}")
                print(f"cos({angle_deg}) = {math.cos(rad):.4f}")
                print(f"tan({angle_deg}) = {math.tan(rad):.4f}")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
        elif choice == '4':
            print("\nSelect Shape:")
            print("a. Circle")
            print("b. Rectangle")
            print("c. Triangle")
            shape_choice = input("Enter shape choice (a/b/c): ").strip().lower()
            
            try:
                if shape_choice == 'a':
                    radius = float(input("Enter radius of circle: ").strip())
                    print(f"Area of Circle: {math.pi * radius * radius:.2f}")
                elif shape_choice == 'b':
                    l = float(input("Enter length: ").strip())
                    w = float(input("Enter width: ").strip())
                    print(f"Area of Rectangle: {l * w:.2f}")
                elif shape_choice == 'c':
                    b = float(input("Enter base: ").strip())
                    h = float(input("Enter height: ").strip())
                    print(f"Area of Triangle: {0.5 * b * h:.2f}")
                else:
                    print("Invalid shape selection.")
            except ValueError:
                print("Invalid numerical value.")
                
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please select 1-5.")


# ==========================================
# 3. RANDOM DATA GENERATION
# ==========================================
def random_data_generation():
    while True:
        print("\n------------------------------------")
        print("Random Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        print("------------------------------------")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            try:
                start = int(input("Enter minimum range: ").strip())
                end = int(input("Enter maximum range: ").strip())
                print(f"Generated Random Number: {random.randint(start, end)}")
            except ValueError:
                print("Invalid range input.")
                
        elif choice == '2':
            try:
                size = int(input("Enter size of list: ").strip())
                start = int(input("Enter minimum value: ").strip())
                end = int(input("Enter maximum value: ").strip())
                rand_list = [random.randint(start, end) for _ in range(size)]
                print(f"Generated Random List: {rand_list}")
            except ValueError:
                print("Invalid input!")
                
        elif choice == '3':
            try:
                pwd_len = int(input("Enter password length: ").strip())
                chars = string.ascii_letters + string.digits + string.punctuation
                password = "".join(random.choice(chars) for _ in range(pwd_len))
                print(f"Generated Password: {password}")
            except ValueError:
                print("Please enter a valid length.")
                
        elif choice == '4':
            otp = random.randint(100000, 999999)
            print(f"Generated OTP: {otp}")
            
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please select 1-5.")


# ==========================================
# 4. GENERATE UNIQUE IDENTIFIERS (UUID)
# ==========================================
def uuid_operations():
    print("\n------------------------------------")
    print("Generate Unique Identifiers:")
    generated_id = str(uuid.uuid4())
    print(f"Generated UUID: {generated_id}")
    print("------------------------------------")


# ==========================================
# 5. FILE OPERATIONS (CUSTOM MODULE SIMULATION)
# ==========================================
def file_operations():
    while True:
        print("\n------------------------------------")
        print("File Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        print("------------------------------------")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            filename = input("Enter file name: ").strip()
            try:
                with open(filename, 'w') as f:
                    pass
                print("File created successfully!")
            except Exception as e:
                print(f"Error creating file: {e}")
                
        elif choice == '2':
            filename = input("Enter file name: ").strip()
            data = input("Enter data to write: ")
            try:
                with open(filename, 'w') as f:
                    f.write(data + "\n")
                print("Data written successfully!")
            except Exception as e:
                print(f"Error writing to file: {e}")
                
        elif choice == '3':
            filename = input("Enter file name: ").strip()
            if os.path.exists(filename):
                try:
                    with open(filename, 'r') as f:
                        content = f.read()
                    print("File Content:")
                    print(content.strip())
                except Exception as e:
                    print(f"Error reading file: {e}")
            else:
                print("File does not exist!")
                
        elif choice == '4':
            filename = input("Enter file name: ").strip()
            data = input("Enter data to append: ")
            try:
                with open(filename, 'a') as f:
                    f.write(data + "\n")
                print("Data appended successfully!")
            except Exception as e:
                print(f"Error appending file: {e}")
                
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please select 1-5.")


# ==========================================
# 6. EXPLORE MODULE ATTRIBUTES (dir())
# ==========================================
def explore_module_attributes():
    print("\n------------------------------------")
    print("Explore Module Attributes:")
    mod_name = input("Enter module name to explore: ").strip()
    
    known_modules = {
        'math': math,
        'datetime': datetime,
        'time': time,
        'random': random,
        'uuid': uuid,
        'os': os,
        'sys': sys
    }
    
    target_module = known_modules.get(mod_name)
    
    if target_module is None:
        try:
            target_module = __import__(mod_name)
        except ImportError:
            print(f"Module '{mod_name}' not found!")
            return
            
    attributes = dir(target_module)
    print(f"Available Attributes in {mod_name} module:")
    if len(attributes) > 10:
        preview = attributes[:10]
        preview.append("...")
        print(preview)
    else:
        print(attributes)
    print("------------------------------------")


# ==========================================
# MAIN MENU CONTROLLER
# ==========================================
def main():
    while True:
        print("\n====================================")
        print("Welcome to Multi-Utility Toolkit")
        print("====================================")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("====================================")
        
        user_choice = input("Enter your choice: ").strip()
        
        if user_choice == '1':
            datetime_operations()
        elif user_choice == '2':
            mathematical_operations()
        elif user_choice == '3':
            random_data_generation()
        elif user_choice == '4':
            uuid_operations()
        elif user_choice == '5':
            file_operations()
        elif user_choice == '6':
            explore_module_attributes()
        elif user_choice == '7':
            print("\n====================================")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("====================================")
            break
        else:
            print("Invalid option! Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()