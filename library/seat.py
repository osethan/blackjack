from pack import Card


class Seat:
  """
  Abstraction of someone playing Blackjack.
  """

  def __init__(self):
    """
    Seat constructor.
    """

    self.name = ''
    self.cards = []
    self.totals = []


  def __str__(self):
    """
    Seat string representation:
    """

    seat_str = f'\n{self.name}\n---\nCards: '
    for i, card in enumerate(self.cards):
      seat_str += f'{card}'
      if i != len(self.cards) - 1:
        seat_str += ', '
    seat_str += '\n'

    return seat_str


  def add_card(self, card):
    """
    Add card to rear of cards.

    In:
    card (Card): Card being added to rear of cards.
    """

    # Add card to hand
    self.cards += [card]
    
    # Update hand scores
    if len(self.totals) == 0:
      if card.pip == 'Ace':
        self.totals = [1, 11]
      else:
        self.totals = [Card.VALUE[card.pip]]
    elif len(self.totals) == 1:
      if card.pip == 'Ace':
        self.totals += [self.totals[0] + 11]
        self.totals[0] = self.totals[0] + 1
      else:
        self.totals[0] = self.totals[0] + Card.VALUE[card.pip]
    else:
      if card.pip == 'Ace':
        self.totals[0] = self.totals[0] + 1
        self.totals[1] = self.totals[1] + 11
      else:
        self.totals[0] = self.totals[0] + Card.VALUE[card.pip]
        self.totals[1] = self.totals[1] + Card.VALUE[card.pip]


class Player(Seat):
  """
  Single client playing Blackjack.
  """

  def __init__(self):
    """
    Player constructor.
    """

    super().__init__()

    self.name = 'Client'
    self.bet = 0
    self.purse = 200


  def __str__(self):
    """
    Player string representation.
    """

    player_str = super().__str__()
    player_str += f'Totals: {self.totals}'
    player_str += f'\nBet: {self.bet}'

    return player_str


class Dealer(Seat):
  """
  Single dealer of Blackjack.
  """

  def __init__(self):
    """
    Dealer constructor.
    """

    super().__init__()

    self.name = 'Dealer'
