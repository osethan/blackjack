from src.bet import Bet
from src.hand import Hand
from src.purse import Purse


class Seat:
  """
  A dealer or a player in Blackjack.
  """

  def __init__(self):
    """
    Seat ctor.
    """

    self.__hand = Hand()


class Dealer(Seat):
  """
  A dealer in Blackjack
  """

  def __init__(self):
    """
    Dealer ctor.
    """

    super().__init__()


class Player(Seat):
  """
  A player in Blackjack.
  """

  def __init__(self):
    """
    Player ctor.
    """

    super().__init__()
    self.__bet = Bet(0)
    self.__purse = Purse()
