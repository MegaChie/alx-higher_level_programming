#!/usr/bin/python3
""" Script that lists all states from database hbtn_0e_0_usa """
import MySQLdb
import sys


def get_states():
    """ 0. Get all states. """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    file = cur.fetchall()
    for lines in file:
        print(lines)

    cur.close()
    db.close()


if __name__ == "__main__":
    get_states()
