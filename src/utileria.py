

import sqlite3
import pprint


def ver_tablas(bdatos):
    con = sqlite3.connect(bdatos)
    cur = con.cursor()
    res = cur.execute("select * from sqlite_schema where type = 'table'")
    tablas = res.fetchall()
    pprint.pp(tablas)

def ver_registros(bdatos, tabla):
    con = sqlite3.connect(bdatos)
    cur = con.cursor()
    res = cur.execute("select * from {0}".format(tabla))
    tablas = res.fetchall()
    pprint.pp(tablas)
    
