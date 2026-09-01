#!/usr/bin/python3
"""List all cities together with their state names."""
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = database.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities INNER JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    for city in cursor.fetchall():
        print(city)

    cursor.close()
    database.close()
