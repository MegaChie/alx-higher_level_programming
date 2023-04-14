#!/usr/bin/python3
""" a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. """
import MySQLdb
import sys


def get_states():
    """ 3. SQL Injection... """
    if len(sys.argv) == 5:
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE BINARY name='{:s}'\
                    ORDER BY id ASC".format(sys.argv[4]))
        file = cur.fetchall()
        for line in file:
            print(line)
        cur.close()
        db.close()
    else:
        return


if __name__ == "__main__":
    get_states()
