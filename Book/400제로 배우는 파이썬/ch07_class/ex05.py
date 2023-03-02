# 세탁기를 추상화해서 클래스로 선언하기

class Washer:
    def __init__(self, size, maker):
        self.size = size
        self.maker = maker

    def washing(self):
        detergent()
        print("{}세탁기가 {}킬로의 빨래를 한다~".format(self.maker, self.size))

# 클래스 선언 끝

def detergent():
    print("세제 투입!")


washer = Washer(10, "LG")
washer.washing()