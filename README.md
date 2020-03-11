# blackjack

# Project Pitch
"Play Blackjack against the computer, start with 200 chips and try to earn 1,000."

The project creates a space to learn software engineer fundamentals. Blackjack is a well-known card game so anyone can easily play. Writing a good workplan is hard but what the Blackjack project aims to do.

## MVP
1. Start a game of Blackjack against the computer through the CLI
2. Play rounds of Blackjack earning or losing chips at the end of each round
3. Win a game by reaching 1,000 chips, lose a game by reaching 0 chips

# Game Rules
Details for how to play Blackjack can be found at the Bicylce Cards [website](https://bicyclecards.com/how-to-play/blackjack/)

# Wireframes
Player can say yes or no to starting a game
```
> Welcome to Blackjack! Do you want to play?
> (client) No
> Come again soon

> Welcome to Blackjack! Do you want to play?
> (client) Yes
> ...
```

At start of hand player will be prompted for bet
```
> You have 50 chips. What is your bet?
> (client) 10
>
> Player: Client
  Hand: (Hearts, 10), (Diamonds, 2)
  Bet: 10

  Dealer: Computer
  Hand: (Spades, 5), (*, *)
```

After cards first two cards dealt player will be prompted for action
```
> What do you want to do?
> hit (h)
  stay (s)
  split pairs (sp)
  double down (dd)
  insurance (i)
```

In case of player hit their new dealt card will be shown
```
> Player: Client
  Hand: (Hearts, 10), (Diamonds, 2), (Clubs, 9)
  Bet: 10
  ...
```

In case of player split pairs new hands will be created and dealt
```
> Player: Client
  Left Hand: (Hearts, Jack)
  Right Hand: (Diamonds, Jack)
  Bet: 10
  ...
```

In case of player double down player will be dealt one face down card and bet will double
```
> Player: Client
  Hand: (Spades, 4), (Clubs, 5), (*, *)
  Bet: 20
  ...
```

In case of player insurance value will be shown in player stats
```
> Player: Client
  Hand: (Spades, 4), (Hearts, Queen)
  Bet: 10
  Insurance: 5
  ...
```

If player bust they're told and next hand starts if player still has chips
```
> You bust
  ...
```

When player's turn is over dealer's turn will be calculated, shown and next hand starts if game not over
```
  ...
> Dealer: Computer
  Hand: (Spades, 9), (Hearts, 8)
>
> Dealer loss
  ...
```

At any prompt the client can quit the game
```
> quit (q)
$
```

The player is told when they lose the game
```
> Sorry you lost all your chips
> Come again soon
```

The player is told when they win the game
```
> Congratulations you reached 1,000 chips! You win!
> Come again soon
```

# User Stories
**(1.)** As a user, I want to be told when the game has started or ended

## Feature Tasks
- [ ] Have a display show before the first hand of a game
- [ ] Have a display show after the hand the player reaches 0 or 1,000 chips

## Acceptance Tests
- [ ] Unit test: Does the display show?
- [ ] Integration test: Does the display show at the right time?

## Time Estimate
"Extra small" taking 0 - 2 hours

**(2.)** As a user, I want prompts and displays to be simple

## Feature Tasks
- [ ] Remove complexity from explanation of displays and prompts

## Acceptance Tests
- [ ] Unit test: The simple display or prompt displays
- [ ] Unit test: The simple prompt handles messy input
- [ ] Integration test: Do the simple display and prompts show the right time?

## Time Estimate
"Small" taking 2 - 4 hours

**(3.)** As a user, I want all Blackjack game rules available

## Feature Tasks

### Pack
- [ ] 6 decks used in pack with discard pile and reshuffle in last 60 - 75 cards

### Bet
- [ ] Player can't bet less than $2 or more than $500

### Deal
- [ ] Hands dealt clockwise dealer taking last card and last card dealt is face down

### Naturals
- [ ] Naturals should be handled right

### Play
- [ ] Player can hit for another card
- [ ] Player can score with soft hands
- [ ] Player can stay not taking another card

### Dealer Play
- [ ] Dealer play is automated

### Splitting Pair
- [ ] Player can split pair making two hands

### Doubling Down
- [ ] Player can double down doubling bet and taking one more card

### Insurance
- [ ] Player can take insurance from dealer hand

### Settlement
- [ ] Stand-off should be handled right

## Acceptance Tests

### Deal
- [ ] Unit test: Player's cards and score increment when player hits
- [ ] Unit test: Player's next card is top card of pack

### Play
- [ ] Unit test: Player's score can be soft hand without breaking scoring rules
- [ ] Unit test: Turn changes when player wants to stay

### Splitting Pair
- [ ] Unit test: Player gets two hands when they split pair

### Doublig Down
- [ ] Unit test: Player takes one card from top of deck face down and doubles bet
- [ ] Unit test: Player's double down is settled with dealer after dealer plays

### Insurance
- [ ] Unit test: Player can take insurance which is up to half of bet when dealer's face up card is an ace
- [ ] Unit test: Dealer has Natural in case of insurance taken
- [ ] Unit test: Dealer doesn't have Natural in case of insurance taken

### Reshuffling
- [ ] Unit test: Pack is shuffled in last 60 - 75 cards

### Settlemnt
- [ ] Unit test: Player wins hand by dealer bust
- [ ] Unit test: Player wins hand by scoring higher than dealer
- [ ] Unit test: Player loses hand by busting
- [ ] Unit test: Player loses hand by scoring less than dealer
- [ ] Unit test: Player wins with Natural
- [ ] Unit test: Player and dealer stand-off
- [ ] Unit test: Player wins/loses with split pair
- [ ] Unit test: Player wins/loses with double down
- [ ] Unit test: Player wins/loses with insurance

## Time Estimate
"Large" taking 8 - 12 hours

**(4.)** As a user, I don't want to mess up the game answering prompts with unexpected values

## Feature Tasks
- [ ] Player can only bet with integer number of chips within minimum and maximum chip bet range ($2 - $500) and not more than what they have
- [ ] Player can only respond to prompts with text expected for prompt response

## Acceptance Tests
- [ ] Unit test: Player's chips bet is integer, not greater than what they have and within minimum and maximum chip bet range
- [ ] Unit test: Player action fits options of action

## Time Estimate
"Extra small" taking 0 - 2 hours

**(5.)** As a user, I want to be able to leave the game anytime

## Feature Tasks
- [ ] Player can quit game at any time

## Acceptance Tests
- [ ] Unit test: Player quitting game closes game gracefully

## Time Estimate
"Small" taking 0 - 2 hours
