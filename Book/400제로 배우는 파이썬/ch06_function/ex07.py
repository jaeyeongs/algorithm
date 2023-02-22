# Global 키워드를 이용해서 전역 변수 값 변경

from pprint import pprint

peoples = [
    {"num":1, "name":"KIM", "phone":'010-1111-1111'},
    {"num":2, "name":"KEE", "phone":'010-2222-2222'},
    {"num":3, "name":"PARK", "phone":'010-3333-3333'}
]

num_seq = 3

def addDictPeople(name, phone):
    # 전역 변수의 값을 변경하려면 global 키워드를 이용
    global num_seq
    num_seq += 1
    # 리스트는 자체를 바꾸는 것이 아니므로 global 없이 변수 사용이 가능
    peoples.append({"num":num_seq, "name":name, "phone":phone})

addDictPeople("Ahn", "010-4444-4444")
# print(peoples)
pprint(peoples)