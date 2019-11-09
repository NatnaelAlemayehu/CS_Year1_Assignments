class Bankaccount: 
    initial_account = 1000455
    def __init__(self, name, balance, type_of_account):
        self.name = name
        self.account_number = Bankaccount.initial_account + 1
        self.balance = float(balance)
        self.interest = 0
        self.type_of_account = type_of_account
        Bankaccount.initial_account += 1

    def check_balance(self):
        return self.balance
    #method to add balance to account

    def deposit(self, amt):
        self.balance += float(amt)
        return self.balance
    #method to withdraw balance

    def withdraw(self, amt):
        self.balance -= float(amt)
        return self.balance
    #method to transfer balance

    def sendbalance(self, amt):
        self.balance -= float(amt)
        return self.balance
    
    def receivebalance(self, amt):
        self.balance += float(amt)
        return self.balance
    #method to chek if user has sufficent or non-sufficient balance for transactions

    def validity_check(self, amt):
        if float(amt) < self.balance:
            boolean = True
        else:
            boolean = False
        return boolean


