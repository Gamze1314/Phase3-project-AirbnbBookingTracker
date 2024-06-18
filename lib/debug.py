from datetime import datetime
from models.__init__ import CONN, CURSOR
from models.rental import Rental
from models.booking import Booking
import ipdb


def reset_database():
    try:
        # Drop and create tables
        Rental.drop_table()
        Booking.drop_table()
        Rental.create_table()
        Booking.create_table()

    # Create seed data
        rental1 = Rental.create("Apartment", "123 Main St", 2, 100)
        rental2 = Rental.create("House", "456 Elm St", 3, 200)

    # Create bookings for rental1
        Booking.create("Joseph Doe",
                       "2024-05-01", "2024-05-06", rental1.id)
        Booking.create("Jane Smith",
                       "2024-06-15", "2024-06-18", rental1.id)

        Booking.create("Alice Johnson",
                       "2024-07-10", "2024-07-17", rental2.id)
        Booking.create("Bob Brown",
                       "2024-08-20", "2024-08-22", rental2.id)

    except Exception as exc:
        print("Error creating database: ", exc)


reset_database()
ipdb.set_trace()
