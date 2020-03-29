import re

# from library.card.card import Hand
from card import Hand


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


  # Instance methods


  def clear_hand(self):
    """
    A seat has tied with versus seat.
    """

    self.__hand = Hand()


  def natural(self):
    """
    A seat has a natural.

    Out:
    (boolean): A seat has a natural.
    """

    cards = self.get_hand().get_cards()
    return [c for c in cards if c.get_pip() == 'Ace'] and [c for c in cards if c.get_pip() in ['10', 'Jack', 'Queen', 'King']]


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


  # Instance methods


  def bet(self, system):
    """
    A player makes a bet.

    Response codes:
    0) Ok
    1) Error with input

    In:
    system (System): I/O and sys interface.

    Out:
    (int): Response code.
    """

    pattern = r'^\d+$'
    bet = system.input('')

    # Bet isn't an integer
    if not re.match(pattern, bet):
      system.print('Can only bet whole number of chips')
      return 1

    bet = int(bet)

    # Bet is too low or high
    if bet < 2 or bet > 500 or bet > self.get_purse():
      system.print('Can only bet 2 - 500 chips and no more than purse')
      return 1

    # Set player bet
    self.set_purse(self.get_purse() - bet)
    self.set_bet(bet)
    return 0


  def hit(self, pack, system):
    """
    A player decides to hit.

    Response code:
    0) Ok
    1) Stay
    2) Bust

    In:
    pack (Pack): A pack of cards.
    system (System): System interface.
    """

    res = system.input('')
    if res != 'y':
      return 1

    self.set_hand(self.get_hand().get_cards() + [pack.hit()])
    score = self.get_hand().get_score()
    if score > 21:
      return 2
    else:
      return 0


  def tie(self):
    """
    A dealer and a player tie.
    """

    self.set_purse(self.get_purse() + self.get_bet())
    self.set_bet(0)


  def win(self, natural = False):
    """
    A player wins and a dealer loses.

    In:
    natural (boolean): A player has won with a natural.
    """

    if natural:
      self.set_purse(self.get_purse() + self.get_bet() + self.get_bet() * 1.5)
      self.set_bet(0)
    else:
      self.set_purse(self.get_purse() + self.get_bet() * 2)
      self.set_bet(0)


  def lose(self):
    """
    A player loses and a dealer wins.
    """

    self.set_bet(0)


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


  # Instance methods


  def hit(self, pack):
    """
    A dealer hits.

    Status codes:
    0) Ok
    1) Stay
    2) Bust

    In:
    pack (Pack): A pack hit from.
    """

    self.set_hand(self.get_hand().get_cards() + [pack.hit()])
    score = self.get_hand().get_score()
    if score < 17:
      return 0
    elif score >= 17 and score < 22:
      return 1
    else:
      return 2


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
