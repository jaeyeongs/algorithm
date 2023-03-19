# NameError 예외 발생 예제
# 정의되지 않은 변수를 사용하면 NameError가 발생

try:
    message = user + "님 안녕하세요"
    print(message)
except NameError as e:
    print("식별자가 정의 되지 않았습니다!")
    print(e)