# from file_name import class_name
from product import Product

class ProductManager:
    def __init__(self):
        self.__products = []  # private list to store Product objects
        self.__load_sample_data()

    def __load_sample_data(self):
        # Load some sample products into the list
        self.__products.append(Product(1, "Laptop", 999.99))
        self.__products.append(Product(2, "Smartphone", 499.99))
        self.__products.append(Product(3, "Headphones", 199.99))
        self.__products.append(Product(4, "Monitor", 299.99))
        self.__products.append(Product(5, "Keyboard", 49.99))


    def __print_menu(self):
        print("\nProduct Management Menu")
        print("1. Display all products")
        print("2. Search for a product by ID")
        print("3. Add a new product")
        print("4. Exit")

    def __display_products(self):
        print('All Products:')
        for product in self.__products:
            product.display()

    def __search_product(self):
        print("Search Product")

        pid = int(input("Enter Product ID: "))
        product = self.__search_by_id(pid)
        if product is not None:
            print("Product Found:")
            product.display()
        else:
            print("Product not found.")

    def __search_by_id(self, pid):
        for product in self.__products:
            if product.pid == pid:
                return product
        return None

    def __add_product(self):
        print('Add new product')

        # enter product details
        pid = int(input("Enter Product ID: "))
        
        if self.__search_by_id(pid) is not None:
            print("Product ID already exists. Cannot add duplicate.")
            return
        
        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))

        # create a new Product object and add to the list
        new_product = Product(pid, name, price)
        self.__products.append(new_product)
        print("Product added successfully.")

    def run(self):
        running = True
        while running:
            self.__print_menu()
            choice = int(input("Select an option: "))

            if choice == 1:
                self.__display_products()
            elif choice == 2:
                self.__search_product()
            elif choice == 3:
                self.__add_product()
            elif choice == 4:
                running = False
                print("Exiting the program.")
            else:
                print('Invalid option. Please try again.')

if __name__ == "__main__":
    # create a manager object and run the program
    manager = ProductManager()
    manager.run()