import json


def load_products(filename='products.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_products(products, filename='products.json'):
    with open(filename, 'w') as file:
        json.dump(products, file, indent=4)


def add_product(products, product):
    if any(p['id'] == product['id'] for p in products):
        print("Error: Product ID must be unique.")
        return False
    
    products.append(product)
    save_products(products)
    print(f"Product '{product['name']}' added successfully.")
    return True



def display_products(products):
    if not products:
        print("No products available.")
        return
    for product in products:
        print("hello world")
        print(f"ID: {product['id']}, Name: {product['name']}, Category: {product['category']}, "
              f"Price: ${product['price']:.2f}, Available: {'Yes' if product['available'] else 'No'}")

def filter_available_products(products):
    return [product for product in products if product['available'] is True]



def display_available_products(products):
    available_products = filter_available_products(products)
    display_products(available_products)

def update_product(products, product_id, updates):
    for product in products:
        if product['id'] == product_id:
            product.update(updates)
            save_products(products)
            print(f"Product with ID {product_id} updated successfully.")
            return True
    print(f"Error: Product with ID {product_id} not found.")
    return False

if __name__ == "__main__":
    products = load_products()
# adding new product
    new_product = {
        "id": 3,
        "name": "macbook",
        "category": "Electronics",
        "price": 15000,
        "available": True
    }
    add_product(products, new_product)
    # display_available_products(products)
    product_id=2
    updates = {}
    updates["name"]="one plus"
    update_product(products, product_id, updates)

    display_products(products)
