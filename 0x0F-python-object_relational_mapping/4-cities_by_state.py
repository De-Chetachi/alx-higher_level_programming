#!/usr/bin/python3
'''this module is a script that lists all states
from the database hbtn_0e_0_usa:'''


import MySQLdb
from sys import argv


def main():
    '''defines the main function'''
    db_pass = argv[2]
    db_usr = argv[1]
    db_name = argv[3]
    db_host = "localhost"
    db_port = 3306
    try:
        connect = MySQLdb.connect(host=db_host, port=db_port, user=db_usr,
                                  passwd=db_pass, db=db_name, charset="utf8")
        cur = connect.cursor()
        query = "SELECT cities.id, cities.name, states.name FROM cities "
        query += "INNER JOIN states ON  cities.state_id = states.id "
        query += "ORDER BY cities.id ASC"
        cur.execute(query)
        result = cur.fetchall()
        for i in result:
            print(i)
    except Exception as e:
        print(e)
        pass
    finally:
        cur.close()
        connect.close()


if __name__ == "__main__":
    main()
