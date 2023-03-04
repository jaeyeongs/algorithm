# 두 번째 자식 클래스인 SamsungWasher 클래스
# ex06 코드에서 부모 클래스 Washer 호출

from ex06 import Washer

class SamsungWasher(Washer):
    def __init__(self, size, maker, name):
        super().__init__(size, maker)
        self.name = name

    def info(self):
        print("크기:", self.size)
        print("회사:", self.maker)
        print("상품명:", self.name)

    def __str__(self):
        return super().__str__() + ", name:{}".format(self.name)


samsungWasher = SamsungWasher(10, "Samsung", "그랑데")
print(samsungWasher)
samsungWasher.washing() # 부모 클래스 Washer에서 정의한 washing 함수 호출