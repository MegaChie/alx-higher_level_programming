#!/usr/bin/python3
"""Using MySQLdb to connect and query a database"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Task #3"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    curs = conn.cursor()
    # print(sys.argv[4])
    curs.execute("select * from states where BINARY '{}' order by id"
                 .format(sys.argv[4]))
    result = curs.fetchall()
    for line in result:
        print(line)
    conn.close()
