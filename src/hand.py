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
