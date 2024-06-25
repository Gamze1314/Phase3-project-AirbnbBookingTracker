from models.__init__ import CONN, CURSOR
from models.booking import Booking


class Rental:

    all = {}
    # Initialize the rental object.

    def __init__(self, property_type, address, number_of_rooms, daily_rate, id=None):
        self.id = id  # pk- db is auto-incrementing id once it is saved to the db.
        self.property_type = property_type
        self.address = address
        self.number_of_rooms = number_of_rooms
        self.daily_rate = daily_rate

    def __str__(self):  # print rental details str representation
        return f'Property Type: {self.property_type}, Address: {self.address}, Number of Rooms: {self.number_of_rooms}, Daily Rate: {self.daily_rate}'

    # Create properties for property type, address(str), number of rooms should be integer in the db.
    @property
    def property_type(self):
        return self._property_type

    @property_type.setter
    def property_type(self, value):
        try:
            if isinstance(value, str):
                self._property_type = value
        except Exception as exc:
            raise TypeError('Property type must be a string.', exc)

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError('Address must be a string')
        self._address = value

    @property
    def number_of_rooms(self):
        return self._number_of_rooms

    @number_of_rooms.setter
    def number_of_rooms(self, value):
        try:
            if isinstance(value, int):
                self._number_of_rooms = value
        except Exception as exc:
            raise TypeError(
                'Number of rooms must be an integer and greater than zero.', exc)

    @property
    def daily_rate(self):
        return self._daily_rate

    @daily_rate.setter
    def daily_rate(self, value):
        if not isinstance(value, int):
            raise TypeError('Daily rate must be an integer')
        self._daily_rate = value


# create class methods to interact with the database.
# create a table

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Rental instances """
        sql = """
            CREATE TABLE IF NOT EXISTS rentals (
            id INTEGER PRIMARY KEY,
            property_type TEXT,
            address TEXT,
            number_of_rooms INTEGER,
            daily_rate INTEGER)
            """
        CURSOR.execute(sql)
        CONN.commit()

# drop table
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Rental instances """
        sql = """
            DROP TABLE IF EXISTS rentals
            """
        CURSOR.execute(sql)
        CONN.commit()
# breakpoint()

    def save(self):
        """ Insert a new row with attribute values of the current Rental instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """ 
            INSERT INTO rentals (property_type, address, number_of_rooms, daily_rate)
            VALUES (?,?,?,?)
            """
        CURSOR.execute(sql, (self.property_type, self.address,
                       self.number_of_rooms, self.daily_rate))
        self.id = CURSOR.lastrowid
        CONN.commit()

# breakpoint()

    def update(self):
        """Update the table row corresponding to the current Rental instance."""
        sql = """
            UPDATE rentals
            SET property_type =?, address =?, number_of_rooms =?, daily_rate =?
            WHERE id =?
            """

        CURSOR.execute(sql, (self.property_type, self.address,
                       self.number_of_rooms, self.daily_rate, self.id))
        CONN.commit()

    # create new instance
    @classmethod
    def create(cls, property_type, address, number_of_rooms, daily_rate):
        """ Initialize a new Rental instance and save the object to the database """
        rental = cls(property_type, address, number_of_rooms, daily_rate)
        rental.save()
        cls.all[rental.id] = rental
        return rental

    def delete(self):
        """Delete the table row corresponding to the current Rental instance."""
        sql = """
            DELETE FROM rentals
            WHERE id=?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    # Delete the dictionary entry using id as the key
        if self.id in type(self).all:
            del type(self).all[self.id]

    # Set the id to None
        self.id = None

    # pull an instance from db with given row as a parameter

    @classmethod
    def instance_from_db(cls, row):
        """Return a Rental object having the attribute values from the table row."""
        # Check the dictionary for an existing instance using the row's primary key
        rental = cls.all.get(row[0])
        if rental:
            rental.property_type = row[1]
            rental.address = row[2]
            rental.number_of_rooms = row[3]
            rental.daily_rate = row[4]
        else:
            # if not in dictionary, create new instance and add to dictionary
            rental = cls(row[1], row[2], row[3], row[4])
            rental.id = row[0]
            cls.all[rental.id] = rental

        return rental

    @classmethod
    def find_by_id(cls, id):
        """Return a Rental object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM rentals
            WHERE id =? """
        
        row = CURSOR.execute(sql, (id,),)
        return cls.instance_from_db(CURSOR.fetchone()) if row else None


    @classmethod
    def get_all(cls):
        """Return a list containing a Rental object per row in the table"""
        sql = """
            SELECT *
            FROM rentals
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_guest_name(cls, guest_name):
        """Return a list of Rental objects corresponding to rows matching the specified guest name."""
        sql = """
            SELECT rentals.*
            FROM rentals
            JOIN bookings ON rentals.id = bookings.rental_id
            WHERE bookings.guest_name = ?
        """

        rows = CURSOR.execute(sql, (guest_name,)).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else []

    @classmethod
    def find_by_address(cls, address):
        """Return a list of Rental objects corresponding to rows matching the specified address."""
        sql = """
            SELECT rentals.*
            FROM rentals
            WHERE rentals.address =?
        """

        rows = CURSOR.execute(sql, (address,)).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else []
    

    def bookings(self):
        # return all bookings associated with this rental.
        from models.booking import Booking

        sql = """
            SELECT *
            FROM bookings
            WHERE rental_id =? """

        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()  # a list of tuples containing all rows of the booking table
        return [
            Booking.instance_from_db(row) for row in rows
        ]
