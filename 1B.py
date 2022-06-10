# define a class to represent A BANK ACCOUNT  include following details like name of depositor account number ,type of account ,balance amoount in account
# write methods to assign initial value to desposit an amount , withdsraw an amount after checking trhe balance , to display name , account number,account type, and  balance

accs = {}


class Bank_Account():
    def __init__(self):
        l = []
        self.accno = int(input("Account Number: "))

        self.name = input("Name: ")
        l.append(self.name)

        print("Choose account type: ")
        print("1. Savings Account")
        print("2. Current Account")
        print("3. Joint Account")

        self.choice = int(input("Choice: "))
        flag = 1
        while(flag):
            if self.choice == 1:
                l.append("Savings Account")
                flag = 0
            elif self.choice == 2:
                l.append("Joint Account")
                flag = 0
            elif self.choice == 3:
                l.append("Current Account")
                flag = 0
            else:
                print("Please select valid account type")
                flag = 1

        self.balance = int(input("Balance: "))
        l.append(self.balance)

        accs[self.accno] = l

    def print(self, accno):
        print(accno)
        print((accs[self.accno])[0])
        print((accs[self.accno])[1])
        print((accs[self.accno])[2])

    def deposit(self):
        dep = int(input("Deposit: "))
        accs[self.accno][2] += dep
   
    def withdsraw(self):
        withd=int(input("Withdraw: "))
        accs[self.accno][2] -= withd

b1 = Bank_Account()
acc = int(input("Account number: "))
b1.print(acc)
b1.deposit()
b1.print(acc)

