import pytest

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


def test_pack_hit():
  """
  Remove front card from pack.
  """

  pack = Pack()

  expected = pack.get_cards()[0].get_pip()
  actual = pack.hit().get_pip()
  assert actual == expected
