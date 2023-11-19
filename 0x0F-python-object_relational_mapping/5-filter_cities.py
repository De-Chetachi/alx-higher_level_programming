#!/usr/bin/python3
'''this module is a script that lists all
states from the database hbtn_0e_0_usa:'''

import MySQLdb
from sys import argv


def main():
    '''defines the main function'''
    db_pass = argv[2]
    db_usr = argv[1]
    db_name = argv[3]
    db_host = "localhost"
    db_port = 3306
    match = argv[4]
    try:
        connect = MySQLdb.connect(host=db_host, port=db_port, user=db_usr,
                                  db=db_name, passwd=db_pass, charset="utf8")
        cur = connect.cursor()
        '''query = "SELECT cities.name FROM cities "
        query += "INNER JOIN states ON cities.state_id = states.id "
        query += "WHERE states.name = %s ORDER BY cities.id"'''
        query = "SELECT name FROM cities "
        query += "WHERE state_id = (SELECT id FROM states "
        query += "WHERE name = %s)"
        cur.execute(query, (match, ))
        result = cur.fetchall()
        result_list = []
        for i in result:
            result_list.append(i)
        print(", ".join(result_list))
        cur.close()
        connect.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
