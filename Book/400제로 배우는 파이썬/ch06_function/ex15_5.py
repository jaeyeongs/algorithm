# 리스트의 익명 함수에 인수 전달

fnclist = [
    lambda msg: print(msg, '첫째 함수'),
    lambda msg: print(msg, '둘째 함수'),
    lambda msg: print(msg, '셋째 함수')
]

fnclist[0]("hello")
fnclist[1]("python")
fnclist[2]("world")