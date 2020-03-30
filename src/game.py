import re

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


  def get_dealer(self):
    """
    Getter.

    Out:
    (Dealer): A game's dealer.
    """

    return self.__dealer

  
  def get_player(self):
    """
    Getter.

    Out:
    (Player): A game's player.
    """

    return self.__player


  def get_pack(self):
    """
    Getter.

    Out:
    (Pack): A game's pack.
    """

    return self.__pack


  # Instance methods


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


  def bet(self):
    """
    A player makes a bet.

    Status codes:
    0) Ok
    1) Exit

    Out:
    (int): Status code.
    """

    while True:
      self.print(f'Your purse has {self.get_player().get_purse().get_size()} chips. What is your bet?')
      res = self.input()

      if res == 'q':
        return 1

      pattern = r'^\d+$'
      if not re.match(pattern, res):
        self.print('Can only bet integer chips')
        continue

      res = int(res)
      if res < 2 or res > 500 or res > self.get_player().get_purse().get_size():
        self.print('Can only bet between 2 - 500 chips and no more than purse')
        continue

      self.get_player().make_bet(res)
      return 0


  def exit(self):
    """
    Exit Blackjack.
    """

    self.print('Come again soon')


if __name__ == "__main__":
  game = Game()
  
  status = game.welcome()
  if status == 1:
    game.exit()
  else:

    status = game.bet()
    if status == 1:
      game.exit()
    else:
      pass
