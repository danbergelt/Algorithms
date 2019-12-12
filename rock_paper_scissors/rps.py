#!/usr/bin/python

import sys

def rock_paper_scissors(n):

  # potential moves in rps
  moves = ["rock", "paper", "scissors"]
  
  # container for full list of plays
  games = []

  # recursive helper function to find combinations of plays
  def helper(gamesPlayed, rounds):
    nonlocal moves
    nonlocal games

    # base case - exits the loop if the rounds in this iteration have exhausted
    if (rounds == 0):
      games.append(gamesPlayed)
      return

    for move in moves:
      helper(gamesPlayed + [move], rounds - 1)
  
    """
      e.g. n == 2
      layer one:      ['r'],           ['p'],              ['s']
      layer two:        ^                ^                   ^
                    [r] [p] [s]     [r] [p] [s]         [r] [p] [s] 
    """  
  helper([], n)

  return games

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')