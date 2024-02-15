#!/usr/bin/python3
"""Using MySQLdb to connect and query a database"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Task #6"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    curs = conn.cursor()
    ques = """select cities.name from cities
              join states on cities.state_id = states.id
              and states.name = '{}' order by cities.id;""".format(sys.argv[4])
    curs.execute(ques)
    result = curs.fetchall()
    statList = []
    for item in result:
        statList.append(item[0])
    print(", ".join(statList))
    conn.close()
