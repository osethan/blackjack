import pytest

from src.card import Card
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


@pytest.mark.parametrize('prints, prompts, inputs, purse', [
  # Expected successes
  # A player makes a bet
  ([
    'Your purse has 200 chips. What is your bet?'
  ], [], [
    '100'
  ], None),
  # Expected failures
  # A player doesn't bet a number
  ([
    'Your purse has 200 chips. What is your bet?',
    'Can only bet integer chips',
    'Your purse has 200 chips. What is your bet?'
  ], [], [
    'Blackjack',
    '100'
  ], None),
  # A player doesn't make an integer bet
  ([
    'Your purse has 200 chips. What is your bet?',
    'Can only bet integer chips',
    'Your purse has 200 chips. What is your bet?'
  ], [], [
    '50.5',
    '100'
  ], None),
  # A player bet under 2 chips
  ([
    'Your purse has 200 chips. What is your bet?',
    'Can only bet between 2 - 500 chips and no more than purse',
    'Your purse has 200 chips. What is your bet?'
  ], [], [
    '1',
    '100'
  ], None),
  # A player bets over purse
  ([
    'Your purse has 200 chips. What is your bet?',
    'Can only bet between 2 - 500 chips and no more than purse',
    'Your purse has 200 chips. What is your bet?'
  ], [], [
    '250',
    '100'
  ], None),
  # A player bets over 500 chips
  ([
    'Your purse has 600 chips. What is your bet?',
    'Can only bet between 2 - 500 chips and no more than purse',
    'Your purse has 600 chips. What is your bet?'
  ], [], [
    '550',
    '100'
  ], 600)
])
def test_game_bet(prints, prompts, inputs, purse):
  """
  A player can make a bet.
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

  if purse:
    game.get_player().get_purse().set_size(purse)

  game.bet()


def test_game_deal():
  """
  A hand is dealt to a player and a dealer.
  """

  def _random(start, end):
    return start

  game = Game(_random = _random)
  game.deal()

  hidden_card = Card('Clubs', '4')
  hidden_card.set_hidden(True)
  expected_dealer_cards = [Card('Clubs', '2'), hidden_card]
  expected_player_cards = [Card('Spades', 'Ace'), Card('Clubs', '3')]

  actual_dealer_cards = game.get_dealer().get_hand().get_cards()
  actual_player_cards = game.get_player().get_hand().get_cards()

  assert len(actual_dealer_cards) == len(expected_dealer_cards)
  for i in range(len(actual_dealer_cards)):
    assert actual_dealer_cards[i].get_suit() == expected_dealer_cards[i].get_suit()
    assert actual_dealer_cards[i].get_pip() == expected_dealer_cards[i].get_pip()
    assert actual_dealer_cards[i].get_hidden() == expected_dealer_cards[i].get_hidden()

  assert len(actual_player_cards) == len(expected_player_cards)
  for i in range(len(actual_player_cards)):
    assert actual_player_cards[i].get_suit() == expected_player_cards[i].get_suit()
    assert actual_player_cards[i].get_pip() == expected_player_cards[i].get_pip()
    assert actual_player_cards[i].get_hidden() == expected_player_cards[i].get_hidden()
