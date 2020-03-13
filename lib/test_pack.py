import pytest

from pack import Pack, _Deck, _Card


def test_deck_cards(deck):
  """
  Deck is made with right cards.
  """
  
  expected_cards = [_Card('Clubs', '2'), _Card('Spades', 'Ace')]
  actual_cards = [deck.cards[0], deck.cards[len(deck.cards) - 1]]

  for i in range(2):
    assert actual_cards[i].suit == expected_cards[i].suit
    assert actual_cards[i].pip == expected_cards[i].pip


def test_deck_size(deck):
  """
  Deck is made with right number of cards.
  """

  expected = 52
  actual = len(deck.cards)

  assert actual == expected


# Fixtures


@pytest.fixture
def deck():
  """
  Instance of _Deck.
  """

  return _Deck()
