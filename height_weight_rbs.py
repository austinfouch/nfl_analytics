import nflgame
import pandas as pd
import matplotlib.pyplot as plt
import datetime

def inchesToFeetStr(n):
    feet = int(n//12)
    inches = int(n%12)
    return str(feet) + "'" + str(inches) + '"' 

# API calls
games = nflgame.games(2017)
players = nflgame.combine_game_stats(games)

# Create figure and axes with labels
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('height and weight of 2017 NFL RBs and FBs', fontsize=14, color='black')
fig.subplots_adjust(top=0.85)
ax.set_ylabel('height')
ax.set_xlabel('weight')
plt.style.use('ggplot')

# Store player data in seperate arrays for axes labels and point annotations
rb_heights = []
rb_weights = []
rb_names = []
for p in players.rushing():
    try:
        if p.player.position in ['RB']:
            rb_heights.append(p.player.height)
            rb_weights.append(p.player.weight)
            rb_names.append(p.player.name)
    except AttributeError:
        print(p.player, ": has an attribute error(s)")

# Plot and convert YAxis labels from inches to string of feet and inches
sc = plt.scatter(rb_weights, rb_heights, c='green')
ax.set_yticklabels([inchesToFeetStr(y) for y in ax.get_yticks()])

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
