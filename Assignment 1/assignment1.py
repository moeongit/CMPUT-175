def parse_players(file_name):
    players = []
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.readlines()
        for line in data:
            fields = line.strip().split(";")
            player = {
                'Country': fields[0],
                'Position': fields[1],
                'Number': fields[2],
                'Name': fields[3],
                'Birthday': fields[4],
                'Age': fields[5]
            }
            players.append(player)
    return players

def parse_matches(file_name):
    matches = []
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.readlines()
        for line in data:
            fields = line.strip().split(";")
            group = fields[0]
            team1 = fields[1]
            team2 = fields[2]
            score1 = []
            score2 = []
            if fields[3] != "()()":
                score1 = [int(x) if x[0]!="X" else int(x[1:]) for x in fields[3][1:-1].split(",")]
                score2 = [int(x) if x[0]!="X" else int(x[1:]) for x in fields[4][:-1].split(",")]
            date = fields[5]
            match = {
                'Group': group,
                'Team1': team1,
                'Team2': team2,
                'Score1': score1,
                'Score2': score2,
                'Date': date
            }
            matches.append(match)
    return matches

def parse_yellowcards(file_name):
    yellow_cards = []
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.readlines()
        for line in data:
            fields = line.strip().split(";")
            match = fields[0]
            team = fields[1]
            player_num = int(fields[2])
            player_name = fields[3]
            yellow_card = {
                'Match': match,
                'Team': team,
                'Player_Number': player_num,
                'Player_Name': player_name
            }
            yellow_cards.append(yellow_card)
    return yellow_cards

players = parse_players("WC22Footballers.txt")
matches = parse_matches("WC22GroupMatches.txt")
yellow_cards = parse_yellowcards("WC22YellowCards.txt")
