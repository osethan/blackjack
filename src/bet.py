
class Bet:
  """
  A player's bet in Blackjack.
  """


  def __init__(self, size):
    """
    Bet ctor.

    In:
    size (int): Size of the bet.
    """

    self.__size = size


  def get_size(self):
    """
    Getter.

    Out:
    (int): A bet's size.
    """

    return self.__size


  def set_size(self, size):
    """
    Setter.

    In:
    size (int): A bet's new size.
    """

    self.__size = size
