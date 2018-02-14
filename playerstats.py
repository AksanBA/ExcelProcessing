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

p2016 = pd.read_excel("nbastats2016.xlsx")
p2017 = pd.read_excel("nbastats2017.xlsx")
p2018 = pd.read_excel("nbastats2018.xlsx")

# Cleaning player column for string matching

pattern = '\\\[a-zA-Z0-9_]*'
p2016['Player'] = p2016['Player'].str.replace(pattern, '')
p2017['Player'] = p2017['Player'].str.replace(pattern, '')
p2018['Player'] = p2018['Player'].str.replace(pattern, '')

def single_player():
    player = input('Enter the player you would like to compare: ')
    year = input('Enter the season you would like to compare: ')

    mask = series.str.match(pattern)

def compare_players():
    players = input('Enter the players you would like to compare: ')
    year = input('Enter the season you would like to compare:')

def output_excel_chart():
