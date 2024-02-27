import time

class CustomerAccount:

    
    def __init__(self, customer_id, customer_name, account_balance):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.account_balance = int(account_balance)
        self.translog = str()
        
    
    def deposit(self,amount):
        self.account_balance += amount
        self.translog += (f"{time.ctime(time.time())} - id: {self.customer_id}, name: {self.customer_name}, deposit amount: "
                                  f"{amount}, balance status: {self.account_balance}\n")
        

    def withdraw(self,amount):
        self.account_balance += amount
        self.account_balance += amount
        self.translog += (f"{time.ctime(time.time())} - id: {self.customer_id}, name: {self.customer_name}, withdraw amount: "
                                  f"{amount}, balance status: {self.account_balance}\n")
        


    def __str__(self) -> str:
        return f"{self.customer_id}: {self.customer_name}"






