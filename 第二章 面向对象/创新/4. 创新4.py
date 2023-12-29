# C-2.31
class Progression:
  """Iterator producing a generic progression.

  Default iterator produces the whole numbers 0, 1, 2, ...
  """

  def __init__(self, start=0):
    """Initialize current to the first value of the progression."""
    self._current = start

  def _advance(self):
    """Update self._current to a new value.

    This should be overridden by a subclass to customize progression.

    By convention, if current is set to None, this designates the
    end of a finite progression.
    """
    self._current += 1

  def __next__(self):
    """Return the next element, or else raise StopIteration error."""
    if self._current is None:    # our convention to end a progression
      raise StopIteration()
    else:
      answer = self._current     # record current value to return
      self._advance()            # advance to prepare for next time
      return answer              # return the answer

  def __iter__(self):
    """By convention, an iterator must return itself as an iterator."""
    return self                  

  def print_progression(self, n):
    """Print next n values of the progression."""
    print(' '.join(str(next(self)) for j in range(n)))

# C-2.31
class AbsProgression(Progression):
  def __init__(self, start: int = 2, second: int = 200):
    super().__init__(start) 
    self._second = second - start
  def _advance(self):
    # start = self._current
    # self._current = self._second
    # self._second = abs(self._second - start)
    self._current, self._second = self._second, abs(self._second - self._current)
    # self._start, self._second = self._second, abs(self._second - self._start)
    # 2 198 
    # 198 196
# C-2.32
class SqrtProgression(Progression):
  def __init__(self, start = 65536):
    super().__init__(start)
  def _advance(self):
    self._current **= 1/2
    # return super()._advance()
if __name__ == "__main__":
  # AbsProgression().print_progression(100)
  # 
  SqrtProgression().print_progression(10)