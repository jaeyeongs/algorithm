# DB 실행 커서 얻기

import sqlite3
conn = sqlite3.connect('test.db')

sql = '''
    create table IF NOT EXISTS saram(
    no integer primary key,
    id varchar(20),
    name varchar(20),
    age integer)
    '''

c = conn.cursor()
c.execute(sql)

c.close()
conn.close()


# SQLite 명령어로 확인
'''
SQLite 실행
> sqlite3 test.db  

DB 테이블 확인
> .table

DB 테이블(saram) 스키마 확인
> .schema saram
'''
