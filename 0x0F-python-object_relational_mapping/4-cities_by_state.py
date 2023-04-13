#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa. """
import MySQLdb
import sys


def Fetch():
    """ Cities by states. """
    cofig = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                            passwd=sys.argv[2], db=sys.argv[3])
    code = config.cursor()
    code.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")
    file = code.fetchall()
    for lines in file:
        print(line)
    code.close()
    config.close()


if __name__ == "__main__":
    get_states()
