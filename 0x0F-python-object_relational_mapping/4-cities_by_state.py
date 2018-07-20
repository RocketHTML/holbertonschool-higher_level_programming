#!/usr/bin/python3
"""
lists all cities

args:
    mysql_username, mysql_password, database_name
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if (len(argv) != 4):
        print("(usage): <db_username> <db_password> <db_name>")
        exit()

    SERVER = {'host': 'localhost', 'port': 3306,
              'user': argv[1], 'passwd': argv[2], 'db': argv[3]}
    db = MySQLdb.connect(**SERVER)
    cur = db.cursor()
    collate = "(name COLLATE latin1_general_cs)"
    query = "SELECT * FROM cities ORDER BY id ASC"

    def main():
        res = cur.execute(query)
        for i in cur.fetchall():
            print(i)

    main()
