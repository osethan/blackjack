import re
import sys

from pack import Pack
from seat import Dealer, Player


class Game:
  """
  Runs play of Blackjack.
  """

  def __init__(self, seats = [Player(), Dealer()], _print = print, _prompt = input):
    """
    Game constructor.
    """
    
    self.print = _print
    self.prompt = _prompt
    self.pack = Pack()
    self.seats = seats


  def main(self):
    """
    Entry point of program execution.
    """

    if not self._welcome():
      self._quit()

    self.pack.shuffle()
    
    if not self._bet():
      self._quit()


  def _bet(self, player):
    """
    Ask player how much they'd like to bet
    """

    p = r'^\d+$'
    bet = self.prompt(f'You have {player.purse} chips. What is your bet?')

    if not re.match(p, bet):
      self.print('Can only bet whole number of chips')
      return False

    bet = int(bet)

    if bet < 2 or bet > 500 or bet > player.purse:
      self.print('Can only bet $2 - $500 and no more than purse')
      return False

    player.bet = bet
    player.purse = player.purse - bet

    return True


  def _welcome(self):
    """
    Print game starting text.
    """

    while True:
      res = self.prompt('Welcome to Blackjack! Do you want to play? (y/n)')

      if res == 'n':
        return False

      if res == 'y':
        return True


  def _quit(self):
    """
    Quit playing Blackjack.
    """

    self.print('Come again soon')
    sys.exit(0)


if __name__ == "__main__":
  game = Game()
  game.main()
