#!/usr/bin/python3
"""Using MySQLdb to connect and query a database"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Using MySQLdb to connect to a database"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    curs = conn.cursor()
    curs.execute("select * from states order by id")
    result = curs.fetchall()
    for line in result:
        print(line)
    curs.close()
