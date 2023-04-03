# 사용자 정의 파일을 모듈 형식으로 불러오기2
# 함수를 호출할 때 매번 모듈 이름을 붙여야 하나 from을 이용하면 함수를 직접 import 가능
from ex01 import say_hello
from ex01 import say_hello2

if __name__ == '__main__':
    say_hello("kim")
    say_hello2("hong")