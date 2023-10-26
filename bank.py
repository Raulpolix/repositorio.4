class Bank_account:
    def __init__ (self,account_number,balance = 0):
        self.account_number = account_number
        self.balance = balance 
    def get_account_number(self):
        return self.account_number
    
    def add_funds(self,funds):
        self.balance += funds

    def get_balance(self):
        return self.balance
        
    

bank_account1 = Bank_account("ES8889994449398")

bank_account1.add_funds(29999)


class SavingAccount(Bank_account):
    def __init__(self, account_number,interest_rate, balance=0):
        super().__init__(account_number,balance)
        self.interest_rate = 5

    def interest_generated(self,months):
        interest = self.balance * self.interest_rate / 100 * months
        return interest


print(f"La cuenta con numero: {bank_account1.get_account_number()} tiene {bank_account1.get_balance()}$ en su balance")



