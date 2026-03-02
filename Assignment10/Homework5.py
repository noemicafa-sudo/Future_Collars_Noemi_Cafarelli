from manager import Manager

def main():
    manager = Manager()

    while True:
        print("\n---Menu---")
        print("1. Add balance")
        print("2. Remove balance")
        print("3. Sell product")
        print("4. Purchase product")
        print("5. Show balance")
        print("6. Show inventory")
        print("7. Product status")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to add: "))
            manager.assign("add_balance", amount)

        elif choice == "2":
            amount = float(input("Enter amount to remove: "))
            manager.assign("remove_balance", amount)

        elif choice == "3":
            manager.show_inventory()
            index = int(input("Choose product index to sell: "))
            qty = int(input("Enter quantity: "))
            manager.assign("sale", index, qty)

        elif choice == "4":
            manager.show_inventory()
            index = int(input("Choose product index to buy: "))
            qty = int(input("Enter quantity: "))
            manager.assign("purchase", index, qty)

        elif choice == "5":
            manager.assign("show_balance")

        elif choice == "6":
            manager.assign("show_inventory")

        elif choice == "7":
            name = input("Enter product name: ")
            manager.assign("product_status", name)

        elif choice == "8":
            manager.save_data()
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
