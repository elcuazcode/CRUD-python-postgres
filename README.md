# CRUD-python-postgres

# **README**

## **Introduction**

This is a script for managing a PostgreSQL database of users. It allows you to create, list, update, and delete user records in a user-friendly way.

## **Requirements**

This script requires the following:

- Python 3.x
- PostgreSQL
- psycopg2
- dotenv

## **Installation**

To use this script, please follow these steps:

1. Clone the repository to your local machine.
2. Install the required packages by running **`pip install -r requirements.txt`** in your terminal.
3. Create a **`.env`** file in the root directory of the project and add your database credentials in the following format:

```
makefileCopy code
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host

```

1. Run the script by running **`python main.py`** in your terminal.

## **Usage**

Once you have run the script, you will be presented with a menu of options:

- **`a`** - Create a new user
- **`b`** - List all users
- **`c`** - Update an existing user
- **`d`** - Delete an existing user
- **`q`** - Quit the script

Select an option by entering the corresponding letter, and follow the prompts to complete the action.

Note that this script is designed to be run in the terminal and may not have a graphical user interface.

## **License**

This script is released under the MIT License. See LICENSE.md for more information.
