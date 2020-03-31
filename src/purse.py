
class Purse:
  """
  A player's purse in Blackjack.
  """


  def __init__(self):
    """
    Purse ctor.
    """

    self.__size = 200


  def get_size(self):
    """
    Getter.

    Out:
    (int): A purse's size.
    """

    return self.__size


  def set_size(self, size):
    """
    Setter.

    In:
    size (int): A purse's new size.
    """

    self.__size = size
