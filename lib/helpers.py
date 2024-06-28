# lib/helpers.py
from models.booking import Booking
from models.rental import Rental
from datetime import datetime

# create a list for the property types
valid_types = ["house", "apartment", "condo", "studio" ,"hotel"]


def get_all_rentals():
    return Rental.get_all()


def print_all_rentals():
    rentals = get_all_rentals()
    print("\n*** Existing Properties ***\n")
    for i, rental in enumerate(rentals, start=1):
        print(f"{i}. 🏠 {rental}")


def validate_property_type(property_type):
    #validates property type.
    if property_type.lower().strip() in valid_types:
        return True
    else:
        print("Please try again with valid types by selecting the option in the main menu.")
        print("\nValid property types :  house, apartment, condo, studio ,hotel\n")
        return False


def validate_address(address):

    # Validate the address format (alphanumeric and spaces allowed)
    if address.replace(' ', '').isalnum() and isinstance(address, str):
        return True
    else:
        print("Error creating property.Please try again by selecting A in the main menu.")
        return False


def validate_number_of_rooms(number_of_rooms):
    # handle number of rooms to be integer and greater than 0.
    # handle exception when input is not a number.
    # handle exception when input is not a positive integer.

    try:
        number_of_rooms = int(number_of_rooms)
        if isinstance(number_of_rooms, int):
            if number_of_rooms > 0:
                return True
        else:
            print("\nNumber of rooms must be a number and greater than 0.\n")
            return False
    except ValueError:
        print("Number of rooms must be an integer.")
        return False


def validate_daily_rate(daily_rate):
    try:
        daily_rate = int(daily_rate)
        if isinstance(daily_rate, int):
            if daily_rate > 0:
                return True
        else:
            print("\nThe daily rate must be a number and greater than 0.\n")
            return False
    except ValueError:
        print("The daily rate must be an integer.")
        return False

# validate rental_id ; whether exists in db and numberical value.


def validate_rental_id(rental_id):
    # validating rental id ; edge case if user enters a number that does not exist in the database.if it can't find the rental will keep reprompts you until you enter the correct rental number.
    if isinstance(rental_id, int):
        if rental_id > 0:
            rental = Rental.find_by_id(rental_id)
            return rental is not None
    else:
        return False


def create_rental(property_type, address, number_of_rooms, daily_rate):
   # input collection and validation before attempting to create new rental.
   # validation functions are called
   # if any validations fail, user will be prompted.

    if not validate_property_type(property_type):
       return

    if not validate_address(address):
        return

    if not validate_number_of_rooms(number_of_rooms):
        return
    number_of_rooms = int(number_of_rooms)

    if not validate_daily_rate(daily_rate):
        return
    daily_rate = int(daily_rate)

    try:
        rental = Rental.create(
            property_type, address, number_of_rooms, daily_rate)
        print(f"{rental} has been created!")

    except Exception as exc:
        print("\nError creating rental: ", exc)


def update_rental(rental_id):
    #true/or false for rental_id validation.
    #if valid integer => find rental => update.
    if not validate_rental_id(rental_id):
        return

    rental = Rental.find_by_id(rental_id)

    if rental:
        try:
            property_type = input("Enter the property's type: ")
            if not validate_property_type(property_type):
                return

            address = input("Enter the property's location: ")
            if not validate_address(address):
                return

            number_of_rooms = input("Enter the number of rooms: ")
            if not validate_number_of_rooms(number_of_rooms):
                return
            number_of_rooms = int(number_of_rooms)

            daily_rate = input("Enter the daily booking rate: ")
            if not validate_daily_rate(daily_rate):
                return
            daily_rate = int(daily_rate)

            # Assign new values to the rental object
            rental.property_type = property_type
            rental.address = address
            rental.number_of_rooms = number_of_rooms
            rental.daily_rate = daily_rate

            # Update the rental in the database
            rental.update()
            print(f'The property at {address} has been updated!')
        except Exception as exc:
            print("Error updating property: ", exc)


def delete_rental(rental_id):
    # true/or false for rental_id validation.
    # if valid integer => find rental => delete.
    if not validate_rental_id(rental_id):
        return
    
    rental = Rental.find_by_id(rental_id)
    try:
        rental.delete()  # Delete the rental
        print(
            f"\nThe property at {rental.address} has been deleted!\n")
    except Exception:
        print("Error deleting property.Please try again.")


# booking helper functions adn validations 

def validate_booking_id(booking_id):
    # validating booking id user enters; edge case if user enters a number that does not exist in the database.if it can't find the booking will keep reprompts until you enter the correct booking number/selection.

    #bookings will be listed according to the rental selection in the main menu. 
    #enumerated numbers will not be same as db ids. 

    if not isinstance(booking_id, int) or booking_id <= 0:
        return False

    booking = Booking.find_by_id(booking_id)
    if booking is None:
        return False

    return True


def validate_guest_name(guest_name):
    pass




def validate_booking_date_range(check_in_date, check_out_date):
    pass


# def create_booking(rental_id, guest_name, check_in_date, check_out_date):
#     pass


# def update_booking(booking_id, guest_name, check_in_date, check_out_date):
#     pass


# def delete_booking(booking_id):
#     pass



def get_all_bookings():
    return Booking.get_all()




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
                    f'\n📅 New booking for {booking.guest_name} has been created!\n')
                #print all bookings for this rental
                print_bookings_by_rental_id(rental_id)
                break
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
                #index of the bookings list starts from 0.
                #user selects 1, we need to pick the index 0.
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
                    print("\nInvalid booking number. Please try again.\n")
            #if user enters "f" ex. string:
            except ValueError:
                print("\nInvalid entry. Please enter a valid booking information.\n")
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
