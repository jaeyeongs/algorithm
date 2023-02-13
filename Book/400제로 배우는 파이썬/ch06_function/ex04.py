# 두 개의 정수를 전달받아 비교 후 더 큰 수를 반환해 주는 함수 선언

def get_max(num1, num2):
    if num1 > num2:
        maximum = num1
    else:
        maximum = num2
    return maximum

result = get_max(10, 100)
print("더 큰수는 {}입니다!".format(result))