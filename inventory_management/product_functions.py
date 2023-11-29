from product_class import *

inventory = []

def add_product():
    try:
        name  = input("Enter the name of product: ").lower()
        if not name:
            raise ValueError("Name cannot be empty")
        id  = int(input("Enter the product id: "))
        if id < 0:
            raise ValueError("Id cannot be negative")
        price  = float(input("Enter the price: "))
        if price < 0:
            raise ValueError("Price cannot be negative")
        quantity  = float(input("Enter the quantity: "))
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        category  = input("Enter the name of category: ").lower()
        if not category:
            raise ValueError("Category cannot be empty")
        prod = Product(name, id, price, quantity, category)
        inventory.append(prod)
    except ValueError as e:
        print(e)

def get_product():
    try:
        not_found = True
        user = int(input("Would you search by name or id? (1 for name and 2 for id): "))
        if user == 1:
            prod_name = input("Enter the name of product: ").lower()
            if not prod_name:
                raise ValueError("Product name cannot be empty")
            for products in inventory:
                if prod_name == products.name:
                    not_found = False
                    print(f"\n\nName {products.name}, ID {products.id}, Price {products.price}, Quantity {products.quantity}, Category {products.category}\n\n")
                    break
            else:
                print("Product not found")
                not_found = True
                
        else:
            not_found = True
            prod_id = int(input("Enter the id of product: "))
            if prod_id < 0:
                raise ValueError("Product id cannot be negative")
            for products in inventory:
                if prod_id == products.id:
                    not_found = False
                    print(f"\n\nName {products.name}, ID {products.id} Price {products.price}, Quantity {products.quantity}, Category {products.category}\n\n")
                    break
            else:
                print("Product not found")
                not_found = True
    except ValueError as e:
        print(e)

def get_value():
    value = 0
    for products in inventory:
        value += products.price * products.quantity
    print(value)

def search_product(choice,name_or_id):
    for product in inventory:
        if (choice == 1 and product.name == name_or_id) or (choice == 2 and product.id == name_or_id):
            return product
    return None

def modify_details(products):
   while True:
        try:
            user = input("What would you like to modify? Select name,price, quantity or category: ").lower()
            if not user:
                raise ValueError("Please enter a command")
            if user == "name":
                prod_name = input("Enter the new product name: ").lower()
                if not prod_name:
                    raise ValueError("Product name cannot be empty")
                products.name = prod_name
                print(f"Product name changed to {products.name}! Press 1 to exit.")
            elif user == "price":
                prod_price = input("Enter the new product price: ")
                if prod_price < 0:
                    raise ValueError("Product price cannot be negative")
                products.price = prod_price
                print(f"Product price changed to {products.price}! Press 1 to exit.")
            elif user == "quantity":
                prod_quantity = input("Enter the new product quantity: ")
                if prod_quantity < 0:
                    raise ValueError("Product quantity cannot be negative")
                products.quantity = prod_quantity
                print(f"Product quantity changed to {products.quantity}! Press 1 to exit.")
            elif user == "category":
                prod_category = input("Enter the new product category: ").lower()
                if not prod_category:
                    raise ValueError("Category cannot be empty")
                products.category = prod_category
                print(f"Product category changed to {products.category}! Press 1 to exit.")
            elif user == "1":
                break      
        except ValueError as e:
            print(e)
        
def modify_product():
    try:
        choice = int(input("Search by name or id? (1 for name and 2 for id): "))
        if not choice:
            raise ValueError("Invalid input. Please enter 1 or 2.")
        name_or_id = input("Enter the name or id of the product: ")
        if not name_or_id:
            raise ValueError("Invalid input. Please enter a name or id.")
        product = search_product(choice, name_or_id)
        if not product:
            print("Product not found")
        else:
            modify_details(product)
    except ValueError as e:
        print(e)
 
def filter_products():
    print("Press 1 to filter by category")
    print("Press 2 to filter by name")
    print("Press 3 to filter both price range and category")
    user = int(input("Choose the option: "))
    if user == 1:
        category = input("Enter the category: ").lower()
        for products in inventory:
            if products.category == category:
                print(products)
        else:
            print("Product not found")
                
    elif user == 2:
        name = input("Enter the name: ").lower()
        product = search_product(1,name)
        if not product:
            print("Product not found")
        print(product)
                
    elif user == 3:
        category = input("Enter the category: ").lower()
        min_price = float(input("Enter the minimum price: "))
        max_price = float(input("Enter the maximum price: "))
        for products in inventory:
            if products.category == category and products.price > min_price and products.price < max_price:
                print(products)
        else:
            print("Product not found")

def delete_product():
    try:
        name = input("Enter the name of the product: ")
        if not name:
            raise ValueError("Name cannot be empty")
        for product in inventory:
            if product.name == name:
                confirm = input("Are you sure you want to delete? (y/n): ")
                if not confirm:
                    raise ValueError("Invalid input")
                if confirm == "y":
                    inventory.remove(product)
                    print("Product deleted successfully")
                    break
                else:
                    print("operation cancelled")
                    break
        else:
            print("Product not found")
    except ValueError as e:
        print(e)
        
def list_items():
    for x in inventory:
        print(f"Name: {x.name}, Quantity: {x.quantity}, Price: {x.price}, Category: {x.category}")
