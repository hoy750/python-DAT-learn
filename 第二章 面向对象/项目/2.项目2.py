import matplotlib.pyplot as plt
def plot(x, data):
    plt.grid(ls="--", alpha=0.5)
    plt.bar(x, data)
    plt.show()
if __name__ == "__main__" :
    fp = open(r'第二章 面向对象\项目\2.项目2.txt', 'r')
    res = {}
    for line in fp:
        for char in line:
            if char not in res.keys():
                res[char] = 1
            else:
                res[char] += 1
    fp.close()
    plot(res.keys(), res.values())