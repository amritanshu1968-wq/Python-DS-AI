#encapsulation

#define a class named bank
class Bank:
#constructor: Automatically called when an object of the class is created
    def __init__(self):

#double underscore(__) makes it private (name)
        self.__balance = 100000      # private attribute
    def deposit(self, amount):
        self.__balance += amount
#display the current balance
    def show_balance(self):
        print(self.__balance)


#calling
b = Bank()
b.deposit(10000)
b.show_balance()  # Output: 110000


