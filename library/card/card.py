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
      for i, pc in enumerate(cards):
        if _card.get_suit() == pc.get_suit() and _card.get_pip() == pc.get_pip():
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


  def get_hidden(self):
    """
    Getter accessor.
    """

    return self.__hidden


  def set_hidden(self, value):
    """
    Change if a card is hidden or visible.

    In:
    value (boolean): Whether a card is hidden or visible.
    """

    self.__hidden = value


class Hand:
  """
  A hand in Blackjack.
  """

  def __init__(self, cards = []):
    """
    Hand ctor.
    """

    self.__cards = cards
    self.__scores = []

    if cards:
      self.set_scores()


  def get_cards(self):
    """
    Getter accessor.
    """

    return self.__cards


  def set_scores(self):
    """
    Setter mutator.
    """

    values = {
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

    cards = self.get_cards()
    scores = []
    for card in cards:
      pip = card.get_pip()
      if len(scores) == 0:
        if pip == 'Ace':
          scores = [1, 11]
        else:
          scores = [values[pip]]
      elif len(scores) == 1:
        if pip == 'Ace':
          scores = [scores[0] + 1, scores[1] + 11]
        else:
          scores = [scores[0] + values[pip]]
      else:
        if pip == 'Ace':
          scores = [scores[0] + 1, scores[1] + 11]
        else:
          scores = [scores[0] + values[pip], scores[0] + values[pip]]

    self.__scores = scores
