#!/usr/bin/python

import argparse

def find_max_profit(prices):
  profit=[]
  profit_per_stock=[]
  for i in range(len(prices)):
    for j in range(i+1,len(prices)):
       profit.append(prices[j]-prices[i])
    profit_per_stock.append(max(profit))
  return(max(profit_per_stock))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))