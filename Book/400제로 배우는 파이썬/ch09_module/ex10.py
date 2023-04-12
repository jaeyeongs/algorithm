# random 모듈 실행

import random

print("{:-^50}".format("랜덤 모듈 실습"))

# 1보다 작은 실수인 난수를 반환
num = random.random()
print("random.random() => ", num)

# 인수로 주어진 a와 b 사이의 난수를 반환
num = random.uniform(4,6)
print("random.uniform(4,6) => ", num)

# 인수로 주어진 start ~ stop 범위 내 정수인 난수 발생
num = random.randrange(105,109,2)
print("random.randrange(105,109,2) => ", num)

# 리스트의 요소 중 선택
num = random.choice(list(range(5,11)))
print("random.choice(list(range(5,11))) => ", num)

# 리스트의 요소 섞기
lis = list(range(1,11))
print("shuffle 전의 lis => ", lis)
random.shuffle(lis)
print("shuffle 후의 lis => ", lis)

# 리스트에서 k개만큼 추출하기
print("추출하기 => ", random.sample(lis, k=2))