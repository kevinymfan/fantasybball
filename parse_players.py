PLAYERS_FILE = "players.txt"

def match_player(prefix, players):
    for player in players:
        if prefix.lower() in player.lower():
            return player
    return None

def parse_input(player):
    print "Enter player data for " + player
    initial_input = raw_input()
    if initial_input == "":
        print "Ended early, entry scrapped"
        return None
    fg_attempts = float(initial_input.split('/')[1])
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

def stringify(stats):
    stats_str = []
    for stat in stats:
        stats_str += [str(stat)]
    return stats_str

def read_player_data():
    file = open(PLAYERS_FILE, "r")
    players = file.readline()[:-1].split(',')
    player_stats = {}
    for player in players:
        player_stats[player] = file.readline()[:-1].split(',')
    file.close()
    return players, player_stats

def write_player_data(names, data):
    file = open(PLAYERS_FILE, "w")
    file.write(','.join(names) + "\n")
    for player in names:
        file.write(','.join(stringify(data[player])) + "\n")
    file.close()

player_names, player_data = read_player_data()

print player_names

while True:
    print "Enter player"
    player_name = raw_input()
    if player_name == "":
        break
    player_name = match_player(player_name, player_names)
    if player_name is None:
        print "Invalid player. Try again."
        continue
    statline = parse_input(player_name)
    if statline is not None:
        player_data[player_name] = statline

write_player_data(player_names, player_data)
