# 사용자 정의 파일을 모듈 형식으로 불러오기1
# ex01 모듈을 import 하여 사용
import ex01 as hello

if __name__ == '__main__':
    hello.say_hello("kim")
    hello.say_hello2("hong")