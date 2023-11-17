#!/usr/bin/python3
'''this module is a script that lists all states from the database hbtn_0e_0_usa:'''

import MySQLdb
from sys import argv

def main():
    '''defines the main function'''
    db_pass = argv[2]
    db_usr = argv[1]
    db_name = argv[3]
    db_host = "localhost"
    db_port =  3306
    try:
        connect = MySQLdb.connect(host=db_host,
                port=db_port,
                user=db_usr,
                db=db_name,
                passwd=db_pass,
                charset="utf8"
                )
        cur = connect.cursor()
        cur.execute("SELECT * FROM states WHERE name REGEXP '^N' ORDER BY id ASC")
        result = cur.fetchall()
        for i in result:
            print(i)
        cur.close()
        connect.close()
    except Exception:
        pass

if __name__ == "__main__":
        main()
