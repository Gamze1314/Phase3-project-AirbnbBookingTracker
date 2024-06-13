#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.rental import Rental
from models.booking import Booking


def seed_database():
    # Drop existing tables
    Booking.drop_table()
    Rental.drop_table()

    # Create tables
    Rental.create_table()
    Booking.create_table()

    # Create seed data for rentals
    rentals_data = [
        {"property_type": "Apartment", "address": "123 Main St", "number_of_rooms": 2, "daily_rate": 200},
        {"property_type": "House", "address": "456 Elm St", "number_of_rooms": 3, "daily_rate": 100}
    ]

    for rental_data in rentals_data:
        rental = Rental(**rental_data)
        rental.save()

    # Create seed data for bookings
    bookings_data = [
        {"guest_name": "John D.", "check_in_date": "2024-05-01",
            "check_out_date": "2024-05-07", "rental_id": 1},
        {"guest_name": "Jane S.", "check_in_date": "2024-06-15",
            "check_out_date": "2024-06-18", "rental_id": 1},
        {"guest_name": "Alice J.", "check_in_date": "2024-07-10",
            "check_out_date": "2024-07-17", "rental_id": 2},
        {"guest_name": "Bob B.", "check_in_date": "2024-08-20",
            "check_out_date": "2024-08-22", "rental_id": 2}
    ]
    for booking_data in bookings_data:
        booking = Booking(**booking_data)
        booking.save()


seed_database()
print("Seeded database")

# use this data to populate the respective tables in the database. Each dictionary represents a single record in the table, with keys corresponding to column names and values representing the data for each column.-DONE
