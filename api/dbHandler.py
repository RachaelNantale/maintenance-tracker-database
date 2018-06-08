import psycopg2
from pprint import pprint



class MyDatabase():
    """
    Create class for the database
    """

    def __init__(self):
        """
        Connect the database to postgre
        """
        self.conn = psycopg2.connect(
            "dbname = 'Finals' user = 'postgres' host= 'localhost' password= 'oscarkirex' port = '5432'"
            )
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        self.create_user_table()
        self.create_request_table()

    def create_user_table(self):
        """
        create a table for users
        """
        create_user_table_cmd = " CREATE TABLE IF NOT EXISTS UserTable(id TEXT PRIMARY KEY NOT NULL,username varchar(200) NOT NULL, Password varchar(100), status boolean, email varchar (30) NOT NULL);"
        self.cur.execute(create_user_table_cmd)

    def create_request_table(self):
        """
        Create a table for requests
        """
        create_request_table_cmd = "CREATE TABLE IF NOT EXISTS RequestTable(id TEXT PRIMARY KEY NOT NULL, requests TEXT, Type varchar(20), status varchar(20) NOT NULL);"
        self.cur.execute(create_request_table_cmd)

    def create_user(self, _id, username, password, email, admin=False):
        """
        Create a User
        """
        self.cur.execute("INSERT INTO UserTable values('{}','{}','{}','{}','{}')".format(
            _id, username, password, admin, email))


    def user_login(self, username):
        """
        User login
        """
        self.cur.execute("SELECT * FROM UserTable WHERE username='{}'".format(username))
        user = self.cur.fetchone()
        return user
    def create_request(self, create_request_cmd):
        """create a request
        """
        self.cur.execute(create_request_cmd)
        pprint(create_request_cmd)

    def modify_request(self, modify_request_cmd):
        """
        Modify a request
        """
        self.cur.execute(modify_request_cmd)
        return True

    def fetch_all_requests_for_a_user(self, _id):
        """
        Fetch all request
        """
        self.cur.execute("SELECT * FROM RequestTable WHERE id = {}".format(_id))
        requests = self.cur.fetchall()
        return requests
        for request in requests:
            pprint(request)

    def fetch_one_user(self):
         """
        Fetch one request
        """
        # self.cur.execute("SELECT * FROM UserTable where username = {}".format(username))
        # users = self.cur.fetchone()
        # return users
        # for username in users:
        #     pprint(username)


    def close(self):
        self.cur.close()
        self.conn.close()
