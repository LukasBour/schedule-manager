# Project files
import User
import Logging
import Credentials

# Modules
import mysql.connector
from icecream import ic
import logging


# Connects to the schedule-manager database and executes the given command
def connect_and_execute(command: str) -> None:
    try:
        my_db = connect_to_database()
        execute_command(my_db, command)
    except mysql.connector.Error as e:
        raise


# Connects to the schedule-manager database and returns the database intance
def connect_to_database():
    try:
        mydb = mysql.connector.connect(  # Connect to database
            host="localhost",
            user=Credentials.db_username,
            password=Credentials.db_password,
            database="schedule-manager"
        )
        return mydb
    except mysql.connector.Error as e:
        Logging.print_error("Connecting to Database failed due to the following error:")
        Logging.print_error(str(e))
        raise


# Executes an command and automatically commits the changes to the database
def execute_command(database, command: str) -> None:
    try:
        # Execute command
        cursor = database.cursor()
        cursor.execute(command)
        # Commit changes
        database.commit()
    except mysql.connector.Error as e:
        Logging.print_error("Could not execute MySQL command due to the following error:")
        Logging.print_error(str(e))
        raise


# Saves a dictionary of data to a specified table in the schedule-manager database
# call directly only if you know what your doing. For saver execution, use specified
# caller functions
def write_to_database(table_name: str, data: dict) -> None:
    mydb = connect_to_database()
    if mydb is None:
        return

    # Craft command from data
    command: str = f"INSERT INTO {table_name} ("
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

    # Execute command and commit
    execute_command(mydb, command)


# Writes the data of a User to the database
def write_user_data(user: User.User) -> None:
    data = {
        "email": user.email,
        "password_hash": user.password_hash,
        "salt": user.salt,
        "alias": user.alias
    }
    write_to_database("users", data)


def get_pw_hash(email: str) -> str:
    my_db = connect_to_database()
    if my_db is None:
        return ""

    my_cursor = my_db.cursor()

    command: str = f"SELECT password_hash FROM users WHERE email=\'{email}\'"
    my_cursor.execute(command)
    result: tuple = my_cursor.fetchone()
    if result is None:
        raise AttributeError(f"Could not find User with E-Mail \"{email}\"")
    return result[0]


def get_user_from_db(email: str) -> User:
    my_db = connect_to_database()
    if my_db is None:
        return ""


# Main entry point for testing only
if __name__ == "__main__":
    get_pw_hash("test@web.de")
