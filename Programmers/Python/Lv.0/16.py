# 공배수
def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0

# 간단히
def solution(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0