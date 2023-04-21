# 파일의 여러 라인을 리스트로 읽어오기

fp = open("io_test.txt", "r", encoding="utf-8")
lines = fp.readlines()

for line in lines:
    print(line, end="")

fp.close()
print("-"*30)