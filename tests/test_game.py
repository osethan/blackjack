import pytest

from src.game import Game


@pytest.mark.parametrize('prints, prompts, inputs', [
  # Expected successes
  # A player says no to playing Blackjack
  ([
    'Welcome to Blackjack!',
    'Start with 200 chips and try to reach 1,000',
    'Bet between 2 - 500 chips and no more than purse',
    'Input \'q\' at any prompt to quit\n',
    'Do you want to play? (y/n)',
    'Come again soon'
  ], [], [
    'n'
  ]),
  # A player says yes to playing Blackjack
  ([
    'Welcome to Blackjack!',
    'Start with 200 chips and try to reach 1,000',
    'Bet between 2 - 500 chips and no more than purse',
    'Input \'q\' at any prompt to quit\n',
    'Do you want to play? (y/n)'
  ], [], [
    'y'
  ]),
  # A player quits playing Blackjack
  ([
    'Welcome to Blackjack!',
    'Start with 200 chips and try to reach 1,000',
    'Bet between 2 - 500 chips and no more than purse',
    'Input \'q\' at any prompt to quit\n',
    'Do you want to play? (y/n)',
    'Come again soon'
  ], [], [
    'q'
  ]),
  # Expected failures
  # A player inputs don't register
  ([
    'Welcome to Blackjack!',
    'Start with 200 chips and try to reach 1,000',
    'Bet between 2 - 500 chips and no more than purse',
    'Input \'q\' at any prompt to quit\n',
    'Do you want to play? (y/n)',
    'Do you want to play? (y/n)',
    'Do you want to play? (y/n)'
  ], [], [
    'Blackjack',
    '21',
    'y'
  ])
])
def test_game_welcome(prints, prompts, inputs):
  """
  A client is welcomed to Blackjack.
  """

  def test_print(message):
    _print = prints.pop(0)
    assert message == _print

  def test_prompt(message = ''):
    if len(prompts) > 0:
      _prompt = prompts.pop(0)
      assert message == _prompt
    return inputs.pop(0)

  game = Game(test_print, test_prompt)
  game.welcome()
