# 데이터 리스트를 반환하는 함수

def mkPersonList():
    newList = []
    newList.append(input("성명을 입력 하세요: "))
    newList.append(input("전화번호를 입력 하세요: "))
    newList.append(input("주소를 입력 하세요: "))
    return newList

personList = mkPersonList()
for person in personList:
    print(person)
