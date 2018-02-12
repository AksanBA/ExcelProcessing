#!/usr/bin/env python
"""
Here we expand the project with pandas with the following aims:
1) Given a player and season, return per game statistics
2) Given a set of player and season per game statistics, return the best or worst player in that set (comparison)
3) Use openpyxl to do something non-trivial that cannot be completed with pandas: charts!

Two separate concepts:
    a) Return information on a single player
    b) Return information on a set of players AND compare on a specified set of statistics (points, rebounds, etc.)
"""
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openpyxl import load_workbook, Workbook
import pandas as pd

def user_choice():
    season =

def load_year():
    year = input('Enter the season you would like to compare: ')
    pd.read_excel()