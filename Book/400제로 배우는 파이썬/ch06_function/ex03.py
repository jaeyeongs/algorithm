# 함수의 매개변수와 인수 전달
# 매개변수 : 함수를 선언할 때 전달되는 인수를 담기 위한 변수

def show_number(num):
    print("[1] 함수로 전달되는 숫자는 ", num, "입니다.", sep="")

show_number(5) # 인수 5는 위에 선언된 show_number() 함수의 num 매개변수에 전달

# 함수로 두 개의 인수 전달
# 함수 안에 한 개 이상의 매개변수를 선언할 수 있음

def show_people(name, age):
    print("[2] ", name, "님은 ",age, "세입니다", sep="")

show_people("김길동", 25)  # 김길동 : name, 25 : age