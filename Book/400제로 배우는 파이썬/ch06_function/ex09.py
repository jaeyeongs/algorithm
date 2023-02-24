# 여러 개의 결과 값 한꺼번에 반환하기

def getInfo():
    return "HONG", "GILDONG", 33

# getInfo() 함수에서 리턴하는 세개의 데이터는 튜플 형식으로 반환하기 때문에 getInfo2() 함수의 리턴값과 같음
def getInfo2():
    return ("HONG", "GILDONG", 33)

def mkTuple(id, name, age):
    return id, name, age

print(getInfo())

id, name, age = getInfo()
print(id, name, age)

tu = mkTuple("PARK", "GILSUN", 25)
print(tu)