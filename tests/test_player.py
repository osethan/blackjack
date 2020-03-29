import pytest

from src.card import Card
from src.seat import Player


def test_player_tie():
  """
  A tie means a player's bet returns to their purse.
  """

  bet = 100
  purse = 200

  player = Player()
  player.get_hand().set_cards([Card('Clubs', '2'), Card('Hearts', '3')])
  player.get_bet().set_size(bet)
  player.get_purse().set_size(player.get_purse().get_size() - player.get_bet().get_size())
  player.tie()
  actual_bet = player.get_bet().get_size()
  actual_purse = player.get_purse().get_size()
  
  assert actual_bet == 0
  assert actual_purse == purse
