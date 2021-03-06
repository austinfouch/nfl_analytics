import nflgame
import pandas as pd
import matplotlib.pyplot as plt
import datetime

games = nflgame.games(2017)
players = nflgame.combine_game_stats(games)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.set_title('age vs. rushing yds', fontsize=14, color='black')
fig.subplots_adjust(top=0.85)
ax.set_ylabel('age (days)')
ax.set_xlabel('rushing_yds')
plt.style.use('ggplot')

rb_age = []
rb_yards = []
rb_names = []
for p in players.rushing():
    try:
        if p.player.position in ['RB']:
            rb_age.append((datetime.datetime.today() - datetime.datetime.strptime(p.player.birthdate,'%m/%d/%Y')).days)
            rb_yards.append(p.rushing_yds)
            rb_names.append(p.player.name)
    except AttributeError:
        print(p.player, ": has an attribute error(s)")

# Plot and convert YAxis labels from inches to string of feet and inches
sc = plt.scatter(rb_yards, rb_age, c='green')

# Set annotaions and make invisible, made visible on hover event
annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = "{}".format(" ".join([rb_names[n] for n in ind["ind"]]))
    annot.set_text(text)
    annot.get_bbox_patch().set_alpha(0.4)

def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()

    