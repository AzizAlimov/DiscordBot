#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:45:56 2019

@author: azuzialimov
"""

import os
from flask import Flask, request, abort, render_template
from threading import Thread
from flask_socketio import SocketIO, send, emit

client = []

TWITCH_KEY = 'live_45462101_agarpYIuK3PMBpMSGPaAmM1AhigGT5'
clientID = '1xulrvwog4x8hxk1xaje7k17yructl'

contentType = 'application/json'
postURI = 'https://api.twitch.tv/helix/webhooks/hub'

app = Flask('Discord bot')
socketio = SocketIO(app)

DISCORD_WEBHOOK = os.environ.get('DISCORD_WEBHOOK')

#Set up 'index' route
@app.route('/')
def main():
    return "Jacky is alive and doing well."

#Starts the server
def run():
    socketio.run(app, host = 'localhost', port = 8080)
    
def keep_alive():
    server = Thread(target=run)
    server.start()

#POST handler
@app.route('/posts', methods=['POST'])
def result():
    pass

#Receives the callback from twitch subscription
@app.route('/gets', methods=['GET'])
def gets():
    message = ''
    socketio.emit('twitch', message)
    return


@socketio.on('message')
def handle_message(message):
    socketio.emit('my response', message)
