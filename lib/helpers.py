# lib/helpers.py
from models.booking import Booking
from models.rental import Rental



def list_rentals():
    rentals = Rental.get_all()
    print(f"There are {len(rentals)} properties found!")
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
    number_of_rooms = input("Enter the number of rooms: ")
    daily_rate = input("Enter the daily booking rate: ")

    try:
        rental = Rental.create(property_type, address,
                               number_of_rooms, daily_rate)
        print(f'Success: {rental} has been created!')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_rental():
    address = input(
        "Enter the property's address in following format '456 Main St': ")
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
    except Exception as exc:
        print("Error updating property: ", exc)


def delete_rental():
    address = input(
        "Enter the property's address in following format '456 Main St': ")
    # returning a list of rental objects.
    rentals = Rental.find_by_address(address)

    if not rentals:
        print(f'The property at {address} is not found.')

    if len(rentals) == 1:
        rental = rentals[0]
        print(f"Property found with address {address}.")
        print(rental)
        try:
            rental.delete()
            print(f'The property at {address} has been deleted.')
        except Exception as exc:
            print("Error deleting property: ", exc)


# booking helper functions
def list_bookings():
    bookings = Booking.get_all() # a list of bookings
    print(f"There are {len(bookings)} bookings found!")
    for i, booking in enumerate(bookings, start=1):
        print(f"{i}. {booking.guest_name} is checking out on {booking.check_out_date}.")


def create_booking():
    guest_name = input("Enter the guest's name: ")
    check_in_date = input("Enter the check-in date (YYYY-MM-DD): ")
    check_out_date = input("Enter the check-out date (YYYY-MM-DD): ")
    rental_id = input("Enter the rental's id: ")

    try:
        booking = Booking.create(
            guest_name, check_in_date, check_out_date, rental_id)
        print(f'Success: The booking for {booking.guest_name} has been created!')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_booking():
    name = input("Enter the guest's name in following format 'Joseph Doe': ")
    if booking := Booking.find_by_guest_name(name):
        print("Matching record found!")
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


def list_rental_bookings():
    address = input('Enter the property address: ')
    rentals = Rental.find_by_address(address)

    if rentals: # rentals is a list of rentals.
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
