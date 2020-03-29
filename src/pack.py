import random

from src.card import Card


class Pack:
  """
  A pack in Blackjack which starts as six standard 52 card decks.
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

    self.__cards = cards


  def get_cards(self):
    """
    Getter.

    Out:
    (Card[]): The state of a pack's cards.
    """

    return self.__cards


  def set_cards(self, cards):
    """
    Setter.

    In:
    cards (Card[]): New state of cards.
    """

    self.__cards = cards


  # Instance methods


  def shuffle(self, _random = random.randint):
    """
    Shuffle a full pack of six decks.

    In:
    _random (function): Random integer between x and y inclusive.
    """

    cards = self.get_cards()

    for i, card in enumerate(cards):
      swap_idx = _random(0, len(cards) - 1)
      swap_card = cards[swap_idx]
      cards[swap_idx] = card
      cards[i] = swap_card

    self.set_cards(cards)


  def hit(self):
    """
    Take front card from pack.

    Out:
    (Card): Card removed from pack.
    """

    return self.get_cards().pop(0)
