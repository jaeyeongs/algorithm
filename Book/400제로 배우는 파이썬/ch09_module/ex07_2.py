# while문을 이용한 map 내장 함수

def mult(i):
    return i * 100


lis = [10, 20, 30, 40]

result = map(mult, lis)

while True:
    try:
        element = result.__next__()
        print(element)
    except:
        break