
# R-2.1 火箭，银行，...

# R-2.4 
class Flower:
    def __init__(self, name: str, number: int ,price: float) -> None:
        self._name = name
        self._number = number
        self._price = price
    def get_name(self) -> str:
        return self._name
    def get_number(self) -> int:
        return self._number
    def get_price(self) -> float:
        return self._price
    def set_name(self, name) -> None:
        self._name = name
    def set_number(self, number) -> None:
        self._number = number
    def set_price(self, price) :
        self._price = price

    
# R-2.5
# 源码部分
class CreditCard:
  """A consumer credit card."""
  
  def __init__(self, customer, bank, acnt, limit):
    """Create a new credit card instance.

    The initial balance is zero.

    customer  the name of the customer (e.g., 'John Bowman')
    bank      the name of the bank (e.g., 'California Savings')
    acnt      the acount identifier (e.g., '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    """
    self._customer = customer
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = 0

  def get_customer(self):
    """Return name of the customer."""
    return self._customer
    
  def get_bank(self):
    """Return the bank's name."""
    return self._bank

  def get_account(self):
    """Return the card identifying number (typically stored as a string)."""
    return self._account

  def get_limit(self):
    """Return current credit limit."""
    return self._limit

  def get_balance(self):
    """Return current balance."""
    return self._balance

  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed; False if charge was denied.
    """
    if price + self._balance > self._limit:  # if charge would exceed limit,
      return False                           # cannot accept charge
    else:
      self._balance += price
      return True

  def make_payment(self, amount):
    """Process customer payment that reduces balance."""
    self._balance -= amount    

# R-2.5 and R-2.6  and R-2.7 
# R-2.8 都不会出现，因为当超过额度是，charge会返回False， 不会修改balance
class ExcepectCreditCard(CreditCard):
    """" 修改了charge 和 make_payment， 以及可选参数 """
    def __init__(self, customer, bank, acnt, limit, balance: int = 0):
        super().__init__(customer, bank, acnt, limit)
        if balance >= limit:
           raise ValueError('balance 的值应该小于limit')
        self._balance = balance
    def charge(self, price: int | float):
       if not isinstance(price, float | int):
          raise TypeError(f"类型错误, 期望收到int or float, 然而收到{type(price)}")
       if price + self._balance > self._limit:
          return False
       else:
          self._balance += price
          return True
    def make_payment(self, amount: int | float):
       if not isinstance(amount, float | int):
          raise TypeError(f"类型错误, 期望收到int or float, 然而收到{type(amount)}")
       if amount <= 0:
          raise ValueError(f"数值错误，期望的得到一个正数，然而得到{amount}")
       return super().make_payment(amount)
    def __str__(self) -> str:
       
       return f"name : {self._customer} \t limit ： {self._limit} \t balance : {self._balance}"


# R-2.9
import collections
# 源码
class Vector:
  """Represent a vector in a multidimensional space."""

  def __init__(self, d):
    if isinstance(d, int):
      self._coords = [0] * d
    else:                                  
      try:                                     # we test if param is iterable
        self._coords = [val for val in d]
      except TypeError:
        raise TypeError('invalid parameter type')

  def __len__(self):
    """Return the dimension of the vector."""
    return len(self._coords)

  def __getitem__(self, j):
    """Return jth coordinate of vector."""
    return self._coords[j]

  def __setitem__(self, j, val):
    """Set jth coordinate of vector to given value."""
    self._coords[j] = val

  def __add__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other):          # relies on __len__ method
      raise ValueError('dimensions must agree')
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result

  def __eq__(self, other):
    """Return True if vector has same coordinates as other."""
    return self._coords == other._coords

  def __ne__(self, other):
    """Return True if vector differs from other."""
    return not self == other             # rely on existing __eq__ definition

  def __str__(self):
    """Produce string representation of vector."""
    return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation

  def __neg__(self):
    """Return copy of vector with all coordinates negated."""
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = -self[j]
    return result

  def __lt__(self, other):
    """Compare vectors based on lexicographical order."""
    if len(self) != len(other):
      raise ValueError('dimensions must agree')
    return self._coords < other._coords

  def __le__(self, other):
    """Compare vectors based on lexicographical order."""
    if len(self) != len(other):
      raise ValueError('dimensions must agree')
    return self._coords <= other._coords

# R-2.9 and R-2.10 and R-2.11 and R-2.12 and R-2.13 and R-2.14 
# R-2.15 源码中就已经实现
class NewVector(Vector):
    def __init__(self, d : int ):
       super().__init__(d)
    def __sub__(self, other) :
        if len(self) != len(other):			
            raise ValueError('dimensions must agree')
        result = NewVector(len(self))           # start with vector of zeros
        for j in range(len(self)):		
            result[j] = self[j] - other[j]
        return result
    def __neg__(self):
        return super().__neg__()
    def __radd__(self, other):
        return super().__add__( other)
    def __mul__(self, factor: int = 3):
        if  isinstance(factor, int):
            result = NewVector(len(self))
            for i in range(len(self)):
                result[i] = self[i] * factor
            return result
        
        else:
            if len(self) != len(factor):
                raise ValueError('两个矩阵大小不同')
            try:
                result = 0
                for i in range(len(self)):
                    result += self[i] + factor[i]
                return result
            except TypeError:
                raise TypeError('两个矩阵大小不同')
            except Exception as e:
               raise Exception(f'发生错误{e}')
    def __rmul__(self, factor: int = 3):
       return self.__mul__(factor)
    
""""
R - 2.16
等差数列
第一个元素 ： start
第二个元素 ： start + step
第n个元素  ： start + step * (n - 1) 
(不可 > stop)
start + step * (n - 1) < stop
start + step * n - step < stop
n < (stop - start + step) // step

"""
# R- 2.17 跳过

# R -2.18
from progressions import FibonacciProgression, ArithmeticProgression
import math
def main_Fi():
    f = FibonacciProgression(2, 2)
    f.print_progression(8)
    a = ArithmeticProgression(128, 0)
    print(math.log2( 2 ** 63 * 2 // 128) )
# R - 2.19
"""

等差数列
(0 + 128) * x // 2 == 2 ** 63
x = 2 ** 57
print(math.log2( 2 ** 63 * 2 // 128) )
"""
# R- 2.20
"""
想一想当创建类Z的新实例以及调用类Z的方法时会发生什么。

有两种直接的效率低下：

（1）构造函数的链接意味着，每次创建深层类Z的实例时，方法调用的潜在集合就会很长
（2）用于确定要使用某种方法的哪个版本的动态调度算法最终可能会在找到合适的类之前先浏览大量类。
"""

# R- 2.21 

"""
考虑一下代码重用。

每当大量类都从单个类扩展时，很可能您会错过不同类中类似方法的潜在代码重用。 在这种情况下，有可能将方法分解为通用类，这可以通过消除重复的代码来节省程序员的时间和维护时间。
"""

# R-2.22
from sequence_abc import Sequence

class EQSequence(Sequence):
    def __init__(self) -> None:
       super().__init__()
    def __eq__(self, __value: object) -> bool:
        if len(self) != len(__value):
           raise ValueError('两个序列长度不一致')
        else: 
           for i in range(len(self)):
              if self[i] != __value[i]:
                return  False
        return True
    def __lt__(self, other):
        if len(self) != len(other):
           raise ValueError('两个序列长度不一致')
        for k in range(len(self)):
            if self[k] < other[k]:
                return True 
            elif self[k] > other[k]:
                return False
        return len(self) < len(other)

if __name__ == "__main__" :
    # A = NewVector([10,20,304])
    # print(A)
    # B = NewVector([10,230,40])
    # print(A - B)
    # print(-(A - B))
    # B = [20, 40, 2] + B
    # print(B)
    # u = NewVector([10, 20, 30])
    # print(3 * u)
    # u = NewVector([1, 2, 3])
    # v = NewVector([1, 2, 3])
    # print(u * v)
    main_Fi()