#!/usr/bin/python3
"""Using MySQLconn to connect and query a database"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """task #4"""
    conn = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                           passwd=argv[2], db=argv[3])
    curs = conn.cursor()
    curs.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY %(name)s \
                 ORDER BY states.id ASC", {"name": argv[4]})
    result = curs.fetchall()
    for line in result:
        print(line)
    conn.close()
