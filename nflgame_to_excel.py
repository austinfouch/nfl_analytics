import nflgame

while True:
    year = raw_input("Enter year to pull nflgame data from:")
    fileName = "season" + str(year) + ".csv"
    try:
        nflgame.combine(nflgame.games(int(year))).csv(fileName)
        break
    except:
        print "Invalid year"