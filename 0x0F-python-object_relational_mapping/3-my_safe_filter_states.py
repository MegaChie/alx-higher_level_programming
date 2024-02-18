#!/usr/bin/python3
"""Using MySQLconn to connect and query a database"""
import MySQLconn
from sys import argv


if __name__ == "__main__":
    """task #4"""
    conn = MySQLconn.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], conn=argv[3])
    curs = conn.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY %(name)s \
                 ORDER BY states.id ASC", {'name': argv[4]})
    result = curs.fetchall()
    for line in result:
        print(line)
