#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 19:38:23 2018

@author: azuzialimov
"""

from discord.ext import commands
import FlaskServer
import socketio
import datetime
import json

with open("/Users/azuzialimov/config.json") as config_file:
    config = json.load(config_file)
TOKEN = config['token']
CHANNEL_ID = config['server']
sio = socketio.AsyncClient()

def get_prefix(client, message):
    
    prefixes = ['=', '==']
    
    if not message.guild:
        prefixes = ['==']
        
    return commands.when_mentioned_or(*prefixes)(client, message)


bot = commands.Bot(
        command_prefix = get_prefix,
        description='A bot used for tutorial',
        owner_id=config['owner_id'],
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