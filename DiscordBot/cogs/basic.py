#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 18:15:32 2019

@author: azuzialimov
"""

from discord.ext import commands
from datetime import datetime as d
from flask import request
import random
import requests
import traceback


# New - The Cog class must extend the commands.Cog class
class Basic(commands.Cog):
    
    
    def __init__(self, bot):
        self.bot = bot
        
    # Define a new command
    @commands.command(
        name='ping',
        description='The ping command',
        aliases=['p']
    )
    async def ping_command(self, ctx):
        start = d.timestamp(d.now())
    	# Gets the timestamp when the command was used

        msg = await ctx.send(content='Pinging')
    	# Sends a message to the user in the channel the message with the command was received.
    	# Notifies the user that pinging has started

        await msg.edit(content=f'Pong!\nOne message round-trip took {( d.timestamp( d.now() ) - start ) * 1000 }ms.')
    	# Ping completed and round-trip duration show in ms
    	# Since it takes a while to send the messages
    	# it will calculate how much time it takes to edit an message.
    	# It depends usually on your internet connection speed
        return
    
    @commands.command(
            name='repeat',
            description='The repeat command',
            aliases=['parrot'],
            usage='<text>'
    )
    async def repeat_command(self, ctx):
        msg = ctx.message.content
        
        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used) + len(alias_used):]
        
        if text == '' or text == ' ':
            await ctx.send(content = 'Error: No text specificed')
            
            pass
        
        else:
            await ctx.send(content = f"**{text}**")
            # Repeats your message back to you
            pass
        
        return
    
    
    @commands.command(
            name='8ball',
            description='Magic 8ball will tell your future',
            aliases=['eightball']
    )
    async def eightball_command(self, ctx):
        possible_responses = [
                'That is a resounding no',
                'It is not looking likely',
                'Too hard to tell',
                'It is quite possible',
                'Definitely',
            ]
        
        msg = random.choice(possible_responses)
        await ctx.send(content = f"**{msg}**")
        return
    
    @commands.command(
            name = 'weather',
            description='Current weather report of vancouver'
            )
    async def weather_command(self, ctx):
    
        msg = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Vancouver&APPID=e6aaca8265d6641552debcd4e62c2e8a')
        temp = float(msg.json().get('main').get('temp')) - 273.15
                   
        msg = "It's all " + msg.json().get('weather')[0].get('description') +\
        " today! The current temperatue is " + str(temp) + " degrees celsius."
        
        await ctx.send(content = msg)
        
    @commands.command(
            name = 'name',
            description='Returns the name of the bot'
            )
    async def name_command(self, ctx):
        msg = 'My name is Jacky, nice to meet you.'
        await ctx.send(content = msg)
        
        
    @commands.command(
            name = 'subscribe',
            description='Subscribes to a twitch streamer'
            )
    async def subscribe_command(self, ctx):
        try:
            
            postURI = 'https://api.twitch.tv/helix/webhooks/hub'
            payload = {"hub.mode":"subscribe",
           "hub.topic":"https://api.twitch.tv/helix/streams?login=imaqtpie",
           "hub.callback":"http://localhost/8080",
           "hub.lease_seconds":"864000"
           }
            clientID = {'Client-ID':'1xulrvwog4x8hxk1xaje7k17yructl'}
            await ctx.send(content = "worked")
            r = request.post(postURI, headers=clientID, params=payload)
            await ctx.send(content = "Succesfully subscribed!")
            await ctx.send(r.json())
        
        except Exception as e:
            traceback.print_exc()
            await ctx.send(content = e)
            
    @commands.command(
            name = 'getclientid',
            description='Gets the client id'
            )
    async def getclient_command(self, ctx):
        try:
            postURI = 'https://api.twitch.tv/helix/users?login=imaqtpie'
            clientID = {'Client-ID':'1xulrvwog4x8hxk1xaje7k17yructl'}
            await ctx.send(content = "checkpoint 1")
            r = request.get(postURI, headers=clientID)
            await ctx.send(content = "checkpoint 2")
            await ctx.send(r.json())
            
        except Exception as e:
            traceback.print_exc()
            await ctx.send(content = e)
        '''
    @commands.command(
            name = 'disconnect',
            description='disconnects the bot'
            )
    async def disconnect_command(self, ctx):
        Main.disconnect()

    @commands.command(
            name = 'twitch',
            description = 'Subscribes to a twitch event'
            )
    
    async def subscribe_command(self, ctx):
        headers = {'Authorization': 'Bearer {0}'.format(get_twitch_api_token()['access_token'])
        param_data = { 'hub.mode': 'subscribe',
                      'hub.topic':'https://api.twitch.tv/helix/streams?user_id={0}'.format('XXXXX'),
                      'hub.callback': 'http://my-endpoint-server.net/1.0/foobar/twitch/callback',
                      'hub.lease_seconds': '90',
                      'hub.secret': 'SECRET SHHH'
                      }
        response = requests.post('https://api.twitch.tv/helix/webhooks/hub', params=param_data, headers=headers, verify=True)

    '''
    
    
def setup(bot):
    bot.add_cog(Basic(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file
