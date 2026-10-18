# Lauren Chavez
# October 18, 2026

# Excercise 1: Basic Selection Structure

age = int(input("Enter your age: ")) 

if age >= 18:
    print("You are eligible to vote.")  
else:
    print("You are not eligible to vote.")  

# Excercise 2: Relational Comparison Operators

num1 = float( input("Enter the first number : " ))
num2 = float( input ("Enter the second number: "))

print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f" {num1} > {num2}: {num1 > num2}")
print(f"{num1} <= {num2}: {num1 <= num2}")
print(f"{num1} >= {num2}: {num1 >= num2}") 

# Excercise 3: AND Logical Operator
score = float(input("Enter your score: "))
attendance = float(input("Enter your attendance percentage: "))

if score >= 70 and attendance >= 80:
    print("You have passed the class.")
else:
    print("You did not pass the class.")

# Excercise 4: OR Logical Operator
has_student_id = input("Do you have a student ID? (yes/no): ").lower() 
has_library_card = input ("Do you have a library card? (yes/no): ").lower()

if has_student_id == "yes" or has_library_card == "yes":
    print("You may enter the library.")
else:
    print("You may not enter the library.") 

# Excercise 5: NOT Logical Operator

is_banned = input("Are you banned from the system? (yes/no): ").lower()

if not is_banned == "yes":
    print("You may access the system.") 
else: 
    print("Access denied.") 

# Excercise 6: Scholarship Eligibility and Operator Precendence

gpa = float(input("Enter your GPA: "))
volunteer_hours = float(input("Enter your volunteer hours: "))
leadership = input("Do you have a leadership position? (yes/no):").lower()

if gpa >= 3.5 and (volunteer_hours >= 50 or leadership == "yes"):
    print("You qualify for the scholarship.")
else:
    print("You do not qualify for the scholarship.")






