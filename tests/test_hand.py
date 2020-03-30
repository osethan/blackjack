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
  ([Card('Spades', 'Ace'), Card('Hearts', 'Ace')], False),
  ([Card('Spades', 'Ace'), Card('Hearts', 'Jack'), Card('Diamonds', '2')], False)
])
def test_hand_natural(cards, expected):
  """
  A hand is a natural.
  """

  hand = Hand()
  hand.set_cards(cards)
  actual = hand.natural()
  assert actual == expected


@pytest.mark.parametrize('cards, expected', [
  # Expected successes
  # Two cards, no ace
  ([Card('Clubs', '2'), Card('Clubs', '3')], [5]),
  # Two cards, one ace
  ([Card('Clubs', '2'), Card('Hearts', 'Ace')], [3, 13]),
  # Two cards, two ace
  ([Card('Clubs', 'Ace'), Card('Hearts', 'Ace')], [2, 12, 22]),
  # Four cards, no ace
  ([Card('Clubs', '2'), Card('Diamonds', '3'), Card('Hearts', '4'), Card('Spades', '5')], [14]),
  # Four cards, one ace
  ([Card('Clubs', '2'), Card('Diamonds', '3'), Card('Hearts', '4'), Card('Spades', 'Ace')], [10, 20]),
  # Four cards, two ace
  ([Card('Clubs', '2'), Card('Diamonds', '3'), Card('Hearts', 'Ace'), Card('Spades', 'Ace')], [7, 17, 27]),
  # Four cards, three ace
  ([Card('Clubs', '2'), Card('Diamonds', 'Ace'), Card('Hearts', 'Ace'), Card('Spades', 'Ace')], [5, 15, 25, 35]),
  # Four cards, four ace
  ([Card('Clubs', 'Ace'), Card('Diamonds', 'Ace'), Card('Hearts', 'Ace'), Card('Spades', 'Ace')], [4, 14, 24, 34, 44])
])
def test_hand_set_scores(cards, expected):
  """
  A hand's cards score correctly.
  """
  
  hand = Hand()
  hand.set_cards(cards)
  actual = hand.get_scores()
  assert actual == expected


@pytest.mark.parametrize('cards, expected', [
  # Expected successes
  # One score
  ([Card('Clubs', '2'), Card('Diamonds', '3'), Card('Hearts', '4'), Card('Spades', '5')], 14),
  # Two scores
  ([Card('Clubs', '2'), Card('Diamonds', '3'), Card('Hearts', '4'), Card('Spades', 'Ace')], 20),
  # Three scores
  ([Card('Clubs', '2'), Card('Diamonds', '3'), Card('Hearts', 'Ace'), Card('Spades', 'Ace')], 17),
  # Four scores
  ([Card('Clubs', '2'), Card('Diamonds', 'Ace'), Card('Hearts', 'Ace'), Card('Spades', 'Ace')], 15),
])
def test_hand_get_score(cards, expected):
  """
  A hand's best score.
  """
  
  hand = Hand()
  hand.set_cards(cards)
  actual = hand.score()
  assert actual == expected
