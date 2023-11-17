#!/usr/bin/env python3  <=== this is for testing it should be #!/usr/bin/python3

import os, MySQLdb


if __name__ == '__main__':
    "using env vars for testing too. use cli args for the 0x0F project"
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    port = int(os.getenv('DB_PORT'))
    database = os.getenv('DATABASE')

    conn = MySQLdb.connect(host="127.0.0.1", port=port, user=user, passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

    print('OK')
