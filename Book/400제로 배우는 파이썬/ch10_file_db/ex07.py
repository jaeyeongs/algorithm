# pickle 모듈을 이용한 객체 입출력

import pickle
from pprint import pprint

# 딕셔너리 객체 데이터
person1 = {'name':'홍길순',
           'height':170,
           'weight':60}

person2 = {'name':'홍길동',
           'height':200,
           'weight':80}

# 딕셔너리 객체 데이터를 리스트로 만듬
people = [person1, person2]

# 데이터 저장
# pickle은 바이너리로 저장되므로 'wb' 모드로 파일 오픈
with open('people.pickle', 'wb') as f:
    pickle.dump(people, f)

# 저장된 데이터 읽기
with open('people.pickle', 'rb') as f:
    loaded_people = pickle.load(f)

pprint(loaded_people)