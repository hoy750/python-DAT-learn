


# P-1.29
# 原书做法
"""
总体而言，一般都是递归的做法
"""
def permute(bag:list[str], permutation):
    if len(bag) == 0:
        print(''.join(permutation))
    else:
        for i in range(len(bag)):
            permutation.append(bag.pop(i))   
            permute(bag, permutation)
            bag.insert(i, permutation.pop())
# 摘自 https://blog.csdn.net/storyfull/article/details/102940318
def full_permutation(list):
    if list == None: # 递归出口
        return None
    if len(list) == 1:  # 因为是从list[1]处开始递归的，若len(list)<=1，list会越界
        return [list]
    res = []
    left = list[0]
    right = full_permutation(list[1:])
    for i in right:
        for j in range(len(i) + 1):
            res.append(i[:j] + [left] + i[j:])
    return res
# 摘自：https://blog.csdn.net/ggdhs/article/details/90285794
def permutations(arr, begin, end):
    if begin == end:  # 当begin等于end，就说明数组中的元素都全部固定了，这是递归的终止条件
        print(arr)  # 打印当前这一次排列
    else:
        for index in range(begin, end):
            arr[index], arr[begin] = arr[begin], arr[index]
            # 数组的第一个元素和其他任意一个元素元素都交换一次，包括刚开始他自己
            permutations(arr, begin + 1, end)
            # 交换完成之后，对剩下的元素进行交换，即全排
            arr[index], arr[begin] = arr[begin], arr[index]
            # 当以arr[index]在第一位时，都排列完的时候，还要将将交换双方换回来，在进行下一次循环

# C-1.30
def count_2_num(n):
    count = 0
    while n  >= 2:
        n = n // 2
        count += 1
    return count

# C-1.31
# 找零钱
def back_money(total, pay, coins: dict = {
        '0.5': 0, '1': 0, '5': 0, '10': 0, '20': 0, '50': 0, '100': 0
    }) :
    rest = pay - total
    for coin in reversed(coins.keys()):
        coins[coin] = int( rest / float(coin))
        rest = int(rest % float(coin))
    return coins.values()

# C-1.32 和 C-1.33
# 跳过


# C-1.34
def copy_count(string: str, n: int = 100, k: int = 8) -> None:
    """n次抄写， k表示错误几次"""
    import random
    sentence = [random.randint(0, n) for i in range(k)]

    count = 0
    for i in range(n):
        if i  in sentence:

            string1  = string + random.choice('feioqodfnsaof')
            print('here')
            print(string1)
        else:
            print(string)
        count += 1
    return count

# C-1.35
# 这个其实有严谨的数学证明, 自己搜一下
def birth_age(num):
    import math
    prop = 1 - math.pow((364 / 365), (num * (num - 1) / 2))
    return prop

# C-1.36
def worlds_num():
    import string
    # 去除标点符号和前后的空格
    temp = input("Please input a string: \n").strip().strip(string.punctuation).split(" ")
    # 首先用set集合去除重复，在转换为list
    keys = list(set(temp))
    # 利用zip形成1对1的元组，在用dict构造字典
    result = dict(zip(keys, [0] * len(keys)))
    for item in temp:
        result[item] += 1
    return result
if __name__ == "__main__":
    import string
    # print(permutations(list('abc') , 0, 3))
    # print(count_2_num(1023))
    coins: dict = {
        '0.5': 0, '1': 0, '5': 0, '10': 0, '20': 0, '50': 0, '100': 0
    }
    # print(back_money(23, 50))
    # print(copy_count("I will never spam my friends again", 100, 8))
    # print(birth_age(23))

    print(worlds_num())