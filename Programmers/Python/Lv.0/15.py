# n의 배수

def solution(num, n):
    if num % n == 0:
        return 1
    else:
        return 0

# 간단히
def solution(num, n):
    return 1 if num % n == 0 else 0