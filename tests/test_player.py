import pytest

from src.card import Card
from src.seat import Player


@pytest.mark.parametrize('cards, expected', [
  # Expected successes
  # A player wins
  ([Card('Clubs', '10'), Card('Hearts', '9')], 300),
  # Edge cases
  # A player wins by natural
  ([Card('Clubs', 'Ace'), Card('Hearts', 'Jack')], 350)
])
def test_player_win(cards, expected):
  """
  A win means a player wins their bet.
  """

  player = Player()
  player.get_hand().set_cards(cards)
  bet = 100
  player.make_bet(bet)

  player.win()
  expected_bet_size = 0
  expected_purse_size = expected
  actual_bet_size = player.get_bet().get_size()
  actual_purse_size = player.get_purse().get_size()

  assert actual_bet_size == expected_bet_size
  assert actual_purse_size == expected_purse_size


def test_player_loss(bet_player):
  """
  A loss means a player loses their bet.
  """

  bet_player.loss()
  expected_bet_size = 0
  expected_purse_size = 100
  actual_bet_size = bet_player.get_bet().get_size()
  actual_purse_size = bet_player.get_purse().get_size()

  assert actual_bet_size == expected_bet_size
  assert actual_purse_size == expected_purse_size


def test_player_tie(bet_player):
  """
  A tie means a player's bet returns to their purse.
  """

  bet_player.tie()
  expected_bet_size = 0
  expected_purse_size = 200
  actual_bet_size = bet_player.get_bet().get_size()
  actual_purse_size = bet_player.get_purse().get_size()
  
  assert actual_bet_size == expected_bet_size
  assert actual_purse_size == expected_purse_size


# Fixutres


@pytest.fixture
def bet_player():
  """
  A player who's made a bet.
  """

  player = Player()
  player.get_hand().set_cards([Card('Clubs', '2'), Card('Hearts', '3')])
  bet = 100
  player.make_bet(bet)
  
  return player
