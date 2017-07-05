import psycopg2
from config import parse_config_file


class PostgreSQLCRUD():
    """ CRUD
    """

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
