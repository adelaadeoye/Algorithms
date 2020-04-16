#!/usr/bin/python
import sys

def rock_paper_scissors(n):
  choices = ['rock', 'paper', 'scissors']

  def possibilities(perm, n):
    if n == 0: #base case
      return perm
    permutations = []
    for arr in perm:
      for move in choices:
        permutations.append([*arr, move])
    return possibilities(permutations, n - 1) # move towards base case
  return possibilities([[]], n)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')