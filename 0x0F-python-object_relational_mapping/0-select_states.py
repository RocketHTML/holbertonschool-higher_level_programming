# lists all states from the database hbtn_0e_0_usa
# args: mysql_username, mysql_password, database_name
# goals: Module that can create, read, update, delete records from a table
#	(e.g.) so that I can add or update user info
#		I'll use sql scripts to create, read, update, delete tables from a database
import MySQLdb
from sys import argv

if (len(argv) != 4):
	print("(usage): states.py <db_username>, <db_password>, <db_name>")

SERVER = {'host': 'localhost', 'port': 3306, 'user': argv[1], 'passwd': argv[2], 'db': argv[3]}
db = MySQLdb.connect(**SERVER)
cur = db.cursor()

def main():
	res = cur.execute("SELECT * FROM states ORDER BY id ASC")
	for i in cur.fetchall():
		print(i)


if __name__ == '__main__':
	main()
