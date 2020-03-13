
class Pack:
  """
  Set of standard 52 card decks used to play Blackjack.
  """

  def __init__(self):
    """
    Pack constructor.
    """
    pass


class _Deck:
  """
  Standard 52 card deck.
  """

  def __init__(self):
    """
    Deck constructor.
    """
    
    self.cards = []

    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    pips = [str(d) for d in list(range(2, 11))] + ['Jack', 'Queen', 'King', 'Ace']

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
    Card constructor.
    """
    
    self.suit = suit
    self.pip = pip
