import pytest

from library.game.game import Game
from library.pack.pack import Pack


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
