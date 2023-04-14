#!/usr/bin/python3
"""Script that lists all states from database hbtn_0e_0_usa"""
import MySQLdb
import sys


def get_states():
    """Takes arguments argv to list from database

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    config = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         config=sys.argv[3])

    code = config.cursor()

    code.execute("SELECT * FROM states ORDER BY id ASC")
    file = code.fetchall()
    for i in file:
        print(i)

    code.close()
    config.close()

if __name__ == "__main__":
    get_states()
