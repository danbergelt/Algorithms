#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# preset cache with limits (stops at 2 since eating_cookies(3) == 4)
def eating_cookies(n, cache={0:1, 1:1, 2:2}):
  # if n is not in cache, recursively call eating_cookies to generate permutation for each amount of cookies at once
  if n not in cache:
    cache[n] = eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
  return cache[n]

"""
e.g. fn(5) == 13 or 2 + 4 + 7

2 + 3           +            4
   ^^^                      ^^^
(1 + 1 + 2 = 4)         (1 + 2 + 3 = 7)
                                ^^^
                          (1 + 2 + 2 = 4)
"""

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')