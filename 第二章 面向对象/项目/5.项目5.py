""" P-2.39"""

"""
polygon  多边形
perimeter 周长
triangle 三角形
quadrilateral 四边形
Pentagon 五边形
Hexagon 六角形
Octagon 八角形
IsoscelesTriangle  等腰三角形
EquilateralTriangle 等边三角形
rectangel 矩形
square 正方形
"""
from abc import  abstractclassmethod
from math import sqrt
class Polygon():
    @abstractclassmethod
    def area(self):
        """返回面积"""
    @abstractclassmethod
    def perimeter(self):
        """返回周长"""

class Triangle(Polygon):
    def __init__(self, a, b, c) -> None:
        # super().__init__()
        if (a + b > c) and (a + c > b) and (b + c > a):
                
            self._a = a
            self._b = b
            self._c = c
        else :
            raise ValueError("无法构成三角形")

    def area(self):
        p=(self._a + self._b + self._c )/2
        return sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
    def perimeter(self):
        return self._a + self._b + self._c

class Quadrilateral(Polygon):
    def __init__(self, a, b, c, d) -> None:
        # super().__init__()
        if a <= 0 or b <= 0 or c <= 0 or d <= 0:
            raise ValueError("无法构成四边形")
        self._a = a
        self._b = b
        self._c = c
        self._d = d
    def area(self):
        z = (self._a + self._b + self._c + self._d) / 2
        return 2 * (sqrt((z - self._a) * (z - self._n ) * (z - self._c) * (z - self._d)))
    def perimeter(self):
        return self._a + self._b + self._c + self._d
    
class Pentagon(Polygon):
    def __init__(self, a, b, c, d, e) -> None:
        if a <= 0 or b <= 0 or c <= 0 or d <= 0 or e <= 0:
            raise ValueError("无法构成五边形")
        else:
            self._a = a
            self._b = b
            self._c = c
            self._d = d
            self._e = e
    def area(self):
        """当五边形为正五边形时，可在仅知道五边形边长的情况下求出"""
        pass
    def perimeter(self):
        return self._a + self._b + self._c + self._d + self._e
    

class Hexagon(Polygon):
    def __init__(self, a, b , c, d, e, f) -> None:
        super().__init__()
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e
        self._f = f

    def area(self):
        """仅适用于正六边形"""
        return (3 * sqrt(3) * (self._a ** 2)) / 2
    def perimeter(self):
        return self._a + self._b + self._c + self._d + self._e + self._f
    
class Octagon(Polygon):
    def __init__(self, array: list) -> None:
        super().__init__()
        self._array = array
    def area(self):
        return (2 + 2 * sqrt(2)) * (self._array[0] ** 2) 
    
    def perimeter(self):
        return sum(self._array)
    


