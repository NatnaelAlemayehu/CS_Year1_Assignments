import saving_account_class
import current_account_class
import sys

#Test methods and results
# Test 1: In the case that the user inputs a character instead of letter when asked for an account number the code
# code can handle this case in each condition through the exception handling code block
# Test 2: Whenever an account is created each account number is given unique account number hence there won't be
# a duplicate or overiding of an exisiting account
# Test 3: The method, validitycheck, checks wheather or not a user can send or recieve money based on their
# current standing account balance
# Test 4: Since there is no password given when an account is created if a user has the account number of someone else
# he/she can easily take control of the other persons account
# Test 5: A user can not use any of the services unless they don't have a bank account. Only those with
# bank account number are able to make transactions, check balance and make deposits
# Test 6: User can create saving account and current account without an error. 
# Test 7: Transaction takes place successfully for both same and differnet types of bank account

#The Algortihm
#to create saving account and current account I created two different files with similar
#methdology of code inside. Then I created an instance of each type of account and store it a dictionary
#where the account number would be a key and the object would be the value. The reason being using 
#dictionary makes storing and accessing any information related to an account/ account number very easy.


#main function
def choice():   
    user_input = input('''    press 1 to create a current account
    press 2 to create savings account
    press 3 to deposit money 
    press 4 to withdraw money
    press 5 to check balance 
    press 6 to transfer money 
    press any other key to exit \n''')
    if user_input == "1":
        current_account_class.create_current_account()       
        
    elif user_input == "2":
        saving_account_class.create_saving_account()      

    elif user_input == "3":
        print(list(current_account_class.user_account_object.keys()))
        customer_account_number = input(
            "Please type in your account number \n")
        try:
            customer_account_number_int = int(customer_account_number)
        except ValueError:
            print("Account number should be numbers only. Try again \n")
            choice()
        # if statement checks if account number exists in the user account dictionary
        if customer_account_number_int in list(saving_account_class.user_account_object.keys()):
            saving_account_class.deposit_money(customer_account_number_int)
        elif customer_account_number_int in list(current_account_class.user_account_object.keys()):
            current_account_class.deposit_money(customer_account_number_int)
        else:
            print("Account doesn't exist")
            choice()

    elif user_input == "4":        
        customer_account_number = input(
            "Please type in your account number \n")
        try:
            customer_account_number_int = int(customer_account_number)
        except ValueError:
            print("Account number should be numbers only. Try again \n")
            choice()
        # if statement checks if account number exists in the user account dictionary
        if customer_account_number_int in list(saving_account_class.user_account_object.keys()):
            saving_account_class.check_money(customer_account_number_int)
        elif customer_account_number_int in list(current_account_class.user_account_object.keys()):
            current_account_class.check_money(customer_account_number_int)
        else:
            print("Account doesn't exist")
            choice()

    elif user_input == "5":
        customer_account_number = input(
            "Please type in your account number \n")
        try:
            customer_account_number_int = int(customer_account_number)
        except ValueError:
            print("Account number should be numbers only. Try again \n")
            choice()
        # if statement checks if account number exists in the user account dictionary
        if customer_account_number_int in list(saving_account_class.user_account_object.keys()):
            saving_account_class.check_money(customer_account_number_int)
        elif customer_account_number_int in list(current_account_class.user_account_object.keys()):
            current_account_class.check_money(customer_account_number_int)
        else:
            print("Account doesn't exist")
            choice() 

    elif user_input == "6":
        customer_account_number = input(
            "Please type in your account number \n")
        try:
            customer_account_number_int = int(customer_account_number)
        except ValueError:
            print("Account number should be numbers only. Try again \n")
            choice()
        # if statement checks if account number exists in the user account object dcitionary
        if customer_account_number_int in list(saving_account_class.user_account_object.keys()):
            saving_account_class.transfer_money(customer_account_number_int)
        elif customer_account_number_int in list(current_account_class.user_account_object.keys()):
            current_account_class.transfer_money(customer_account_number_int)
        else:
            print("Account doesn't exist. Please create account first \n")
            choice()  
                     
    else:
        sys.exit()

# code runs when executed only from this file. If this file gets imported to another file as a 
# module the fucntion won't run automatically thus aviods repetition.
if __name__ == "__main__":
    print(" ---------------------------------------------- ")
    print("|   Welcome to Dangote Bank Customer Service.  |")
    print(" ---------------------------------------------- ")  
    choice()


