import sqlite3
from schemas.users import User


class DatabaseHandler:
    connection = None
    def __init__(self):
        self.connection = self.startup()


    def startup(self):
        try:
            with sqlite3.connect(":memory:") as conn:
                cursor = conn.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, age INTEGER, role TEXT)")
                conn.commit()

                cursor.execute("INSERT INTO users (username, age, role) VALUES (?, ?, ?)", ("Nazarii", "23", "admin"))
                cursor.execute("INSERT INTO users (username, age, role) VALUES (?, ?, ?)", ("Jonas", "87", "user"))

                conn.commit()

                return cursor

        except Exception as e:
            print(e)


    def get_all_users(self):
        self.connection.execute("SELECT * FROM users")

        users = []
        for row in self.connection.fetchall():
            user = User(id=row[0], username=row[1], age=row[2], role=row[3])
            users.append(user)

        return users

    def get_user_by_search(self, search_term):
        self.connection.execute("SELECT * FROM users WHERE username LIKE ?", (f"%{search_term}%",))

        users = []
        for row in self.connection.fetchall():
            user = User(id=row[0], username=row[1], age=row[2], role=row[3])
            users.append(user)

        return users
