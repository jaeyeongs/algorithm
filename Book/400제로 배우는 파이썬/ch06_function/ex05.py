# 가변 매개변수 선언 및 호출

def findMax(*args):
    print("args의 타입은:", type(args))

    max = 0
    for num in args:
        if num > max:
            max = num

    return max

# 하나 이상 여러 개의 인수를 가변적으로 전달
maximum = findMax(10)
print("가장 큰 수는 :", maximum)

# 여러 인수를 입력 개수에 상관없이 튜플에 전달
maximum = findMax(2, 5, 10, 30, 100, 40, 7, 9)
print("가장 큰 수는 :", maximum)