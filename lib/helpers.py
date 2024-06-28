# lib/helpers.py
from models.booking import Booking
from models.rental import Rental
from datetime import datetime


def get_all_rentals():
    return Rental.get_all()


def print_all_rentals():
    rentals = get_all_rentals()
    print("\n*** Existing Properties ***\n")
    for i, rental in enumerate(rentals, start=1):
        print(f"{i}. 🏠 {rental}")


def validate_property_type(property_type):
    #create a list for the property types
    valid_types = ["house", "apartment", "condo", "studio", "hotel"]
    if property_type.lower().strip() in valid_types:
        return True
    else:
        print("\nInvalid property type. Please choose from: house, apartment, condo, studio, hotel.\n")
        print("Error creating property.Please try again by selecting A in the main menu.")
        return False
    

def validate_address(address):
    # Validate the address format (alphanumeric and spaces allowed)
    if address.replace(' ', '').isalnum() and isinstance(address, str):
        return True
    else:
        print("Invalid address format. Please enter a valid address with alphanumeric characters and spaces only.")
        print("Error creating property.Please try again by selecting A in the main menu.")
        return False


def validate_number_of_rooms(rooms):
    if isinstance(rooms, int):
        if rooms >= 0:
            return True
    else:
        print("\nNumber of rooms must be 0 or greater than 0.\n")
        print("Error creating property.Please try again by selecting A in the main menu.")
        return False
    
def validate_daily_rate(rate):
    if isinstance(rate, int):
        if rate >= 0:
            return True
    else:
        print("\nDaily rate must be 0 or greater than 0.\n")
        print("Error creating property.Please try again by selecting A in the main menu.")
        return False

def create_rental(address, property_type, daily_rate, number_of_rooms):
    if not validate_property_type(property_type):
        return

    if not validate_address(address):
        return
    
    if not validate_number_of_rooms(number_of_rooms):
        return
    
    if not validate_daily_rate(daily_rate):
        return

    try:
        rental = Rental.create(property_type, address,
                               number_of_rooms, daily_rate)
        print(f"{rental} has been created!")
    except Exception as exc:
        print("Error creating department: ", exc)


def update_rental(rental_id):
    rental = Rental.find_by_id(rental_id)

    if rental:
        try:
            property_type = input("Enter the property's type: ")
            if not validate_property_type(property_type):
                return
            
            address = input("Enter the property's location: ")
            if not validate_address(address):
                return
            
            number_of_rooms = int(input("Enter the number of rooms: "))
            if not validate_number_of_rooms(number_of_rooms):
                return
            
            daily_rate = int(input("Enter the daily booking rate: "))
            if not validate_daily_rate(daily_rate):
                return

            # Assign new values to the rental object
            rental.property_type = property_type
            rental.address = address
            rental.number_of_rooms = number_of_rooms
            rental.daily_rate = daily_rate

            # Update the rental in the database
            rental.update()
            print(f'The property at {address} has been updated!')
            print_all_rentals()
        except Exception:
            print("Error updating property: ")


def delete_rental(rental_id):
    rental = Rental.find_by_id(rental_id)

    if not rental:
        print('The property is not found.Please try again.')
    else:
        try:
            rental.delete()  # Delete the rental
            print(
                f'Success: The property at {rental.address} has been deleted!')
        except Exception as exc:
            print("Error deleting property: ", exc)


# booking helper functions

def get_all_bookings():
    return Booking.get_all()

#validate rental_id ; whether exists in db and numberical value.
def validate_rental_id(rental_id):
    # validating rental id ; edge case if user enters a number that does not exist in the database.if it can't find the rental will keep reprompts you until you enter the correct rental number.
    if isinstance(rental_id, int) and rental_id > 0:
        rental = Rental.find_by_id(rental_id)
        return rental is not None
    else:
        return False

def print_bookings_by_rental_id(rental_id):
    rental = Rental.find_by_id(rental_id)

    if rental:
        bookings = rental.bookings()
        print(
            f"\nYou are at the property address: {rental.address}. The current number of bookings: {len(bookings)}.\n")
        for i, booking in enumerate(bookings, start=1):
            print(
                f"{i}. 📅 {booking.guest_name} is checking out on {booking.check_out_date}.")
    else:
        print(f"No bookings found at rental address {rental.address}.")



def print_sorted_bookings():
    # a list of bookings with associated rentals.
    bookings = get_all_bookings()

    sorted_bookings = sorted(bookings, key=lambda booking: Rental.find_by_id(
        booking.rental_id).address if Rental.find_by_id(booking.rental_id) else "")

    current_address = ""
    for i, booking in enumerate(sorted_bookings, start=1):
        rental = Rental.find_by_id(booking.rental_id)
        if rental:
            if rental.address != current_address:
                current_address = rental.address
                print(
                    f"\nThe bookings for property address: {current_address}\n")
            print(
                f"{i}. 📅 {booking.guest_name} is checking out on {booking.check_out_date}.")
        else:
            print(f"The booking {booking.guest_name} at (unknown address)")

# validation for date, takes prompt string and validates the check-in/check-out dates every after entry.

def get_valid_date(prompt_message):
    while True:
        date_str = input(prompt_message)
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            formatted_date = date_obj.strftime('%Y-%m-%d')
            return formatted_date
        except ValueError:
            print("\nInvalid date format. Please enter the date in YYYY-MM-DD format.\n")

# Validating rental_id, guest_name.


def create_booking(rental_id, guest_name=None):
    rental = Rental.find_by_id(rental_id)
    # validating rental id ; edge case if user enters a number that does not exist in the database.if it can't find the rental will keep reprompts you until you enter the correct rental number.
    while not rental:
        print("The property is not found. Please try a valid property number.Please select from the existing properties.")
        print_all_rentals()
        rental_id = input("\nPlease select property number (1,2...): ")
        rental = Rental.find_by_id(rental_id)

    rental_id = int(rental_id)
    guest_name = input("Enter the guest's name: ").title()

    if guest_name.isalpha():
        # validate check-in/check-out dates if user enters invalid format.
        while True:
            check_in_date = get_valid_date(
                "Enter the check-in date (YYYY-MM-DD): ")

            check_out_date = get_valid_date(
                "Enter the check-out date (YYYY-MM-DD): ")

            try:
                booking = Booking.create(
                    guest_name, check_in_date, check_out_date, rental_id)
                print("🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠")
                print(
                    f' 📅 New booking for {booking.guest_name} has been created!')
            except Exception as exc:
                print("Please try again: ", exc)
    else:
        print("\nThe guest name can only contain letters.\n")
        # recalling func to re-prompt for guest name, passing rental id.
        create_booking(rental_id)


def update_booking(rental_id):
    rental = Rental.find_by_id(rental_id)

    if rental:
        bookings = rental.bookings()
        if bookings:
            try:
                booking_index = int(
                    input("Enter the booking number you want to update: ")) - 1
                if 0 <= booking_index < len(bookings):
                    selected_booking = bookings[booking_index]

                    new_guest_name = input(
                        f"Enter the new guest's name (current: {selected_booking.guest_name}): ").title()
                    new_check_in_date = input(
                        f"Enter the new check-in date (YYYY-MM-DD) (current: {selected_booking.check_in_date}): ")
                    new_check_out_date = input(
                        f"Enter the new check-out date (YYYY-MM-DD) (current: {selected_booking.check_out_date}): ")

                    selected_booking.guest_name = new_guest_name or selected_booking.guest_name
                    selected_booking.check_in_date = new_check_in_date or selected_booking.check_in_date
                    selected_booking.check_out_date = new_check_out_date or selected_booking.check_out_date

                    selected_booking.update()

                    print(
                        f" 📅 The booking for {selected_booking.guest_name} has been updated successfully!")
                    print("🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠")
                else:
                    print("Invalid booking number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid booking number.")
        else:
            print(f"No bookings found for the property at {rental.address}.")
    else:
        print("Rental property not found.")


def delete_booking(rental_id):
    rental = Rental.find_by_id(rental_id)

    if rental:
        bookings = rental.bookings()
        if bookings:
            try:
                booking_index = int(
                    input("Enter the booking number you want to delete: ")) - 1
                if 0 <= booking_index < len(bookings):
                    selected_booking = bookings[booking_index]

                    confirmation = input(
                        f"Are you sure you want to delete the booking for {selected_booking.guest_name}? (y/n): ").lower()
                    if confirmation == 'y':
                        selected_booking.delete()
                        print(
                            f"Booking for {selected_booking.guest_name} has been deleted successfully!")
                    else:
                        print("Booking deletion canceled.")
                else:
                    print("Invalid booking number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid booking number.")
        else:
            print(f"No bookings found for the property at {rental.address}.")
    else:
        print("Rental property not found.")


def exit_program():
    print("Thank you!")
    exit()
