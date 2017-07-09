import psycopg2
from config import parse_config_file


class PostgreSQLCRUD():
    """ CRUD, work with DB
    """

    def __init__(self):
        pass



    def db_insert(self, table, fields, values):
        """Build insert query with user parameters
        Args:
            table (str): table name
            fields (list or tuple): names of fields to insert values into
            values (list or tuple): values for inserting
        Returns:
            True: if operation was successful
            None: if operation wasn't successful
        """
        pass

    def db_update(self, table, set_data, filter_data):
        pass

    def db_select(self, table, fields):
        pass

    def db_delete(self, table, filter_field, filter_val):
        pass



    def db_connect(**kwargs):
        """Connect to DB, using parsed data

        :return:
        Connecting status.
        """

        db_query = ''

        for key, value in kwargs.iteritems():
            db_query += "%s='%s' " % (key, value)

        try:
            conn = psycopg2.connect(db_query)
            cursor = conn.cursor()
            print "Opened database successfully"
        except:
            print "I am unable to connect to the database"
        return True


    def db_create():
        cursor.execute('''CREATE TABLE HOSTEL
              (ID INT PRIMARY KEY     NOT NULL,
              NAME            TEXT    NOT NULL,
              PLACES          INT     NOT NULL,
              ADDRESS         CHAR(50),
              PRICE           REAL);''')
        print "Table created successfully"


kwargs = parse_config_file("db_access")
PostgreSQLCRUD.db_connect(**kwargs)
PostgreSQLCRUD.db_create()

# conn.commit()
# conn.close()
