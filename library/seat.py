
class Seat:
  """
  Abstraction of someone playing Blackjack.
  """

  def __init__(self):
    """
    Seat constructor.
    """

    self.name = ''
    self.cards = []


class Player(Seat):
  """
  Single client playing Blackjack.
  """

  def __init__(self):
    """
    Player constructor.
    """

    super().__init__()

    self.name = 'Client'
    self.bet = 0
    self.purse = 200


class Dealer(Seat):
  """
  Single dealer of Blackjack.
  """

  def __init__(self):
    """
    Dealer constructor.
    """

    super().__init__()

    self.name = 'Dealer'
