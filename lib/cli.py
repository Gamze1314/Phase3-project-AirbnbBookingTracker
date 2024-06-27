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
)


def main():
    # responsible for displaying the main menu and property/booking management menu
    while True:
        # continuously runs the loop that calls the main menu
        main_menu()
        choice = input("> ")

        if choice.lower() == "p":
            main_rental_menu()
        elif choice.lower() == "b": #for booking management
            booking_management_loop()
        elif choice.lower() == "e":
            exit_program()


def main_rental_menu():
    while True:
        print_all_rentals()
        rental_menu_one()  # Prints options for rentals
        rental_choice = input("\nPlease enter your selection (A, U, D, B, E or 1, 2...): ").lower()

        if rental_choice.isdigit():
            rental_id = int(rental_choice)
            booking_menu_loop_one(rental_id)

        elif rental_choice == "a":
            create_rental()
        elif rental_choice == "u":
            rental_id = int(input("Please select property number (1,2...): "))
            update_rental(rental_id)
        elif rental_choice == "d":
            rental_id = int(input("Please select property number (1,2...): "))
            delete_rental(rental_id)
        elif rental_choice.lower() == "b": # go back to main() menu
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
            #create a new booking after listing all rentals and let the user choose the rental to add new booking. 
            print_all_rentals()
            rental_id = input("\nPlease select property number (1,2...): ")
            create_booking(rental_id)
        elif booking_choice == "b":
            break
        elif booking_choice == "e":
            exit_program()
        else:
            print("Invalid choice. Please try again.")


#create loop for listing rental bookings and update, create, delete booking menu
# this will be displayed after user select one of enumerated numbers (rental id). 
def booking_menu_loop_one(rental_id):
    while True:
        print_bookings_by_rental_id(rental_id)
        booking_menu_two() # options a,u, d, b, e for bookings associated with rental_id
        booking_choice = input("\nPlease enter your selection (A, U, D, B, E): ").lower() #store user input

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
