**AirbnbBookingTracker CLI Application**

Table of Contents
*Introduction
*Features
*Technologies
*Installation
*Usage
*Main Menu
*Property Management
*Booking Management
*Helper Functions
*Contributing

Introduction
AirbnbBookingTracker is a command-line interface (CLI) application designed to manage property rentals and bookings. The application allows users to add, update, delete, and list properties and bookings efficiently. This CLI application is intended to be built to manage rental properties and guests' bookings for each property. The users are also able to add, update, delete, and list bookings individually.

Features
Property Management
Booking Management for Associated Properties

Technologies Used
Python: The primary programming language used to develop the CLI application.
SQLite: A lightweight, disk-based database used to store rental and booking data.
Object Relational Mapping (ORM): Used for database operations, making it easier to interact with the database using Python objects.
Table Relations: Utilized to manage the relationships between rental and bookings table.

View all properties
Find rental by guest name
Add a new property
Update a property
Delete a property


List all bookings
Create a new booking
Update a booking
Delete a booking
List all bookings for a property

Installation
Clone the repository:

git clone https://github.com/yourusername/AirbnbBookingTracker.git
cd AirbnbBookingTracker

Install the required dependencies:

pip install -r requirements.txt

Set up the database:

Ensure you have your database configured and connected correctly as per your application requirements.

Usage
Run the main CLI application:

python cli.py

Main Menu
Once you run the application, you will be presented with the main menu:


🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠
        *****Welcome to AirbnbBookingTracker!*****

                ______
               /      \
              /        \
             /__________\
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

🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠
>> Enter P for Property Management
>> Enter B for Booking Management
>> Enter E to exit
Property Management
Selecting P or p will take you to the Property Management menu:


*** Property Management ***
1. View all properties
2. Find rental by guest name
3. Back to Main Menu
4. Exit

View all properties: Lists all the properties.
Find rental by guest name: Finds and lists properties based on guest name.
Back to Main Menu: Returns to the main menu.
Exit: Exits the application.

Aditional Property Management options can be accessed after viewing properties:

Please select from below options:
1. Add a new property record
2. Update a property record
3. Delete a property record
4. Back to Main Menu
5. Exit



Booking Management
Selecting B or b will take you to the Booking Management menu:


*** Booking Management ***
1. List all bookings
2. List all bookings for a property
3. Back to Main Menu
4. Exit

List all bookings: Additional booking management options can be accessed after viewing bookings:

🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠
1. Create a new booking record
2. Update a booking record
3. Delete a booking record
4. Back to Main Menu
5. Exit


List all bookings for a property: Lists bookings for a particular property.
Back to Main Menu: Returns to the main menu.
Exit: Exits the application.

Helper Functions
The application uses several helper functions to manage the rental and booking data:

exit_program: Exits the application.
print_rentals: Prints the list of all rentals.
find_rental_by_guest_name: Finds and prints rentals based on guest name.
create_rental: Adds a new rental property.
update_rental: Updates an existing rental property.
delete_rental: Deletes a rental property.
print_bookings: Lists all bookings.
create_booking: Adds a new booking.
update_booking: Updates an existing booking.
delete_booking: Deletes a booking.
list_rental_bookings: Lists all bookings for a specific property.
clear_screen: Clears the console screen for better readability.


Contributing
Fork the repository.
Create your feature branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a pull request.




DB Diagram is created to demonstrate which rental and booking information is used to create instances.


![alt text](image.png)