"""
Assignment: 56
Write a program to create a Bank class. Write an instance method to calculate
interest at the rate of 10% for the amount passed during object initialization.
Write two more classes Branch1 & Branch2. Branch1 & Branch2 will inherit from Bank class.
Override the interest calculation method, in Branch1 calculate interest rate at 11% and
in Branch2 calculate the interest rate at 9%.
Amount on which interest to be calculated will be passed during object creation.
Along with the respective branch interest amount display, also print the interest
calculation by Bank.
Hint: Call Bank calculation method from Branch classes
"""


class Bank:
    int_rate = 10

    def __init__(self, amount):
        self.amount = amount
        self.int_amt = 0

    def calc_int(self):
        bank_int = (self.amount * Bank.int_rate)/100
        return bank_int


class Branch1(Bank):
    int_rate = 11

    def __init__(self, amount):
        super().__init__(amount)
        self.amount = amount
        self.int_amt = 0

    def calc_int(self):
        bank_int = super().calc_int()
        branch_int = (self.amount * Branch1.int_rate)/100
        print(f"Interest amount to be paid in Bank: {bank_int}")
        print(f"Interest amount to be paid in Branch1: {branch_int}")


class Branch2(Bank):
    int_rate = 9

    def __init__(self, amount):
        super().__init__(amount)
        self.amount = amount
        self.int_amt = 0

    def calc_int(self):
        branch_int = (self.amount * Branch2.int_rate)/100
        bank_int = super().calc_int()
        print(f"Interest amount to be paid in Bank: {bank_int}")
        print(f"Interest amount to be paid in Branch2: {branch_int}")


bank = Bank(10000)
print(f"Interest amount for bank: {bank.calc_int()}")

brn1 = Branch1(10000)
brn1.calc_int()

brn2 = Branch2(10000)
brn2.calc_int()
