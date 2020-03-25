# from pack import Card


class Seat:
  """
  Abstraction of someone playing Blackjack.
  """

  def __init__(self):
    """
    Seat ctor.
    """

    self.__name = ''
    self.__cards = []
    self.__totals = []


  # def __str__(self):
  #   """
  #   Seat string representation:
  #   """

  #   seat_str = f'\n{self.name}\n---\nCards: '
  #   for i, card in enumerate(self.cards):
  #     seat_str += f'{card}'
  #     if i != len(self.cards) - 1:
  #       seat_str += ', '
  #   seat_str += '\n'

  #   return seat_str


  # def add_card(self, card):
  #   """
  #   Add card to rear of cards.

  #   In:
  #   card (Card): Card being added to rear of cards.
  #   """

  #   # Add card to hand
  #   self.cards += [card]
    
  #   # Update hand scores
  #   if len(self.totals) == 0:
  #     if card.pip == 'Ace':
  #       self.totals = [1, 11]
  #     else:
  #       self.totals = [Card.VALUE[card.pip]]
  #   elif len(self.totals) == 1:
  #     if card.pip == 'Ace':
  #       self.totals += [self.totals[0] + 11]
  #       self.totals[0] = self.totals[0] + 1
  #     else:
  #       self.totals[0] = self.totals[0] + Card.VALUE[card.pip]
  #   else:
  #     if card.pip == 'Ace':
  #       self.totals[0] = self.totals[0] + 1
  #       self.totals[1] = self.totals[1] + 11
  #     else:
  #       self.totals[0] = self.totals[0] + Card.VALUE[card.pip]
  #       self.totals[1] = self.totals[1] + Card.VALUE[card.pip]


class Player(Seat):
  """
  Non-dealer playing Blackjack.
  """

  def __init__(self):
    """
    Player ctor.
    """

    super().__init__()

    self.__name = 'Player'
    self.__purse = 200
    self.__bet = 0
    self.__insurance_bet = 0
    self.__double_down_bet = 0
    self.__split_pair_bets = []
    self.__split_pair_hands = []
    self.__split_pair_totals = []


  def get_purse(self):
    """
    Getter accessor.
    """

    return self.__purse


  def set_purse(self, purse):
    """
    Setter mutator.
    """

    self.__purse = purse


  def set_bet(self, bet):
    """
    Setter mutator.
    """

    self.__bet = bet


  # def __str__(self):
  #   """
  #   Player string representation.
  #   """

  #   player_str = super().__str__()
  #   player_str += f'Totals: {self.totals}'
  #   player_str += f'\nBet: {self.bet}'

  #   return player_str


class Dealer(Seat):
  """
  Dealer of Blackjack.
  """

  def __init__(self):
    """
    Dealer ctor.
    """

    super().__init__()

    self.__name = 'Dealer'
