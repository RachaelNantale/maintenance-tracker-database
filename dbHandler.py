import psycopg2
from pprint import pprint


class MyDatabase():
    def __init__(self):
        self.conn = psycopg2.connect(
            "dbname = 'db' user = 'postgres' host= 'localhost' password= 'oscarkirex' port = '5432'")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def create_user_table(self):
        self.cur.execute("DROP TABLE IF EXISTS users")
        create_user_table_cmd = " CREATE TABLE users(username varchar(20), Password varchar(10), type varchar(20) NOT NULL);"
        self.cur.execute(create_user_table_cmd)

    def create_request_table(self):
        self.cur.execute("DROP TABLE IF EXISTS requests")
        create_request_table_cmd = "CREATE TABLE requests( id int, requests varchar(20), Type varchar(10), status varchar(20) NOT NULL);"
        self.cur.execute(create_request_table_cmd)

    def create_user(self):
        create_request_cmd = "INSERT INTO users VALUES('rachael', '123abc', 'admin');"
        pprint(create_request_cmd)

    def fetch_all_requests(self):
        self.cur.execute("SELECT * FROM requests")
        requests = self.cur.fetchall()
        for request in requests:
            pprint(request)

    def fetch_all_users(self):
        self.cur.execute("SELECT * FROM users")
        users = self.cur.fetchall()
        for username in users:
            pprint(username)

    def delete_request(self, id):
        self.cur.execute("DELETE FROM requests WHERE id = {} ".format(id))

    def modify_request(self, id):
        self.cur.execute("UPDATE requests SET request =%s WHERE id = %s ")

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == "__main__":

    db = MyDatabase()
    db.create_user_table()
    db.create_request_table()
    db.create_user()
    db.fetch_all_users()
    db.close()
#
