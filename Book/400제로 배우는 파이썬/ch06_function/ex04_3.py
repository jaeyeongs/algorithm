# 매개변수 없이 return만 있는 함수

def mkPersonDict():
    name = input("성명 입력 >>> ")
    phone = input("전화번호 입력 >>> ")

    return {"name":name, "phone":phone}

dictList = []

dictList.append(mkPersonDict())
dictList.append(mkPersonDict())
dictList.append(mkPersonDict())

for dic in dictList:
    print(dic)