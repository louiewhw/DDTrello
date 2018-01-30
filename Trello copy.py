# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:03:28 2018

@author: louie.wong
"""
from trello import TrelloClient
import pandas as pd
import numpy as np
from datetime import datetime


#DD Ping Pong to dataframe 
df = pd.read_json('https://api.trello.com/1/boards/lr4kcjux/cards')
df = df[['id','idList', 'name','url','dateLastActivity']]

#Find created date
time = []
for i in range(len(df)):
    time.append(datetime.fromtimestamp(int(df.id[i][0:8], 16)))
    
df['time'] = time

#BoardList to dataframe
Rank = df[df.idList == '5913a83766152518bcb603c2']
Unrank = df[df.idList == '5913a90e3f59c15f91ecdfce']
Challenge = df[df.idList == '5914c4fdfa425a62a5cbc3ec']
History = df[df.idList == '5914c54af867d23f762aa977']

#Date Cleansing 

History['Challenger'] = History.name.str.split(' ').str[0]
History['Opponent']
History['Score'] = History.name.str.split(':').str[1]