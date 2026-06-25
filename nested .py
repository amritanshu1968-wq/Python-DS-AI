age = int(input("Enter your age: "))
license = input("do you have a driving license? (yes/no): ")
if age >= 18:
    if license.lower() == "yes":
        print("you can drive")
    else:
        print("you need first make a driving license")
else:
    print("you are under age")