# 튜플 형식의 데이터를 DB에 입력

import sqlite3
conn = sqlite3.connect('test.db')

sql = '''
    insert into saram(id, name, age)
    values(?,?,?)
    '''

c = conn.cursor()
c.execute(sql, ('lee','gilsun',21))
c.close()

conn.commit()
conn.close()