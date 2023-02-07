# enumerate() 함수 활용
lis = ["오징어", "꼴뚜기", "대구", "명태", "거북이"]


for index, fish in enumerate(lis):
    print(index, fish)

"""
lis로 선언된 리스트 자료가 fish라는 임시 변수에 저장되는 동시에 index라는 임시 변수도 각각 index 번호를 부여하여 저장
"""

# 딕셔너리 구조를 사용할 때 items() 함수를 이용하여 임시 변수에 키와 값을 함께 전달 받을 수 있음

dic = {"번호1":1, "번호2":2, "번호3":3}

for key, value in dic.items():
    print(key, value)
