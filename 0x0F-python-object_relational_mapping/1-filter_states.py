#!/usr/bin/python3
"""Using MySQLdb to connect and query a database"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Task #2"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    curs = conn.cursor()
    stat = """select * from states 
              where name like REGEXP '^[N].*$' order by id"""
    curs.execute(stat)
    result = curs.fetchall()
    for line in result:
        print(line)
    conn.close()
