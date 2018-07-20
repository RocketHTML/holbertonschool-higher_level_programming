#!/usr/bin/python3
"""
lists all cities in state

args:
    mysql_username, mysql_password, database_name, state
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if (len(argv) != 5):
        print("(usage): db_username db_password db_name, state")
        exit()

    SERVER = {'host': 'localhost', 'port': 3306,
              'user': argv[1], 'passwd': argv[2], 'db': argv[3]}
    db = MySQLdb.connect(**SERVER)
    cur = db.cursor()
    C = "cities as C"
    S = "states as S"
    COLS = "C.id, C.name, S.name"
    J = "INNER JOIN {} ON S.id = C.state_id".format(S)
    collate = "({} COLLATE latin1_general_cs)".format("S.name")
    W = "WHERE {}=%s".format(collate)
    O = "ORDER BY C.id ASC"
    query = "SELECT {} FROM {} {} {} {}".format(COLS, C, J, W, O)

    def main():
        res = cur.execute(query, (argv[4],))
        for i in cur.fetchall():
            print(i)

    main()
