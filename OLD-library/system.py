import sys


class System:
  """
  I/O and system interface.
  """

  def __init__(self, _print = print, _input = input):
    """
    System ctor.
    """

    self.__print = _print
    self.__input = _input


  def print(self, msg):
    """
    Getter accessor.

    In:
    msg (string): Message to print.
    """

    self.__print(msg)


  def input(self, msg):
    """
    Setter mutator.

    In:
    msg (string): Message for prompt.
    """

    return self.__input(msg)


  # Instance methods


  def exit(self, msg):
    """
    Exit a process.
    """

    if msg:
      self.print(msg)

    sys.exit(0)
