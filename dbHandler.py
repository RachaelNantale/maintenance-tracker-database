import psycopg2
from pprint import pprint


class MyDatabase():
    def __init__(self):
        self.conn = psycopg2.connect(
            "dbname = 'db' user = 'postgres' host= 'localhost' password= 'oscarkirex' port = '5432'")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def create_user_table(self):
        self.cur.execute("DROP TABLE IF EXISTS UserTable")
        create_user_table_cmd = " CREATE TABLE UserTable(username varchar(20), Password varchar(10), type varchar(20) NOT NULL);"
        self.cur.execute(create_user_table_cmd)

    def create_request_table(self):
        self.cur.execute("DROP TABLE IF EXISTS RequestTable")
        create_request_table_cmd = "CREATE TABLE RequestTable( id int, requests varchar(2000), Type varchar(10), status varchar(20) NOT NULL);"
        self.cur.execute(create_request_table_cmd)

    def create_user(self):
        create_user_cmd = "INSERT INTO users VALUES('rachael', '123abc', 'admin');"
        self.cur.execute(create_user_cmd)
        pprint(create_user_cmd)

    def create_request(self):
        create_request_cmd = "INSERT INTO requests VALUES(1, 'The request','Repair','admin');"
        self.cur.execute(create_request_cmd)
        pprint(create_request_cmd)

    def fetch_all_requests(self):
        self.cur.execute("SELECT * FROM requests")
        requests = self.cur.fetchall()
        return requests
        for request in requests:
        	pprint(request)

    def fetch_one_users(self):
        self.cur.execute("SELECT * FROM users")
        users = self.cur.fetchone()
        return users
        for username in users:
            pprint(username)

    def delete_request(self, id):
        self.cur.execute("DELETE FROM requests WHERE id = {} ".format(id))
        return True


    def modify_request(self, id):
        self.cur.execute("UPDATE requests SET request =%s WHERE id = %s ")
        return True

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == "__main__":

    db = MyDatabase()
    # db.create_user_table()
    # db.create_request_table()
    db.create_user()
    db.create_request()
    # db.fetch_all_users()
    db.close()
#
