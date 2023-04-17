# 파일 내용을 라인으로 읽어오기

fp = open("io_test.txt", "r", encoding="utf-8")
while True:
    data = fp.readline()
    data = data[0:len(data)-1]  # 마지막의 \n(개행) 문자를 제거
    if not data:
        break
    print(data)
fp.close()