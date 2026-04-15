class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    @property
    def pid(self):
        return self.__pid
    
    @pid.setter
    def pid(self, value):
        if isinstance(value, int) and value > 0:
            self.__pid = value
        else:
            print("Invalid Product ID. It must be a positive integer.")
            self.__pid = 0  # default value for invalid ID

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip() != "":
            self.__name = value.strip()
        else:
            print("Invalid Product Name. It must be a non-empty string.")
            self.__name = "Unknown Product"  # default value for invalid name

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__price = float(value)
        else:
            print("Invalid Product Price. It must be a positive number.")
            self.__price = 1.0  # default value for invalid price

    def display(self):
        print(f"ID: {self.pid}, Name: {self.name}, Price: ${self.price:.2f}")