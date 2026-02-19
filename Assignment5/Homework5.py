import json

balance = 5
sale = 0
purchase = 0
inventory = [
    {"object" : "Pen", "price" : 3 , "amount" : 2},
    {"object" : "Notebook", "price" : 5 , "amount" : 5}
]
operations = []

try:
    with open("data.json", "r") as file:
        data = json.load(file)

        balance = data["balance"]
        inventory = data["inventory"]
        operations = data["operations"]

    print("Data saved")
except:
    print("Data not saved")

def save_data():
    data = {
        "balance" : balance,
        "inventory" : inventory,
        "operations" : operations
    }
    with open("data.json", "w") as file:
        json.dump(data, file)
    print("Data saved")

while True:

    print("\n---Menu---")
    print("1. Add or remove balance")
    print("2. Sell product")
    print("3. Purchase product")
    print("4. Current balance")
    print("5. Show inventory")
    print("6. Product status ")
    print("7. Display operations")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            add_remove = input("Select 1 to add or 2 to remove balance: ")
            if add_remove == "1":
                added_amount = float(input("Enter amount to be added: "))
                if added_amount > 0:
                    balance += added_amount
                    print (f"The available balance is {balance}")
                    operations.append(f"Added balance {added_amount}")
                else:
                    print ("The number is not valid")
            elif add_remove == "2":
                removed_amount = float(input("Enter amount to be removed: "))
                if removed_amount <= balance:
                    balance -= removed_amount
                    print(f"The available balance is {balance}")
                    operations.append(f"Removed balance {removed_amount}")
                else:
                    print ("Not enough balance to remove this amount")
            else:
                print ("The choice is not valid")
        except ValueError:
            print("Invalid input. Enter a number")

    elif choice == "2":
        print("\n INVENTORY")
        for i, product in enumerate(inventory):
            print(f"{i + 1}. {product['object']} - price: {product['price']} - amount: {product['amount']}")

        try:
            sell_choice = int(input("Choose the product to sell: "))
            if 1<= sell_choice <= len(inventory):
                inventory_product = inventory[sell_choice -1]
            else:
                print("Invalid choice")
                continue

            amount_choice = int(input("Choose the amount to sell: "))
            if amount_choice > 0:
                if amount_choice <= inventory_product["amount"]:
                    inventory_product["amount"] -= amount_choice
                    balance += amount_choice * inventory_product["price"]
                    operations.append(f"Sold product {inventory_product['object']}")
                    print(f"You sold a {inventory_product['object']}")

                elif amount_choice > inventory_product["amount"]:
                    print ("Not enough quantity to sell this item")

                elif inventory_product["amount"] == 0:
                    print (f"The selected {inventory_product['object']} is not available")
            else:
                print ("Wrong value entered")

        except ValueError:
            print ("Invalid input. Enter a number")

    elif choice == "3":
        print("\n INVENTORY")
        for i, product in enumerate(inventory):
            print(f"{i + 1}. {product['object']} - price: {product['price']}")

        try:
            buy_choice = int(input("Choose the product to buy: "))
            if  buy_choice >= 1:
                inventory_product = inventory[buy_choice - 1]
            else:
                print("Invalid choice")
                continue

            amount_choice_buy = int(input("Choose the amount to buy: "))
            if amount_choice_buy > 0:
                cost = amount_choice_buy * inventory_product["price"]
                if cost <= balance:
                    inventory_product["amount"] += amount_choice_buy
                    balance -= cost
                    operations.append(f"Bought product {inventory_product['object']}")
                    print(f"You bought a {inventory_product['object']}")
                else:
                    print ("Not enough balance to buy this amount")
            else:
                print("Wrong value entered")
        except ValueError:
            print ("Invalid input. Enter a number")

    elif choice == "4":
        print (f"The available balance is {balance} ")
        operations.append(f"Balance request: {balance}")

    elif choice == "5":
        print ("\n INVENTORY")
        for i, product in enumerate(inventory):
            print(f"{i+1}. {product['object']} - price: {product['price']} - amount: {product['amount']}")
        operations.append("Show inventory")

    elif choice == "6":
        try:
            product_name = input("Enter product name: ").strip()
            found = False
            for product in inventory:
                if product["object"].lower() == product_name.lower():
                    found = True
                    if product["amount"] > 0:
                        print(f" {product['object']} - AVAILABLE")
                    else:
                        print(f"{product['object']} - UNAVAILABLE")
                    break
            if not found:
                print("Product not available")

        except ValueError:
            print("Invalid input. Enter a number")
        operations.append(f"Product status requested")

    if choice == "7":
        try:
            from_index = input("Enter 'from' index: ").strip()
            to_index = input("Enter 'to' index: ").strip()

            if from_index == "" and to_index == "":
                for op in operations:
                    print(op)
            else:
                try:
                    from_index = int(from_index) if from_index != "" else 1
                    to_index = int(to_index) if to_index != "" else len(operations)
                    if from_index < 1 or to_index > len(operations) or from_index > to_index:
                        print("Index out of range")
                    else:
                        for op in operations[from_index - 1:to_index]:
                            print(op)
                except ValueError:
                    print("Invalid indices. Enter numbers")
        except ValueError:
            print("Invalid input. Enter a number")

    if choice =="8":
        save_data()
        break










