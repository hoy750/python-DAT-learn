import random
from math import inf

# R-1.1
def is_multiple(n : int , m : int) -> bool:
    """ 当n = m * i 则返true"""
    if not isinstance(n, int) or not isinstance(m, int):
        raise TypeError("n or m is not int Type")
    else:
        if n < m :
            raise ValueError('except n > m, however m > n')
        else :
            return True if n % m == 0 else False

# R-1.2 
def is_even(k: int) -> bool:
    """ 偶数返回True, 奇数返回False"""
    if not isinstance(k , int):
        raise TypeError(" k is not int type")
    return True if k & 1 == 0 else False

# R-1.3 
def minmax(datas: list) -> tuple:
    min = inf
    max = -inf
    for data in datas:
        if data < min :
            min = data
        if data > max:
            max = data
    return (max, min)

# R-1.4
def sum_of_squares(n: int) -> int: 
    total = 0
    for i in range(n) :
        total += (i + 1)   ** 2
    return total

# R-1.5 
def sum_of_squares_2(n: int) -> int:
    return sum([ (i + 1) ** 2 for i in range(n)])

# R-1.6
def odd_sum_of_squares(n : int) -> int:
    total = 0
    for i in range(1, n + 1) :
        if not is_even(i):
            total += i ** 2
    return total
# R-1.7
def odd_sum_of_squares_2(n : int) -> int:
    return sum( [ (i ) ** 2  for i in range(1,  n + 1) if  not is_even(i)])

# R-1.8
def negative_index_to_positive_index(data: list, k: int) -> int: 
    if k > 0:
        raise ValueError(' k should < 0')
    return len(data) + k
# R-1. 9
def gener_seq()->list:
    return [data for data in range(50, 90, 10)]
# R-1.10
# 跳过，太简单了

# R-1.11
def gen_list() -> list:
    return [2 ** i for i in range(9)]

# R-1.12
def myChoice(data) -> int | float | str:
    return data[random.randrange(0, len(data))]

if __name__ == '__main__' :
    data1 = [ random.randint(1, 100) for i in range(10)]
    data2 = "dwadwdfwqf"
    data3 =  [ random.random() * 100 for i in range(10)]
    # print(gen_list())
    print(data3)
    print(myChoice(data3))