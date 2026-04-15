list_ids = [101, 102, 103, 104, 105]
list_names = ["Laptop", "Smartphone", "Tablet", "Monitor", "Keyboard"]
list_prices = [999.99, 499.99, 299.99, 199.99, 49.99]

def main():
    running = True

    while running:
        print_menu()
        choice = input("Select an option: ")

        if choice == '1':
            display_products()
        elif choice == '2':
            search_product()
        elif choice == '3':
            add_product()
        elif choice == '4':
            running = False
            print("Exiting the program.")
        else:
            print('Invalid option. Please try again.')

def print_menu():
    print("\nProduct Management Menu")
    print("1. Display all products")
    print("2. Search for a product by ID")
    print("3. Add a new product")
    print("4. Exit")

def display_products():
    print('All Products:')
    for i in range(len(list_ids)):
        pid = list_ids[i]
        name = list_names[i]
        price = list_prices[i]
        print(f"ID: {pid}, Name: {name}, Price: ${price:.2f}")

def search_product():
    print("Search Product by ID")
    pid = int(input("Enter Product ID: "))
    found_pos = -1

    for i in range(len(list_ids)):
        if list_ids[i] == pid:
            found_pos = i   # Found the product
            break

    if found_pos != -1:
        name = list_names[found_pos]
        price = list_prices[found_pos]
        print(f"Product Found - ID: {pid}, Name: {name}, Price: ${price:.2f}")
    else:
        print("Product not found.")

def add_product():
    print('Add New Product')
    pid = int(input("Enter Product ID: "))
    if pid in list_ids:
        print("Product ID already exists. Cannot add duplicate.")
        return
    
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))

    # add pid, name and price to respective lists
    list_ids.append(pid)
    list_names.append(name)
    list_prices.append(price)

if __name__ == "__main__":
    main()