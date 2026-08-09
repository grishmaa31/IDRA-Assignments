import csv

class ShoppingCart:
    def __init__(self):
        self.products = {
            1: ("T-Shirt", 500),
            2: ("Jeans", 1200),
            3: ("Shoes", 1500),
            4: ("Bag", 800),
            5: ("Watch", 1000)
        }
        self.cart = []

    def show_products(self):
        print("\n----- PRODUCTS -----")
        for number, product in self.products.items():
            print(number, product[0], "- ₹", product[1])

    def add_item(self):
        self.show_products()

        try:
            choice = int(input("Enter product number: "))

            if choice in self.products:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    name, price = self.products[choice]
                    self.cart.append((name, price, quantity))
                    print("Item added to cart!")
                else:
                    print("Invalid quantity.")
            else:
                print("Invalid product number.")

        except ValueError:
            print("Please enter a valid number.")

    def view_cart(self):
        if not self.cart:
            print("\nYour cart is empty.")
            return

        total = 0

        print("\n----- YOUR CART -----")

        for name, price, quantity in self.cart:
            amount = price * quantity
            total += amount
            print(name, "x", quantity, "=", "₹", amount)

        print("---------------------")
        print("Total = ₹", total)

    def checkout(self):
        if not self.cart:
            print("Your cart is empty.")
            return

        total = 0

        with open("shopping_cart.csv", "a", newline="") as file:
            writer = csv.writer(file)

            for name, price, quantity in self.cart:
                amount = price * quantity
                total += amount
                writer.writerow([name, price, quantity, amount])

        print("Order placed successfully!")
        print("Total amount = ₹", total)

        self.cart.clear()


def main():
    cart = ShoppingCart()

    while True:
        print("\n===== SHOPPING CART =====")
        print("1. Show Products")
        print("2. Add Item")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                cart.show_products()

            elif choice == 2:
                cart.add_item()

            elif choice == 3:
                cart.view_cart()

            elif choice == 4:
                cart.checkout()

            elif choice == 5:
                print("Thank you for shopping!")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")


main()
