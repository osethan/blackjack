import random
import re

from src.seat import Dealer, Player
from src.pack import Pack


class Game:
  """
  Game of Blackjack.
  """

  def __init__(self, _print = print, _input = input, _random = random.randint):
    """
    Game ctor.
    """

    pack = Pack()
    pack.shuffle(_random)

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


  def deal(self):
    """
    Cards are dealt for a hand in Blackjack.
    """

    # Range is the number of seats * 2
    for i in range(4):
      card = self.get_pack().hit()

      # A dealer's second card, last card dealt, is face down
      if i == 3:
        card.set_hidden(True)

      # Modulo the number of seats
      hand = None
      if i % 2 == 0:
        hand = self.get_player().get_hand()
      elif i % 2 == 1:
        hand = self.get_dealer().get_hand()

      hand.set_cards(hand.get_cards() + [card])


  def natural(self):
    """
    Cards dealt may be a natural.

    Out:
    (bool): A player or a dealer has a natural.
    """

    return self.get_dealer().get_hand().natural() or self.get_player().get_hand().natural()


  def settle(self):
    """
    Round of Blackjack ends.
    """

    # A dealer and a player have natural
    if self.get_dealer().get_hand().natural() and self.get_player().get_hand().natural():
      self.get_player().tie()
    
    # A dealer has natural
    elif self.get_dealer().get_hand().natural():
      self.get_player().loss()

    # A player has natural
    elif self.get_player().get_hand().natural():
      self.get_player().win()

    # Empty a player's and a dealer's hands
    self.get_player().get_hand().set_cards([])
    self.get_dealer().get_hand().set_cards([])


  def exit(self):
    """
    Exit Blackjack.
    """

    self.print('Come again soon')


if __name__ == "__main__":
  def main():
    game = Game()

    status = game.welcome()
    if status == 1:
      return

    # Game loop
    while True:
      if 1000 <= game.get_player().get_purse().get_size() <= 0:
        game.exit()
        break

      status = game.bet()
      if status == 1:
        return

      game.deal()

      if game.natural():
        game.settle()
        continue


  main()
