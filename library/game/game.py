import re

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


  def bet(self, player):
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


  # def dealer_natural(self):
  #   """
  #   A dealer may have a natural.

  #   Out:
  #   (bool): A dealer has a natural.
  #   """
  #   pass



  # def check_dealer_natural(self):
  #   """
  #   Check dealer for dealt natural before player plays.
  #   """

  #   dealer = self.get_dealer()
  #   dealer_cards = dealer.get_cards()
  #   player = self.get_player()
  #   player_cards = player.get_cards()

  #   # Dealer face card is ace so player can call insurance
  #   if dealer_cards[0].get_pip() == 'Ace':
  #     while not self.make_insurance(player):
  #       continue

  #     # # Dealer has natural so player wins insurance
  #     # if dealer_cards[1].get_pip() in ['10', 'Jack', 'Queen', 'King']:
  #     #   # Player wins double insurance bet
  #     #   insurance_bet = player.get_insurance_bet()
  #     #   player.set_insurance_bet(0)
  #     #   player.set_purse(player.get_purse() + 2 * insurance_bet)

  #     #   # Player keeps bet if they have natural
  #     #   if self.check_player_natural(player):
  #     #     bet = player.get_bet()
  #     #     player.set_bet(0)
  #     #     player.set_purse(player.get_purse() + bet)
  #     #   else:
  #     #     player.set_bet(0)
  #     # # Dealer doesn't have natural so player loses insurance
  #     # else:


      #   # Hand is settled


  # def player_hit(self, player, _card = None):
  #   """
  #   A player may be able to hit.

  #   In:
  #   player (Player): A player who may be able to hit.
  #   _card (Card): Optional card a player can take as hit.

  #   Out:
  #   (bool): A player's turn continues.
  #   """

  #   player_totals = player.get_totals()
  #   if min(player_totals) < 22:
  #     response = self.input('Do you want to hit? (y/n)')

  #     if response != 'y':
  #       return False

  #     player_cards = player.get_cards()
  #     card = self.get_pack().hit(_card)
  #     player_cards.append(card)
  #     player.set_cards(player_cards)
  #     return True
  #   else:
  #     self.print('Player bust')
  #     return False


  # def dealer_hit(self, _card = None):
  #   """
  #   A dealer's hits are automated.

  #   In:
  #   _card (Card): Optional card to give to dealer from hit.

  #   Out:
  #   (bool): A dealer's turn continues.
  #   """

  #   dealer_totals = dealer.get_totals()
  #   if max(dealer_totals) < 17:
  #     dealer_cards = dealer.get_cards()
  #     card = self.get_pack().hit(_card)
  #     dealer_cards.append(card)
  #     dealer.set_cards(dealer_cards)
  #     return True
  #   else:
  #     pass


  # def check_player_double_down(self, player, card = None):
  #   """
  #   A player may be able to double down.

  #   In:
  #   player (Player): A player who may be able to double down.
  #   card (Card): Optional card a player can take as double down hit.

  #   Out:
  #   (bool): A player's turn continues.
  #   """

  #   player_totals = player.get_totals()
  #   if sum(player_totals) in [9, 10, 11]:
  #     response = self.input('Do you want to double down? (y/n)')

  #     if response != 'y':
  #       return True

  #     # Get new card and give to player
  #     new_card = self.get_pack.hit(card)
  #     new_card.set_hidden(True)
  #     player_cards = [player.get_cards(), new_card]
  #     player.set_cards(player_cards)

  #     # Set player double down bet
  #     player.set


  def seat_natural(self, seat):
    """
    A seat may have dealt natural.

    In:
    seat (Seat): A seat who may have been dealt a natural.

    Out:
    (bool): A seat has been dealt a natural.
    """

    seat_cards = seat.get_cards()
    return [sc for sc in seat_cards if sc.get_pip() == 'Ace'] and [sc for sc in seat_cards if sc.get_pip() in ['10', 'Jack', 'Queen', 'King']]


  # def make_insurance(self, player):
  #   """
  #   Player can call insurance.

  #   In:
  #   player (Player): A player deciding to make insurance.

  #   Out:
  #   (bool): A player has made insurance.
  #   """

  #   # Player decides to take insurance
  #   response = self.input('Dealer has has an ace. Do you want insurance? (y/n)')
  #   if response != 'y':
  #     return False

  #   # Player decides size of insurance
  #   pattern = r'^\d+$'
  #   insurance_bet = 0
  #   insurance_bet = self.input('Can take up to half original bet. How much insurance do you want?')

  #   # Insurance bet isn't an integer
  #   if not re.match(pattern, insurance_bet):
  #     self.print('Can only bet whole number of chips')
  #     return False

  #   insurance_bet = int(insurance_bet)

  #   # Insurance bet is too low or high
  #   player_bet = player.get_bet()
  #   if insurance_bet < 2 or insurance_bet > player_bet // 2:
  #     self.print(f'Can only bet 2 - {player_bet // 2} chips')
  #     return False

  #   player.set_purse(player.get_purse() - insurance_bet)
  #   player.set_insurance_bet(insurance_bet)
  #   return True



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
  # player = game.get_player()
  # dealer = game.get_dealer()
  
  # # Game loop
  # while 0 < sum(player.get_totals()) < 1000:
  #   # Player makes bet
  #   game.make_bet(player)

  #   # Deal hands
  #   game.make_deal(player)
  #   game.make_deal(dealer)

  #   # Player hits
  #   while game.player_hit(player):
  #     continue
