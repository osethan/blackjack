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


  def get_hand(self):
    """
    Getter.

    Out:
    (Hand): A seat's hand.
    """
    
    return self.__hand


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


  def get_bet(self):
    """
    Getter.

    Out:
    (Bet): A player's bet.
    """

    return self.__bet
  

  def get_purse(self):
    """
    Getter.

    Out:
    (Purse): A player's purse.
    """

    return self.__purse


  # Instance methods


  def win(self):
    """
    A player's hand wins and a dealer's hand loses.
    """

    bet = self.get_bet()
    purse = self.get_purse()

    purse.set_size(purse.get_size() + bet.get_size() * 2)

    # A player's win by natural
    if self.get_hand().natural():
      purse.set_size(purse.get_size() + bet.get_size() // 2)

    bet.set_size(0)
  
  
  def loss(self):
    """
    A player's hand loses and a dealer's hand wins.
    """

    self.get_bet().set_size(0)


  def tie(self):
    """
    A player's hand ties with a dealer's hand.
    """
    
    bet = self.get_bet()
    purse = self.get_purse()

    purse.set_size(purse.get_size() + bet.get_size())
    bet.set_size(0)


  # Helper methods


  def make_bet(self, size):
    """
    A player's bet and purse change when they make a bet.

    In:
    size (int): A player's bet's size.
    """

    bet = self.get_bet()
    purse = self.get_purse()

    bet.set_size(size)
    purse.set_size(purse.get_size() - bet.get_size())
