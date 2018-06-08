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
        create_request_table_cmd = "CREATE TABLE IF NOT EXISTS RequestTable(id TEXT PRIMARY KEY NOT NULL, requests TEXT, Type varchar(20), status varchar(20) NOT NULL, user_id TEXT);"
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
        self.cur.execute("SELECT * FROM RequestTable WHERE user_id = '{}' ".format(_id[0]))
        requests = self.cur.fetchall()
        my_requests = []
        for request in requests:
            my_dict = {}
            my_dict['id'] = request[0]
            my_dict['type'] = request[1]
            my_dict['status'] = request[2]
            my_requests.append(my_dict)

        return requests
        

    def fetch_one_user(self, request_id):
        self.cur.execute("SELECT * FROM RequestTable WHERE id = '{}' ".format(request_id[0]))
        request = self.cur.fetchone()
        
        
        my_dict = {}
        my_dict['id'] = request[0]
        my_dict['type'] = request[1]
        my_dict['status'] = request[2]
        return my_dict


    def close(self):
        self.cur.close()
        self.conn.close()
