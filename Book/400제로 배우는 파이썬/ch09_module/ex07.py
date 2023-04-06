# for문과 함께 map 내장 함수 사용

def mult(i):
    return i * 100


lis = [10, 20, 30, 40]

result = map(mult, lis)

'''결과 타입을 리스트로 변환하지 않고 바로 사용하기 위해 반복문 사용'''
for item in result:
    print(item, end=" ")