import json


class ShoppingCart:
    def __init__(self):
        self.foods = []
        self.prices = []
        self.categories = []
        self.quantities = []
        self.discount_type = None
        self.discount_value = 0
        self.load_cart()

    def load_cart(self):
        try:
            with open("cart.json", "r") as f:
                data = json.load(f)
                self.foods = data["foods"]
                self.prices = data["prices"]
                self.categories = data["categories"]
                self.quantities = data["quantities"]
                self.discount_type = data.get("discount_type")
                self.discount_value = data.get("discount_value", 0)
                print("🛒 Previous cart loaded successfully!\n")
        except FileNotFoundError:
            print("🔄 No saved cart found. Starting fresh.\n")

    def save_cart(self):
        data = {
            "foods": self.foods,
            "prices": self.prices,
            "categories": self.categories,
            "quantities": self.quantities,
            "discount_type": self.discount_type,
            "discount_value": self.discount_value,
        }
        with open("cart.json", "w") as f:
            json.dump(data, f)
        print("💾 Cart saved.")

    def display_cart(self):
        print("\n========== 🧾 YOUR CART ==========")
        print(f"{'No.':<4}{'Item':<15}{'Category':<15}{'Qty':<5}{'Price':>10}")
        print("-" * 55)
        total = 0
        for i, (food, category, quantity, price) in enumerate(
            zip(self.foods, self.categories, self.quantities, self.prices)
        ):
            print(f"{i+1:<4}{food:<15}{category:<15}{quantity:<5}{price:>10.2f}")
            total += price
        print("-" * 55)
        total = self.apply_discount_to_total(total)
        print(f"{'Total':<39}${total:.2f}")
        print("===================================\n")

    def apply_discount_to_total(self, total):
        if self.discount_type:
            print(f"{'Subtotal':<39}${total:.2f}")
            if self.discount_type == "flat":
                total -= self.discount_value
                print(f"{'Flat Discount':<39}-$ {self.discount_value:.2f}")
            elif self.discount_type == "percent":
                discount = total * (self.discount_value / 100)
                total -= discount
                print(f"{'Discount (' + str(self.discount_value) + '%)':<39}-$ {discount:.2f}")
        return total

    def search_item(self, name):
        print(f"\n🔍 Searching for '{name}'...")
        found = False
        for food, category, quantity, price in zip(
            self.foods, self.categories, self.quantities, self.prices
        ):
            if name.lower() in food.lower():
                print(f"✔ Found: {food} (Category: {category}, Qty: {quantity}, Price: ${price:.2f})")
                found = True
        if not found:
            print("❌ Item not found in cart.")

    def remove_or_edit_item(self):
        self.display_cart()
        try:
            index = int(input("Enter item number to remove/edit: ")) - 1
            if 0 <= index < len(self.foods):
                action = input("Type 'r' to remove or 'e' to edit: ").lower()
                if action == "r":
                    self.remove_item(index)
                elif action == "e":
                    self.edit_item(index)
                else:
                    print("⚠ Invalid action.")
            else:
                print("⚠ Invalid item number.")
        except ValueError:
            print("⚠ Enter a valid number.")

    def remove_item(self, index):
        print(f"❌ Removing {self.foods[index]}")
        del self.foods[index]
        del self.prices[index]
        del self.categories[index]
        del self.quantities[index]

    def edit_item(self, index):
        print(f"✏ Editing {self.foods[index]}")
        new_name = input("New name (or press Enter to keep): ")
        new_cat = input("New category (or press Enter to keep): ")
        new_qty = input("New quantity (or press Enter to keep): ")
        new_price = input("New price per item (or press Enter to keep): ")

        if new_name:
            self.foods[index] = new_name
        if new_cat:
            self.categories[index] = new_cat
        if new_qty:
            self.quantities[index] = int(new_qty)
            self.prices[index] = self.prices[index] / self.quantities[index] * int(new_qty)
        if new_price:
            self.prices[index] = float(new_price) * self.quantities[index]

        print("✅ Item updated.")

    def generate_receipt(self):
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
            total = self.apply_discount_to_total(total)
            file.write(f"{'Total':<40}${total:.2f}\n")
            file.write("Thank you for shopping with us!\n")
            file.write("==================================\n")
        print("🧾 Receipt generated as 'receipt.txt'.")

    def apply_discount(self):
        print("\n💰 APPLY DISCOUNT")
        print("1. Flat amount off (e.g., $10)")
        print("2. Percentage off (e.g., 10%)")
        print("3. Remove discount")
        option = input("Choose an option: ")

        if option == "1":
            self.discount_value = float(input("Enter flat discount amount: $"))
            self.discount_type = "flat"
            print(f"✅ Applied flat discount of ${self.discount_value:.2f}.")
        elif option == "2":
            self.discount_value = float(input("Enter discount percentage: "))
            self.discount_type = "percent"
            print(f"✅ Applied {self.discount_value:.0f}% discount.")
        elif option == "3":
            self.discount_type = None
            self.discount_value = 0
            print("❌ Discount removed.")
        else:
            print("⚠ Invalid choice.")

    def add_item(self):
        category = input("Enter category (e.g., Fruits, Snacks): ")
        food = input("Enter item name: ")
        quantity = int(input(f"Enter quantity of {food}: "))
        price = float(input(f"Enter price per item of {food}: $"))
        total_price = price * quantity

        self.categories.append(category)
        self.foods.append(food)
        self.quantities.append(quantity)
        self.prices.append(total_price)

        print(f"✅ {food} added to your cart under '{category}'.\n")


def main():
    cart = ShoppingCart()

    while True:
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
            cart.add_item()
        elif choice == "2":
            cart.display_cart()
        elif choice == "3":
            search = input("Enter item name to search: ")
            cart.search_item(search)
        elif choice == "4":
            cart.remove_or_edit_item()
        elif choice == "5":
            cart.save_cart()
        elif choice == "6":
            cart.generate_receipt()
        elif choice == "7":
            cart.apply_discount()
        elif choice == "8":
            cart.save_cart()
            print("👋 Thank you for using the cart. Goodbye!")
            break
        else:
            print("⚠ Invalid option. Try again.\n")


if __name__ == "__main__":
    main()
