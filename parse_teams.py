import parse_input

result = parse_input.getTeamInput()
file = open("team_stats.txt", "a")
file.write(str(result))
file.write("\n")
file.close()

print result
