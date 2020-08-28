# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

print('Задача 1')
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def calculate_area(self):
        r = 0.5*abs((p2["x"]-p1["x"])*(p3["y"]-p1["y"]) - (p3["x"]-p1["x"])*(p2["y"])-p1["y"])
        return r

    def calculate_heights(self):
        def get_height(p1, p2, p3):
            import math
            distance = abs((p3["y"]-p2["y"])*p1["x"]-(p3["x"]-p2["x"])*p1["y"]+p3["x"]*p2["y"]-p3["y"]*p2["x"])/math.sqrt((p3["y"]-p2["y"])**2 + (p3["x"]-p2["x"])**2)
            return distance
        h1 = get_height(self.p1, self.p2, self.p3)
        h2 = get_height(self.p2, self.p3, self.p1)
        h3 = get_height(self.p3, self.p1, self.p2)
        return h1,h2,h3

    def calculate_perimeter(self):
        def get_len(p1,p2):
            import math
            len = math.sqrt((self.p2["x"] - self.p1["x"]) ** 2 + (self.p2["y"] - self.p1["y"]) ** 2)
            return len

        p1p2 = get_len(p1,p2)
        p2p3 = get_len(p2,p3)
        p3p1 = get_len(p3,p1)
        perimeter = p1p2+p2p3+p3p1
        return perimeter

p1 = {"x": 5,
      "y": 7}
p2 = {"x": 3,
      "y": 4}
p3 = {"x": 6,
      "y": 1}
tr = Triangle(p1,p2,p3)
print("Площадь:", tr.calculate_area())
print("h1, h2, h3", tr.calculate_heights())
print("Периметр:", tr.calculate_perimeter())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

print('-' * 50)
print('Задача 2')
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Side:
    def _length(self, p1: Point, p2: Point):
        return math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))

class Trapezoid(Side):
    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.AB = self._length(p1, p2)
        self.BC = self._length(p2, p3)
        self.CD = self._length(p3, p4)
        self.DA = self._length(p4, p1)
        self.height_trap = None

    def Side_AB(self):
        return self.AB

    def Side_BC(self):
        return self.BC

    def Side_CD(self):
        return self.CD

    def Side_DA(self):
        return self.DA

    def height_Trapezoid(self):
        if self.AB == self.CD:
            self.height_trap = self.p2.y - self.p1.y
        else:
            self.height_trap = self.p3.y - self.p2.y
        return self.height_trap

    def perimeter_Trapezoid(self):
        return self.AB + self.BC + self.CD + self.DA

    def area_Trapezoid(self):
        if self.AB == self.CD:
            area = self.height_trap * (self.BC + self.DA) / 2
        else:
            area = self.height_trap * (self.AB + self.CD) / 2
        return area

    def check_Trapezoid(self) -> bool:
        return bool(self.AB == self.CD and (self.p4.x - self.p1.x) / self.DA == (self.p3.x - self.p2.x) / self.BC or (
                self.BC == self.DA and (self.p2.x - self.p1) / self.AB == (self.p3.x - self.p4.x) / self.CD) or (
                            self.AB == self.CD and self.BC == self.DA))

test_trapezoid = Trapezoid(Point (0, 0), Point(2, 4), Point(6, 4), Point(8, 0))
if test_trapezoid.check_Trapezoid():
    print('Трапеция равнобедренная')
    print('AB = {}, BC = {}, CD = {}, DA = {}'.format(test_trapezoid.Side_AB(), test_trapezoid.Side_BC(), test_trapezoid.Side_CD(), test_trapezoid.Side_DA()))
    print('Высота трапеции равна = {}'.format(test_trapezoid.height_Trapezoid()))
    print('Периметр = {}'.format(test_trapezoid.perimeter_Trapezoid()))
    print('Площадь = {}'.format(test_trapezoid.area_Trapezoid()))
else:
    print('Трапеция неравнобедренная')
