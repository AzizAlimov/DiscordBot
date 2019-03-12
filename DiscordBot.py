#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 19:38:23 2018

@author: azuzialimov
"""

from pprint import pprint
import requests
import discord
import random

TOKEN = 'NTI0MDU2NTE2NzAyMTA5NzEx.DvinXA.KhdDPSrzsZwErmhyfD4vm2yl0BQ'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('!8ball'):
        possible_responses = [
                'That is a resounding no',
                'It is not looking likely',
                'Too hard to tell',
                'It is quite possible',
                'Definitely',
            ]
        
        msg = random.choice(possible_responses)
        await client.send_message(message.channel, msg)
        
        #Gives the current weather in vancouver
    if message.content.startswith('!weather'):
        #location = message.content[9,]
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Vancouver&APPID=e6aaca8265d6641552debcd4e62c2e8a')
        await client.send_message(message.channel, r.json())
        #await client.send_message(message.channel, weather)
        
        #Get the bot to say its name
    if message.content.startswith('!name'):
        msg = 'My name is Jacky, pleased to meet you.'
        await client.send_message(message.channel, msg)
        
        
        
        #Gives the current CAD to USD exchange rate
    if message.content.startswith('!ExchangeRate'):
        r = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=CAD&to_currency=USD&apikey=VTYLNCZ3EHQZKCTA')
        y = r.json()
        await client.send_message(message.channel, y)
        
        #Trying to modified the parsed string (Currently unsuccesfully)
        '''
        x = y.find("Realtime")
        #r = str(x)
        #await client.send_message(message.channel, r)
        #t = y[x:x+17]
        #t = "The CAD to USD exchange rate is currently " + y[x: x+17] + " CAD for every USD."
        await client.send_message(message.channel, t)
        '''

        

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
   


client.run(TOKEN)