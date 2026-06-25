#wap to check whether the number is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

#wap to check whether the number is positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print(num, "is a positive number")
elif num < 0:
    print(num, "is a negative number")
else:
    print(num, "is zero")