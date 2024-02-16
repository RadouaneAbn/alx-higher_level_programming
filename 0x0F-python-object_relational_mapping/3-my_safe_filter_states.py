#!/usr/bin/python3
""" This script takes in an argument <state name> and displays all values
    in the states table where name matches the arg <state name>
    but its safe from MySQL injections ;D
Usage:
    3-my_safe_filter_states.py <username> <password> <database> <state name>
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    import re
    host_u, port_u = "localhost", 3306
    name_u, password_u, database_u = argv[1:4]
    state_name = re.match(r"^([^';]+)", argv[4]).group(1)

    with MySQLdb.connect(host=host_u, port=port_u, user=name_u,
                         password=password_u, database=database_u) as db:
        with db.cursor() as cur:
            cur.execute(f"SELECT * FROM states WHERE name='{state_name}' \
ORDER BY id ASC")
            query_rows = cur.fetchall()
            for row in query_rows:
                print(row)
