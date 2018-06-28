import nflgame
import pandas as pd
import matplotlib.pyplot as plt
import datetime

games = nflgame.games(2016)
players = nflgame.combine_game_stats(games)

count = 1
for p in players.sort('receiving_tds').limit(20):
    print count, p.player, p.receiving_tds, p.receiving_yds
    count += 1
    #plt.scatter(p.rushing_tds, (datetime.datetime.today().year - p.player.birthdate.year))
#plt.show()