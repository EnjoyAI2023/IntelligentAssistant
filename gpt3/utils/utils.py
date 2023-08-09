#-*-coding:utf-8-*-
# date:2023-08-02
# Author: Eric
# function: utils

import os
import json
def load_json(pth_):
    with open(pth_, 'r',encoding="utf-8") as f:
        msg = json.load(f)
    return msg

def say_text(engine,text):
    """ RATE"""
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    print (rate)                        #printing current voice rate
    engine.setProperty('rate', 153)     # setting up new voice rate

    """VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    print (volume)                          #printing current volume level
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

    #-------------------------------------------------------------------------------
    engine.say(text)
    engine.runAndWait()
    print("runAndWait")
