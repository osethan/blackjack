import re
# import sys

from library.pack.pack import Pack
from library.seat.seat import Dealer, Player


class Game:
  """
  Play Blackjack.
  """

  def __init__(self, _print = print, _input = input):
    """
    Game ctor.
    """

    self.__print = _print
    self.__input = _input
    self.__pack = Pack()
    self.__player = Player()
    self.__dealer = Dealer()


  def get_player(self):
    """
    Getter accessor.
    """

    return self.__player


  def get_dealer(self):
    """
    Getter accessor.
    """

    return self.__dealer


  def get_pack(self):
    """
    Getter accessor.
    """

    return self.__pack

  # def __init__(self, seats = [Player(), Dealer()], _print = print, _prompt = input):
  #   """
  #   Game constructor.
  #   """
    
  #   self.print = _print
  #   self.prompt = _prompt
  #   self.pack = Pack()
  #   self.seats = seats


  # def main(self):
  #   """
  #   Entry point of program execution.
  #   """

  #   if not self._welcome():
  #     self._quit()

  #   self.pack.shuffle()
    
  #   # Game loop

  #   # Get bets from players
  #   for i, seat in enumerate(self.seats):
  #     if i >= len(self.seats) - 1:
  #       continue

  #     while True:
  #       if self._bet(seat):
  #         break

  #   # Deal cards to all seats
  #   for i in range(2 * len(self.seats)):
  #     game._deal(self.seats, i)

  #   # for seat in self.seats:
  #   #   self.print(seat)


  def make_bet(self, player):
    """
    Ask player for bet.

    In:
    player (Player): A player making a bet.

    Out:
    (boolean): A bet was made successfully.
    """

    pattern = r'^\d+$'
    bet = self.__input(f'You have {player.get_purse()} chips. What is your bet?')

    # Bet isn't an integer
    if not re.match(pattern, bet):
      self.__print('Can only bet whole number of chips')
      return False

    bet = int(bet)

    # Bet is too low or high
    if bet < 2 or bet > 500 or bet > player.get_purse():
      self.__print('Can only bet 2 - 500 chips and no more than purse')
      return False

    # Set player bet
    player.set_purse(player.get_purse() - bet)
    player.set_bet(bet)
    return True

  
  def make_deal(self, seat, cards = []):
    """
    Deal 2 cards to a seat.

    In:
    seat (Seat): A player or a dealer.
    cards (Card[]): Optional list of cards to deal to seat.
    """

    seat_cards = []
    if cards:
      seat_cards = [self.get_pack().hit(card) for card in cards]
    else:
      seat_cards = [self.get_pack().hit() for _ in range(2)]

    if isinstance(seat, Dealer):
      seat_cards[1].set_hidden(True)

    seat.set_cards(seat_cards)


  # def _welcome(self):
  #   """
  #   Print game starting text.
  #   """

  #   while True:
  #     res = self.prompt('Welcome to Blackjack! Do you want to play? (y/n)')

  #     if res == 'q':
  #       self._quit()

  #     if res == 'n':
  #       return False

  #     if res == 'y':
  #       return True


  # def _quit(self):
  #   """
  #   Quit playing Blackjack.
  #   """

  #   self.print('Come again soon')
  #   sys.exit(0)


if __name__ == "__main__":
  game = Game()
