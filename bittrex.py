#!/usr/bin/env python3
"""Bittrex Module.

This is a module of helper functions to access the Bittrex API
using Python.

Requires Python 3.x
"""
# import urllib
# import urllib2
import hashlib
import hmac
import json
import time
import urllib.request
from urllib.parse import urlencode


class Bittrex(object):
    """Bittrex class object.

    The bittrex API methods are grouped into: public, market, and account
    methods. Public methods do not require keys, however market and account
    methods require a Bitrex public and private key pair.

    The Bittrex python class converts python style queries into API url
    queries and returns the result in JSON format.
    """

    def __init__(self, key, secret):
        """__init__ method for bittrex class.

        Define pubic and private key. Group API methods as Public, Market,
        or Account.
        """
        self.key = key
        self.secret = secret
        self.public = ['getmarkets', 'getcurrencies', 'getticker',
                       'getmarketsummaries', 'getmarketsummary',
                       'getorderbook', 'getmarkethistory']
        self.market = ['buylimit', 'buymarket', 'selllimit', 'sellmarket',
                       'cancel', 'getopenorders']
        self.account = ['getbalances', 'getbalance', 'getdepositaddress',
                        'withdraw', 'getorder', 'getorderhistory',
                        'getwithdrawalhistory', 'getdeposithistory']

    def query(self, method, values={}):
        """Create URL for API method call and return bittrex response."""
        if method in self.public:
            url = 'https://bittrex.com/api/v1.1/public/'
        elif method in self.market:
            url = 'https://bittrex.com/api/v1.1/market/'
        elif method in self.account:
            url = 'https://bittrex.com/api/v1.1/account/'
        else:
            return 'Something went wrong, sorry.'

        url += method + '?' + urlencode(values)

        if method not in self.public:
            url += '&apikey=' + self.key
            url += '&nonce=' + str(int(time.time()))
            signature = hmac.new(bytearray(self.secret.encode('UTF-8')),
                                 url.encode('UTF-8'),
                                 hashlib.sha512).hexdigest()
            headers = {'apisign': signature}
        else:
            headers = {}

        req = urllib.request.Request(url, headers=headers)
        response = json.loads(urllib.request.urlopen(req).read().
                              decode('utf-8'))

        if response["success"]:
            return response["result"]
        else:
            return response["message"]

    def getmarkets(self):
        """Get all open and available trading markets at Bittrex.

        Other meta data: MarketCurrency, BaseCurrency, MarketCurrencyLong,
        BaseCurrencyLong, MinTradeSize, MarketName, IsActive, Created
        Public method.
        """
        return self.query('getmarkets')

    def getcurrencies(self):
        """Do what(?) returns what. Public method."""
        return self.query('getcurrencies')

    def getticker(self, market):
        """Do what(?) returns what. Public method."""
        return self.query('getticker', {'market': market})

    def getmarketsummaries(self):
        """Do what(?) returns what. Public method."""
        return self.query('getmarketsummaries')

    def getmarketsummary(self, market):
        """Do what(?) returns what. Public method."""
        return self.query('getmarketsummary', {'market': market})

    def getorderbook(self, market, type):
        """Do what(?) returns what. Public method.

        Also, I have removed obsolete depth parameter from this method.
        """
        return self.query('getorderbook', {'market': market, 'type': type})

    def getmarkethistory(self, market):
        """Do what(?) returns what. Public method."""
        return self.query('getmarkethistory', {'market': market})

    def buylimit(self, market, quantity, rate):
        """Do what(?) returns what. Market method."""
        return self.query('buylimit', {'market': market,
                          'quantity': quantity, 'rate': rate})

    def buymarket(self, market, quantity):
        """Do what(?) returns what. Market method."""
        return self.query('buymarket', {'market': market,
                          'quantity': quantity})

    def selllimit(self, market, quantity, rate):
        """Do what(?) returns what. Market method."""
        return self.query('selllimit', {'market': market,
                          'quantity': quantity, 'rate': rate})

    def sellmarket(self, market, quantity):
        """Do what(?) returns what. Market method."""
        return self.query('sellmarket', {'market': market,
                          'quantity': quantity})

    def cancel(self, uuid):
        """Do what(?) returns what. Market method."""
        return self.query('cancel', {'uuid': uuid})

    def getopenorders(self, market):
        """Do what(?) returns what. Market method."""
        return self.query('getopenorders', {'market': market})

    def getbalances(self):
        """Do what(?) returns what. Account method."""
        return self.query('getbalances')

    def getbalance(self, currency):
        """Do what(?) returns what.Account method."""
        return self.query('getbalance', {'currency': currency})

    def getdepositaddress(self, currency):
        """Do what(?) returns what. Account method."""
        return self.query('getdepositaddress', {'currency': currency})

    def withdraw(self, currency, quantity, address):
        """Do what(?) returns what. Account method."""
        return self.query('withdraw', {'currency': currency,
                          'quantity': quantity, 'address': address})

    def getorder(self, uuid):
        """Do what(?) returns what. Account method."""
        return self.query('getorder', {'uuid': uuid})

    def getorderhistory(self, market, count):
        """Do what(?) returns what. Account method."""
        return self.query('getorderhistory', {'market': market,
                          'count': count})

    def getwithdrawalhistory(self, currency, count):
        """Do what(?) returns what. Account method."""
        return self.query('getwithdrawalhistory', {'currency': currency,
                          'count': count})

    def getdeposithistory(self, currency, count):
        """Do what(?) returns what. Account method."""
        return self.query('getdeposithistory', {'currency': currency,
                          'count': count})
