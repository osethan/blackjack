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

    if len(self.get_cards()) < 6 * 52:
      self.set_cards(Pack().get_cards())

    cards = self.get_cards()

    for i, card in enumerate(cards):
      swap_idx = _random(0, len(cards) - 1)
      swap_card = cards[swap_idx]
      cards[swap_idx] = card
      cards[i] = swap_card

    self.set_cards(cards)


  def hit(self, card = None):
    """
    Take front card from pack.

    In:
    card (Card): A card to remove from a pack.

    Out:
    (Card): Card removed from pack.
    """

    if card:
      for i, c in enumerate(self.get_cards()):
        if c.get_suit() == card.get_suit() and c.get_pip() == card.get_pip():
          return self.get_cards().pop(i)
      return None

    return self.get_cards().pop(0)
