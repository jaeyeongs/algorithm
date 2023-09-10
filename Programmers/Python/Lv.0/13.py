# 더 크게 합치기

# sol1
def solution(a, b):
    int1 = str(a) + str(b)
    int2 = str(b) + str(a)
    if int(int1) > int(int2):
        return int(int1)
    else:
        return int(int2)

# 위 풀이를 더 간단히
def solution(a, b):
    int1 = str(a) + str(b)
    int2 = str(b) + str(a)
    return int(int1) if int(int1) > int(int2) else int(int2)

# 다른 풀이
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))