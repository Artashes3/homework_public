from bank import CustomerAccount


def run():
    while True:
        
        try:
            customer = CustomerAccount(customer_id=input("input the customer id:"),customer_name=input("input customer name: "),account_balance=input("input start balance: "))
            print(customer)
            customer.deposit(int(input("input deposit: ")))
            print(customer.translog)
            customer.withdraw(int(input("output withdraw: ")))
            print(customer.translog)
            ex = input("type 'exit' to terminate!: ")
            if ex == "exit":
                break   
        except:
            print("input correct info!!!")
        # if ex == "exit" or "EXIT":
        #         break



if __name__ == "__main__":
    run()