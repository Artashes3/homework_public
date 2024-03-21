from datetime import datetime



class Account:

    
    __account_number_generator = 1000
    __interest_rate = 0.3
    __transaction_id_default = 0
    
    

    def __init__(self,first_name,last_name,balance=0,utc=4):
        self.__owner_first_name  = first_name
        self.__owner_last_name = last_name
        self.__owner_full_name = f"{self.__owner_first_name} {self.__owner_last_name}"
        self.__balance = balance
        self.__account_number = self.__account_number_generator
        self.__transaction_id = self.__transaction_id_default
        Account.__account_number_generator += 1
        self.__utc_offset = utc
        self.__dict__["transactions"] = {}

    
    @property
    def get_transaction_id(self):
        return self.__transaction_id
    
    @property
    def get_account_number(self):
        return self.__account_number
    
    @property
    def get_accout_balance(self):
        return f"The current balance is -> {self.__balance}"
    
    
    @staticmethod
    def transaction(func):

        def wrapper(*args):
            confirmation_code = lambda x=0: f"X-{args[0].get_account_number}"\
                                            f"-{(str(datetime.date(datetime.now())).replace("-",""))}"\
                                            f"-{args[0].get_transaction_id}"\
                                                    if x == "x" else \
                                            f"{func.__name__[0].upper()}"\
                                            f"-{args[0].get_account_number}-{(str(datetime.date(datetime.now())).replace("-",""))}-{args[0].get_transaction_id}"

            
            if func.__name__ == "withdrawal":
                if args[0].__balance - args[1] < 0:
                        args[0].__transaction_id += 1
                        confirmation = confirmation_code("x")
                        args[0].__dict__["transactions"][args[0].get_transaction_id] = confirmation
                        print(f"Your confirmatiom_code: {confirmation}")
                        raise Exception
                args[0].__transaction_id += 1
                confirmation = confirmation_code()
                args[0].__dict__["transactions"][args[0].get_transaction_id] = confirmation
                result =  func(*args)
                print(f"Your confirmatiom_code: {confirmation}")
                return result
            
            if func.__name__ == "deposit":
                args[0].__transaction_id += 1
                confirmation = confirmation_code()
                args[0].__dict__["transactions"][args[0].get_transaction_id] = confirmation
                result = func(*args)
                print(f"Your confirmatiom_code: {confirmation}")
                return result
            
            if func.__name__ == "calc_interest_rate":
                args[0].__transaction_id += 1
                confirmation = confirmation_code()
                args[0].__dict__["transactions"][args[0].get_transaction_id] = confirmation
                result = func(*args)
                print(f"Your confirmatiom_code: {confirmation}")
                return result
                
                
        return wrapper     

    
    def parser(self,confirmation_id):
        result = {}
        confirmation = self.__dict__["transactions"].get(confirmation_id,0)
        if confirmation != 0:
            confirmation = confirmation.split("-")

            if confirmation[0] == "W":
                result["transaction_type"] = "Withdrowal"
            if confirmation[0] == "D":
                result["transaction_type"] = "Deposit"
            if confirmation[0] == "C":
                result["transaction_type"] = "Calculated_interest_rate"

            result["account_number"] = confirmation[1]
            result["date"] = datetime.strptime(confirmation[2],"%Y%m%d")
            result["transaction_id"] = confirmation[3]
            
            return result
        else:
            print("cant find !")
            return result
        
    
    @transaction
    def withdrawal(self,value):
        old_balance = float(self.__balance)
        self.__balance -= value
        print(f"You withdraw {value}$ from the balance\n"
              f"The old balance  was -> {old_balance}$\n"
              f"The new balance  is -> {float(self.__balance)}$")
        return self.__balance
        
       

    
    
    @transaction
    def deposit(self,value):
        old_balance = float(self.__balance)
        self.__balance += value
        print(f"You put {value}$ on the balance\n"
              f"The old balance  was -> {old_balance}$\n"
              f"The new balance  is -> {float(self.__balance)}$")
        return self.__balance
        
    
    
    
    @transaction
    def calc_interest_rate(self):
        old_balance = float(self.__balance)
        self.__balance += (self.__balance * self.__interest_rate) / 100
        print(f"You add calculated interest rate to your balance \n"
              f"The interest rate  is -> {self.__interest_rate}%\n"
              f"The old balance  was -> {old_balance}$\n"
              f"The new balance  is -> {float(self.__balance)}$")
        return self.__balance

    
    
    




            


