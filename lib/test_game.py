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

  game = Game(test_print, test_prompt)
  game._welcome()
