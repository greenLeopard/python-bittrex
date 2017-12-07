#!/usr/bin/env python3
"""BotTest using bittrex.py.

This program gets the balance of your portfolio.
Reviews the price of Bitcoin, Bitcoin Cash, Litecoin, Ether, Omisego.
Makes a suggestion for a new portfolio rebalance.
"""
from bittrex import Bittrex

import os

import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from helpers.exchange_helpers import BittrexHelpers

DEBUG = True
count = 10
# Get these from https://bittrex.com/Account/ManageApiKey
exchange = None  # 'Bittrex'
# Get these from https://bittrex.com/Account/ManageApiKey
if(exchange == 'Bittrex'):
    bh = BittrexHelpers()
    bh.get_account_data()
    key = bh.get_key()
    secret = bh.get_secret()
else:
    key = 'key'
    secret = 'secret'

api = Bittrex(key, secret)


# Market coins to assess
currencies = ['BTC', 'BCC', 'LTC', 'ETH', 'OMG']
market = '{0}-{1}'.format(currencies[0], currencies[1])
if (DEBUG):
    print('DEBUG: Market: {}, type {}'.format(market, type(market)))

# public api methods
result = api.getmarkets()
if (DEBUG):
    print('DEBUG: getmarkets (size {})'.format(len(result)))
    # print(result)
    for res in result[:count]:
        print('Market: {0:>10}, MinTradeSize: {1:15.4f}'.format(
              res['MarketName'], res['MinTradeSize']))

# result = api.getcurrencies()
# if (DEBUG):
# 	print('DEBUG: getcurrencies')
# 	print(result)

# result = api.getticker(market)
# if (DEBUG):
# 	print('DEBUG: getticker')
# 	print(result)

# result = api.getmarketsummaries()
# if (DEBUG):
# 	print('DEBUG: getmarketsummaries')
# 	# print(result)
# 	for marketSummary in result:
# 		print('Market: {0:>10}, Volume: {1:15.4f}'.format(
#             marketSummary['MarketName'], marketSummary['Volume']))

# result = api.getmarketsummary(market)
# if (DEBUG):
# 	print('DEBUG: getmarketsummary')
# 	print(result)

# result = api.getorderbook(market, 'both')
# if (DEBUG):
# 	print('DEBUG: getorderbook')
# 	print(result)

result = api.getmarkethistory(market)
if (DEBUG):
    print('DEBUG: marketHistory {} size {}'.format(market, len(result)))
    for marketHistory in result[:count]:
        print('Qty: {0:8.4f}, Price: {1:10.5f}, Type: {2:>6}, Time: {3}'.
              format(marketHistory['Quantity'], marketHistory['Price'],
                     marketHistory['OrderType'], marketHistory['TimeStamp']))

# market: getopenorders

# account: getbalances
