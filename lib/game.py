import sys

from pack import Pack


class Game:
  """
  Runs play of Blackjack.
  """

  def __init__(self, _print = print, _prompt = input):
    """
    Game constructor.
    """
    
    self.print = _print
    self.prompt = _prompt
    self.pack = Pack()

  def introduction(self):
    """
    Prepare to play Blackjack.
    """
    pass

  def _welcome(self):
    """
    Print game starting text.
    """

    while True:
      res = self.prompt('Welcome to Blackjack! Do you want to play? (y/n)')

      if res == 'n':
        self.print('Come again soon')
        return False

      if res == 'y':
        return True
