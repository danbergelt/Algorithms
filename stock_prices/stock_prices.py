#!/usr/bin/python

import argparse
import math

def find_max_profit(prices):

  # instantiate a max difference (i.e. final answer) 
  # and a smallest number in list to perform comparisons
  maxDiff = -math.inf
  minNumber = prices[0]

  for i in range(0, len(prices) - 1):
    # if the current price in loop is less than the smallest number,
    # set that price to be the smallest number
    if prices[i] < minNumber:
      minNumber = prices[i]

    # if the price one slot ahead (to simulate a buy/sell) is greater than
    # the current max diff, that's the new max diff
    if prices[i + 1] - minNumber > maxDiff:
      maxDiff = prices[i + 1] - minNumber
  
  return maxDiff

  



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))