import pytest

from src.card import Card
from src.pack import Pack


def test_pack_shuffle():
  """
  Pack shuffles cards.
  """

  def test_random(x, y):
    return x

  pack = Pack()

  unshuffled_pips = [card.get_pip() for card in pack.get_cards()]
  pip = unshuffled_pips.pop()
  unshuffled_pips.insert(0, pip)
  expected = unshuffled_pips

  pack.shuffle(test_random)
  shuffled_pips = [card.get_pip() for card in pack.get_cards()]
  actual = shuffled_pips 
  
  assert actual == expected


@pytest.mark.parametrize('cards', [
  # Expected successes
  # Full pack's cards
  (Pack().get_cards()),
  # Unfull pack's cards
  (Pack().get_cards()[:10])
])
def test_pack_shuffle_size(cards):
  """
  A full or unfull pack shuffles as a full pack.
  """

  pack = Pack()
  pack.set_cards(cards)
  pack.shuffle()
  assert len(pack.get_cards()) == 6 * 52


@pytest.mark.parametrize('card, expected', [
  # Expected successes
  # No card
  (None, Card('Clubs', '2')),
  # Selected card
  (Card('Spades', 'Ace'), Card('Spades', 'Ace'))
])
def test_pack_hit(card, expected):
  """
  Remove front card from pack.
  """

  pack = Pack()
  actual = pack.hit(card)
  assert actual.get_suit() == expected.get_suit()
  assert actual.get_pip() == expected.get_pip()
  assert actual.get_hidden() == expected.get_hidden()
