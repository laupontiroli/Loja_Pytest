import sqlite3 

conn = sqlite3.connect("e_magic_shop_v2.db")
cursor = conn.cursor()


def cadastro():
    return False