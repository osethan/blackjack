# from library.card.card import Pack
# from library.seat.seat import Dealer, Player
# from library.system.system import System
from card import Pack
from seat import Dealer, Player
from system import System


class Game:
  """
  Play Blackjack.
  """

  def __init__(self, system = System()):
    """
    Game ctor.
    """

    pack = Pack()
    pack.shuffle()

    self.__pack = pack
    self.__player = Player()
    self.__dealer = Dealer()
    self.__system = system


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


  def sys(self):
    """
    Getter accessor.
    """

    return self.__system


  # Instance methods


  def welcome(self):
    """
    Welcome player to Blackjack.

    Response codes:
    0) Ok
    1) Exit

    Out:
    (int): Response code.
    """

    self.sys().print('Welcome to Blackjack!')
    self.sys().print('Start with 200 chips and try to reach 1,000')
    self.sys().print('Can only bet between 2 - 500 chips and no more than purse')
    res = self.sys().input('Do you want to play? (y/n)')

    if res == 'y':
      return 0
    else:
      return 1


  def bet(self):
    """
    Bet stage of Blackjack.

    Response codes:
    0) Ok
    1) Exit

    Out:
    (int): Response code.
    """

    self.sys().print(f'Purse is {self.get_player().get_purse()}. What is your bet?')
    return self.get_player().bet(self.sys())


  def deal(self, cards = []):
    """
    Deal stage of Blackjack.

    In:
    cards (Card[]): Optional ordered list of 4 cards to deal.
    """

    if cards:
      self.get_player().set_hand(self.get_player().get_hand().get_cards() + [self.get_pack().hit(cards[0])])
      self.get_dealer().set_hand(self.get_dealer().get_hand().get_cards() + [self.get_pack().hit(cards[1])])
      self.get_player().set_hand(self.get_player().get_hand().get_cards() + [self.get_pack().hit(cards[2])])
      self.get_dealer().set_hand(self.get_dealer().get_hand().get_cards() + [self.get_pack().hit(cards[3]).set_hidden(True)])
    else:
      self.get_player().set_hand(self.get_player().get_hand().get_cards() + [self.get_pack().hit()])
      self.get_dealer().set_hand(self.get_dealer().get_hand().get_cards() + [self.get_pack().hit()])
      self.get_player().set_hand(self.get_player().get_hand().get_cards() + [self.get_pack().hit()])
      card = self.get_pack().hit()
      card.set_hidden(True)
      self.get_dealer().set_hand(self.get_dealer().get_hand().get_cards() + [card])


  def natural(self):
    """
    Natural dealt in Blackjack.

    Response codes:
    0) Ok
    1) Next round
    2) Exit program

    Out:
    (int): Response code.
    """

    if self.get_dealer().natural() and self.get_player().natural():
      self.settle('DEALER_PLAYER_NATURAL')
      return 1
    elif self.get_dealer().natural():
      self.settle('DEALER_NATURAL')
      return 1
    elif self.get_player().natural():
      self.settle('PLAYER_NATURAL')
      return 1
    
    return 0


  def hit(self):
    """
    A player then a dealer hit.

    Status codes:
    0) Ok
    1) Player bust
    2) Dealer bust

    Out:
    (string): Status code.
    """

    # Player hit
    while True:
      self.sys().print(f'Score is {self.get_player().get_hand().get_score()}. Do you want to hit? (y/n)')
      res = self.get_player().hit(self.get_pack(), self.sys())
      if res == 0:
        continue
      elif res == 1:
        break
      elif res == 2:
        self.settle('PLAYER_BUST')
        return 1

    # Dealer hit
    while True:
      res = self.get_dealer().hit(self.get_pack())
      if res == 0:
        continue
      elif res == 1:
        break
      elif res == 2:
        self.settle('DEALER_BUST')
        return 2

    return 0


  def settle(self, type):
    """
    Settle a hand of Blackjack.

    Types:
    DEALER_PLAYER_NATURAL) A dealer and a player both have a natural
    DEALER_NATURAL) A dealer has a natural
    PLAYER_NATURAL) A player has a natural
    PLAYER_BUST) A player scores over 21
    DEALER_BUST) A dealer scores over 21
    HAND) A player and a dealer compare hands

    In:
    type (string): The settle method to apply.
    """

    if type == 'DEALER_PLAYER_NATURAL':
      self.get_player().tie()
    elif type == 'DEALER_NATURAL':
      self.get_player().lose()
    elif type == 'PLAYER_NATURAL':
      self.get_player().win()      
    elif type == 'PLAYER_BUST':
      self.get_player().lose()
    elif type == 'DEALER_BUST':
      self.get_player().win()
    elif type == 'HAND':
      player_score = self.get_player().get_hand().get_score()
      dealer_score = self.get_dealer().get_hand().get_score()
      if player_score == dealer_score:
        self.get_player().tie()
      elif player_score > dealer_score:
        self.get_player().win()
      elif player_score < dealer_score:
        self.get_player().lose()

    self.get_player().clear_hand()
    self.get_dealer().clear_hand()


if __name__ == "__main__":
  game = Game()

  # Game opener
  res = game.welcome()
  if res == 1:
    game.sys().exit('Come again soon')

  # Game loop
  while 0 < game.get_player().get_purse() < 1000:
    res = game.bet()
    if res == 1:
      game.sys().exit('Come again soon')

    game.deal()

    res = game.natural()
    if res == 1:
      continue

    res = game.hit()
    if res == 1:
      continue
    elif res == 2:
      continue

    game.settle('HAND')

  game.sys().exit('Come again soon')
