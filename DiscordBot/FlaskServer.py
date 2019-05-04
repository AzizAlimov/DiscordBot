#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:45:56 2019

@author: azuzialimov
"""

from flask import Flask
from flask import request

from threading import Thread

app = Flask(__name__)
#bot = commands.Bot(command_prefix="!")

#Set up 'index' route
@app.route('/')
def main():
    return "Your bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()