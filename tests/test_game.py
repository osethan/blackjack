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
    '\nYour purse has 200 chips. What is your bet?'
  ], [], [
    '100'
  ], None),
  # Expected failures
  # A player doesn't bet a number
  ([
    '\nYour purse has 200 chips. What is your bet?',
    'Can only bet integer chips',
    '\nYour purse has 200 chips. What is your bet?'
  ], [], [
    'Blackjack',
    '100'
  ], None),
  # A player doesn't make an integer bet
  ([
    '\nYour purse has 200 chips. What is your bet?',
    'Can only bet integer chips',
    '\nYour purse has 200 chips. What is your bet?'
  ], [], [
    '50.5',
    '100'
  ], None),
  # A player bet under 2 chips
  ([
    '\nYour purse has 200 chips. What is your bet?',
    'Can only bet between 2 - 500 chips and no more than purse',
    '\nYour purse has 200 chips. What is your bet?'
  ], [], [
    '1',
    '100'
  ], None),
  # A player bets over purse
  ([
    '\nYour purse has 200 chips. What is your bet?',
    'Can only bet between 2 - 500 chips and no more than purse',
    '\nYour purse has 200 chips. What is your bet?'
  ], [], [
    '250',
    '100'
  ], None),
  # A player bets over 500 chips
  ([
    '\nYour purse has 600 chips. What is your bet?',
    'Can only bet between 2 - 500 chips and no more than purse',
    '\nYour purse has 600 chips. What is your bet?'
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


@pytest.mark.parametrize('prints, player_cards, dealer_cards, player_bet, expected_player_purse', [
  # Expected successes
  # A player and a dealer have natural
  (['Dealer and Player natural'],
  [Card('Clubs', 'Ace'), Card('Hearts', '10')],
  [Card('Diamonds', 'Jack'), Card('Spades', 'Ace')],
  100,
  200),
  # A player has natural
  (['Player natural'],
  [Card('Clubs', 'Ace'), Card('Hearts', '10')],
  [Card('Diamonds', 'Jack'), Card('Spades', '9')],
  100,
  350),
  # A dealer has natural
  (['Dealer natural'],
  [Card('Clubs', 'Ace'), Card('Hearts', '9')],
  [Card('Diamonds', 'Jack'), Card('Spades', 'Ace')],
  100,
  100),
  # A player busts
  (['Player bust'],
  [Card('Spades', '9'), Card('Spades', '10'), Card('Hearts', 'Queen')],
  [Card('Clubs', '2'), Card('Clubs', '3')],
  100,
  100),
  # A dealer busts
  (['Dealer bust'],
  [Card('Clubs', '9'), Card('Clubs', '10')],
  [Card('Spades', '9'), Card('Spades', '10'), Card('Hearts', 'Queen')],
  100,
  300),
  # A player wins over a dealer
  (['Player win'],
  [Card('Hearts', '9'), Card('Hearts', '10')],
  [Card('Diamonds', '8'), Card('Diamonds', '10')],
  100,
  300),
  # A player and a dealer tie
  (['Dealer and Player tie'],
  [Card('Hearts', '9'), Card('Hearts', '10')],
  [Card('Diamonds', '9'), Card('Diamonds', '10')],
  100,
  200),
  # A player loses to a dealer
  (['Player loss'],
  [Card('Diamonds', '8'), Card('Diamonds', '10')],
  [Card('Hearts', '9'), Card('Hearts', '10')],
  100,
  100)
])
def test_game_settle(prints, player_cards, dealer_cards, player_bet, expected_player_purse):
  """
  Round of Blackjack settled.
  """

  def test_print(message):
    _print = prints.pop(0)
    assert message == _print

  game = Game(_print = test_print)
  game.get_player().get_hand().set_cards(player_cards)
  game.get_dealer().get_hand().set_cards(dealer_cards)
  game.get_player().make_bet(player_bet)
  game.settle()

  expected_player_cards = []
  expected_player_bet = 0
  expected_player_purse = expected_player_purse
  expected_dealer_cards = []

  actual_player_cards = game.get_player().get_hand().get_cards()
  actual_player_bet = game.get_player().get_bet().get_size()
  actual_player_purse = game.get_player().get_purse().get_size()
  actual_dealer_cards = game.get_dealer().get_hand().get_cards()

  assert actual_player_cards == expected_player_cards
  assert actual_player_bet == expected_player_bet
  assert actual_player_purse == expected_player_purse
  assert actual_dealer_cards == expected_dealer_cards


@pytest.mark.parametrize('prints, prompts, inputs, cards, new_card, expected', [
  # Expected successes
  # A player stays
  ([
    '\nYour score is 20. Do you want to hit? (y/n)'
  ], [], [
    'n'
  ],
  [Card('Diamonds', '9'), Card('Diamonds', 'Ace')],
  None,
  0),
  # A player hits, then stays
  ([
    '\nYour score is 5. Do you want to hit? (y/n)',
    '\nYour score is 10. Do you want to hit? (y/n)'
  ], [], [
    'y',
    'n'
  ],
  [Card('Clubs', '2'), Card('Clubs', '3')],
  Card('Hearts', '5'),
  0),
  # A player hits, and busts
  ([
    '\nYour score is 20. Do you want to hit? (y/n)'
  ], [], [
    'y'
  ],
  [Card('Diamonds', '10'), Card('Diamonds', 'Queen')],
  Card('Clubs', '2'),
  2),
  # A player quits
  ([
    '\nYour score is 20. Do you want to hit? (y/n)'
  ], [], [
    'q'
  ],
  [Card('Diamonds', '10'), Card('Diamonds', 'Queen')],
  None,
  1),
])
def test_game_hit_player(prints, prompts, inputs, cards, new_card, expected):
  """
  A player can hit, stay or bust.
  """

  def test_print(message):
    _print = prints.pop(0)
    assert message == _print

  def test_prompt(message = ''):
    if len(prompts) > 0:
      _prompt = prompts.pop(0)
      assert message == _prompt
    return inputs.pop(0)

  game = Game(_print = test_print, _input = test_prompt)
  game.get_player().get_hand().set_cards(cards)
  actual = game.hit_player(new_card)
  assert actual == expected


@pytest.mark.parametrize('prints, prompts, inputs, cards, new_card, expected', [
  # Expected successes
  # A dealer stays
  (['Dealer score is 20'], [], [],
  [Card('Diamonds', '9'), Card('Diamonds', 'Ace')],
  None,
  0),
  # A dealer hits, then stays
  (['Dealer score is 18'], [], [],
  [Card('Diamonds', '9'), Card('Diamonds', '7')],
  Card('Clubs', '2'),
  0),
  # A dealer hits, then busts
  (['Dealer score is 26'], [], [],
  [Card('Diamonds', '9'), Card('Diamonds', '7')],
  Card('Clubs', '10'),
  3)
])
def test_game_hit_dealer(prints, prompts, inputs, cards, new_card, expected):
  """
  A dealer can hit, stay, or bust.
  """

  def test_print(message):
    _print = prints.pop(0)
    assert message == _print

  game = Game(_print = test_print)
  game.get_dealer().get_hand().set_cards(cards)
  actual = game.hit_dealer(new_card)
  assert actual == expected


@pytest.mark.parametrize('size, expected', [
  # Expected successes
  # 0 chips
  (0, False),
  # 1 chip
  (1, False),
  # 1000 chips
  (1000, False),
  # Over 1000 chips
  (1001, False),
  # Playable number of chips
  (500, True)
])
def test_game_play(size, expected):
  """
  Game ends when player has 0, 1, or 1000 or over chips.
  """

  game = Game()
  game.get_player().get_purse().set_size(size)
  actual = game.play()
  assert actual == expected
