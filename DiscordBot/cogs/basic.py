#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 18:15:32 2019

@author: azuzialimov
"""

from discord.ext import commands
from datetime import datetime as d
import random
import requests

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
        #dict = msg.json()
        #content = dict.get('weather')
        temp = float(msg.json().get('main').get('temp')) - 273.15
                   
        msg = "It's all" + msg.json().get('weather')[0].get('description') +\
        " today! The current temperatue is " + str(temp) + " degrees celsius."
        #msg = "It's all " + msg + " today!"
        
        await ctx.send(content = msg)
        
    @commands.command(
            name = 'name',
            description='Returns the name of the bot'
            )
    async def name_command(self, ctx):
        msg = 'My name is Jacky, nice to meet you.'
        await ctx.send(content = msg)


def setup(bot):
    bot.add_cog(Basic(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file
