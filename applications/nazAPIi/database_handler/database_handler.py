import sqlite3


class DatabaseHandler:
    connection = None
    def __init__(self):
        self.connection = self.startup()


    def startup(self):
        try:
            with sqlite3.connect(":memory:") as conn:
                c = conn.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, age INTEGER, role TEXT)")
                conn.commit()

                c.execute("INSERT INTO users (username, age, role) VALUES (?, ?, ?)", ("Nazarii", "23", "admin"))
                c.execute("INSERT INTO users (username, age, role) VALUES (?, ?, ?)", ("Jonas", "87", "user"))

                conn.commit()

                return c

        except Exception as e:
            print(e)


    def get_all_users(self):
        self.connection.execute("SELECT * FROM users")
        return self.connection.fetchall()

    def get_user_by_search(self, search_term):
        self.connection.execute("SELECT * FROM users WHERE username LIKE ?", (f"%{search_term}%",))
        return self.connection.fetchall()
