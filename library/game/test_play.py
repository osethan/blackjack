import pytest

from library.game.game import Game
from library.pack.pack import Pack, Card


@pytest.mark.parametrize('prints, inputs, responses', [
  # Expected successes
  ([], ['You have 200 chips. What is your bet?'], ['100']),
  # Expected failures
  # Bet not a number
  ([
    'Can only bet whole number of chips'
  ], [
    'You have 200 chips. What is your bet?'
  ], [
    'Blackjack'
  ]),
  # Bet not an integer
  ([
    'Can only bet whole number of chips'
  ], [
    'You have 200 chips. What is your bet?'
  ], [
    '100.5'
  ]),
  # Bet is under 2 chips
  ([
    'Can only bet 2 - 500 chips and no more than purse'
  ], [
    'You have 200 chips. What is your bet?'
  ], [
    '1'
  ]),
  # Bet is over 500 chips
  (['Can only bet 2 - 500 chips and no more than purse'
  ], [
    'You have 200 chips. What is your bet?'
  ], [
    '501'
  ]),
  # Bet is over purse
  (['Can only bet 2 - 500 chips and no more than purse'
  ], [
    'You have 200 chips. What is your bet?'
  ], [
    '201'
  ]),
])
def test_game_make_bet(prints, inputs, responses):
  """
  Player can make a bet.
  """

  def test_print(message):
    _print = prints.pop(0)
    assert _print == message

  def test_input(message):
    _input = inputs.pop(0)
    assert _input == message
    return responses.pop(0)

  game = Game(_print = test_print, _input = test_input)
  player = game.get_player()
  game.make_bet(player)


@pytest.mark.parametrize('name, cards', [
  ('Player', [Card('Clubs', 'Ace'), Card('Hearts', '2')]),
  ('Dealer', [Card('Clubs', 'Ace'), Card('Hearts', '2')]),
])
def test_game_make_deal(name, cards):
  """
  Seat is dealt cards.
  """

  game = Game()

  if name == 'Player':
    player = game.get_player()
    game.make_deal(player, cards)

    assert len(player.get_cards()) == 2
    
    for card in player.get_cards():
      assert card.get_hidden() == False

  elif name == 'Dealer':
    dealer = game.get_dealer()
    game.make_deal(dealer, cards)

    assert len(dealer.get_cards()) == 2

    dealer_cards = dealer.get_cards()
    assert dealer_cards[0].get_hidden() == False
    assert dealer_cards[1].get_hidden() == True


@pytest.mark.parametrize('prints, inputs, responses', [
  # Expected successes
  ([], [
    'You have 200 chips. What is your bet?',
    'Dealer has has an ace. Do you want insurance? (y/n)',
    'Can take up to half original bet. How much insurance do you want?',
  ], [
    '100',
    'y',
    '50'
  ]),
])
def test_make_insurance(prints, inputs, responses):
  """
  Player can make insurance.
  """

  def test_print(message):
    _print = prints.pop(0)
    assert _print == message

  def test_input(message):
    _input = inputs.pop(0)
    assert _input == message
    return responses.pop(0)

  game = Game(_print = test_print, _input = test_input)
  player = game.get_player()
  game.make_bet(player)
  game.make_insurance(player)
  assert player.get_bet() == 100
  assert player.get_insurance_bet() == 50
  assert player.get_purse() == 50


@pytest.mark.parametrize('prints, inputs, responses, expected', [
  # Expected failures
  # Player says no to taking insurance
  ([], [
    'You have 200 chips. What is your bet?',
    'Dealer has has an ace. Do you want insurance? (y/n)'
  ], [
    '100',
    'n'
  ], False),
  # Player's insurance isn't an integer
  ([
    'Can only bet whole number of chips'
  ], [
    'You have 200 chips. What is your bet?',
    'Dealer has has an ace. Do you want insurance? (y/n)',
    'Can take up to half original bet. How much insurance do you want?'
  ], [
    '100',
    'y',
    '40.5'
  ], False),
  # Player's insurance is too low
  ([
    'Can only bet 2 - 50 chips'
  ], [
    'You have 200 chips. What is your bet?',
    'Dealer has has an ace. Do you want insurance? (y/n)',
    'Can take up to half original bet. How much insurance do you want?'
  ], [
    '100',
    'y',
    '1'
  ], False),
  # Player's insurance is too high
  ([
    'Can only bet 2 - 50 chips'
  ], [
    'You have 200 chips. What is your bet?',
    'Dealer has has an ace. Do you want insurance? (y/n)',
    'Can take up to half original bet. How much insurance do you want?'
  ], [
    '100',
    'y',
    '60'
  ], False),
])
def test_make_insurance_failures(prints, inputs, responses, expected):
  """
  Player says no to taking insurance.
  """

  def test_print(message):
    _print = prints.pop(0)
    assert _print == message

  def test_input(message):
    _input = inputs.pop(0)
    assert _input == message
    return responses.pop(0)

  game = Game(_print = test_print, _input = test_input)
  player = game.get_player()
  game.make_bet(player)
  actual = game.make_insurance(player)
  assert actual == expected


@pytest.mark.parametrize('cards, expected', [
  # Expected successes
  ([Card('Clubs', 'Ace'), Card('Hearts', 'Jack')], True),
  # Expected failures
  ([Card('Clubs', '2'), Card('Hearts', '3')], False),
])
def test_check_player_natural(cards, expected):
  """
  Player checked for a dealt natural.
  """

  game = Game()
  player = game.get_player()
  game.make_deal(player, cards)
  actual = game.check_player_natural(player)
  assert actual == expected
