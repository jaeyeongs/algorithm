# 부모 클래스인 Washer 클래스

class Washer:
    def __init__(self, size, maker):
        self.size = size
        self.maker = maker

    def washing(self):
        print("{}세탁기가 {}킬로의 빨래를 한다~".format(self.maker, self.size))

    def __str__(self):
        return "size:{}, maker:{}".format(self.size, self.maker)


# 첫 번째 자식 클래스인 LG Washer 클래스

class LGWasher(Washer):
    def __init__(self, size, maker, name):
        super().__init__(size, maker)
        self.name = name

    def info(self):
        print("사이즈:", self.size)
        print("제조사:", self.maker)
        print("제품명:", self.name)

    def __str__(self):
        return super().__str__() + ", name:{}".format(self.name)


lgWasher = LGWasher(10, "LG", "트롬")
print(lgWasher)
lgWasher.washing() # 부모 클래스 Washer에서 정의한 washing 함수 호출