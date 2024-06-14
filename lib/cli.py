# lib/cli.py

# import helper functions and define main and menu functions.
from helpers import (
    exit_program,
    list_rentals,
    find_rental_by_id,
    find_rental_by_guest_name,
    create_rental,
    update_rental,
    delete_rental,
    list_bookings,
    find_booking_by_id,
    create_booking,
    update_booking,
    delete_booking,
    list_rental_bookings,
)


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice.lower() == "p":
            while True:
                rental_menu()
                rental_choice = input("> ")
                if rental_choice == "1":
                    list_rentals()
                elif rental_choice == "2":
                    find_rental_by_id()
                elif rental_choice == "3":
                    find_rental_by_guest_name()
                elif rental_choice == "4":
                    create_rental()
                elif rental_choice == "5":
                    update_rental()
                elif rental_choice == "6":
                    delete_rental()
                elif rental_choice == "7":
                    break  # Go back to the main menu
                elif rental_choice == "8":
                    exit_program()
                else:
                    print("Invalid choice. Please try again.")
        elif choice.lower() == "b":
            while True:
                booking_menu()
                booking_choice = input("> ")
                if booking_choice == "1":
                    list_bookings()
                elif booking_choice == "2":
                    find_booking_by_id()
                elif booking_choice == "3":
                    create_booking()
                elif booking_choice == "4":
                    update_booking()
                elif booking_choice == "5":
                    delete_booking()
                elif booking_choice == "6":
                    list_rental_bookings()
                elif booking_choice == "7":
                    break  # Go back to the main menu
                elif booking_choice == "8":
                    exit_program()
                else:
                    print("Invalid choice. Please try again.")
        elif choice.lower() == "e":
            exit_program()
        else:
            print("Invalid choice. Please try again.")


def main_menu():
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
    print(">> Enter P or p for Property Management")
    print(">> Enter B or b for Booking Management")
    print(">> Enter E or e to exit")


def rental_menu():
    print("\n*** Property Management ***")
    print("1. List all properties")
    print("2. Find rental by ID")
    print("3. Find rental by guest name")
    print("4. Create a new property record")
    print("5. Update a property record")
    print("6. Delete a property record")
    print("7. Back to Main Menu")
    print("8. Exit")


def booking_menu():
    print("\n*** Booking Management ***")
    print("1. List all bookings")
    print("2. Find booking by ID")
    print("3. Create a new booking record")
    print("4. Update a booking record")
    print("5. Delete a booking record")
    print("6. List all bookings for a property")
    print("7. Back to Main Menu")
    print("8. Exit")


if __name__ == "__main__":
    main()
