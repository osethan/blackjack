import pytest

from pack import Pack, _Deck, _Card


@pytest.mark.parametrize('card_holder, expected_cards', [
  # Pack has expected cards
  (Pack(), [_Card('Clubs', '2'), _Card('Spades', 'Ace')]),
  # Deck has expected cards
  (_Deck(), [_Card('Clubs', '2'), _Card('Spades', 'Ace')])
])
def test_cards(card_holder, expected_cards):
  """
  Deck is made with right cards.
  """
  
  actual_cards = [card_holder.cards[0], card_holder.cards[len(card_holder.cards) - 1]]

  for i in range(2):
    assert actual_cards[i].suit == expected_cards[i].suit
    assert actual_cards[i].pip == expected_cards[i].pip


@pytest.mark.parametrize('card_holder, expected_size', [
  # Pack has 6 * 52 cards
  (Pack(), Pack._DECKS * _Deck._CARDS),
  # Deck has 52 cards
  (_Deck(), _Deck._CARDS)
])
def test_cards_size(card_holder, expected_size):
  """
  Card holder is made with right number of cards.
  """

  expected = expected_size
  actual = len(card_holder.cards)

  assert actual == expected


def test_pack_shuffle(pack):
  """
  Pack shuffles cards to random state.
  """

  def _random(start, end):
    return start

  pack.shuffle(_random)

  expected_cards = [_Card('Spades', 'Ace'), _Card('Spades', 'King')]
  actual_cards = [pack.cards[0], pack.cards[len(pack.cards) - 1]]

  for i in range(2):
    assert actual_cards[i].suit == expected_cards[i].suit
    assert actual_cards[i].pip == expected_cards[i].pip


# Fixtures


@pytest.fixture
def pack():
  """
  Instance of Pack.
  """

  return Pack()


@pytest.fixture
def deck():
  """
  Instance of _Deck.
  """

  return _Deck()
