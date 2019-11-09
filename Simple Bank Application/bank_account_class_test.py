from bank_account_class import Bankaccount

account = Bankaccount("Nati", 200, "saving")
print(account)

account.check_balance()
print(account.check_balance())

account.withdraw(200)
print(account.check_balance())

account.sendbalance(200)
print(account.sendbalance(200))

account.receivebalance(200)
print(account.receivebalance(200))
