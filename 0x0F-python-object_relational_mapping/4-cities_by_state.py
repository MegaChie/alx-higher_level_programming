#!/usr/bin/python3
""" a script that lists all cities from the database hbtn_0e_4_usa. """
import MySQLdb
import sys


def Fetch():
    """ 4. Cities by states. """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")
    file = cur.fetchall()
    for line in file:
        print(line)
    cur.close()
    db.close()


if __name__ == "__main__":
    Fetch()
