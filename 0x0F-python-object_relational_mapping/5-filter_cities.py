#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa. """
import MySQLdb
import sys


def Fetch():
    """ All cities by state. """
    if len(sys.argv) == 5:
        cofig = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                passwd=sys.argv[2], db=sys.argv[3])
        code = config.cursor()
        code.execute("SELECT cities.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    AND states.name = '{:s}'\
                    ORDER BY cities.id ASC".format(sys.argv[4]))
        file = code.fetchall()
        result = []
        for place in rows:
            result.append(place[0])

        print(", ".join(result))
        code.close()
        config.close()
    else:
        return


if __name__ == "__main__":
    get_states()
