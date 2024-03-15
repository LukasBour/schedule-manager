import mysql.connector
import User
import Logging
from icecream import ic


# Saves a dictionary of data to a specified table in the schedule-manager database
# call directly only if you know what your doing. For saver execution, use specified
# caller functions
def write_to_database(table_name: str, data: dict):
    mydb = mysql.connector.connect(  # Connect to database
        host="localhost",
        user="",
        password="",
        database="schedule-manager"
    )

    # Create cursor for database access
    mycursor = mydb.cursor()

    # Craft command from data
    command = f"INSERT INTO {table_name} ("
    for key in data.keys():
        command += f"{key}, "
    command = command[:-2]
    command += ") VALUES ("
    for key in data.keys():
        if type(data.get(key)) is str:
            command += f"\'{data.get(key)}\', "
        else:
            command += f"{data.get(key)}, "
    command = command[:-2]
    command += ")"

    # Execute command
    try:
        mycursor.execute(command)
    except mysql.connector.Error as e:
        Logging.print_error("Could not execute MySQL command due to the following error:")
        Logging.print_error(str(e))
    # Commit changes
    mydb.commit()


def write_user_data(user: User.User) -> None:
    data = {
        "email": user.email,
        "password_hash": user.password_hash,
        "salt": user.salt,
        "alias": user.alias
    }
    write_to_database("users", data)


# Main entry point for testing only
if __name__ == "__main__":
    user_test = User.User("test@web.de", "Test1234", "Timmy Turner")
    write_user_data(user_test)
