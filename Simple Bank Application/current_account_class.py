from bank_account_class import Bankaccount
import main_program
import saving_account_class

user_number = 0
#stores account numbers with account number as keys and the account object as value
user_account_object = {}

class Currentaccount(Bankaccount):
    def __init__(self, name, balance, deposit_duration, typeofaccount="current"):
        super().__init__(name, balance, typeofaccount)
        self.deposit_duration = deposit_duration        
        if deposit_duration >= 1:
            self.interest = 0.01 * self.balance
            self.balance = self.balance + self.interest        
    def deposit(self, amt):
        if self.deposit_duration >= 1:
            self.balance = self.balance + amt
            self.interest = 0.01 * self.balance
            self.balance = self.balance + self.interest            
        else:
            self.balance = self.balance + amt


def create_current_account(): 
    global user_number   
    customer_name = input("Type in full name. \n")
    inital_deposit = input(
        "How much do you want to deposit? Input numbers only. \n")
    # this block tries to convert user account input to an int value
    deposit_duration = input('''How many months do you want to put the money in your current account. 
Numbers only allowed. \n''')
    try:
        inital_deposit = int(inital_deposit)
        deposit_duration = int(deposit_duration)
    except ValueError:
        print("Only numbers are allowed. Try again")
        main_program.choice()
    if inital_deposit < 0:
        print("Amount can't be negative.")
        main_program.choice()
    user_account_object.update({Bankaccount.initial_account: Currentaccount(
        customer_name, inital_deposit, deposit_duration)})
    print("Account has been successfully created.",
          "Your account number is", str(Bankaccount.initial_account - 1))
    user_number += 1
    main_program.choice()

def deposit_money(account):
    deposit_amt = input("Enter your amount to deposit \n")
    try:
        deposit_amt = int(deposit_amt)
    except ValueError:
        print("Only numbers are allowed. Try again")
        main_program.choice()
    if deposit_amt < 0:
        print("Amount can't be negative.")
        main_program.choice()    
    user_account_object[account].deposit(deposit_amt)
    print("you have deposited", deposit_amt)
    main_program.choice()

def withdraw_money(account):
    withdraw_amt = input("Enter your amount. \n")
    try:
        withdraw_amt = int(withdraw_amt)
    except ValueError:
        print("Only numbers are allowed. Try again")
        main_program.choice()
    if withdraw_amt < 0:
        print("Amount can't be negative.")
        main_program.choice()
    validity = user_account_object[account].validity_check(
        withdraw_amt)
    if validity:
        user_account_object[account].withdraw(
            withdraw_amt)
        print("You have successfully withdrawn", withdraw_amt)
        main_program.choice()
    else:
        print("The amount you put exceeded your current balance. Try again.")
        main_program.choice()


def check_money(customer_account_number_int):  
    checked_balance = user_account_object[customer_account_number_int].check_balance()
    print("Your current balance is", checked_balance)
    main_program.choice()     

def transfer_money(customer_account_number_int):    
    transfer_amount = input("Enter the amount to transfer.\n")
    try:
        transfer_amount = int(transfer_amount)
    except ValueError:
        print("Only numbers are allowed. Try again")
        main_program.choice()
    if transfer_amount < 0:
        print("Amount can't be negative.")
        main_program.choice()
    validity = user_account_object[customer_account_number_int].validity_check(
        transfer_amount)
    if validity:
        transfer_person_account = input(
            "Enter account to transfer money.\n")
        try:
            transfer_person_account_int = int(transfer_person_account)
        except ValueError:
            print("Account number should be numbers only. Try again \n")
            main_program.choice()  
        if transfer_person_account_int in list(user_account_object.keys()):
            #balance is substracted from the sender
            user_account_object[customer_account_number_int].sendbalance(
                transfer_amount)
            #balance is added to the receiver
            user_account_object[transfer_person_account_int].receivebalance(
                transfer_amount)
            print("USD " + str(transfer_amount) + " has been scueessfully sent to " +
                    user_account_object[transfer_person_account_int].name)
            main_program.choice()
        elif transfer_person_account_int in list(saving_account_class.user_account_object.keys()):
            #balance is substracted from the sender
            user_account_object[customer_account_number_int].sendbalance(
                transfer_amount)
            #balance is added to the receiver
            saving_account_class.user_account_object[transfer_person_account_int].receivebalance(
                transfer_amount)
            print("USD " + str(transfer_amount) + " has been scueessfully sent to " +
                  saving_account_class.user_account_object[transfer_person_account_int].name)
            main_program.choice()
        else:
            print("user doesn't exist. \n")
            main_program.choice()
    else:
        main_program.choice()
    
    
