#!/usr/bin/python3
"""takes in an argument and displays values in the states table of
hbtn_0e_0_usa where name matches the argument safe from SQL injections"""
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
    cur.execute("""SELECT * FROM states WHERE name = %s
    ORDER BY id ASC""",(state_searched,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
