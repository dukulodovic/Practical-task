class BankAccount:
    # Class variable (interest rate applied to all accounts)
    interest_rate = 0.05  # 5% interest
    
    def __init__(self, account_holder):
        # Instance variables
        self.account_holder = account_holder
        self.balance = 0  # Initial balance set to zero
    
    def deposit(self, amount):
        """Adds the amount to the balance."""
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")
    
    def withdraw(self, amount):
        """Subtracts the amount from the balance if there are sufficient funds."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print(f"Insufficient funds for withdrawal of {amount}. Current balance: {self.balance}")
    
    def apply_interest(self):
        """Adds interest to the current balance based on the class variable interest_rate."""
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"Interest applied. New balance: {self.balance}")
    
    def display_account_info(self):
        """Displays the account holder’s name and the current balance."""
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")

# 1. Create two instances of BankAccount with different account holders.
account1 = BankAccount("Alice")
account2 = BankAccount("Bob")

# 2. Perform a few deposits and withdrawals.
account1.deposit(1000)
account1.withdraw(200)
account2.deposit(2000)
account2.withdraw(500)

# 3. Apply interest using the apply_interest() method.
account1.apply_interest()
account2.apply_interest()

# 4. Display account information for each account.
account1.display_account_info()
account2.display_account_info()








 
class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        """Displays product details."""
        print(f"Product: {self.product_name}, Price: {self.price}, Quantity in stock: {self.quantity_in_stock}")

class ShoppingCart:
    total_carts = 0

    def __init__(self):
        self.items = []  # List of tuples (product, quantity)
        ShoppingCart.total_carts += 1

    def add_to_cart(self, product, quantity):
        """Adds a product to the cart if the quantity is available."""
        if quantity <= product.quantity_in_stock:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
            print(f"Added {quantity} of {product.product_name} to the cart.")
        else:
            print(f"Cannot add {quantity} of {product.product_name}. Only {product.quantity_in_stock} available in stock.")

    def remove_from_cart(self, product):
        """Removes a product from the cart."""
        self.items = [item for item in self.items if item[0] != product]
        print(f"Removed {product.product_name} from the cart.")

    def display_cart(self):
        """Displays all items in the cart."""
        if not self.items:
            print("Cart is empty.")
        else:
            for product, quantity in self.items:
                print(f"Product: {product.product_name}, Quantity: {quantity}, Subtotal: {product.price * quantity}")

    def calculate_total(self):
        """Calculates and returns the total price of items in the cart."""
        total = sum(product.price * quantity for product, quantity in self.items)
        return total

# Create three Product objects with varying prices and quantities
product1 = Product("Laptop", 1000, 10)
product2 = Product("Phone", 500, 20)
product3 = Product("Headphones", 100, 30)

# Create two separate ShoppingCart instances
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Adding products to cart1
cart1.add_to_cart(product1, 1)
cart1.add_to_cart(product3, 2)

# Adding products to cart2
cart2.add_to_cart(product2, 2)
cart2.add_to_cart(product3, 5)

# Removing a product from cart2
cart2.remove_from_cart(product3)

# Display the contents of each cart and calculate the total amount due
print("\nCart 1:")
cart1.display_cart()
print(f"Total for Cart 1: {cart1.calculate_total()}")

print("\nCart 2:")
cart2.display_cart()
print(f"Total for Cart 2: {cart2.calculate_total()}")
