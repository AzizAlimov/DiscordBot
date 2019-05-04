#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 19:38:23 2018

@author: azuzialimov
"""

from pprint import pprint
from discord.ext import commands
import requests
import discord
import random
import FlaskServer



TOKEN = 'NTI0MDU2NTE2NzAyMTA5NzEx.DvinXA.KhdDPSrzsZwErmhyfD4vm2yl0BQ'

def get_prefix(client, message):
    
    prefixes = ['=', '==']
    
    if not message.guild:
        prefixes = ['==']
        
    return commands.when_mentioned_or(*prefixes)(client, message)

client = discord.Client()

bot = commands.Bot(
        command_prefix = get_prefix,
        description='A bot used for tutorial',
        owner_id=110505715809947648,
        case_insensitive=True
)

'''
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
        #Gives the current CAD to USD exchange rate
    if message.content.startswith('!ExchangeRate'):
        r = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=CAD&to_currency=USD&apikey=VTYLNCZ3EHQZKCTA')
        y = r.json()
        await client.send_message(message.channel, y)
        
        #Trying to modified the parsed string (Currently unsuccesfully)

        x = y.find("Realtime")
        #r = str(x)
        #await client.send_message(message.channel, r)
        #t = y[x:x+17]
        #t = "The CAD to USD exchange rate is currently " + y[x: x+17] + " CAD for every USD."
        await client.send_message(message.channel, t)
'''
        




cogs = ['cogs.basic', 'cogs.embed']

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for cog in cogs:
        bot.load_extension(cog)
    return
    
FlaskServer.keep_alive()
   


bot.run(TOKEN)