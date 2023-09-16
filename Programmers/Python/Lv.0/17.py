# 홀짝에 따라 다른 값 반환하기

def solution(n):
    if n % 2 == 0:
        return sum([n ** 2 for n in range(2, n+1, 2)])
    else:
        return sum([n for n in range(1, n+1, 2)])