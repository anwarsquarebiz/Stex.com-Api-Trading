#These are the stex api libraries
from stex_client.public import Public
from stex_client.private import Private

#Libraries to perform oprations

import requests
import time
from random import * 
import random

#Calls for public class from stex_client.public import Public
public = Public()

#Shows the list of pairs in LTC
#This will help you know your coin pair ID
listofpairs = public.currency_pairs_list('LTC')

#Shows the list of pairs in public order book for yourcoint as per coin pair ID eg.
your_coin_order_book = public.orderbook_by_currency_pair_id(128, {'limit_asks': 1, 'limit_bids': 1})

#Pulls the ask price and bid price from the dictionary of your_coin_order_book  
ask_price = (((your_coin_order_book['data'])['ask'])[0])['price']
bid_price = (((your_coin_order_book['data'])['bid'])[0])['price']

#This class of private will help you connect with your wallet
private = Private({
    'client': {
        'id': 'obtain from stex website',
        'secret': 'obtain from stex website'
    },
    'tokenObject': {
        'access_token': 'Obtain with the help of postman website with the help of id and secret',
        'refresh_token': 'Obtain with the help of postman website with the help of id and secret',
    },
    'accessTokenUrl': 'https://api3.stex.com/oauth/token',
    'scope': 'trade profile push',
})

#These functions will help you create an order in order from your account
#Read this to understand the parameters
#from (3, 'BUY', randomNum, randomPrice) 3 is the your pair id which is unique for your coins pair. Eg. BTC/USD is pair id 1
#randomNum is a varaible which will hold a function to define random number of coins to buy and sell
#randomPrice is a variable which will hold a function to define random price to buy and sell

#Function to buy coins
def buyYourCoin():
    private.create_trading_orders_by_pair_id(3, 'BUY', randomNum, randomPrice)

#Function to sell coins
def sellYourCoin():
    private.create_trading_orders_by_pair_id(3, 'SELL', randomNum, randomPrice)

#Creates a random number between 2 numbers change value of 337 and 1350 as per your desired number of coins to be traded in each trade
randomNum = randint(337, 1350)

#Calculate the range for self trading
#float is used to convert the number strings from dictory to float
#New ask price and new bid price will make use of gap between orderbook and only trade between them
new_ask_price = float(ask_price) - 0.00000001
new_bid_price = float(bid_price) + 0.00000001

#Make use of random library to generate random numbers
secure_random = random.SystemRandom()
randomPrice = secure_random.uniform(new_bid_price, new_ask_price)

#Since the random numbers are now generated below lines will buy and sell as per those random numbers
sellYourCoin()
time.sleep(2)
buyYourCoin()

#This will print the result
print("Ran ", count, " times")
