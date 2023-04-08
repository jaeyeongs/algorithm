# reduce 내장 함수 사용 예제

from functools import reduce

def sum(x, y):
    return x+y

lis2 = [x for x in range(1, 11)] # lis2 = list(range(1,11)) 동일
print(lis2)

total = reduce(sum, lis2)

print("total =>", total)