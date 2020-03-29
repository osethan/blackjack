from src.seat import Dealer, Player
from src.pack import Pack


class Game:
  """
  Game of Blackjack.
  """

  def __init__(self, _print = print, _input = input):
    """
    Game ctor.
    """

    pack = Pack()
    pack.shuffle()

    self.__dealer = Dealer()
    self.__player = Player()
    self.__pack = pack
    self.print = _print
    self.input = _input


  def welcome(self):
    """
    Welcome a player to Blackjack.

    Status codes:
    0) Ok
    1) Exit

    Out:
    (int): Status code.
    """

    self.print('Welcome to Blackjack!')
    self.print('Start with 200 chips and try to reach 1,000')
    self.print('Bet between 2 - 500 chips and no more than purse')
    self.print('Input \'q\' at any prompt to quit\n')

    while True:
      self.print('Do you want to play? (y/n)')
      res = self.input()

      if res == 'y':
        return 0

      if res in ['n', 'q']:
        return 1


  def exit(self):
    """
    Exit Blackjack.
    """

    self.print('Come again soon')


if __name__ == "__main__":
  game = Game()
  
  status = game.welcome()
  if status:
    game.exit()
