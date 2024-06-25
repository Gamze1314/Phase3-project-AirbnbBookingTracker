# lib/helpers.py
from models.booking import Booking
from models.rental import Rental
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
# It uses os.system('cls' if os.name == 'nt' else 'clear') to clear the screen on both Windows and Unix-based systems


def get_all_rentals():
    return Rental.get_all()


def print_rentals():
    rentals = get_all_rentals()
    num_rentals = len(rentals)
    print(f"There are {num_rentals} properties found!")
    print("🏠" * num_rentals)
    for i, rental in enumerate(rentals, start=1):
        print(f"{i}. {rental}")


def find_rental_by_guest_name():
    name = input("Please enter the guest name: ")
    rentals = Rental.find_by_guest_name(name)
    if rentals:
        print(f'Rentals for guest name {name}:')
        for i, rental in enumerate(rentals, start=1):
            print(f"{i}. {name.title()} is currently staying at {rental.address}. The property's daily rate ${rental.daily_rate}.")
    else:
        print(f'Guest name {name} not found')


def create_rental():
    property_type = input("Enter the property's type: ")
    address = input("Enter the property's location: ")
    number_of_rooms = int(input("Enter the number of rooms: "))
    daily_rate = int(input("Enter the daily booking rate: "))

    try:
        rental = Rental.create(property_type, address,
                               number_of_rooms, daily_rate)
        print(f'Success: {rental} has been created!')
        print_rentals()
    except Exception as exc:
        print("Error creating department: ", exc)


def update_rental():
    address = input(
        "Enter the property's address in the format '456 Main St': ").lower()

    rentals = Rental.find_by_address(address)

    if not rentals:
        print(f'Property at {address} not found')
        return

    if len(rentals) == 1:
        rental = rentals[0]
        print(f"Property found with address {address}.")
    else:
        print("Multiple properties found:")
        for i, rental in enumerate(rentals, 1):
            print(f"{i}. {rental}")
        choice = int(
            input("Enter the number of the property you want to update: "))
        rental = rentals[choice - 1]

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
        print(f'Success: The property at {address} has been updated!')
        print_rentals()
    except Exception as exc:
        print("Error updating property: ", exc)


def delete_rental():
    address = input(
        "Enter the property's address in the following format '456 Main St': ")

    # Find rentals by address
    rentals = Rental.find_by_address(address)

    if not rentals:
        print(f'The property at {address} is not found.')
    else:
        for rental in rentals:
            # Check if the lowercase rental's address matches the input address
            if rental.address == str(address):
                print(f"Property found with address {address}.")
                try:
                    rental.delete()  # Delete the rental
                    print(
                        f'Success: The property at {rental.address} has been deleted!')
                except Exception as exc:
                    print("Error deleting property: ", exc)


# booking helper functions

def get_all_bookings():
    return Booking.get_all()


def print_bookings():
    bookings = get_all_bookings()  # a list of bookings
    print(f"There are {len(bookings)} bookings found!")
    print("🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠")
    for i, booking in enumerate(bookings, start=1):
        print(f"{i}. {booking.guest_name} is checking out on {booking.check_out_date}.")


def create_booking():
    guest_name = input("Enter the guest's name: ").title()
    check_in_date = input("Enter the check-in date (YYYY-MM-DD): ")
    check_out_date = input("Enter the check-out date (YYYY-MM-DD): ")
    address = input("Enter the address of the property: ")

    rental = Rental.find_by_address(address)

    while not rental:
        print("Not a valid address.Please try again.")
        address = input("Enter the address of the property: ")
        rental = Rental.find_by_address(address)

    try:
        booking = Booking.create(guest_name, check_in_date, check_out_date, rental[0].id)
        print(
            f'Success: The booking for {booking.guest_name} has been created!')
        print_bookings()
    except Exception as exc:
        print("Error creating department: ", exc)


def update_booking():
    name = input("Enter the guest's name in following format 'Joseph Doe': ")
    if booking := Booking.find_by_guest_name(name):
        print(
            f"Matching record found  >>>>   The guest '{booking.guest_name}' is checking out on {booking.check_out_date}")
        try:
            guest_name = input("Enter the guest's name: ")
            check_in_date = input("Enter the check-in date (YYYY-MM-DD): ")
            check_out_date = input("Enter the check-out date (YYYY-MM-DD): ")

            # assign new values to the booking object
            booking.guest_name = guest_name
            booking.check_in_date = check_in_date
            booking.check_out_date = check_out_date
        # update the booking in the database
            booking.update()
            print(f'Success: The booking for {name} has been updated!')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Booking for guest "{name}" not found')

    print_bookings()


def delete_booking():
    name = input("Enter the guest name: ")
    if booking := Booking.find_by_guest_name(name):
        try:
            booking.delete()
            print(f'The booking for {name} deleted')
        except Exception as exc:
            print("Error deleting department: ", exc)
    else:
        print(f'The booking for {name} not found')

    print_bookings()


def list_rental_bookings():
    address = input('Enter the property address: ')
    rentals = Rental.find_by_address(address)

    if rentals:  # rentals is a list of rentals.
        for rental in rentals:
            # List associated bookings for each rental
            bookings = rental.bookings()
            print(f"There are {len(bookings)} bookings found!")
            for i, booking in enumerate(bookings, start=1):
                print(
                    f"{i}. {booking.guest_name} is checking out on {booking.check_out_date}.")
    else:
        print("No rentals found for the given address.")


def exit_program():
    print("Thank you. Goodbye!")
    exit()
