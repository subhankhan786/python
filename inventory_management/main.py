from product_functions import *
from sales_function import *

choices = {1: add_product, 2: get_product, 3: get_value, 4: modify_product, 5: sale, 6: filter_products, 7: delete_product, 8: get_sale_record, 9: list_items,10: exit}

def main():
    while True:
        print("Welcome to the inventory manager!\n\n")
        print("Enter 1 for adding a product\n")
        print("Enter 2 for getting info of a product\n")
        print("Enter 3 for value of stock\n")
        print("Enter 4 for modifying the info of a product\n")
        print("Enter 5 for selling the product\n")
        print("Enter 6 for filtering products\n")
        print("Enter 7 for deleting a product\n")
        print("Enter 8 for viewing sales history\n")
        print("Enter 9 for listing all the products\n")
        print("Enter 10 for exiting\n")
        user = int(input("Choose the task to execute: "))
        choices[user]()

if __name__ == '__main__':
    main()
