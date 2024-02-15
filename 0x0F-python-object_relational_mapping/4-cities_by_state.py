#!/usr/bin/python3
"""Using MySQLdb to connect and query a database"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Task #5"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    curs = conn.cursor()
    ques = """select cities.id, cities.name, states.name from cities
              where join cities on cities.id = states.id
              order by cities.id"""
    curs.execute(ques)
    result = curs.fetchall()
    for line in result:
        print(line)
    conn.close()
