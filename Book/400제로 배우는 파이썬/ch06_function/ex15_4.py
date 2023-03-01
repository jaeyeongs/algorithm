# 람다 함수를 리스트에 저장하기

fnclist = [
    lambda : print('첫째 함수'),
    lambda: print('둘째 함수'),
    lambda: print('셋째 함수')
]

fnclist[0]()
fnclist[1]()
fnclist[2]()