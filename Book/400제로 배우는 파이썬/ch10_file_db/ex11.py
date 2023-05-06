# DB에 데이터 입력하기

import sqlite3
conn = sqlite3.connect('test.db')

sql = '''
    insert into saram(id, name, age)
    values("park", "gildong", "34")
    '''

# SQL문을 실행해 줄 커서 객체를 생성
c = conn.cursor()
c.execute(sql)
c.close()

# 트랜잭션을 commit
# commit 하지 않으면 DB 테이블에 변경 사항이 적용되지 않음
conn.commit()
conn.close()


# SQLite 명령어로 확인
'''
saram 테이블 불러오기
> select * from saram;
'''