# 두 수의 연산값 비교하기

def solution(a, b):
    int1 = str(a) + str(b)
    int2 = 2 * a * b
    return max(int(int1), int2)