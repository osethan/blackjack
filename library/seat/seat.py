from library.card.card import Hand


class Seat:
  """
  Abstraction of someone playing Blackjack.
  """

  def __init__(self):
    """
    Seat ctor.
    """

    self.__title = ''
    self.__hand = Hand()


  def get_title(self):
    """
    Getter accessor.
    """

    return self.__title


  def get_hand(self):
    """
    Getter accessor.
    """

    return self.__hand


  def set_hand(self, cards = []):
    """
    Setter mutator.

    In:
    cards (Card[]): New cards in a hand.
    """

    self.__hand = Hand(cards)


class Player(Seat):
  """
  Non-dealer playing Blackjack.
  """

  def __init__(self):
    """
    Player ctor.
    """

    super().__init__()

    self.__title = 'Player'
    self.__purse = Purse()
    self.__bet = Bet()


  def get_bet(self):
    """
    Getter accessor.
    """

    return self.__bet.get_size()


  def set_bet(self, bet):
    """
    Setter mutator.

    In:
    bet (int): New size of bet.
    """

    self.__bet.set_size(bet)


  def get_purse(self):
    """
    Getter accessor.
    """

    return self.__purse.get_size()


  def set_purse(self, purse):
    """
    Setter mutator.

    In:
    purse (int): New size of purse.
    """

    self.__purse.set_size(purse)


class Dealer(Seat):
  """
  Dealer of Blackjack.
  """

  def __init__(self):
    """
    Dealer ctor.
    """

    super().__init__()

    self.__title = 'Dealer'


class Bet:
  """
  A player bet made in Blackjack.
  """

  def __init__(self):
    """
    Bet ctor.
    """

    self.__size = 0

  
  def get_size(self):
    """
    Getter accessor.
    """

    return self.__size


  def set_size(self, size):
    """
    Setter mutator.

    In:
    size (int): New size of bet.
    """

    self.__size = size


class Purse:
  """
  A purse of a player in Blackjack.
  """

  def __init__(self):
    """
    Purse ctor.
    """

    self.__size = 200


  def get_size(self):
    """
    Getter accessor.
    """

    return self.__size


  def set_size(self, size):
    """
    Setter mutator.

    In:
    size (int): New size of bet.
    """

    self.__size = size
