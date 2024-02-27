class Product:
    def __init__(self,product_id, product_name, price,inventory_count):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.inventory_count = int(inventory_count)


    def apply_discount(self,discount_percentage):
        self.price -= (self.price * discount_percentage / 100)
        print(f"price after discount {discount_percentage}% is {self.price}")
        return self.price

    def sell(self,quantity):
        self.inventory_count -= quantity
        print(f"quantity after selling: {self.inventory_count}")
        return self.inventory_count



class DynamicPricing:
    
    def modify(product,price):
        product.price = price
        print(f"new modified price: {product.price}")
        return product.price




