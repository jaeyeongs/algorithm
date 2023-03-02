# 클래스 선언 작업 순서 예제
import math

class Circle:
    def __init__(self, r):
        self.r = r
        self.mkArea()
        self.mkLine()

    def mkArea(self):
        self.area = math.pi * self.r**2

    def mkLine(self):
        self.line = 2 * math.pi * self.r

    def __str__(self):
        return "area:%.3f, line:%.3f" %(self.area, self.line)


circle = Circle(10)
print(circle)