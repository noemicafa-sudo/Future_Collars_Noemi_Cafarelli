import json

class Manager:
    def __init__(self):
        self.balance = 5
        self.inventory = [
            {"object": "Pen", "price": 3, "amount": 2},
            {"object": "Notebook", "price": 5, "amount": 5}
        ]
        self.operations = []
        self.load_data()


    def load_data(self):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                self.balance = data.get("balance", self.balance)
                self.inventory = data.get("inventory", self.inventory)
                self.operations = data.get("operations", self.operations)
            print("Data loaded")
        except FileNotFoundError:
            print("No data file found")

    def save_data(self):
        data = {
            "balance": self.balance,
            "inventory": self.inventory,
            "operations": self.operations
        }
        with open("data.json", "w") as file:
            json.dump(data, file)
        print("Data saved")

    def log_operation(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            self.operations.append(f"{func.__name__.capitalize()} operation executed")
            return result
        return wrapper

    @property
    def tasks(self):
        return {
            "add_balance": self.add_balance,
            "remove_balance": self.remove_balance,
            "sale": self.sale,
            "purchase": self.purchase,
            "show_balance": self.show_balance,
            "show_inventory": self.show_inventory,
            "product_status": self.product_status
        }

    @log_operation
    def add_balance(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Balance added. Current balance: {self.balance}")
        else:
            print("Invalid amount")

    @log_operation
    def remove_balance(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Balance removed. Current balance: {self.balance}")
        else:
            print("Invalid amount")

    @log_operation
    def sale(self, product_index, quantity):
        try:
            product = self.inventory[product_index]
            if 0 < quantity <= product["amount"]:
                product["amount"] -= quantity
                self.balance += product["price"] * quantity
                print(f"Sold {quantity} x {product['object']}")
            else:
                print("Not enough quantity")
        except IndexError:
            print("Invalid product index")

    @log_operation
    def purchase(self, product_index, quantity):
        try:
            product = self.inventory[product_index]
            cost = product["price"] * quantity
            if quantity > 0 and cost <= self.balance:
                product["amount"] += quantity
                self.balance -= cost
                print(f"Bought {quantity} x {product['object']}")
            else:
                print("Not enough balance or invalid quantity")
        except IndexError:
            print("Invalid product index")

    @log_operation
    def show_balance(self):
        print(f"Current balance: {self.balance}")

    @log_operation
    def show_inventory(self):
        for i, p in enumerate(self.inventory):
            print(f"{i}. {p['object']} - price: {p['price']} - amount: {p['amount']}")

    @log_operation
    def product_status(self, name):
        for p in self.inventory:
            if p["object"].lower() == name.lower():
                status = "AVAILABLE" if p["amount"] > 0 else "UNAVAILABLE"
                print(f"{p['object']} - {status}")
                return
        print("Product not found")

    def assign(self, task_name, *args):
        task = self.tasks.get(task_name)
        if task:
            task(*args)
        else:
            print("Task not found")
