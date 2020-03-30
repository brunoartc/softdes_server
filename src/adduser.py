import sqlite3
import hashlib

def addUser(user, pwd, type):
    """add user to database"""
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('Insert into USER(user,pass,type) values("{0}","{1}","{2}");'.format(user, pwd, type))
    conn.commit()
    conn.close()  

addUser('online', '7f46165474d11ee5836777d85df2cdab', 'admin')
