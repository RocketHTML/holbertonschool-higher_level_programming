#!/usr/bin/python3
"""
lists all states where name matches state

args:
    mysql_username, mysql_password, database_name, state
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if (len(argv) != 5):
        print("(usage): <db_username> <db_password> <db_name> <state>")
        exit()

    SERVER = {'host': 'localhost', 'port': 3306,
              'user': argv[1], 'passwd': argv[2], 'db': argv[3]}
    db = MySQLdb.connect(**SERVER)
    cur = db.cursor()
    state = argv[4]
    collate = "(name COLLATE latin1_general_cs)"
    query = "SELECT * FROM states WHERE {}=%s ORDER BY id ASC"

    def main():
        res = cur.execute(query.format(collate), (state,))
        for i in cur.fetchall():
            print(i)

    main()
