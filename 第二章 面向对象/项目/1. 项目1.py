""" P-2.33 输入一个标准的代数多项式， 输出该多项式的一阶导数， 参考numpy的poly1d"""
import numpy as np


class poly:
    def __init__(self, array) -> None:
        self._num = array
    def diff(self):
        array = []
        for i in range(len(self._num) - 1):
            array.append(self._num[i] * ( len(self._num) - i - 1))
        return poly(array)
    def __str__(self) -> str:
        string = "<"
        for i in range(len(self._num)):
            string += str(self._num[i]) + "x^" + str(len(self._num) - i - 1) + " "
        string += ">"
        return string 
if __name__ == "__main__" :
    var = np.poly1d([5, 4, 9, 5, 1, 6])
    print(var, type(var))
    print(var.deriv())
    var = poly([5, 4, 9, 5, 1, 6])
    print(var)
    print(var.diff())