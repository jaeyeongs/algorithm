# 리스트에 담을 객체 생성을 위한 People 클래스 선언

class People:
    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def greeting(self):
        return self.name + "님 안녕하세요 !"

kim = People("KIM")
pList = [kim, People("LEE"), People("Park")]

# setName 함수를 이용하여 pList[0]에 있는 "KIM" 값을 "HONG"으로 변환
pList[0].setName("HONG")

for person in pList:
    print(person.greeting())