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


  def print(self, message):
    """
    Print to output.
    """

    self.__print(message)


  def input(self, message):
    """
    Take input.
    """

    return self.__input(message)

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
    bet = self.input(f'You have {player.get_purse()} chips. What is your bet?')

    # Bet isn't an integer
    if not re.match(pattern, bet):
      self.print('Can only bet whole number of chips')
      return False

    bet = int(bet)

    # Bet is too low or high
    if bet < 2 or bet > 500 or bet > player.get_purse():
      self.print('Can only bet 2 - 500 chips and no more than purse')
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


  def check_dealer_natural(self):
    """
    Check dealer for dealt natural before player plays.
    """

    # Dealer face card is ace so player can call insurance
    if 'Ace' == dealer_cards[0].get_pip():
      self.make_insurance()

      # Dealer has natural
      dealer_cards = self.get_dealer().get_cards()
      if [ten for ten in ['10', 'Jack', 'Queen', 'King'] if ten in dealer_cards]:
        # Player wins double insurance bet
        insurance_bet = self.get_player().get_insurance_bet()
        self.get_player().set_insurance_bet(0)
        self.get_player().set_purse(self.get_player().get_purse() + 2 * insurance_bet)

        # Player keeps bet if they have natural



  def make_insurance(self, player):
    """
    Player can call insurance.

    In:
    player (Player): A player deciding to make insurance.
    """

    # Player decides to take insurance
    response = self.input('Dealer has has an ace. Do you want insurance? (y/n)')
    if response != 'y':
      return False

    # Player decides size of insurance
    pattern = r'^\d+$'
    insurance_bet = 0
    insurance_bet = self.input('Can take up to half original bet. How much insurance do you want?')

    # Insurance bet isn't an integer
    if not re.match(pattern, insurance_bet):
      self.print('Can only bet whole number of chips')
      return False

    insurance_bet = int(insurance_bet)

    # Insurance bet is too low or high
    player_bet = player.get_bet()
    if insurance_bet < 2 or insurance_bet > player_bet // 2:
      self.print(f'Can only bet 2 - {player_bet // 2} chips')
      return False

    player.set_purse(player.get_purse() - insurance_bet)
    player.set_insurance_bet(insurance_bet)
    return True



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
