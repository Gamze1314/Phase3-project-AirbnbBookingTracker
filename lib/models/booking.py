from models.__init__ import CONN, CURSOR
from datetime import datetime


class Booking:

    all = {}

    # initialize
    def __init__(self, guest_name, check_in_date, check_out_date, rental_id, id=None):
        self.id = id  # pk
        self.guest_name = guest_name
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.rental_id = rental_id

    # properties to validate the type of data user enters

    @property
    def guest_name(self):
        return self._guest_name

    @guest_name.setter
    def guest_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Guest name must be a string')
        self._guest_name = value

    @property
    def check_in_date(self):
        return self._check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        if not isinstance(value, str):
            raise TypeError('Check-in date must be a string')

        # Convert string to datetime object
        date_object = datetime.strptime(value, '%Y-%m-%d')

        # Format the datetime object to display only the date (year-month-day)
        formatted_date = date_object.strftime('%Y-%m-%d')

        self._check_in_date = formatted_date

    @property
    def check_out_date(self):
        return self._check_out_date

    @check_out_date.setter
    def check_out_date(self, value):
        if not isinstance(value, str):
            raise TypeError('Check-out date must be a string')

        # Convert string to datetime object
        date_object = datetime.strptime(value, '%Y-%m-%d')

        # Format the datetime object to display only the date (year-month-day)
        formatted_date = date_object.strftime('%Y-%m-%d')

        self._check_out_date = formatted_date

        # Check if check-out date is before or equal to check-in date
        if self.check_in_date and self._check_out_date <= self.check_in_date:
            raise ValueError('Check-out date must be later than check-in date')
# Receive user input
# user_input = input("Enter the check-out date (YYYY-MM-DD): ")

# create a table
    @classmethod
    def create_table(cls):
        """create a table to persist the attributes of Booking instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS
            bookings (
            id INTEGER PRIMARY KEY,
            guest_name TEXT,
            check_in_date TEXT,
            check_out_date TEXT,
            rental_id INTEGER,
            FOREIGN KEY(rental_id) REFERENCES rentals(id))
            """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ drop the table that persists Booking instances"""
        sql = """
            DROP TABLE IF EXISTS bookings
            """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """save Booking instances by inserting into the database.
        Update object id attribute using the PK value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO bookings (guest_name, check_in_date, check_out_date, rental_id)
            VALUES (?,?,?,?)
            """

        CURSOR.execute(sql, (self.guest_name, self.check_in_date,
                       self.check_out_date, self.rental_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE bookings
            SET guest_name =?, check_in_date =?, check_out_date =?, rental_id =?
            WHERE id =?
            """

        CURSOR.execute(sql, (self.guest_name, self.check_in_date,
                       self.check_out_date, self.rental_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Booking instance."""
        sql = """
            DELETE FROM bookings
            WHERE id =?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

    @classmethod
    def create(cls, guest_name, check_in_date, check_out_date, rental_id):
        booking = cls(guest_name, check_in_date, check_out_date, rental_id)
        booking.save()
        return booking

    @classmethod
    def instance_from_db(cls, row):
        """Return a Booking object corresponding to the table row matching the specified primary key"""
        booking = cls.all.get(row[0])
        if booking:
            print("Booking found in cache:", booking)
            booking.guest_name = row[1]
            booking.check_in_date = row[2]
            booking.check_out_date = row[3]
            booking.rental_id = row[4]

        else:
            print("Booking not found in cache. Creating new instance.")
            # if not in dictionary, create new instance and add to dictionary
            booking = cls(row[1], row[2], row[3], row[4])
            booking.id = row[0]
            cls.all[booking.id] = booking

    @classmethod
    def find_by_id(cls, id):
        """Return a Booking object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM bookings
            WHERE id =? """

        CURSOR.execute(sql, (id,),)

        row = CURSOR.fetchone()  # a tuple containing all rows of the booking table
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_all(cls):
        """Return a list containing a Booking object per row in the table"""
        sql = """
            SELECT *
            FROM bookings
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_guest_name(cls, guest_name):
        """Return a Booking object corresponding to first table row matching specified guest name"""
        sql = """
            SELECT *
            FROM bookings
            WHERE guest_name is ?
        """

        row = CURSOR.execute(sql, (guest_name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_rental_id(cls, rental_id):
        sql = """SELECT *
            FROM bookings
            WHERE rental_id =?
            """

        row = CURSOR.execute(sql, (rental_id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_check_in_date(cls, check_in_date):
        sql = """ SELECT *
            FROM bookings
            WHERE check_in_date=?
            """
        rows = CURSOR.execute(sql, (check_in_date,)).fetchall()
        # converts each row to a Booking instance using instance_from_db()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_check_out_date(cls, check_out_date):

        sql = """ SELECT *
            FROM bookings
            WHERE check_out_date=?
            """
        rows = CURSOR.execute(sql, (check_out_date,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    # rentals => list all associated rentals
    def rentals(self):
        from models.rental import Rental

        sql = """SELECT *
            FROM rentals
            WHERE id =?
            """
        rows = CURSOR.execute(sql, (self.rental_id,)).fetchall()
        return [Rental.instance_from_db(row) for row in rows]

# if __name__ == "__main__":
# calculate total amount for each booking = length of stay * daily rate.
