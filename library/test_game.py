import pytest

from game import Game
from seat import Player
from pack import Card


@pytest.mark.parametrize('prints, prompts, responses', [
  # Expected successes
  # 'yes' response
  ([], ['Welcome to Blackjack! Do you want to play? (y/n)'], ['y']),
  # Expected failures
  # 'no' response
  (['Come again soon'], ['Welcome to Blackjack! Do you want to play? (y/n)'], ['n']),
  # Edge cases
  # Messy response
  (['Come again soon'], [
    'Welcome to Blackjack! Do you want to play? (y/n)',
    'Welcome to Blackjack! Do you want to play? (y/n)',
    'Welcome to Blackjack! Do you want to play? (y/n)'
  ], [
    'no',
    'yes',
    'n'
  ])
])
def test_game_welcome(prints, prompts, responses):
  """
  Game welcome handles all responses.
  """

  def test_print(message):
    _print = prints.pop(0)
    assert _print == message

  def test_prompt(message):
    _prompt = prompts.pop(0)
    assert _prompt == message
    return responses.pop(0)

  game = Game(_print = test_print, _prompt = test_prompt)
  game._welcome()


@pytest.mark.parametrize('prints, prompts, responses', [
  # Expected failures
  # Bet not a number
  (['Can only bet whole number of chips'], [
    'You have 200 chips. What is your bet?'
  ], [
    'Blackjack'
  ]),
  # Bet not an integer
  (['Can only bet whole number of chips'], [
    'You have 200 chips. What is your bet?'
  ], [
    '100.5'
  ]),
  # Bet is under $2
  (['Can only bet $2 - $500 and no more than purse'], [
    'You have 200 chips. What is your bet?'
  ], [
    '1'
  ]),
  # Bet is over $500
  (['Can only bet $2 - $500 and no more than purse'], [
    'You have 200 chips. What is your bet?'
  ], [
    '501'
  ]),
  # Bet is over purse
  (['Can only bet $2 - $500 and no more than purse'], [
    'You have 200 chips. What is your bet?'
  ], [
    '201'
  ]),
  # Expected successes
  ([], ['You have 200 chips. What is your bet?'], ['100']),
])
def test_bet(prints, prompts, responses):
  """
  Player makes a bet.
  """

  def test_print(message):
    _print = prints.pop(0)
    assert _print == message

  def test_prompt(message):
    _prompt = prompts.pop(0)
    assert _prompt == message
    return responses.pop(0)

  game = Game(_print = test_print, _prompt = test_prompt)
  game._bet(game.seats[0])


@pytest.mark.parametrize('index, expected', [
  # Expected successes
  (0, "('Clubs', '2')"),
  (3, "('*', '*')"),
])
def test_deal_card(index, expected):
  """
  Deal cards to seats.

  In:
  index (int): Which seat is being dealt a card.
  expected (str): String representation of the hand of the seat.
  """

  game = Game()
  game._deal(game.seats, index)
  actual = str(game.seats[index % len(game.seats)].cards[0])

  assert actual == expected


def test_deal_totals_no_score_ace(init_deal_totals):
  """
  Player totals having no score and gets ace.

  In:
  init_deal_totals (dict): Initialized values for deal totals.
  """

  # Test specific values
  game = init_deal_totals['game']
  index = init_deal_totals['index']
  expected = [1, 11]

  # Act on values
  card = game.pack.hit(card_str = "('Spades', 'Ace')")
  game._deal(game.seats, index, card)

  # Check values
  actual = game.seats[index].totals
  assert actual == expected


def test_deal_totals_no_score_not_ace(init_deal_totals):
  """
  Player totals having no score and gets not ace.

  In:
  init_deal_totals (dict): Initialized values for deal totals.
  """

  # Test specific values
  game = init_deal_totals['game']
  index = init_deal_totals['index']
  expected = [2]

  # Act on values
  card = game.pack.hit(card_str = "('Clubs', '2')")
  game._deal(game.seats, index, card)

  # Check values
  actual = game.seats[index].totals
  assert actual == expected


def test_deal_totals_one_score_ace(init_deal_totals):
  """
  Player totals having one score and gets ace.

  In:
  init_deal_totals (dict): Initialized values for deal totals.
  """

  # Test specific values
  game = init_deal_totals['game']
  index = init_deal_totals['index']
  expected = [3, 13]

  # Act on values
  card = game.pack.hit(card_str = "('Clubs', '2')")
  game._deal(game.seats, index, card)

  card = game.pack.hit(card_str = "('Spades', 'Ace')")
  game._deal(game.seats, index, card)

  # Check values
  actual = game.seats[index].totals
  assert actual == expected


def test_deal_totals_one_score_not_ace(init_deal_totals):
  """
  Players totals having one score and gets not ace.

  In:
  init_deals_totals (dict): Initialized values for deal totals.
  """

  # Test specific values
  game = init_deal_totals['game']
  index = init_deal_totals['index']
  expected = [5]

  # Act on values
  card = game.pack.hit(card_str = "('Clubs', '2')")
  game._deal(game.seats, index, card)

  card = game.pack.hit(card_str = "('Hearts', '3')")
  game._deal(game.seats, index, card)

  # Check values
  actual = game.seats[index].totals
  assert actual == expected


def test_deal_totals_two_scores_ace(init_deal_totals):
  """
  Player totals having two scores and gets ace.

  In:
  init_deals_totals (dict): Initialized values for deal totals.
  """

  # Test specific values
  game = init_deal_totals['game']
  index = init_deal_totals['index']
  expected = [2, 22]

  # Act on values
  card = game.pack.hit(card_str = "('Spades', 'Ace')")
  game._deal(game.seats, index, card)

  card = game.pack.hit(card_str = "('Hearts', 'Ace')")
  game._deal(game.seats, index, card)

  # Check values
  actual = game.seats[index].totals
  assert actual == expected


def test_deal_totals_two_scores_not_ace(init_deal_totals):
  """
  Player tools having two scores and gets not ace.

  In:
  init_deals_totals (dict): Initialized values for deal totals.
  """

  # Test specific values
  game = init_deal_totals['game']
  index = init_deal_totals['index']
  expected = [4, 14]

  # Act on values
  card = game.pack.hit(card_str = "('Spades', 'Ace')")
  game._deal(game.seats, index, card)

  card = game.pack.hit(card_str = "('Hearts', '3')")
  game._deal(game.seats, index, card)

  # Check values
  actual = game.seats[index].totals
  assert actual == expected


# Fixtures


@pytest.fixture
def init_deal_totals():
  """
  Initialized values for deal totals.
  """

  player = Player()
  seats = [player]

  return {
    'game': Game(seats = seats),
    'index': 0
  }
