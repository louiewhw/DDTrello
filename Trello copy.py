# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:03:28 2018

@author: louie.wong
"""
import Trello_credentials
from trello import TrelloClient
import pandas as pd
import numpy as np

#https://api.trello.com/1/boards/lr4kcjux/cards
#https://api.trello.com/1/actions/lr4kcjux
df = pd.read_json('https://api.trello.com/1/boards/lr4kcjux/cards')