#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa. """
import MySQLdb
import sys


def Fetch():
    """ Filter states. """
    cofig = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                            passwd=sys.argv[2], db=sys.argv[3])
    code = config.cursor()
    code.execute("SELECT * FROM states WHERE BINARY name = '{:s}\
        ORDER BY id ASC".format(sys.argv[4]))
    file = code.fetchall()
    for lines in file:
        print(line)
    code.close()
    config.close()


if __name__ == "__main__":
    get_states()
