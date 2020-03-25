import pytest

# from pack import Pack, _Deck, _Card
from library.pack.pack import Pack, Card


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
  assert card.suit == suit
  assert card.pip == pip


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
  assert len(pack.cards) == 312
  assert len([card for card in pack.cards if card.suit == 'Clubs' and card.pip == 'Ace']) == 6
  assert len([card for card in pack.cards if card.suit == 'Hearts' and card.pip == '2']) == 6


# @pytest.mark.skip
# @pytest.mark.parametrize('card_holder, expected_cards', [
#   # Pack has expected cards
#   (Pack(), [_Card('Clubs', '2'), _Card('Spades', 'Ace')]),
#   # Deck has expected cards
#   (_Deck(), [_Card('Clubs', '2'), _Card('Spades', 'Ace')])
# ])
# def test_cards(card_holder, expected_cards):
#   """
#   Deck is made with right cards.
#   """
  
#   actual_cards = [card_holder.cards[0], card_holder.cards[len(card_holder.cards) - 1]]

#   for i in range(2):
#     assert actual_cards[i].suit == expected_cards[i].suit
#     assert actual_cards[i].pip == expected_cards[i].pip


# @pytest.mark.skip
# @pytest.mark.parametrize('card_holder, expected_size', [
#   # Pack has 6 * 52 cards
#   (Pack(), Pack._DECKS * _Deck._CARDS),
#   # Deck has 52 cards
#   (_Deck(), _Deck._CARDS)
# ])
# def test_cards_size(card_holder, expected_size):
#   """
#   Card holder is made with right number of cards.
#   """

#   expected = expected_size
#   actual = len(card_holder.cards)

#   assert actual == expected


def test_pack_shuffle():
  """
  Shuffle pack of cards.
  """

  def _random(start, end):
    return start

  pack = Pack()
  pack.shuffle(_random)

  expected_cards = [Card('Spades', 'Ace'), Card('Spades', 'King')]
  actual_cards = [pack.cards[0], pack.cards[len(pack.cards) - 1]]

  for i in range(2):
    assert actual_cards[i].suit == expected_cards[i].suit
    assert actual_cards[i].pip == expected_cards[i].pip


@pytest.mark.parametrize('card', [
  (Card('Clubs', 'Ace')),
])
def test_pack_hit(card):
  """
  Take a card from a pack.
  """

  pack = Pack()
  _card = pack.hit(card)
  assert len(pack.cards) == 311
  assert _card.suit == card.suit
  assert _card.pip == card.pip



# @pytest.mark.skip
# def test_str_card():
#   """
#   String representation of card is right.
#   """

#   card = _Card('Clubs', '2')

#   print(card.hidden)

#   expected = "('Clubs', '2')"
#   actual = str(card)
#   assert actual == expected


# Fixtures


# @pytest.fixture
# def pack():
#   """
#   Instance of Pack.
#   """

#   return Pack()


# @pytest.fixture
# def deck():
#   """
#   Instance of _Deck.
#   """

#   return _Deck()
