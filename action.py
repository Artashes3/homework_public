from pandas import DataFrame
from bank import Account


def user_input():
    account = Account(first_name=input("type account user first name: "),last_name=input("type account user last name: "))
    transaction_type = input("Choose transaction type:\nDesposit=1\nWithdrawal=2\nCalculate and add interest rate=3\n")
    if transaction_type == "1":
        account.deposit(int(input("How much do you want to deposit to your account: ")))
    if transaction_type == "2":
        account.withdrawal(int(input("How much do you want to withdrawal: ")))
    if transaction_type == "3":
        account.calc_interest_rate()
    input("Do you want get all transactions press 'enter'")
    print(DataFrame({"Transactions":account.__dict__["transactions"]}))
    t_n = input("get info from transaction number:")
    print(DataFrame({"Result":account.parser(int(t_n))}))



user_input()


