from CarRentalApp.CarRental import CarRental
from CarRentalApp.Customer import Customer


def display_menu():
    """
    Display the main menu of the car rental system
    """
    print("\n===== Welcome to Car Rental System =====")
    print("1. Display available cars")
    print("2. Rent a car")
    print("3. Return a car")
    print("4. Exit")
    return input("Enter your choice (1-4): ")

def main():
    """
    Main function to run the car rental program
    """
    print("Car Rental System - OOP Implementation")
    print("=======================================")

    # Create a car rental shop with 20 cars
    shop = CarRental(20)

    # Customer ID counter
    customer_id_counter = 100

    # Dictionary to keep track of customers
    customers = {}

    # Main program loop
    while True:
        choice = display_menu()

        try:
            choice = int(choice)

            if choice == 1:
                # Display available cars
                shop.display_available_cars()

            elif choice == 2:
                # Rent a car
                customer_id = customer_id_counter
                customer_id_counter += 1

                # Create a new customer
                customer = Customer(customer_id)
                customers[customer_id] = customer

                print(f"Your customer ID is: {customer_id}")
                print("Please remember this ID for returning the car.")

                # Display available cars
                available = shop.display_available_cars()
                if available <= 0:
                    continue

                # Get rental details
                try:
                    num_cars = int(input(f"How many cars would you like to rent (1-{available})? "))

                    print("\nRental Options:")
                    print("1. Hourly rental ($50 per car per hour)")
                    print("2. Daily rental ($500 per car per day)")
                    print("3. Weekly rental ($2500 per car per week)")

                    rental_choice = int(input("Choose rental type (1-3): "))

                    if rental_choice == 1:
                        customer.request_car(shop, num_cars, "hourly")
                    elif rental_choice == 2:
                        customer.request_car(shop, num_cars, "daily")
                    elif rental_choice == 3:
                        customer.request_car(shop, num_cars, "weekly")
                    else:
                        print("Invalid rental type choice!")
                        # Remove the customer if rental fails
                        del customers[customer_id]

                except ValueError:
                    print("Please enter a valid number!")
                    # Remove the customer if rental fails
                    del customers[customer_id]

            elif choice == 3:
                # Return a car
                try:
                    customer_id = int(input("Enter your customer ID: "))
                    if customer_id in customers:
                        customer = customers[customer_id]
                        customer.return_car(shop)
                        # Remove customer after return
                        del customers[customer_id]
                    else:
                        print("Customer ID not found!")
                except ValueError:
                    print("Please enter a valid customer ID!")

            elif choice == 4:
                # Exit the program
                print("Thank you for using our Car Rental System. Goodbye!")
                break

            else:
                print("Invalid choice! Please enter a number between 1 and 4.")

        except ValueError:
            print("Please enter a valid number!")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
