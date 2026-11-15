
# Question 1: Car Class

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print("The car is starting.")


car1 = Car("BMW", "Blue")
print("Brand:", car1.brand)
print("Color:", car1.color)
car1.start()


# Question 2: Book Class

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Book Title:", self.title)
        print("Author:", self.author)


book1 = Book("Python Basics", "John")
book2 = Book("Learn Programming", "Ali")
book3 = Book("Computer Science", "Ahmed")

book1.display_info()
book2.display_info()
book3.display_info()


# Question 3: Calculator Class

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        print("Addition:", self.num1 + self.num2)

    def subtraction(self):
        print("Subtraction:", self.num1 - self.num2)

    def multiplication(self):
        print("Multiplication:", self.num1 * self.num2)

    def division(self):
        if self.num2 != 0:
            print("Division:", self.num1 / self.num2)
        else:
            print("Cannot divide by zero.")


calc = Calculator(20, 10)

calc.addition()
calc.subtraction()
calc.multiplication()
calc.division()


# Question 4: BankAccount Class

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)


account1 = BankAccount("Murk", 5000)

account1.deposit(2000)
account1.withdraw(1000)
account1.display_balance()
