# lib/cli.py

# Import helper functions and define main and menu functions.
from helpers import (
    exit_program,
    print_all_rentals,
    print_bookings_by_rental_id,
    create_rental,
    update_rental,
    delete_rental,
    print_bookings,
    create_booking,
    update_booking,
    delete_booking,
)


def main():
    # responsible for displaying the main menu and property management menu
    while True:
        # continuously runs the loop that calls the main menu
        main_menu()
        choice = input("> ")

        if choice.lower() == "p":
            main_rental_menu()
        elif choice.lower() == "b": #for booking management
            booking_management_loop() # >> stuck
        elif choice.lower() == "e": # to exit the program.
            exit_program()


def main_rental_menu():
    while True:
        print_all_rentals()
        rental_menu_one()  # Prints options for rentals
        rental_choice = input("> ").strip().lower()

        if rental_choice.isdigit():
            rental_id = int(rental_choice)
            booking_menu_loop_one(rental_id)

        elif rental_choice == "a":
            create_rental()
        elif rental_choice == "u":
            rental_id = int(input("Please select property number: "))
            update_rental(rental_id)
        elif rental_choice == "d":
            rental_id = int(input("Please select property number: "))
            delete_rental(rental_id)
        elif rental_choice.lower() == "b": # goes back to main() menu
            break
        elif rental_choice.lower() == "e":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def booking_management_loop():
    while True:
        booking_management_menu()
        # booking_choice = input("> ").strip().lower()
        booking_choice = input("> ")

        if booking_choice == "1":
            print_bookings()
        elif booking_choice == "2":
            #create a new booking after listing all rentals and letting user choose the rental to add new booking. 
            print_all_rentals()
            try:
                rental_id = int(input("Please select property number: "))
                create_booking(rental_id)
            except ValueError:
                print("Invalid input. Please enter a numeric property number.")
        elif booking_choice == "3":
            break
        elif booking_choice == "4":
            exit_program()
        else:
            print("Invalid choice. Please try again.")


#create loop for listing rental bookings and update, create, delete booking menu
# this will be displayed after user select the specific id (rental id). 
def booking_menu_loop_one(rental_id):
    while True:
        print_bookings_by_rental_id(rental_id)
        booking_menu_two() # options a,u, d, b, e for bookings associated with rental_id
        booking_choice = input("Please enter your selection: ").lower() #store user input

        if booking_choice == "a":
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
    print("🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠")
    print(">> Enter P for Property Management")
    print(">> Enter B for Booking Management")
    print(">> Enter E to exit")


def rental_menu_one():
    print("\n*** Property Management ***")
    print("*** Select rental number to manage its bookings ***") # selection based on id; 1,2,3...creates new loop.
    print("*** Enter A to add new property")
    print("*** Enter U to update a property ***")
    print("*** Enter D to delete a property ***")
    print("*** Enter B to go back to previous menu ***")
    print("*** Enter E to exit ***")



def booking_management_menu():
    print("\n*** Booking Management ***")
    print("1. View all bookings")
    print("2. Create new booking")
    print("3. Back to Previous Menu")
    print("4. Exit")


def booking_menu_two():
    print("🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠")
    print("*** Enter A to add new booking  ***")
    print("*** Enter U to update a booking  ***")
    print("*** Enter D to delete a booking  ***")
    print("*** Enter B to go back to previous menu  ***")
    print("*** Enter E to exit  ***")


if __name__ == "__main__":
    main()
