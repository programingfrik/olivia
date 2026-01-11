

import sqlite3
import pprint


def ver_tablas():
    con = sqlite3.connect("d:\\pmercader\\proyectos\\olivia\\src\\olivia_project\\db.sqlite3")
    cur = con.cursor()
    res = cur.execute("select * from sqlite_schema where type = 'table'")
    tablas = res.fetchall()
    pprint.pp(tablas)

