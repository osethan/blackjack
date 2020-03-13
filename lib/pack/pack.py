
class Pack:
  """
  Set of standard 52 card decks used to play Blackjack.
  """

  def __init__(self):
    """
    Pack ctor.
    """
    pass


class _Deck:
  """
  Standard 52 card deck.
  """

  def __init__(self):
    """
    Deck ctor.
    """
    
    self.cards = []

    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    pips = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']

    for suit in suits:
      for pip in pips:
        card = _Card(suit, pip)
        self.cards += [card]


class _Card:
  """
  Single card of a standard 52 card deck.
  """

  def __init__(self, suit, pip):
    """
    Card ctor.
    """
    
    self.suit = suit
    self.pip = pip
