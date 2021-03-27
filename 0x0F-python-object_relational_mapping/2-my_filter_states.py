#!/usr/bin/python3
"""takes in an argument and displays values in the states table of
hbtn_0e_0_usa where name matches the argument"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    user_name = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_searched = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=user_name,
                         passwd=password, db=database_name, charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name = LIKE BINARY
    '{}' ORDER BY id ASC""".format(state_searched))
    print(cur.fetchone())
    cur.close()
    db.close()
