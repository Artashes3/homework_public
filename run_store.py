from online_store import *


def run():
    while True:
        try:
            product = Product(product_id=input("enter product id: "),\
                                product_name=input("enter product name: "),\
                                price=int(input("input product price: ")),\
                                inventory_count=input("input inventory count: "))
            product.apply_discount(float(input("input discount: ")))
            product.sell(int(input("input sell count: ")))
            in_product=input("enter product name: ")
            if in_product == product.product_name:
                DynamicPricing.modify(product,input("input new price: "))
            else:
                print("no product found!")

            ex = input("type 'exit' to terminate!  ")
            if ex == "exit":
                break
        except:

            print("input correct info!!!")
       
            


run()
