#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    user_name = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=user_name,
                         passwd=password, db=database_name, charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
