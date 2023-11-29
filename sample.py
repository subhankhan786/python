from product_functions import *
from datetime import date

sales_record = []

def sale():
    try:
        prod = input("Enter the name of the product to be sold: ").lower()
        if not prod:
            raise ValueError("Name cannot be empty")
        products = search_product(1, prod)
        if not products:
            print("Product not found")
        try:
            quantity = int(input("Enter the quantity of the product: "))
            if quantity < 0:
                raise ValueError("Quantity cannot be negative")
        except ValueError as e:
            print(e)
        stock_left = products.quantity - quantity
        products.quantity = stock_left
        print(f"{quantity} of {prod} sold. {products.quantity} is left in stock.")
        sales_history(prod,quantity)
    except ValueError as e:
        print(e)
        
def sales_history(prod, quantity):
    date = date.today()
    li = [f"Date: {date}, Name: {prod}, Quantity_Sold: {quantity}"]
    record = sales_record.append(li)    