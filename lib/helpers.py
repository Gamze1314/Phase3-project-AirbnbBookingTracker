# lib/helpers.py
from models.booking import Booking
from models.rental import Rental


def get_all_rentals():
    return Rental.get_all()


def print_all_rentals():
    rentals = get_all_rentals()
    for i, rental in enumerate(rentals, start=1):
        print(f"{i}. 🏠 {rental}")


def create_rental():
    property_type = input("Enter the property's type: ")
    address = input("Enter the property's location: ")
    number_of_rooms = int(input("Enter the number of rooms: "))
    daily_rate = int(input("Enter the daily booking rate: "))

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
            address = input("Enter the property's location: ")
            number_of_rooms = int(input("Enter the number of rooms: "))
            daily_rate = int(input("Enter the daily booking rate: "))

            # Assign new values to the rental object
            rental.property_type = property_type
            rental.address = address
            rental.number_of_rooms = number_of_rooms
            rental.daily_rate = daily_rate

            # Update the rental in the database
            rental.update()
            print(f'The property at {address} has been updated!')
            print_all_rentals()
        except Exception as exc:
            print("Error updating property: ", exc)


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


def print_bookings_by_rental_id(rental_id):
    rental = Rental.find_by_id(rental_id)
    # bookings = rental.bookings()

    if rental:
        bookings = rental.bookings()
        print(f"\nYou are at the property address: {rental.address}. The current number of bookings: {len(bookings)}.\n")
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
                print(f"\nThe bookings for property address: {current_address}\n")
            print(
                f"{i}. 📅 {booking.guest_name} is checking out on {booking.check_out_date}.")
        else:
            print(f"The booking {booking.guest_name} at (unknown address)")


def create_booking(rental_id):
    #prompt user for booking details.
    guest_name = input("Enter the guest's name: ").title()
    check_in_date = input("Enter the check-in date (YYYY-MM-DD): ")
    check_out_date = input("Enter the check-out date (YYYY-MM-DD): ")

    try:
        booking = Booking.create(
            guest_name, check_in_date, check_out_date, rental_id)
        print("🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠")
        print(
            f' 📅 New booking for {booking.guest_name} has been created!')
    except Exception as exc:
        print("Please try again: ", exc)


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
