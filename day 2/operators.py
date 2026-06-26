#Arithmetic Operators

#Addition, Subtraction, Multiplication, Division
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)

#Quotient and Remainder
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Quotient =", a // b)
print("Remainder =", a % b)

#Square and Cube of a Number
a = int(input("Enter a number: "))
print("Square =", a ** 2)
print("Cube =", a ** 3)

#Area of a Circle
radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius ** 2
print("Area of the circle =", area)

#Simple Interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)

#compound interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
compound_interest = principal * (1 + rate / 100) ** time - principal
print("Compound Interest =", compound_interest)

#BMI Calculation
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print("Your BMI is:", bmi)


#Relational Operators
#Comparison of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("a > b =", a > b)
print("a < b =", a < b)
print("a == b =", a == b)
print("a != b =", a != b)
print("a >= b =", a >= b)
print("a <= b =", a <= b)

#logical Operators

#voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#Check Multiple of 3 and 5
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(num, "is a multiple of both 3 and 5.")
else:
    print(num, "is not a multiple of both 3 and 5.")

#Login System
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "password123":
    print("Login successful!")
else:
    print("Invalid username or password.")

#Assignment Operators
#Assignment operators Demo

a = 10

a += 5
print("After += :", a)

a -= 3
print("After -= :", a)

a *= 2
print("After *= :", a)

a /= 4
print("After /= :", a)

a %= 3
print("After %= :", a)

#Membership Operators
#Check character in a string
Text = input("Enter a string: ")
char = input("Enter a character to check: ")
if char in Text:
    print(char, "is present in the string.")
else:
    print(char, "is not present in the string.")

#Check number in a list
numbers = [1, 2, 3, 4, 5]
num = int(input("Enter a number to check: "))
if num in numbers:
    print(num, "is present in the list.")
else:
    print(num, "is not present in the list.")

#Identity Operators

#Identity operator
a = [10, 20, 30]
b = a
c = [10, 20, 30]
print(a is b)  # True, because b references the same object as a
print(a is c)  # False, because c is a different object with the same content
print(a is not c)  # True, because a and c are different objects

#Bitwise Operators

#bitwise operators demo
a = 5  # binary: 0101
b = 3  # binary: 0011
print("AND =", a & b)
print("OR =", a | b)
print("XOR =", a ^ b)
print("NOT =", ~a)
print("Left Shift =", a << 1)
print("Right Shift =", a >> 1)

#mixed Expression
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
result = (a + b) * c - a / b
print("Result =", result)

