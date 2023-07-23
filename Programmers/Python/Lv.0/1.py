# 정수 a와 b가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.

a, b = map(int, input().split())

if a >= -100000 and b <= 100000:
    print("a =", a)
    print("b =", b)
else:
    print("다시 입력")