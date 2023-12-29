
# C-2.27
import bisect
class Range:
  """A class that mimic's the built-in range class."""

  def __init__(self, start, stop=None, step=1):
    """Initialize a Range instance.

    Semantics is similar to built-in range class.
    """
    if step == 0:
      raise ValueError('step cannot be 0')
      
    if stop is None:                  # special case of range(n)
      start, stop = 0, start          # should be treated as if range(0,n)

    # calculate the effective length once
    self._length = max(0, (stop - start + step - 1) // step)

    # need knowledge of start and step (but not stop) to support __getitem__
    self._start = start
    self._step = step

  def __len__(self):
    """Return number of entries in the range."""
    return self._length

  def __getitem__(self, k):
    """Return entry at index k (using standard interpretation if negative)."""
    if k < 0:
      k += len(self)                  # attempt to convert negative index

    if not 0 <= k < self._length:
      raise IndexError('index out of range')

    return self._start + k * self._step
#   def __contains__(self, value):
#         for v in self:
#             if v is value or v == value:
#                 return True
#         return False
  def __contains__(self, value):
    if (value - self._start) % self._step == 0:
       index = bisect.bisect_left(self, value)
       if index < len(self) and self[index] == value:
          return True
    return False
import time

def main_test():
    # 记录开始时间
    start1 = time.time()
    # 判断2是否在范围内
    result1 = 2 in Range(10000000)
    # 记录结束时间
    end1 = time.time()
    # 计算运行时间
    time1 = end1 - start1

    # 记录开始时间
    start2 = time.time()
    # 判断9999999是否在范围内
    result2 = 9999999 in Range(10000000)
    # 记录结束时间
    end2 = time.time()
    # 计算运行时间
    time2 = end2 - start2

    # 打印结果
    print("2 in range(10000000) is", result1, "and takes", time1, "seconds")
    print("9999999 in range(10000000) is", result2, "and takes", time2, "seconds")
if __name__ == "__main__":
    main_test()