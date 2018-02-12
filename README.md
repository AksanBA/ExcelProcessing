# ExcelProcessing

This module follows on from the tutorial by Elizabeth Siegle:
https://github.com/elizabethsiegle/nba-stats-twilio-sms-bot

This is a project to demonstrate the use of text processing with python using a combination of numpy, pandas, openpyxl
and deployment via flask.

Here we expand the project with pandas with the following aims:
1) Given a player and season, return per game statistics
2) Given a set of player and season per game statistics, return the best or worst player in that set (comparison)
3) Use openpyxl to do something non-trivial that cannot be completed with pandas: charts!

Player data is sourced from: https://www.basketball-reference.com