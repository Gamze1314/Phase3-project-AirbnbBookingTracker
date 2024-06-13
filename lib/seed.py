# #!/usr/bin/env python3

# from models.__init__ import CONN, CURSOR
# from models.rental import Rental
# from models.room import Room
# from models.booking import Booking


# def seed_database():
#     # Drop existing tables
#     Room.drop_table()
#     Booking.drop_table()
#     Rental.drop_table()

#     # Create tables
#     Rental.create_table()
#     Room.create_table()
#     Booking.create_table()

#     # Create seed data for rental
#     rental_data = {"property_type": "Apartment",
#                    "address": "123 Main St", "number_of_rooms": 2}
#     rental = Rental(**rental_data)
#     rental.save()

#     # Create seed data for room
#     room_data = {"room_number": 101, "rental_id": 1}
#     room = Room(**room_data)
#     room.save()

#     # Create seed data for booking
#     booking_data = {"room_id": 1, "check_in_date": "2024-05-01", "check_out_date": "2024-05-07",
#                     "guest_name": "John Doe", "length_of_stay": 7, "daily_rate": 100, "total": 700}
#     booking = Booking(**booking_data)
#     booking.save()


# seed_database()
# print("Seeded database")


# use this data to populate the respective tables in the database. Each dictionary represents a single record in the table, with keys corresponding to column names and values representing the data for each column.
