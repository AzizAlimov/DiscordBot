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
import FlaskServer
import socketio
import datetime
from cogs import basic


TOKEN = 'NTI0MDU2NTE2NzAyMTA5NzEx.DvinXA.KhdDPSrzsZwErmhyfD4vm2yl0BQ'
CHANNEL_ID = 524062208209190945
sio = socketio.AsyncClient()

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

cogs = ['cogs.basic']

#Run whenever the bot is turned on, connects the client to the server
@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    time = datetime.datetime.now()
    msg = "Logged in as Jacky at " + str(time.hour) + ":" + str(time.minute)
    await channel.send(msg)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for cog in cogs:
        bot.load_extension(cog)
    await sio.connect('http://localhost:8080')
    return

#Broadcasts a message to the server when connected
@sio.on('connect')
async def on_connect():
    channel = bot.get_channel(CHANNEL_ID)
    msg = "I'm connected!"
    await channel.send(msg)
    return

#Disconnects the bot
@sio.on('disconnect')
async def on_disconnect():
    channel = bot.get_channel(CHANNEL_ID)
    msg = "beep boop disconnecting"
    await channel.send(msg)
    return
    
@sio.on('message')
async def on_message(data):
    channel = bot.get_channel(CHANNEL_ID)
    msg = "I received a message"
    await channel.send(msg)
    return

@sio.on('subscription')
async def on_sub(data):
    return

@sio.on('live')
async def on_live(data):
    return

@sio.on('twitch')
async def on_twitch(message):
    channel = bot.get_channel(CHANNEL_ID)
    msg = "twitch worked"
    await channel.send(msg)
    return




FlaskServer.keep_alive()

bot.run(TOKEN)