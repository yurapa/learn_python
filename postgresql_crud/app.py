import ConfigParser
import psycopg2

Config = ConfigParser.ConfigParser()
Config.read('config.ini')


def parse_config_file(section):
    """Parse config.ini file with DB access

    :return:
    options for connect with DB
    """

    db_parameters = {}

    if Config.has_section(section):
        options = Config.options(section)
        for option in options:
            db_parameters[option] = Config.get(section, option)
    return db_parameters


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
        print "Connected!\n"
    except:
        print "I am unable to connect to the database."


kwargs = parse_config_file("db_access")
db_connect(**kwargs)

# cur = conn.cursor()
# cur.execute('''CREATE TABLE COMPANY
#       (ID INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       AGE            INT     NOT NULL,
#       ADDRESS        CHAR(50),
#       SALARY         REAL);''')
# print "Table created successfully"

# conn.commit()
# conn.close()


# cur = conn.cursor()

# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#     VALUES (1, 'Paul', 32, 'California', 20000.00 )");

# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#     VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

# cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

# conn.commit()
# print "Records created successfully";
# conn.close()
