from src.card import Card


class Hand:
  """
  A player's or dealer's hand in Blackjack.
  """

  def __init__(self):
    """
    Hand ctor.
    """

    self.__cards = []
    self.__scores = [0]


  def get_cards(self):
    """
    Getter.

    Out:
    (Card[]): A hand's cards.
    """

    return self.__cards


  # TODO: Write set_cards for natural testing
  def set_cards(self, cards):
    """
    Setter.

    In:
    cards (Card[]): A hand's new cards.
    """

    self.__cards = cards


  # Instance methods


  def natural(self):
    """
    A hand is a natural.

    Out:
    (bool): A hand is a natural.
    """

    cards = self.get_cards()
    if [card for card in cards if card.get_pip() == 'Ace'] and [card for card in cards if card.get_pip() in ['10', 'Jack', 'Queen', 'King']] and len(cards) == 2:
      return True
    else:
      return False
