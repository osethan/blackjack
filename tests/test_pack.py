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


def test_pack_hit():
  """
  Remove front card from pack.
  """

  pack = Pack()

  expected = pack.get_cards()[0].get_pip()
  actual = pack.hit().get_pip()
  assert actual == expected
