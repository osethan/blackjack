
class Card:
  """
  A card from a standard 52 card deck.
  """


  SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  PIPS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


  def __init__(self, suit, pip):
    """
    Card ctor.

    In:
    suit (str): One of Clubs, Diamonds, Hearts or Spades.
    pip (str): One of 2 - 10, Jack, Queen, King or Ace.
    """

    self.__suit = suit
    self.__pip = pip
    self.__hidden = False


  def get_pip(self):
    """
    Getter.

    Out:
    (str)
    """
