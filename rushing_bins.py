import nflgame
import pandas as pd
import matplotlib.pyplot as plt
import datetime

games = nflgame.games(2015)
players = nflgame.combine_game_stats(games)
runs = pd.Series([p.rushing_yds for p in players.rushing()])
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.set_title('rushing yards 2015 season', fontsize=14, color='black')

ax.set_ylabel('frequency')
ax.set_xlabel('bins')

plt.style.use('ggplot')
plt.hist(runs, color='purple')

plt.show()
    