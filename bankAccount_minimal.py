#Given the bankAccount class
#  from Week 9, question 2, create a subclass
#  MinimumBalanceAccount that inherits bankAccount. MinimumBalanceAccount should have
#  a minimum balance value and overwrite the method withdrawal so the new balance is
#  not below the minimum balance after withdrawing.

class BankAccount(object):

    def __init__(self, IBAN: str, account_number: int, available_funds=0):
        self.IBAN = IBAN
        self.account_number = account_number
        self.available_funds = available_funds
        self.transactions = []

    def deposit(self, amount: float):

        if type(amount) != float and type(amount) != int:
            print("Please pass a positive value for deposit")
            return

        if amount < 0:
            print("Deposit can only be positive")
            return

        self.available_funds += amount

        # if len(self.transactions) == 5:
        #     del self.transactions[0]

        self.transactions.append("Deposit of {}".format(amount))

    def withdraw(self, amount: float):

        if type(amount) != float and type(amount) != int:
            print("Please pass a positive value for withdraw")
            return

        if amount < 0:
            print("Withdraw can only be positive")
            return

        if self.available_funds - amount < 0:
            print("Not enough funds for withdraw")
            return

        self.available_funds -= amount

        # if len(self.transactions) == 5:
        #     del self.transactions[0]

        self.transactions.append("Withdraw of {}".format(amount))

    def __str__(self):
        account_info = "IBAN: " + self.IBAN + "\n"
        account_info += "Account number: " + str(self.account_number) + "\n"
        account_info += "Available funds: " + str(self.available_funds) + "\n\n"

        account_info += "Transactions: " + "\n"
        if len(self.transactions) >= 5:
            for i in range(-5, 0):
                account_info += str(self.transactions[i]) + "\n"
        else:
            for transaction in self.transactions:
                account_info += transaction

        return account_info

class MinimalBalanceAccount(BankAccount):
    def __init__(self,IBAN: str, account_number: int, available_funds=0,minimal_balance=0):
        BankAccount.__init__(self,IBAN,account_number,available_funds)
        self.minimal_balance = minimal_balance

    def __str__(self):
        result_str = 'Minimal balance account'+'\n'+BankAccount.__str__(self)
        result_str+='Minimal balance: {}'.format(self.minimal_balance)
        return result_str
    def withdraw(self, amount):
        if self.minimal_balance>(self.available_funds-amount):
            print("Unable to withdraw money")
        else:
            if type(amount) != float and type(amount) != int:
                print("Please pass a positive value for withdraw")
                return

            if amount < 0:
                print("Withdraw can only be positive")
                return

            if self.available_funds - amount < 0:
                print("Not enough funds for withdraw")
                return

            self.available_funds -= amount

            # if len(self.transactions) == 5:
            #     del self.transactions[0]

            self.transactions.append("Withdraw of {}".format(amount))


# Main scope
lucas_account = BankAccount("IE1234567", 1234567)
lucas_account.deposit(100)
lucas_account.withdraw(50)
lucas_account.withdraw(25)
lucas_account.deposit(101)
lucas_account.deposit(110)
lucas_account.withdraw(10)
print(lucas_account)
new_account = MinimalBalanceAccount("13Eef",333,1000,200)
print(new_account)
new_account.withdraw(500)
print(new_account)
new_account.withdraw(300)
print(new_account)
new_account.withdraw(100)
print(new_account)