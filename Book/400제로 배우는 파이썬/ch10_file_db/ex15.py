# DB에 저장된 데이터 불러오기

import sqlite3
conn = sqlite3.connect('test.db')

sql = '''
    select * from saram
    '''

c = conn.cursor()
c.execute(sql)

# 테이블에 저장된 레코드를 한 줄 읽어옴
print(c.fetchone())

# 테이블에 저장된 레코드를 size행만큼 읽어옴
# for s in c.fetchmany(2):
#     print(s)

#  테이블에 저장된 레코드를 모두 읽어옴
# for s in c.fetchall():
#     print(s)

c.close()
conn.close()