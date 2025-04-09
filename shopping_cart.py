import json  # Importing the JSON module to handle saving and loading cart data


class ShoppingCart:
    def __init__(self):
        # Initialize the shopping cart with empty lists and default discount values
        self.foods = []  # List to store food items
        self.prices = []  # List to store prices of items
        self.categories = []  # List to store categories of items
        self.quantities = []  # List to store quantities of items
        self.discount_type = None  # Type of discount applied (flat or percent)
        self.discount_value = 0  # Value of the discount
        self.load_cart()  # Load the cart data from a file if it exists

    def load_cart(self):
        # Load cart data from a JSON file
        try:
            with open("cart.json", "r") as f:
                data = json.load(f)
                # Populate the cart attributes with the loaded data
                self.foods = data["foods"]
                self.prices = data["prices"]
                self.categories = data["categories"]
                self.quantities = data["quantities"]
                self.discount_type = data.get("discount_type")  # Get discount type if available
                self.discount_value = data.get("discount_value", 0)  # Get discount value or default to 0
                print("🛒 Previous cart loaded successfully!\n")
        except FileNotFoundError:
            # If the file doesn't exist, start with an empty cart
            print("🔄 No saved cart found. Starting fresh.\n")

    def save_cart(self):
        # Save the current cart data to a JSON file
        data = {
            "foods": self.foods,
            "prices": self.prices,
            "categories": self.categories,
            "quantities": self.quantities,
            "discount_type": self.discount_type,
            "discount_value": self.discount_value,
        }
        with open("cart.json", "w") as f:
            json.dump(data, f)  # Write the cart data to the file
        print("💾 Cart saved.")

    def display_cart(self):
        # Display the contents of the cart in a formatted table
        print("\n========== 🧾 YOUR CART ==========")
        print(f"{'No.':<4}{'Item':<15}{'Category':<15}{'Qty':<5}{'Price':>10}")
        print("-" * 55)
        total = 0  # Initialize total cost
        for i, (food, category, quantity, price) in enumerate(
            zip(self.foods, self.categories, self.quantities, self.prices)
        ):
            # Print each item's details
            print(f"{i+1:<4}{food:<15}{category:<15}{quantity:<5}{price:>10.2f}")
            total += price  # Add the item's price to the total
        print("-" * 55)
        total = self.apply_discount_to_total(total)  # Apply any discounts to the total
        print(f"{'Total':<39}${total:.2f}")
        print("===================================\n")

    def apply_discount_to_total(self, total):
        # Apply the discount to the total amount if any
        if self.discount_type:
            print(f"{'Subtotal':<39}${total:.2f}")
            if self.discount_type == "flat":
                # Subtract a flat discount amount
                total -= self.discount_value
                print(f"{'Flat Discount':<39}-$ {self.discount_value:.2f}")
            elif self.discount_type == "percent":
                # Subtract a percentage discount
                discount = total * (self.discount_value / 100)
                total -= discount
                print(f"{'Discount (' + str(self.discount_value) + '%)':<39}-$ {discount:.2f}")
        return total

    def search_item(self, name):
        # Search for an item in the cart by name
        print(f"\n🔍 Searching for '{name}'...")
        found = False  # Flag to check if the item is found
        for food, category, quantity, price in zip(
            self.foods, self.categories, self.quantities, self.prices
        ):
            if name.lower() in food.lower():  # Case-insensitive search
                print(f"✔ Found: {food} (Category: {category}, Qty: {quantity}, Price: ${price:.2f})")
                found = True
        if not found:
            print("❌ Item not found in cart.")

    def remove_or_edit_item(self):
        # Allow the user to remove or edit an item in the cart
        self.display_cart()  # Show the current cart
        try:
            index = int(input("Enter item number to remove/edit: ")) - 1
            if 0 <= index < len(self.foods):  # Check if the index is valid
                action = input("Type 'r' to remove or 'e' to edit: ").lower()
                if action == "r":
                    self.remove_item(index)  # Remove the item
                elif action == "e":
                    self.edit_item(index)  # Edit the item
                else:
                    print("⚠ Invalid action.")
            else:
                print("⚠ Invalid item number.")
        except ValueError:
            print("⚠ Enter a valid number.")

    def remove_item(self, index):
        # Remove an item from the cart by index
        print(f"❌ Removing {self.foods[index]}")
        del self.foods[index]
        del self.prices[index]
        del self.categories[index]
        del self.quantities[index]

    def edit_item(self, index):
        # Edit the details of an item in the cart
        print(f"✏ Editing {self.foods[index]}")
        new_name = input("New name (or press Enter to keep): ")
        new_cat = input("New category (or press Enter to keep): ")
        new_qty = input("New quantity (or press Enter to keep): ")
        new_price = input("New price per item (or press Enter to keep): ")

        if new_name:
            self.foods[index] = new_name  # Update the name
        if new_cat:
            self.categories[index] = new_cat  # Update the category
        if new_qty:
            self.quantities[index] = int(new_qty)  # Update the quantity
            self.prices[index] = self.prices[index] / self.quantities[index] * int(new_qty)  # Adjust the price
        if new_price:
            self.prices[index] = float(new_price) * self.quantities[index]  # Update the price

        print("✅ Item updated.")

    def generate_receipt(self):
        # Generate a receipt and save it to a text file
        with open("receipt.txt", "w") as file:
            file.write("=========== 🧾 RECEIPT ===========\n")
            file.write(f"{'Item':<15}{'Category':<15}{'Qty':<5}{'Price':>10}\n")
            file.write("-" * 50 + "\n")
            total = 0
            for food, category, quantity, price in zip(
                self.foods, self.categories, self.quantities, self.prices
            ):
                file.write(f"{food:<15}{category:<15}{quantity:<5}{price:>10.2f}\n")
                total += price
            file.write("-" * 50 + "\n")
            total = self.apply_discount_to_total(total)  # Apply discounts to the total
            file.write(f"{'Total':<40}${total:.2f}\n")
            file.write("Thank you for shopping with us!\n")
            file.write("==================================\n")
        print("🧾 Receipt generated as 'receipt.txt'.")

    def apply_discount(self):
        # Allow the user to apply a discount to the cart
        print("\n💰 APPLY DISCOUNT")
        print("1. Flat amount off (e.g., $10)")
        print("2. Percentage off (e.g., 10%)")
        print("3. Remove discount")
        option = input("Choose an option: ")

        if option == "1":
            self.discount_value = float(input("Enter flat discount amount: $"))
            self.discount_type = "flat"  # Set discount type to flat
            print(f"✅ Applied flat discount of ${self.discount_value:.2f}.")
        elif option == "2":
            self.discount_value = float(input("Enter discount percentage: "))
            self.discount_type = "percent"  # Set discount type to percentage
            print(f"✅ Applied {self.discount_value:.0f}% discount.")
        elif option == "3":
            self.discount_type = None  # Remove any discounts
            self.discount_value = 0
            print("❌ Discount removed.")
        else:
            print("⚠ Invalid choice.")

    def add_item(self):
        # Add a new item to the cart
        category = input("Enter category (e.g., Fruits, Snacks): ")
        food = input("Enter item name: ")
        quantity = int(input(f"Enter quantity of {food}: "))
        price = float(input(f"Enter price per item of {food}: $"))
        total_price = price * quantity  # Calculate the total price for the item

        self.categories.append(category)
        self.foods.append(food)
        self.quantities.append(quantity)
        self.prices.append(total_price)

        print(f"✅ {food} added to your cart under '{category}'.\n")


def main():
    # Main function to run the shopping cart program
    cart = ShoppingCart()

    while True:
        # Display the menu and handle user input
        print("📋 MENU")
        print("1. Add item by category")
        print("2. View cart")
        print("3. Search item")
        print("4. Remove/Edit item")
        print("5. Save cart")
        print("6. Generate receipt")
        print("7. Apply discount")
        print("8. Quit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            cart.add_item()  # Add a new item
        elif choice == "2":
            cart.display_cart()  # Display the cart
        elif choice == "3":
            search = input("Enter item name to search: ")
            cart.search_item(search)  # Search for an item
        elif choice == "4":
            cart.remove_or_edit_item()  # Remove or edit an item
        elif choice == "5":
            cart.save_cart()  # Save the cart
        elif choice == "6":
            cart.generate_receipt()  # Generate a receipt
        elif choice == "7":
            cart.apply_discount()  # Apply a discount
        elif choice == "8":
            cart.save_cart()  # Save the cart before exiting
            print("👋 Thank you for using the cart. Goodbye!")
            break
        else:
            print("⚠ Invalid option. Try again.\n")


if __name__ == "__main__":
    main()  # Run the main function
