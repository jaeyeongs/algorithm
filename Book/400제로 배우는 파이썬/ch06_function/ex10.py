# 하나의 함수를 여러 변수가 참조하기

def fncA():
    print("fncA 함수를 실행합니다")


refA = fncA

refA()