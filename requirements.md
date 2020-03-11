# Software Requirements

# Vision
"Play Blackjack against the computer, start with 200 chips and try to earn 1,000."

The project creates a space to learn software engineer fundamentals. Blackjack is a well-known card game so anyone can easily play. Writing a good workplan is hard but what the Blackjack project aims to do.

# Scope (In/Out)

## In
- A client can play Blackjack through their CLI
- A client can't raise an error with the program because the project will have good error handling
- A client will always see a display of the current state of their Blackjack game against the computer dealer
- A client can exit the program at any prompt

## Out
- The project will not make use of a database
- The project will remain in the CLI, e.g. and not become a web or desktop program

# MVP vs Stretch Goals

## MVP
1. Start a game of Blackjack against the computer through the CLI
2. Play rounds of Blackjack earning or losing chips at the end of each round
3. Win a game by reaching 1,000 chips, lose a game by reaching 0 chips

## Stretch
1. The game can be played multi-player

# Functional Requirements
1. Working CLI
2. Working monitor
3. Working keyboard

## Data Flow
All data will be local to the running CLI program

# Non-Functional Requirements
1. Security: Security will not be written for the project but is assumed for a sound working CLI
2. Memory: All data of the program will be stored in RAM and non-retrievable after the program ends because data will not be stored on a drive
