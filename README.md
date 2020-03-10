# blackjack

# Project Pitch
"Play Blackjack against the computer, start with 50 chips and try to earn 200."

The project creates a space to learn software engineer fundamentals. Blackjack is a well-known card game so anyone can easily play. Writing a good workplan is hard but what the Blackjack project aims to do.

## MVP
1. Start a game of Blackjack against the computer through the CLI
2. Play rounds of Blackjack earning or losing chips at the end of each round
3. Win a game by reaching 200 chips, lose a game by reaching 0 chips

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
> Congratulations you reached 500 chips! You win!
> Come again soon
```
