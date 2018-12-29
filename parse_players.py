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

def update_roster(player_names, player_data):
    print "Who are you dropping?"
    player_to_drop = raw_input()
    if player_to_drop == "":
        print "Cancelling."
        return
    player_to_drop = match_player(player_to_drop, player_names)
    if player_to_drop is None:
        print "Player not found. Cancelling."
        return
    print "Dropping " + player_to_drop + ". Who are you adding?"
    player_to_add = raw_input()
    if player_to_add == "":
        print "Cancelling."
        return
    print "Adding " + player_to_add + ". Press enter again to confirm, do anything else to cancel."
    if raw_input() != "":
        print "Cancelling."
        return

    player_names.remove(player_to_drop)
    del player_data[player_to_drop]
    player_names += [player_to_add]
    player_data[player_to_add] = []

    print "Dropped " + player_to_drop + ", added " + player_to_add + "."
    return

def update_stats(player_names, player_data):
    while True:
        print "Enter player to update:"
        player_name = raw_input()
        if player_name == "":
            return
        player_name = match_player(player_name, player_names)
        if player_name is None:
            print "Player not found. Try again."
            continue
        statline = parse_input(player_name)
        if statline is not None:
            player_data[player_name] = statline

player_names, player_data = read_player_data()

print "Your roster: " + ', '.join(player_names)
print "What would you like to do?"
print "1. Update player data"
print "2. Modify roster"

option = raw_input()

if option == "1":
    update_stats(player_names, player_data)
elif option == "2":
    update_roster(player_names, player_data)

write_player_data(player_names, player_data)

print "Goodbye!"
