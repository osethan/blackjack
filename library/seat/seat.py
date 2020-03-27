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


  def get_cards(self):
    """
    Getter accessor.
    """

    return self.__cards


  def set_cards(self, cards):
    """
    Setter mutator.

    In:
    cards (Card[]): New state of a seat's cards.
    """

    self.__cards = cards


  def get_name(self):
    """
    Getter accessor.
    """

    return self.__name


  def get_totals(self):
    """
    Getter accessor.
    """

    return self.__totals


  def set_totals(self):
    """
    Setter mutator.
    """

    values = {
      '2': 2,
      '3': 3,
      '4': 4,
      '5': 5,
      '6': 6,
      '7': 7,
      '8': 8,
      '9': 9,
      '10': 10,
      'Jack': 10,
      'Queen': 10,
      'King': 10
    }

    cards = self.get_cards()
    totals = []
    for card in cards:
      pip = card.get_pip()
      if len(totals) == 0:
        if pip == 'Ace':
          totals = [1, 11]
        else:
          totals = [values[pip]]
      elif len(totals) == 1:
        if pip == 'Ace':
          totals = [totals[0] + 1, totals[1] + 11]
        else:
          totals = [totals[0] + values[pip]]
      else:
        if pip == 'Ace':
          totals = [totals[0] + 1, totals[1] + 11]
        else:
          totals = [totals[0] + values[pip], totals[0] + values[pip]]

    self.__totals = totals


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


  def get_bet(self):
    """
    Getter accessor.
    """

    return self.__bet


  def get_purse(self):
    """
    Getter accessor.
    """

    return self.__purse


  def get_insurance_bet(self):
    """
    Getter accessor.
    """

    return self.__insurance_bet


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


  def set_insurance_bet(self, insurance_bet):
    """
    Setter mutator.
    """

    self.__insurance_bet = insurance_bet


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
