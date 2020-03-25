import random

class Pack:
  """
  Six standard 52 card decks used to play Blackjack.
  """

  def __init__(self):
    """
    Pack ctor.
    """
    
    cards = []
    for _ in range(6):
      for suit in Card.SUITS:
        for pip in Card.PIPS:
            cards.append(Card(suit, pip))

    self.cards = cards


  def shuffle(self, _random = None):
    """
    Shuffle a full pack of cards.

    In:
    random (function): Set random behavior.
    """

    for i, card in enumerate(self.cards):
      swap_idx = -1
      if _random:
        swap_idx = _random(0, len(self.cards) - 1)
      else:
        swap_idx = random.randint(0, len(self.cards) - 1)

      swap_card = self.cards[swap_idx]
      self.cards[swap_idx] = card
      self.cards[i] = swap_card

  
  def hit(self, card = None):
    """
    Take a card from pack.

    In:
    card (Card): Optional card to remove from pack.

    Out:
    (Card): Card taken from pack.
    """

    if card:
      for i, _card in enumerate(self.cards):
        if _card.suit == card.suit and _card.pip == card.pip:
          return self.cards.pop(i)

    return self.cards.pop(0)


class Card:
  """
  A card of a standard 52 card deck.
  """

  SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  PIPS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


  def __init__(self, suit, pip):
    """
    Card ctor.

    In:
    suit (string): One of Clubs, Diamonds, Hearts or Spades.
    pip (string): One of 2 - 10, Jack, Queen, King or Ace.
    """
    
    if suit not in Card.SUITS or pip not in Card.PIPS:
      return None

    self.suit = suit
    self.pip = pip
    self.hidden = False


  # def __str__(self):
  #   """
  #   String representation of a card.

  #   Out:
  #   (str): The string representation of a card.
  #   """

  #   if not self.hidden:
  #     return str((self.suit, self.pip))
  #   else:
  #     return "('*', '*')"


  # def set_hidden(self, value):
  #   """
  #   Change if a card is hidden or visible.

  #   In:
  #   value (bool): Whether the card is hidden or visible.
  #   """

  #   self.hidden = value
