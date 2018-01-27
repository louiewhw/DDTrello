# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:03:28 2018

@author: louie.wong
"""
import Trello_credentials
from trello import TrelloClient
import pandas as pd
import numpy as np
DDBoard = TrelloClient(api_key= Trello_credentials.api_key).get_board('lr4kcjux')

pingpong = []


for i in DDBoard.get_cards():
    pingpong.append(str(i))
    
    
pingpong = pd.DataFrame(data = np.array(pingpong).T)
pingpong = pingpong[0].str.split('<Card').str[1].str.split('>').str[0].str.lstrip()
#
#pingpong[0] = str(DDBoard.get_cards()[1:26]).split(' ,')
#pingpong[1] = str(DDBoard.get_cards()[27:]).split(' ,')

#pingpong = pd.DataFrame(np.array(pingpong))