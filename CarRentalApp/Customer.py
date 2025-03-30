class Customer:
    def __init__(self, customer_id):
        """
        Constructor for Customer class
        """
        self.customer_id = customer_id
        self.rented = False

    def request_car(self, car_rental, num_cars, rental_type):
        """
        Method for requesting a car rental
        """
        if self.rented:
            print("You already have cars rented. Please return them before renting again.")
            return None

        if rental_type == "hourly":
            result = car_rental.rent_hourly(self.customer_id, num_cars)
        elif rental_type == "daily":
            result = car_rental.rent_daily(self.customer_id, num_cars)
        elif rental_type == "weekly":
            result = car_rental.rent_weekly(self.customer_id, num_cars)
        else:
            print("Invalid rental type. Choose from 'hourly', 'daily', or 'weekly'.")
            return None

        if result:
            self.rented = True
            return result
        return None

    def return_car(self, car_rental):
        """
        Method for returning rented cars
        """
        if not self.rented:
            print("You don't have any cars rented.")
            return None

        bill = car_rental.return_car(self.customer_id)
        if bill:
            self.rented = False
            return bill
        return None
