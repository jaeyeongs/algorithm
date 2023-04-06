# filter 내장 함수 사용

def choose(a):
    if(a % 10 == 0):
        return a


lis = [10, 25, 30, 46, 50]
lis2 = list(filter(choose, lis))
print(lis2)