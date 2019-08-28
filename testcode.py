# class Question:
    
#     def trial(self):
#         user_name = input('what is your answer? ')
#         return user_name 

# example = Question()

# print(example.trial())

# bank account example from slack content
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self):
        deposit_amount = int(input('How much would you like to deposit? '))
        self.balance += deposit_amount
        print (f'Your account now holds ${self.balance}')

    def withdraw(self):
        withdrawal_amount = int(input('How much would you like to withdraw? '))
        while withdrawal_amount > self.balance:
            if withdrawal_amount > self.balance:
                print(f'You cannot withdraw that much as it will overdraw your account. Your account balance is ${self.balance}. Please try agian.')
                withdrawal_amount = int(input('How much would you like to withdraw? '))
        self.balance -= withdrawal_amount
        print(f'Your account balance is ${self.balance}.')
            


sarah = Account('Sarah', 100)
sarah.deposit()
sarah.withdraw()



