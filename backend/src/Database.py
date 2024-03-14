import mysql.connector
import User
import Logging
from icecream import ic


# Saves a dictionary of data to a specified table in the schedule-manager database
def save_to_database(table_name: str, data: dict):
    mydb = mysql.connector.connect(  # Connect to database
        host="localhost",
        user="",
        password="",
        database="schedule-manager"
    )

    # From here on only testing
    mycursor = mydb.cursor()

    user = User.User("test3", "test1234")
    user2 = User.User("test2", "test1234")

    try:
        mycursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (%s, %s, %s)",
                         (user.username, user.password_hash, user.salt))
        mycursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (%s, %s, %s)",
                         (user2.username, user2.password_hash, user2.salt))
        mydb.commit()
    except mysql.connector.Error as e:
        Logging.print_error("MySQL command not executed due to the following error:")
        Logging.print_error(e.msg)

    mycursor.execute("SELECT * FROM users")
    result = mycursor.fetchall()
    ic(result)


# Main entry point for testing only
if __name__ == "__main__":
    save_to_database("", {})
