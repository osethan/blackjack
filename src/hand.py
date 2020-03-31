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


  def set_cards(self, cards):
    """
    Setter.

    In:
    cards (Card[]): A hand's new cards.
    """

    self.__cards = cards
    self.set_scores()


  def get_scores(self):
    """
    Getter.

    Out:
    (int[]): A hand's scores.
    """

    return self.__scores


  def set_scores(self):
    """
    Setter.
    """

    cards = self.get_cards()
    scores = [0]
    values = {
      '2': [2],
      '3': [3],
      '4': [4],
      '5': [5],
      '6': [6],
      '7': [7],
      '8': [8],
      '9': [9],
      '10': [10],
      'Jack': [10],
      'Queen': [10],
      'King': [10],
      'Ace': [1, 11]
    }

    for card in cards:
      pip = card.get_pip()
      score = scores[-1]
      scores = [scr + values[pip][0] for scr in scores]
      if pip == 'Ace':
        scores += [score + values[pip][1]]

    self.__scores = scores


  # Instance methods


  def score(self):
    """
    The highest score in a hand's scores equal or under 21.

    Out:
    (int): The highest score in a hand's scores equal or under 21.
    """

    for score in self.get_scores()[-1::-1]:
      if score <= 21:
        return score
    
    return self.get_scores()[0]

  
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
