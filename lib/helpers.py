#lib/helpers.py
from models.booking import Booking
from models.rental import Rental


def list_rentals():
    rentals = Rental.get_all()
    for rental in rentals:
        print(rental)


def find_rental_by_guest_name():
    name = input("Please enter the guest name: ")
    rental = Rental.find_by_guest_name(name)
    if rental:
        print(f'{name} is currently at rental ID {rental.id}') # rental id or address ?
    else:
        print(f'Guest name {name} not found')


def find_rental_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the property's id: ")
    rental = Rental.find_by_id(id_)
    if rental:
        print(rental)
    else:
        print(f'Rental ID {id_} not found')


def create_rental():
    property_type = input("Enter the property's type: ")
    address = input("Enter the property's location: ")
    number_of_rooms = input("Enter the number of rooms: ")
    daily_rate = input("Enter the daily booking rate: ")

    try:
        rental = Rental.create(property_type, address, number_of_rooms, daily_rate)
        print(f'Success: {rental} has been created!')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_rental():
    id_ = input("Enter the property's id: ")
    if rental := Rental.find_by_id(id_):
        try:
            property_type = input("Enter the property's type: ")
            address = input("Enter the property's location: ")
            number_of_rooms = input("Enter the number of rooms: ")
            daily_rate = input("Enter the daily booking rate: ")

            #assign new values to the rental object
            rental.property_type = property_type
            rental.address = address
            rental.number_of_rooms = number_of_rooms
            rental.daily_rate = daily_rate
        #update the rental in the database
            rental.update()
            print(f'Success: {rental} has been updated!')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Property {id_} not found')


def delete_rental():
    id_ = input("Enter the property's id: ")
    if rental := Rental.find_by_id(id_):
        rental.delete()
        print(f'The property {id_} deleted')
    else:
        print(f'The property {id_} not found')


# booking helper functions
def list_bookings():
    bookings = Booking.get_all()
    for booking in bookings:
        print(booking)


def find_booking_by_id():
    id_ = input("Enter the booking's id: ")
    booking = Booking.find_by_id(id_)
    if booking:
        print(booking)
    else:
        print(f'Booking ID {id_} not found')



def create_booking():
    guest_name = input("Enter the guest's name: ")
    check_in_date = input("Enter the check-in date (YYYY-MM-DD): ")
    check_out_date = input("Enter the check-out date (YYYY-MM-DD): ")
    rental_id = input("Enter the rental's id: ")

    try:
        booking = Booking.create(guest_name, check_in_date, check_out_date, rental_id)
        print(f'Success: {booking} has been created!')
    except Exception as exc:
        print("Error creating department: ", exc)



def update_booking():
    id_ = input("Enter the booking's id: ")
    if booking := Booking.find_by_id(id_):
        try:
            guest_name = input("Enter the guest's name: ")
            check_in_date = input("Enter the check-in date (YYYY-MM-DD): ")
            check_out_date = input("Enter the check-out date (YYYY-MM-DD): ")
            rental_id = input("Enter the rental's id: ")

            #assign new values to the booking object
            booking.guest_name = guest_name
            booking.check_in_date = check_in_date
            booking.check_out_date = check_out_date
            booking.rental_id = rental_id
        #update the booking in the database
            booking.update()
            print(f'Success: {booking} has been updated!')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Booking ID {id_} not found')


def delete_booking():
    id_ = input("Enter the booking's id: ")
    if booking := Booking.find_by_id(id_):
        booking.delete()
        print(f'The booking {id_} deleted')
    else:
        print(f'The booking {id_} not found')


def list_rental_bookings():
    id_ = input('Enter a rental ID: ')
    rental = Rental.find_by_id(id_)
    #List associated bookings
    all_bookings = rental.bookings()
    for booking in all_bookings:
        print(booking)


def exit_program():
    print("Goodbye!")
    exit()
        
