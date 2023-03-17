# ZeroDivisionError 예외 발생 예제

try:
    result = 10/0
except ZeroDivisionError as zero:
    print("0으로 나눌 수 없습니다!")
    print(zero)