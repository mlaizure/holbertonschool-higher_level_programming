#!/usr/bin/python3
"""lists all states with a name starting with N"""


import MySQLdb
import sys

if __name__ == "__main__":

    user_name = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=user_name,
                         passwd=password, db=database_name, charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY'N%'
    ORDER BY id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
