def getPlayerInput():
    print "Enter player data"
    fg_attempts = float(raw_input().split('/')[1])
    fg_perc = float(raw_input())
    ft_attempts = float(raw_input().split('/')[1])
    ft_perc = float(raw_input())
    threept_attempts = float(raw_input().split('/')[1])
    threept_perc = float(raw_input())
    pts = float(raw_input())
    reb = float(raw_input())
    ast = float(raw_input())
    stl = float(raw_input())
    blk = float(raw_input())
    to = float(raw_input())

    return [fg_attempts, fg_perc, ft_attempts, ft_perc, threept_attempts,
            threept_perc, pts, reb, ast, stl, blk, to]

def getTeamInput():
    print "Enter team data"
    fg_perc = float(raw_input())
    raw_input()
    ft_perc = float(raw_input())
    raw_input()
    threept_perc = float(raw_input())
    pts = float(raw_input())
    reb = float(raw_input())
    ast = float(raw_input())
    stl = float(raw_input())
    blk = float(raw_input())
    to = float(raw_input())

    return [fg_perc, ft_perc, threept_perc, pts, reb, ast, stl, blk, to]

print "Player or team? (p/t)"
option = raw_input()
if (option == "p"):
    result = getPlayerInput()
    file = open("player_stats.txt", "a")
    file.write(str(result))
    file.write("\n")
    file.close()
else:
    result = getTeamInput()
    file = open("team_stats.txt", "a")
    file.write(str(result))
    file.write("\n")
    file.close()

print result
