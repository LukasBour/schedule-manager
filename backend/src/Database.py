import mysql.connector
import User
import Logging
import Credentials
from icecream import ic


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
        return None


# Executes an command and automatically commits the changes to the database
def execute_command(database, command: str) -> None:
    # Execute command
    try:
        cursor = database.cursor()
        cursor.execute(command)
    except mysql.connector.Error as e:
        Logging.print_error("Could not execute MySQL command due to the following error:")
        Logging.print_error(str(e))
        return
    # Commit changes
    database.commit()


# Saves a dictionary of data to a specified table in the schedule-manager database
# call directly only if you know what your doing. For saver execution, use specified
# caller functions
def write_to_database(table_name: str, data: dict) -> None:

    mydb = connect_to_database()
    if mydb is None:
        return None

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


# Main entry point for testing only
if __name__ == "__main__":
    user_test = User.User("test@web.de", "Test1234", "Timmy Turner")
    write_user_data(user_test)
