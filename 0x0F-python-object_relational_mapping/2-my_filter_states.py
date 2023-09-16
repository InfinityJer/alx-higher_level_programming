#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
Usage: ./2-my_filter_states.py <mysql_username>
                             <mysql_password>
                             <database_name>
                             <state_name_searched>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if four command-line arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> <state_name_searched>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    mysql_username, mysql_password, database_name, state_name_searched = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Use format to create the SQL query with user input
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name_searched)
    
    # Execute the SQL query
    cursor.execute(query)

    # Fetch all the rows from the result set
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
