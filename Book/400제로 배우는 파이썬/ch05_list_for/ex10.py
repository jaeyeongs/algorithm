# range() 함수를 이용한 for 반복문 실행
for i in range(5):
    print(i, end=" ")  # end 속성은 출력 값을 한 줄에 표시하도록 하기 위해 설정

print()

# range() 함수의 입력 범위와 증가 값 설정
# range(시작 값, 종료 값, 증가 값)
for num in range(3, 10, 2):
    print(num, end=" ")

print()

# 거꾸로 감소하기
for cnt in range(10, 0, -1):
    print(cnt, end=" ")