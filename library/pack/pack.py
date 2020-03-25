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

    self.__cards = cards


  def get_cards(self):
    """
    Getter accessor.
    """

    return self.__cards


  def set_cards(self, cards):
    """
    Setter mutator.

    In:
    cards (Card[]): New state of cards.
    """

    self.__cards = cards


  def set_card(self, idx, card):
    """
    Setter mutator. A card at an index is set.

    In:
    idx (int): Index of card to set.
    card (Card): A card to insert at the index.
    """

    self.__cards[idx] = card


  def shuffle(self, _random = None):
    """
    Shuffle a full pack of cards.

    In:
    random (function): Set random behavior.
    """

    for i, card in enumerate(self.get_cards()):
      swap_idx = -1
      if _random:
        swap_idx = _random(0, len(self.get_cards()) - 1)
      else:
        swap_idx = random.randint(0, len(self.cards) - 1)

      swap_card = self.get_cards()[swap_idx]
      self.set_card(swap_idx, card)
      self.set_card(i, swap_card)

  
  def hit(self, _card = None):
    """
    Take a card from pack.

    In:
    _card (Card): Optional card to remove from pack.

    Out:
    (Card): Card taken from pack.
    """

    cards = self.get_cards()
    if _card:
      for i, pack_card in enumerate(cards):
        if _card.get_suit() == pack_card.get_suit() and _card.get_pip() == pack_card.get_pip():
          card = cards.pop(i)
          self.set_cards(cards)
          return card

    card = cards.pip(0)
    self.set_cards(cards)
    return card


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

    self.__suit = suit
    self.__pip = pip
    self.__hidden = False


  def get_suit(self):
    """
    Getter accessor.
    """

    return self.__suit


  def get_pip(self):
    """
    Getter accessor.
    """

    return self.__pip


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
