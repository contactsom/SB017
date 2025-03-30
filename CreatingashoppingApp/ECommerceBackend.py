class ECommerceBackend:
    def __init__(self):
        # Initialize demo databases
        self.users = {
            "user1": {"password": "pass1", "name": "Regular User"},
            "user2": {"password": "pass2", "name": "John Doe"}
        }

        self.admins = {
            "admin1": {"password": "admin1", "name": "Admin User"},
            "admin2": {"password": "admin2", "name": "Super Admin"}
        }

        self.categories = {
            1: "Footwear",
            2: "Clothing",
            3: "Electronics",
            4: "Accessories"
        }

        self.products = {
            101: {"name": "Sports Shoes", "category_id": 1, "price": 1500},
            102: {"name": "Leather Boots", "category_id": 1, "price": 2000},
            103: {"name": "T-Shirt", "category_id": 2, "price": 500},
            104: {"name": "Jeans", "category_id": 2, "price": 1200},
            105: {"name": "Smartphone", "category_id": 3, "price": 15000},
            106: {"name": "Laptop", "category_id": 3, "price": 45000},
            107: {"name": "Cap", "category_id": 4, "price": 300},
            108: {"name": "Watch", "category_id": 4, "price": 2500}
        }

        self.active_sessions = {}  # {session_id: {"username": username, "type": "user/admin"}}
        self.user_carts = {}  # {session_id: {product_id: quantity}}

        self.next_session_id = 1
        self.next_product_id = 109
        self.next_category_id = 5

    def display_welcome_message(self):
        print("=" * 50)
        print("Welcome to the Demo Marketplace")
        print("=" * 50)

    def login(self, username, password, user_type="user"):
        if user_type == "user":
            database = self.users
        else:  # admin
            database = self.admins

        if username in database and database[username]["password"] == password:
            session_id = str(self.next_session_id)
            self.next_session_id += 1
            self.active_sessions[session_id] = {
                "username": username,
                "type": user_type
            }
            if user_type == "user":
                self.user_carts[session_id] = {}

            print(f"Login successful. Welcome {database[username]['name']}!")
            return session_id
        else:
            print("Invalid credentials. Please try again.")
            return None

    def logout(self, session_id):
        if session_id in self.active_sessions:
            username = self.active_sessions[session_id]["username"]
            user_type = self.active_sessions[session_id]["type"]
            del self.active_sessions[session_id]

            if user_type == "user" and session_id in self.user_carts:
                del self.user_carts[session_id]

            print(f"Logout successful. Goodbye!")
            return True
        else:
            print("Invalid session. Please login again.")
            return False

    def is_valid_session(self, session_id, required_type=None):
        if session_id not in self.active_sessions:
            print("Invalid session. Please login again.")
            return False

        if required_type and self.active_sessions[session_id]["type"] != required_type:
            print(f"Access denied. This action requires {required_type} privileges.")
            return False

        return True

    def display_catalog(self, session_id):
        if not self.is_valid_session(session_id):
            return False

        print("\n" + "=" * 50)
        print("Product Catalog")
        print("=" * 50)
        print("{:<10} {:<20} {:<15} {:<10}".format("ID", "Name", "Category", "Price"))
        print("-" * 55)

        for product_id, product in self.products.items():
            category_name = self.categories.get(product["category_id"], "Unknown")
            print("{:<10} {:<20} {:<15} ₹{:<10}".format(
                product_id,
                product["name"],
                category_name,
                product["price"]
            ))

        return True

    def display_categories(self, session_id):
        if not self.is_valid_session(session_id):
            return False

        print("\n" + "=" * 50)
        print("Product Categories")
        print("=" * 50)
        print("{:<10} {:<20}".format("ID", "Category Name"))
        print("-" * 30)

        for category_id, category_name in self.categories.items():
            print("{:<10} {:<20}".format(category_id, category_name))

        return True

    # User Cart Operations
    def display_cart(self, session_id):
        if not self.is_valid_session(session_id, "user"):
            return False

        cart = self.user_carts.get(session_id, {})

        if not cart:
            print("\nYour cart is empty.")
            return True

        total_amount = 0
        print("\n" + "=" * 50)
        print("Your Shopping Cart")
        print("=" * 50)
        print("{:<10} {:<20} {:<10} {:<10} {:<10}".format(
            "ID", "Product", "Price", "Quantity", "Total"
        ))
        print("-" * 60)

        for product_id, quantity in cart.items():
            if product_id in self.products:
                price = self.products[product_id]["price"]
                total = price * quantity
                total_amount += total

                print("{:<10} {:<20} ₹{:<10} {:<10} ₹{:<10}".format(
                    product_id,
                    self.products[product_id]["name"],
                    price,
                    quantity,
                    total
                ))

        print("-" * 60)
        print(f"Total Amount: ₹{total_amount}")

        return True

    def add_to_cart(self, session_id, product_id, quantity=1):
        if not self.is_valid_session(session_id, "user"):
            return False

        product_id = int(product_id)
        quantity = int(quantity)

        if product_id not in self.products:
            print(f"Product with ID {product_id} not found.")
            return False

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return False

        cart = self.user_carts.get(session_id, {})

        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity

        self.user_carts[session_id] = cart

        print(f"Added {quantity} {self.products[product_id]['name']}(s) to your cart.")
        return True

    def remove_from_cart(self, session_id, product_id, quantity=None):
        if not self.is_valid_session(session_id, "user"):
            return False

        product_id = int(product_id)

        if session_id not in self.user_carts or product_id not in self.user_carts[session_id]:
            print(f"Product with ID {product_id} not found in your cart.")
            return False

        if quantity is None or quantity >= self.user_carts[session_id][product_id]:
            # Remove completely
            product_name = self.products.get(product_id, {}).get("name", "Unknown Product")
            del self.user_carts[session_id][product_id]
            print(f"Removed {product_name} from your cart.")
        else:
            # Reduce quantity
            quantity = int(quantity)
            self.user_carts[session_id][product_id] -= quantity
            product_name = self.products.get(product_id, {}).get("name", "Unknown Product")
            print(f"Reduced {product_name} quantity by {quantity}.")

        return True

    # Payment Processing
    def checkout(self, session_id, payment_method):
        if not self.is_valid_session(session_id, "user"):
            return False

        if session_id not in self.user_carts or not self.user_carts[session_id]:
            print("Your cart is empty. Nothing to checkout.")
            return False

        total_amount = sum(
            self.products[product_id]["price"] * quantity
            for product_id, quantity in self.user_carts[session_id].items()
            if product_id in self.products
        )

        payment_methods = {
            "1": "Net Banking",
            "2": "PayPal",
            "3": "UPI",
            "4": "Debit Card",
            "5": "Credit Card"
        }

        payment_name = payment_methods.get(payment_method, payment_method)

        print("\n" + "=" * 50)
        print("Checkout Process")
        print("=" * 50)

        if payment_name.lower() == "upi":
            print(
                f"You will be shortly redirected to the portal for Unified Payment Interface to make a payment of ₹{total_amount}")
        else:
            print(f"You will be redirected to {payment_name} to complete your payment of ₹{total_amount}")

        print("\nProcessing payment...")
        print("Your order is successfully placed!")

        # Clear the cart after successful checkout
        self.user_carts[session_id] = {}

        return True

    # Admin Operations - Product Management
    def add_product(self, session_id, name, category_id, price):
        if not self.is_valid_session(session_id, "admin"):
            return False

        category_id = int(category_id)
        price = float(price)

        if category_id not in self.categories:
            print(f"Category with ID {category_id} does not exist.")
            return False

        if price <= 0:
            print("Price must be greater than zero.")
            return False

        new_product_id = self.next_product_id
        self.next_product_id += 1

        self.products[new_product_id] = {
            "name": name,
            "category_id": category_id,
            "price": price
        }

        print(f"Product '{name}' added successfully with ID {new_product_id}.")
        return True

    def update_product(self, session_id, product_id, name=None, category_id=None, price=None):
        if not self.is_valid_session(session_id, "admin"):
            return False

        product_id = int(product_id)

        if product_id not in self.products:
            print(f"Product with ID {product_id} not found.")
            return False

        if name:
            self.products[product_id]["name"] = name

        if category_id:
            category_id = int(category_id)
            if category_id not in self.categories:
                print(f"Category with ID {category_id} does not exist.")
                return False
            self.products[product_id]["category_id"] = category_id

        if price:
            price = float(price)
            if price <= 0:
                print("Price must be greater than zero.")
                return False
            self.products[product_id]["price"] = price

        print(f"Product with ID {product_id} updated successfully.")
        return True

    def delete_product(self, session_id, product_id):
        if not self.is_valid_session(session_id, "admin"):
            return False

        product_id = int(product_id)

        if product_id not in self.products:
            print(f"Product with ID {product_id} not found.")
            return False

        product_name = self.products[product_id]["name"]
        del self.products[product_id]

        # Remove from all user carts
        for cart in self.user_carts.values():
            if product_id in cart:
                del cart[product_id]

        print(f"Product '{product_name}' with ID {product_id} deleted successfully.")
        return True

    # Admin Operations - Category Management
    def add_category(self, session_id, category_name):
        if not self.is_valid_session(session_id, "admin"):
            return False

        new_category_id = self.next_category_id
        self.next_category_id += 1

        self.categories[new_category_id] = category_name

        print(f"Category '{category_name}' added successfully with ID {new_category_id}.")
        return True

    def delete_category(self, session_id, category_id):
        if not self.is_valid_session(session_id, "admin"):
            return False

        category_id = int(category_id)

        if category_id not in self.categories:
            print(f"Category with ID {category_id} not found.")
            return False

        # Check if there are products in this category
        products_in_category = [p_id for p_id, p in self.products.items() if p["category_id"] == category_id]

        if products_in_category:
            print(f"Cannot delete category. There are {len(products_in_category)} products in this category.")
            return False

        category_name = self.categories[category_id]
        del self.categories[category_id]

        print(f"Category '{category_name}' with ID {category_id} deleted successfully.")
        return True


def display_menu(session_type=None):
    print("\n" + "=" * 50)
    print("Demo Marketplace Menu")
    print("=" * 50)

    if session_type is None:
        # Not logged in
        print("1. User Login")
        print("2. Admin Login")
        print("3. Exit")
    elif session_type == "user":
        # User menu
        print("1. View Product Catalog")
        print("2. View Categories")
        print("3. View Cart")
        print("4. Add to Cart")
        print("5. Remove from Cart")
        print("6. Checkout")
        print("7. Logout")
    elif session_type == "admin":
        # Admin menu
        print("1. View Product Catalog")
        print("2. View Categories")
        print("3. Add New Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Add New Category")
        print("7. Delete Category")
        print("8. Logout")

    return input("\nEnter your choice: ")


def display_payment_methods():
    print("\n" + "=" * 50)
    print("Payment Methods")
    print("=" * 50)
    print("1. Net Banking")
    print("2. PayPal")
    print("3. UPI")
    print("4. Debit Card")
    print("5. Credit Card")

    return input("\nChoose payment method: ")


def main():
    e_commerce = ECommerceBackend()
    e_commerce.display_welcome_message()

    session_id = None
    session_type = None

    while True:
        choice = display_menu(session_type)

        if session_type is None:
            # Not logged in
            if choice == "1":  # User Login
                username = input("Enter username: ")
                password = input("Enter password: ")
                session_id = e_commerce.login(username, password, "user")
                if session_id:
                    session_type = "user"

            elif choice == "2":  # Admin Login
                username = input("Enter admin username: ")
                password = input("Enter admin password: ")
                session_id = e_commerce.login(username, password, "admin")
                if session_id:
                    session_type = "admin"

            elif choice == "3":  # Exit
                print("Thank you for visiting Demo Marketplace. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        elif session_type == "user":
            # User menu
            if choice == "1":  # View Product Catalog
                e_commerce.display_catalog(session_id)

            elif choice == "2":  # View Categories
                e_commerce.display_categories(session_id)

            elif choice == "3":  # View Cart
                e_commerce.display_cart(session_id)

            elif choice == "4":  # Add to Cart
                e_commerce.display_catalog(session_id)
                product_id = input("\nEnter product ID to add to cart: ")
                quantity = input("Enter quantity: ")
                e_commerce.add_to_cart(session_id, product_id, quantity)

            elif choice == "5":  # Remove from Cart
                e_commerce.display_cart(session_id)
                product_id = input("\nEnter product ID to remove from cart: ")
                quantity = input("Enter quantity to remove (leave blank to remove all): ")
                quantity = int(quantity) if quantity.strip() else None
                e_commerce.remove_from_cart(session_id, product_id, quantity)

            elif choice == "6":  # Checkout
                e_commerce.display_cart(session_id)
                payment_method = display_payment_methods()
                e_commerce.checkout(session_id, payment_method)

            elif choice == "7":  # Logout
                if e_commerce.logout(session_id):
                    session_id = None
                    session_type = None

            else:
                print("Invalid choice. Please try again.")

        elif session_type == "admin":
            # Admin menu
            if choice == "1":  # View Product Catalog
                e_commerce.display_catalog(session_id)

            elif choice == "2":  # View Categories
                e_commerce.display_categories(session_id)

            elif choice == "3":  # Add New Product
                name = input("Enter product name: ")
                e_commerce.display_categories(session_id)
                category_id = input("Enter category ID: ")
                price = input("Enter product price: ")
                e_commerce.add_product(session_id, name, category_id, price)

            elif choice == "4":  # Update Product
                e_commerce.display_catalog(session_id)
                product_id = input("\nEnter product ID to update: ")
                name = input("Enter new name (leave blank to keep current): ")
                e_commerce.display_categories(session_id)
                category_id = input("Enter new category ID (leave blank to keep current): ")
                price = input("Enter new price (leave blank to keep current): ")

                e_commerce.update_product(
                    session_id,
                    product_id,
                    name if name.strip() else None,
                    category_id if category_id.strip() else None,
                    price if price.strip() else None
                )

            elif choice == "5":  # Delete Product
                e_commerce.display_catalog(session_id)
                product_id = input("\nEnter product ID to delete: ")
                e_commerce.delete_product(session_id, product_id)

            elif choice == "6":  # Add New Category
                category_name = input("Enter new category name: ")
                e_commerce.add_category(session_id, category_name)

            elif choice == "7":  # Delete Category
                e_commerce.display_categories(session_id)
                category_id = input("\nEnter category ID to delete: ")
                e_commerce.delete_category(session_id, category_id)

            elif choice == "8":  # Logout
                if e_commerce.logout(session_id):
                    session_id = None
                    session_type = None

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()