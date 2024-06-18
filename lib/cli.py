# lib/cli.py

# Import helper functions and define main and menu functions.
from helpers import (
    exit_program,
    print_rentals,
    find_rental_by_guest_name,
    create_rental,
    update_rental,
    delete_rental,
    print_bookings,
    create_booking,
    update_booking,
    delete_booking,
    list_rental_bookings,
    clear_screen,
)


def main():
    # responsible for displaying the main menu and property management menu
    while True:
        # continuously runs the loop that calls the main menu
        main_menu()
        choice = input("> ")
        if choice.lower() == "p":
            while True:
                rental_menu_one()
                rental_choice = input("> ")
                if rental_choice == "1":
                    print_rentals()
                    # Pause to let the user see the properties, it clears the screen immediately after printing the properties.
                    input("\nPress Enter to continue...")
                    clear_screen()
                    rental_menu_loop()
                elif rental_choice == "2":
                    find_rental_by_guest_name()
                elif rental_choice == "3":
                    break  # Go back to the main menu
                elif rental_choice == "4":
                    exit_program()

        elif choice.lower() == "b":
            booking_menu_loop()

        elif choice.lower() == "e":
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
    print("🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠")
    print(">> Enter P for Property Management")
    print(">> Enter B for Booking Management")
    print(">> Enter E to exit")


def rental_menu_one():
    print("\n*** Property Management ***")
    print("1. View all properties")
    print("2. Find rental by guest name")
    print("3. Back to Main Menu")
    print("4. Exit")


def rental_menu_two():
    print("🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠")
    print("Please select from below options:")
    print("1. Add a new property record")
    print("2. Update a property record")
    print("3. Delete a property record")
    print("4. Back to Main Menu")
    print("5. Exit")


def rental_menu_loop():
    while True:
        rental_menu_two()
        rental_choice = input("> ")
        if rental_choice == "1":
            create_rental()
        elif rental_choice == "2":
            update_rental()
        elif rental_choice == "3":
            delete_rental()
            # needed break after deletion.
            input("\nPress Enter to view updated property list...")
            print_rentals()
        elif rental_choice == "4":
            break  # Go back to the first rental menu
        elif rental_choice == "5":
            exit_program()
        else:
            print("Invalid choice. Please try again.")


def booking_menu_loop():
    while True:
        booking_menu_one()
        booking_choice = input("> ")
        if booking_choice == "1":
            print_bookings()
            while True:
                booking_menu_two()
                booking_choice = input("> ")
                if booking_choice == "1":
                    create_booking()
                elif booking_choice == "2":
                    update_booking()
                elif booking_choice == "3":
                    delete_booking()
                elif booking_choice == "4":
                    break
                elif booking_choice == "5":
                    exit_program()
                else:
                    print("Invalid choice. Please try again.")
        elif booking_choice == "2":
            list_rental_bookings()
        elif booking_choice == "3":
            break  # Go back to the main menu
        elif booking_choice == "4":
            exit_program()
        else:
            print("Invalid choice. Please try again.")


def booking_menu_one():
    print("\n*** Booking Management ***")
    print("1. List all bookings")
    print("2. List all bookings for a property")
    print("3. Back to Main Menu")
    print("4. Exit")


def booking_menu_two():
    print("🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠")
    print("1. Create a new booking record")
    print("2. Update a booking record")
    print("3. Delete a booking record")
    print("4. Back to Main Menu")
    print("5. Exit")


if __name__ == "__main__":
    main()
