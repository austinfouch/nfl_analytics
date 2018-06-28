import nflgame
import pandas as pd
import matplotlib.pyplot as plt
import datetime

games = nflgame.games(2015)
players = nflgame.combine_game_stats(games)
runs = pd.Series([p.rushing_yds for p in players.rushing()])
fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(111)
ax.set_title('age vs. rushing touchdowns', fontsize=14, color='black')
fig.subplots_adjust(top=0.85)

plt.style.use('ggplot')

ax.set_ylabel('age (days)')
ax.set_xlabel('rushing_tds')

for p in players.rushing():
    print p, datetime.datetime.now().year - p.birthdate.year
    #plt.scatter(p.rushing_tds, (datetime.datetime.today().year - p.player.birthdate.year))
#plt.show()