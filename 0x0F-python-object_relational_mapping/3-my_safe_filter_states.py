#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument, using parameterized queries.
Usage: ./3-my_safe_filter_states.py <mysql_username>
                                   <mysql_password>
                                   <database_name>
                                   <state_name_searched>
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         port=3306,
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM `states`
                 WHERE BINARY states.name = %s
                 ORDER BY states.id ASC""", [argv[4]])
    [print(state) for state in cur.fetchall()]
