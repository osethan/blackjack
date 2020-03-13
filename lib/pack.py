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

      swap_card = self.cards[swap_idx]
      self.cards[swap_idx] = card
      self.cards[i] = swap_card


class _Deck:
  """
  Standard 52 card deck.
  """

  _CARDS = 52

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

    In:
    suit (string): One of Clubs, Diamonds, Hearts or Spades
    pip (string): One of 1 - 10, Jack, Queen, King or Ace
    """
    
    self.suit = suit
    self.pip = pip
