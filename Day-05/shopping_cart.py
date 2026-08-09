import csv

class Restaurant:
    def __init__(self):
        self.menu = {
            1: ("Pizza", 250),
            2: ("Burger", 150),
            3: ("Pasta", 180),
            4: ("Sandwich", 120),
            5: ("Coffee", 80)
        }
        self.orders = []

    def show_menu(self):
        print("\n----- MENU -----")
        for number, item in self.menu.items():
            print(number, item[0], "- ₹", item[1])

    def add_order(self):
        self.show_menu()

        try:
            choice = int(input("Enter item number: "))

            if choice in self.menu:
                item, price = self.menu[choice]
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    self.orders.append((item, price, quantity))
                    print("Item added successfully!")
                else:
                    print("Quantity must be greater than 0.")
            else:
                print("Invalid item number.")

        except ValueError:
            print("Please enter a valid number.")

    def view_order(self):
        if not self.orders:
            print("\nNo items in your order.")
            return

        total = 0

        print("\n----- YOUR ORDER -----")

        for item, price, quantity in self.orders:
            amount = price * quantity
            total += amount
            print(f"{item} x {quantity} = ₹{amount}")

        print("----------------------")
        print(f"Total = ₹{total}")

    def place_order(self):
        if not self.orders:
            print("Your order is empty.")
            return

        total = 0

        for item, price, quantity in self.orders:
            total += price * quantity

        with open("orders.csv", "a", newline="") as file:
            writer = csv.writer(file)
            for item, price, quantity in self.orders:
                writer.writerow([item, price, quantity, price * quantity])

        print(f"Order placed successfully!")
        print(f"Total amount: ₹{total}")

        self.orders.clear()


def main():
    restaurant = Restaurant()

    while True:
        print("\n===== RESTAURANT ORDERING SYSTEM =====")
        print("1. Show Menu")
        print("2. Add Item")
        print("3. View Order")
        print("4. Place Order")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                restaurant.show_menu()
            elif choice == 2:
                restaurant.add_order()
            elif choice == 3:
                restaurant.view_order()
            elif choice == 4:
                restaurant.place_order()
            elif choice == 5:
                print("Thank you for visiting!")
                break
            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")


main()
