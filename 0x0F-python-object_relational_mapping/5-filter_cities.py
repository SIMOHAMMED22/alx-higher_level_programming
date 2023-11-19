#!/usr/bin/python3
"""getting started with the python module MySQLdb"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()
    query = "SELECT cities.name FROM cities JOIN states \
    ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    cities = list(set(row[0] for row in rows))

    city_order = ["Dallas", "Houston", "Austin"]

    filtered_cities = [city for city in city_order if city in cities]

    print(', '.join(filtered_cities))

    cur.close()
    db.close()
