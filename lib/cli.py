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
        menu()
        choice = input("> ")
        if choice == "1":
            list_rentals()
        elif choice == "2":
            find_rental_by_id()
        elif choice == "3":
            find_rental_by_guest_name()
        elif choice == "4":
            create_rental()
        elif choice == "5":
            update_rental()
        elif choice == "6":
            delete_rental()
        elif choice == "7":
            list_bookings()
        elif choice == "8":
            find_booking_by_id()
        elif choice == "9":
            create_booking()
        elif choice == "10":
            update_booking()
        elif choice == "11":
            delete_booking()
        elif choice == "12":
            exit_program()


def menu():
    print("Please select one of following options:")
    print("1. List all properties")
    print("2. Find rental by ID")
    print("3. Create a new property record")
    print("4. Update a property record")
    print("5. Delete a property record")
    print("6. List all bookings")
    print("7. Find booking by ID")
    print("8. Create a new booking record")
    print("9. Update a booking record")
    print("10. Delete a booking record")
    print("11. List all bookings for a property")
    print("12. Exit")


if __name__ == "__main__":
    main()
