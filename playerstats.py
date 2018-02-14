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
from openpyxl import Workbook
from openpyxl.chart import Reference, Series, BarChart
import pandas as pd

p2016 = pd.read_excel("nbastats2016.xlsx")
p2017 = pd.read_excel("nbastats2017.xlsx")
p2018 = pd.read_excel("nbastats2018.xlsx")

# Cleaning player column for string matching

pattern = '\\\[a-zA-Z0-9_]*'
p2016['Player'] = p2016['Player'].str.replace(pattern, '')
p2016['Player'] = p2016['Player'].str.lower()

p2017['Player'] = p2017['Player'].str.replace(pattern, '')
p2017['Player'] = p2017['Player'].str.lower()

p2018['Player'] = p2018['Player'].str.replace(pattern, '')
p2018['Player'] = p2018['Player'].str.lower()


def single_player():
    player = input('Enter the player you would like to compare: ').lower()
    year = input('Enter the season you would like to compare: ')

    yeardict = {'2016': p2016, '2017': p2017, '2018': p2018}

    season = yeardict[year]

    mask = season['Player'].str.match(player)

    return season[mask]


def compare_players():
    compare = 'yes'
    players = pd.DataFrame(columns=p2016.columns)
    while compare == 'yes':
        player = single_player()
        players = players.append(player)

        compare = input('Would you like to enter another player (yes or no): ')

    # Statistical categories for input: FG%, 3P%

    statistics = input('Input the statistical category you would like to compare: ')
    playerstats = players.loc[:, ['Player', statistics]]

    highestplayer = playerstats.loc[playerstats[statistics].idxmax()]

    return playerstats, highestplayer


def sample_output_excel_chart():
    # Sample from http://zetcode.com/articles/openpyxl/
    book = Workbook()
    sheet = book.active

    rows = [
        ("USA", 46),
        ("China", 38),
        ("UK", 29),
        ("Russia", 22),
        ("South Korea", 13),
        ("Germany", 11)
    ]

    for row in rows:
        sheet.append(row)

    data = Reference(sheet, min_col=2, min_row=1, max_col=2, max_row=6)
    categs = Reference(sheet, min_col=1, min_row=1, max_row=6)

    chart = BarChart()
    chart.add_data(data=data)
    chart.set_categories(categs)

    chart.legend = None
    chart.y_axis.majorGridlines = None
    chart.varyColors = True
    chart.title = "Olympic Gold medals in London"

    sheet.add_chart(chart, "A8")

    book.save("bar_chart.xlsx")

if __name__ == "__main__":
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(compare_players())

