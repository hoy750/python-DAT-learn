
# C-2.24

"""
实体类
    书籍类
    图书馆类
    购物篮类
    用户类
行为类
    用户类（行为部分）
    控制类
"""
# C-2.25
"""在巩固的R-2.14中已经实现了"""

# C-2.26


class ReversedSequence() :
    def __init__(self, sequence):
        self._seq = sequence
        self._k = len(self._seq)
    def __next__(self):
        self._k -= 1
        if self._k >= 0:
            return self._seq[self._k]
        else:
            raise StopIteration()
        # return super().__next__()
    def __iter__(self):
        return self

# C-2.27

if __name__ == "__main__" :
    a = ReversedSequence([10, 20, 30])
    for i in a:
        print(i)