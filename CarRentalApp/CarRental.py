import datetime

class CarRental:
    def __init__(self, total_cars=20):
        """
        Constructor for initializing the car rental shop
        """
        self.available_cars = total_cars
        self.rented_cars = 0

        # Dictionary to store rentals with customer ID as key
        # Value is a tuple (number_of_cars, rental_time, rental_type)
        self.rentals = {}

        # Rental rates
        self.hourly_rate = 50  # $50 per car per hour
        self.daily_rate = 500  # $500 per car per day
        self.weekly_rate = 2500  # $2500 per car per week

    def display_available_cars(self):
        """
        Displays the number of available cars
        """
        print(f"We have {self.available_cars} cars available to rent.")
        return self.available_cars

    def _validate_rental(self, num_cars):
        """
        Helper method to validate rental conditions
        """
        if num_cars <= 0:
            print("Number of cars should be positive!")
            return False

        if num_cars > self.available_cars:
            print(f"Sorry! We only have {self.available_cars} cars available to rent.")
            return False

        return True

    def rent_hourly(self, customer_id, num_cars):
        """
        Rents cars on hourly basis
        """
        if not self._validate_rental(num_cars):
            return None

        rental_time = datetime.datetime.now()
        self.rentals[customer_id] = (num_cars, rental_time, "hourly")

        self.available_cars -= num_cars
        self.rented_cars += num_cars

        print(f"You have rented {num_cars} car(s) on hourly basis at {rental_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"You will be charged ${self.hourly_rate} per car per hour")
        print("We hope you enjoy our service!")

        return rental_time

    def rent_daily(self, customer_id, num_cars):
        """
        Rents cars on daily basis
        """
        if not self._validate_rental(num_cars):
            return None

        rental_time = datetime.datetime.now()
        self.rentals[customer_id] = (num_cars, rental_time, "daily")

        self.available_cars -= num_cars
        self.rented_cars += num_cars

        print(f"You have rented {num_cars} car(s) on daily basis at {rental_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"You will be charged ${self.daily_rate} per car per day")
        print("We hope you enjoy our service!")

        return rental_time

    def rent_weekly(self, customer_id, num_cars):
        """
        Rents cars on weekly basis
        """
        if not self._validate_rental(num_cars):
            return None

        rental_time = datetime.datetime.now()
        self.rentals[customer_id] = (num_cars, rental_time, "weekly")

        self.available_cars -= num_cars
        self.rented_cars += num_cars

        print(f"You have rented {num_cars} car(s) on weekly basis at {rental_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"You will be charged ${self.weekly_rate} per car per week")
        print("We hope you enjoy our service!")

        return rental_time

    def return_car(self, customer_id):
        """
        Return rented cars and calculate the bill
        """
        if customer_id not in self.rentals:
            print("Error: Customer ID not found in rentals.")
            return None

        num_cars, rental_time, rental_type = self.rentals[customer_id]

        # Calculate the rental period
        return_time = datetime.datetime.now()
        rental_period = return_time - rental_time

        # Calculate the bill based on rental type
        bill = 0

        if rental_type == "hourly":
            # Calculate hours, rounding up partial hours
            hours = rental_period.seconds / 3600
            if rental_period.seconds % 3600 != 0:
                hours += 1
            hours = int(hours)
            bill = hours * self.hourly_rate * num_cars
            print(f"Rental period: {hours} hour(s)")

        elif rental_type == "daily":
            # Calculate days, rounding up partial days
            days = rental_period.days
            if rental_period.seconds > 0:
                days += 1
            bill = days * self.daily_rate * num_cars
            print(f"Rental period: {days} day(s)")

        elif rental_type == "weekly":
            # Calculate weeks, rounding up partial weeks
            weeks = rental_period.days // 7
            if rental_period.days % 7 != 0:
                weeks += 1
            bill = weeks * self.weekly_rate * num_cars
            print(f"Rental period: {weeks} week(s)")

        # Update inventory
        self.available_cars += num_cars
        self.rented_cars -= num_cars

        # Remove rental from records
        del self.rentals[customer_id]

        # Generate and print the bill
        print("\n===== AUTO-GENERATED BILL =====")
        print(f"Rental start time: {rental_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Return time: {return_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Number of cars rented: {num_cars}")
        print(f"Rental basis: {rental_type}")
        print(f"Total bill: ${bill}")
        print("Thank you for using our service!")
        print("===============================")

        return bill