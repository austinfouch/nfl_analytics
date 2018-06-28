import nflgame
import pandas as pd
import matplotlib.pyplot as plt
import datetime

games = nflgame.games(2015)
players = nflgame.combine_game_stats(games)
runs = pd.Series([p.rushing_yds for p in players.rushing()])
fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(111)
ax.set_title('height and weight of 2015 NFL RBs and FBs', fontsize=14, color='black')

fig.subplots_adjust(top=0.85)

ax.set_ylabel('height')
ax.set_xlabel('weight')

plt.style.use('ggplot')

for p in players.rushing():
    if p.player.position in ['RB', 'FB']:
        plt.scatter(p.player.weight, p.player.height, c='green')

        if p.player.name == 'Mike Tolbert':
            plt.annotate(
                p.player.name + ', ' + p.player.team, color='black',
                xy = (p.player.weight, p.player.height), xytext = (p.player.weight, p.player.height-1.5), alpha = 0.9,
                xycoords='data',
                textcoords='data',
                arrowprops=dict(arrowstyle="-|>", color='black',
                                connectionstyle="arc3"))

plt.show()