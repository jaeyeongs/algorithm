# 여러 개의 튜플을 한꺼번에 삽입

import sqlite3
conn = sqlite3.connect('test.db')

sql = '''
    insert into saram(id, name, age)
    values(?,?,?)
    '''

data = [
    ('kim','gisu',11),
    ('cho','gildong',21),
    ('nam','gildong',31)
]

c = conn.cursor()
c.executemany(sql, data)  # 여러 데이터를 저장하기 위해서는 executemany() 함수 사용
c.close()

conn.commit()
conn.close()