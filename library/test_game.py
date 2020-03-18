import pytest

from game import Game


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
  # Expected successes
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
