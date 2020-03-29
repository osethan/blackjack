import pytest

from src.card import Card
from src.hand import Hand


@pytest.mark.parametrize('cards, expected', [
  # Expected successes
  ([Card('Clubs', 'Ace'), Card('Hearts', 'Jack')], True),
  ([Card('Hearts', 'King'), Card('Clubs', 'Ace')], True),
  # Expected failures
  ([Card('Clubs', '2'), Card('Hearts', '3')], False),
  ([Card('Diamonds', '10'), Card('Diamonds', 'Queen')], False),
  ([Card('Spades', 'Ace'), Card('Hearts', 'Ace')], False)
])
def test_hand_natural(cards, expected):
  """
  A hand is a natural.
  """

  hand = Hand()
  hand.set_cards(cards)
  actual = hand.natural()
  assert actual == expected
