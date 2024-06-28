# lib/cli.py

# Import helper functions and define main and menu functions.
from helpers import (
    exit_program,
    print_all_rentals,
    print_bookings_by_rental_id,
    create_rental,
    update_rental,
    delete_rental,
    print_sorted_bookings,
    create_booking,
    update_booking,
    delete_booking,
    validate_rental_id,
    validate_address,
    validate_daily_rate,
    validate_number_of_rooms,
    validate_property_type,
)


def main():
    # responsible for displaying the main menu.
    while True:
        # continuously runs the loop that calls the main menu
        main_menu()
        choice = input("> ")

        if choice.lower() == "p":
            main_rental_menu()
        elif choice.lower() == "b":  # for booking viewing/creating.
            booking_management_loop()
        elif choice.lower() == "e":
            exit_program()


def main_rental_menu():
    while True:
        print_all_rentals()
        rental_menu_one()  # Prints options for rentals
        rental_choice = input(
            "\nPlease enter your selection (A, U, D, B, E or 1, 2...to manage bookings): ").lower()

        if rental_choice.isdigit():
            rental_id = int(rental_choice)
            rental_exists = validate_rental_id(
                rental_id)  # return True or false
            if rental_exists:
                print_bookings_by_rental_id(rental_id)
                # if user selects the rental number and is valid, it will show the booking menu to a,u,d,e,b.
                booking_menu_loop_one(rental_id)
            else:
                print("\nInvalid rental number. Please try again.\n")

        elif rental_choice == "a":
            # if validation is successful, create rental. it does not keep user stuck in the loop if any of these values is not valid.returns True/false and pass the values to create_rental() func.
            address = input("Enter the property's location: ")
            if not validate_address(address):
                continue

            property_type = input(
                "Enter the property's type (house, apartment, condo, studio, hotel): ")
            if not validate_property_type(property_type):
                continue

            daily_rate = input("Enter the daily booking rate: ")
            if not validate_daily_rate(daily_rate):
                continue

            number_of_rooms = input("Enter the number of rooms: ")
            if not validate_number_of_rooms(number_of_rooms):
                continue

            if validate_address(address) and validate_property_type(property_type) and validate_daily_rate(daily_rate) and validate_number_of_rooms(number_of_rooms):
                # if all validations are successful, create a new rental.

                create_rental(property_type, address,
                              number_of_rooms, daily_rate)

        elif rental_choice == "u":
            rental_id = input(
                "Please select existing property number (1,2...): ")
            # check if rental_id is a number
            if rental_id.strip().isdigit():
                rental_id = int(rental_id)
                # check for rental_id is in the database, returns a boolean value
                rental_exists = validate_rental_id(rental_id)

                # if the rental exists, update the rental
                if rental_exists:
                    # if rental id exists/valid, call update_rental()
                    update_rental(rental_id)
                else:
                    print("\nInvalid rental number. Please try again.\n")
            else:
                print("\nInvalid rental number. Please try again.\n")

        elif rental_choice == "d":
            rental_id = input(
                "Please select existing property number (1,2...): ")

            if rental_id.strip().isdigit():
                rental_id = int(rental_id)
                print(rental_id)
                rental_exists = validate_rental_id(rental_id)

                if rental_exists:
                    delete_rental(rental_id)
                else:
                    print("\nInvalid rental number. Please try again.\n")
            else:
                print("\nInvalid rental number. Please try again.\n")

        elif rental_choice.lower() == "b":  # go back to main() menu
            break
        elif rental_choice.lower() == "e":
            exit_program()
        else:
            print("Invalid choice. Please try again.")


def booking_management_loop():
    while True:
        booking_management_menu()
        booking_choice = input("> ").lower()

        if booking_choice == "v":
            print_sorted_bookings()
        elif booking_choice == "c":
            # create a new booking after listing all rentals and let the user choose the rental to add new booking.
            print_all_rentals()
            rental_id = input("\nPlease select property number (1,2...): ")
            create_booking(rental_id)
        elif booking_choice == "b":
            break
        elif booking_choice == "e":
            exit_program()
        else:
            print("Invalid choice. Please try again.")


# create loop for listing rental bookings and update, create, delete booking menu
# this will be displayed after user select one of enumerated numbers (rental id).
def booking_menu_loop_one(rental_id):
    while True:
        booking_menu_two()  # options a,u, d, b, e for bookings associated with rental_id
        booking_choice = input(
            "\nPlease enter your selection (A, U, D, B, E): ").lower()  # store user input

        if booking_choice == "a":
            # create a new booking for selected rental_id.
            # validate the booking checkin/checkout, guest_name
            # before creating a booking.
            create_booking(rental_id)
        elif booking_choice == "u":
            update_booking(rental_id)
        elif booking_choice == "d":
            delete_booking(rental_id)
        elif booking_choice == "b":
            break
        elif booking_choice == "e":
            exit_program()
        else:
            print("Invalid choice. Please try again.")


def main_menu():
    print("🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠")
    house_art = """
        *****Welcome to AirbnbBookingTracker!*****
    
                    ______
                   /      \\
                  /        \\
                 /__________\\
                 |  __  __  |
                 | |  ||  | |
                 | |  ||  | |
                 | |__||__| |
                 |  __  __()|
                 | |  ||  | |
                 | |  ||  | |
                 | |  ||  | |
                 | |__||__| |
                 |__________|
                """
    print(house_art)
    print("\n🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠\n")
    print(">>  P: Manage Property and Bookings")
    print(">>  B: View/Create Bookings")
    print(">>  E: Exit")


def rental_menu_one():
    print("\n*** Property Management ***\n")
    # selection based on id; 1,2,3...creates new loop.
    print(">> Enter rental number to manage its bookings")
    print(">> Enter A to add a new property")
    print(">> Enter U to update a property")
    print(">> Enter D to delete a property")
    print(">> Enter B to go back to the previous menu")
    print(">> Enter E to exit")


def booking_management_menu():
    print("\n*** Bookings Menu ***\n")
    print(">> Enter V to view all bookings")
    print(">> Enter C to create a new booking for an existing address")
    print(">> Enter B to go back to the previous menu")
    print(">> Enter E to exit")


def booking_menu_two():
    print("\n***  Manage Bookings for this property  ***\n")
    print(">> Enter A to add a new booking")
    print(">> Enter U to update a booking")
    print(">> Enter D to delete a cancelled booking")
    print(">> Enter B to go back to the previous menu")
    print(">> Enter E to exit\n")


if __name__ == "__main__":
    main()
