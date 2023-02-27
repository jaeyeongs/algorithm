# 삼항 연산자 사용하기
# 참일 때 결과 if 조건식 else 거짓일 때 결과

result = (lambda x,y : x if x > y else y)(5, 10)
print("result => ", result)