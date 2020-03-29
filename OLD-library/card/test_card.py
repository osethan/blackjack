import pytest

from library.card.card import Pack, Card


@pytest.mark.parametrize('suit, pip', [
  # Expected successes
  ('Clubs', 'Ace'),
  ('Hearts', '2'),
])
def test_create_card(suit, pip):
  """
  Card can be made.
  """

  card = Card(suit, pip)
  assert card
  assert card.get_suit() == suit
  assert card.get_pip() == pip


@pytest.mark.skip
@pytest.mark.parametrize('suit, pip', [
  # Expected failures
  ('Rocks', 'Ace'),
  ('Hearts', 'Paper'),
])
def test_not_create_card(suit, pip):
  """
  Card fails to be made.
  """

  card = Card(suit, pip)


def test_create_pack():
  """
  Pack can be made.
  """

  pack = Pack()
  assert len(pack.get_cards()) == 312
  assert len([card for card in pack.get_cards() if card.get_suit() == 'Clubs' and card.get_pip() == 'Ace']) == 6
  assert len([card for card in pack.get_cards() if card.get_suit() == 'Hearts' and card.get_pip() == '2']) == 6


def test_pack_shuffle():
  """
  Shuffle pack of cards.
  """

  def _random(start, end):
    return start

  pack = Pack()
  pack.shuffle(_random)

  expected_cards = [Card('Spades', 'Ace'), Card('Spades', 'King')]
  actual_cards = [pack.get_cards()[0], pack.get_cards()[len(pack.get_cards()) - 1]]

  for i in range(2):
    assert actual_cards[i].get_suit() == expected_cards[i].get_suit()
    assert actual_cards[i].get_pip() == expected_cards[i].get_pip()


@pytest.mark.parametrize('card', [
  (Card('Clubs', 'Ace')),
])
def test_pack_hit(card):
  """
  Take a card from a pack.
  """

  pack = Pack()
  _card = pack.hit(card)
  assert len(pack.get_cards()) == 311
  assert _card.get_suit() == card.get_suit()
  assert _card.get_pip() == card.get_pip()
