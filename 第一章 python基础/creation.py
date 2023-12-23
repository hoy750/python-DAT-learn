import random
from practice import is_even

# C-1.13
def reverse_list(data: list) -> list:
    return [data[len(data) - i - 1] for i in range(len(data))]


# C-1.14
def has_odd_product(data: list[int] ) -> bool:
    temp = []
    for item in data:
        if not is_even(item) and item not in temp:
            temp.append(item)
    return (len(temp) > 2)

# C-1.15
def has_diff(data: list[int | float]) -> bool:
    temp = set()
    for item in data:
        if item not in temp:
            temp.add(item)
        else :
            return False
    return True
# C-1.16 and C-1.17
# 实际上这样并不会修改data，如果想要修改的话，需要重新建立一个列表返回
# 这个编程技巧称之为：返回新对象而不是修改原对象
def scale(data, factor) :
    temp = []
    for val in data:
        val *= factor
        temp.append(val)
    return temp
    # return data
# 这样子并不会修改实际的data

# 但是这样会修改，val *= 和 data[i] *= 是不一样的
def scale_2(data, factor) :
    for i in range(len(data)):
        data[i] *= factor
        
def gen_list_2() -> list:
    # temp = [0]
    # for i in range(1, 10):
    #     temp.append(temp[i - 1] + 2 * i)
    # return temp
    return [ i * ( i + 1) for i in range( 10)]

# C-1.19
def gen_list_3() -> list[str] :
    a = 'a'
    return [ chr(ord(a) + i) for i in range(26)]

# C-1.20
def myShuffle(data: list) -> None: 
    for i in reversed(range(1, len(data))):
        j = random.randint(0, i + 1)
        data[i], data[j] = data[j] , data[i]

# C-1.21
def function():
    list = []
    try:
        while(1):
            a = input("请输入(or ctrl-z(window， linux是CTRl-d))结束")
            list.append(a)
            if a == '\x04':
                raise EOFError('ctrl-d')
    except EOFError as e:
        list = reverse_list(list)
        print(list, e)
# C-1.22
def A_B_dot(a, b):
    if len(a) != len(b):
        raise ValueError('两个列表的长度不一致')
    return [a[i] * b[i] for i in range(len(a))]
def A_B_dot_np(a, b):
    import numpy as np
    return np.array(a) *  np.array(b)
# C-1.24
def count_vowel(data: str) -> int:
    e = ['a', 'A', 'e','E','i','I','o','O','u','U']
    count = 0
    for item in data:

        if item in e:
            count += 1
    return count

# C-1.25
def replacePuntuationMark(string):
    import re
    return re.sub("[.`',]", "", string)
# C-1.26
def is_correct()->bool:
    list = []
    while (1):
        a = int(input ('输入一个数'))
        list . append(a)
        if len(list) == 3:
            break
    a, b, c = list[0] , list[1], list[2]
    if (( a + b == c) or ( b - c == a) or (a * b == c) ):
        return True
    else:
        return False

# C-1.27
import collections
def factors(n):
    k = 1
    temp = []
    while k * k < n:
        if n % k == 0:
            yield k
            temp.append(n // k)
        k += 1
    if k * k == n:
        yield k
    for item in temp[::-1]:
        yield item
# C-1.28 
def norm(v: list[int ], p: int = 2) -> int:
    res = sum(val ** p for val in v) 
    return res ** (1 / p)

if __name__ == "__main__":
    data1 = [ random.randint(1, 100) for i in range(10)]
    # print(has_odd_product(data1))
    data2 = [ random.randint(1, 100) for i in range(10)]
    # print(replacePuntuationMark('hq, of. ew`ohfioe'))
    # print(is_correct())
    # print(list(factors(100)))
    v = [3, 4, 32, 45, 54, 54, 5]
    print(norm(v, 12))
