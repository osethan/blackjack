import random

class Pack:
  """
  Set of standard 52 card decks used to play Blackjack.
  """

  _DECKS = 6
  _DECK_SIZE = 52


  def __init__(self):
    """
    Pack constructor.
    """
    
    self.cards = []

    for _ in range(Pack._DECKS):
      deck = _Deck()
      for card in deck.cards:
        self.cards += [card]


  def shuffle(self, _random = None):
    """
    Shuffle a pack of six card decks.

    In:
    random (function): random
    """

    for i, card in enumerate(self.cards):
      swap_idx = -1
      if _random:
        swap_idx = _random(0, Pack._DECK_SIZE * Pack._DECKS - 1)
      else:
        swap_idx = random.randint(0, Pack._DECK_SIZE * Pack._DECKS - 1)

      swapCard = self.cards[swap_idx]
      self.cards[swap_idx] = card
      self.cards[i] = swapCard

  
  def hit(self, card_str = None):
    """
    Take a card from pack.

    In:
    card_str (str): Optional card to remove from pack.

    Out:
    (Card): Card taken from pack.
    """

    if card_str:
      for i, card in enumerate(self.cards):
        if str(card) == card_str:
          return self.cards.pop(i)

    return self.cards.pop(0)


class _Deck:
  """
  Standard 52 card deck.
  """

  CardS = 52


  def __init__(self):
    """
    Deck constructor.
    """
    
    self.cards = []

    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    pips = [str(d) for d in list(range(2, 11))] + ['Jack', 'Queen', 'King', 'Ace']

    for suit in suits:
      for pip in pips:
        card = Card(suit, pip)
        self.cards += [card]


class Card:
  """
  Single card of a standard 52 card deck.
  """

  VALUE = {
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


  def __init__(self, suit, pip):
    """
    Card constructor.

    In:
    suit (string): One of Clubs, Diamonds, Hearts or Spades
    pip (string): One of 1 - 10, Jack, Queen, King or Ace
    """
    
    self.suit = suit
    self.pip = pip
    self.hidden = False


  def __str__(self):
    """
    String representation of a card.

    Out:
    (str): The string representation of a card.
    """

    if not self.hidden:
      return str((self.suit, self.pip))
    else:
      return "('*', '*')"


  def set_hidden(self, value):
    """
    Change if a card is hidden or visible.

    In:
    value (bool): Whether the card is hidden or visible.
    """

    self.hidden = value
