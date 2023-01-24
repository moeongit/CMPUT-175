import codecs

def players(filename):
    players = []
    with codecs.open(filename, 'r', 'utf-8') as file:
        for line in file:
            stats = line.strip().split(";")
            country_number = stats[0]
            position = stats[1]
            name = stats[2]
            dob, age = stats[3].split(" (")
            age = age.strip("aged ").strip(")")
            number = country_number[-2:]
            country = country_number[:-3]
            players.append({
                "country": country,
                "number": number,
                "position": position,
                "name": name,
                "dob": dob,
                "age": age
            })
    return players

def matches(filename):
    matches = []
    with codecs.open(filename, 'r', 'utf-8') as file:
        for line in file:
            stats = line.strip().split(";")
            if stats[0] and stats[1] and stats[2] and stats[3] and stats[4]:
                group = stats[0]
                team1 = stats[1]
                team2 = stats[2]
                scores = stats[3]
                date = stats[4]
                team1_scores = scores.split(")(")[0].strip("(")
                team2_scores = scores.split(")(")[1].strip(")")
                matches.append({
                    "group": group,
                    "team1": team1,
                    "team2": team2,
                    "team1_scores": team1_scores,
                    "team2_scores": team2_scores,
                    "date": date
                })
    return matches

def cards(filename):
    cards = []
    with codecs.open(filename, 'r', 'utf-8') as file:
        for i, line in enumerate(file):
            stats = line.strip().split(";")
            if len(stats) == 5:
                match, country, name, card_type, time = stats
                cards.append({
                    "match": match,
                    "country": country,
                    "name": name,
                    "type": card_type,
                    "time": time
                })

    return cards

def write_groups(filepath, matches):
    groups = {}
    for match in matches:
        group = match["group"]
        team1 = match["team1"]
        team2 = match["team2"]
        if group not in groups:
            groups[group] = set()
        groups[group].add(team1)
        groups[group].add(team2)
    with open(filepath, "w") as f:
        for group, countries in sorted(groups.items()):
            f.write("Group {}\n".format(group))
            for country in sorted(countries):
                f.write("{}\n".format(country))
            f.write("\n")

def knockout_stage(filepath, matches, cards):
    teams = {}
    for match in matches:
        team1 = match["team1"]
        team2 = match["team2"]
        score1 = match["team1_scores"]
        score2 = match["team2_scores"]
        if team1 not in teams:
            teams[team1] = {"played": 0, "wins": 0, "draws": 0, "losses": 0, "goals_for": 0, "goals_against": 0, "points": 0, "yellow_cards": 0, "red_cards": 0}
        if team2 not in teams:
            teams[team2] = {"played": 0, "wins": 0, "draws": 0, "losses": 0, "goals_for": 0, "goals_against": 0, "points": 0, "yellow_cards": 0, "red_cards": 0}
        if match["team2_scores"]:
            score2 = list(map(int, match["team2_scores"].split(',')))
        else:
            print("Invalid score for team 2")
            return

        score1 = list(map(int, match["team1_scores"].split(',')))
        score2 = list(map(int, match["team2_scores"].split(',')))
        # for s in score1:
        #     teams[team1]["goals_for"] += s
        # for s in score2:
        #     teams[team2]["goals_for"] += s

        teams[team1]["goals_for"] += sum(score1)
        teams[team1]["goals_against"] += sum(score2)
        teams[team2]["goals_for"] += sum(score2)
        teams[team2]["goals_against"] += sum(score1)

        if score1 > score2:
            teams[team1]["wins"] += 1
            teams[team2]["losses"] += 1
        elif score1 < score2:
            teams[team1]["losses"] += 1
            teams[team2]["wins"] += 1
        else:
            teams[team1]["draws"] += 1
            teams[team2]["draws"] += 1
    for card in cards:
        fields = card.strip().split(';')
        match, team, player, card_type, time = fields
        if team not in teams:
            teams[team] = {'played': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'goals_for': 0, 'goals_against': 0, 'points': 0, 'yellow_cards': 0, 'red_cards': 0}
        if card_type == 'Y':
            teams[team]['yellow_cards'] += 1
        else:
            teams[team]['red_cards'] += 1
        #calculating points
        for team in teams:
            wins = teams[team]['wins']
            draws = teams[team]['draws']
            teams[team]['points'] = wins * 3 + draws
        #sorting teams alphabetically
        sorted_teams = dict(sorted(teams.items(), key=lambda item: item[0]))
        #calculating goal difference
        for team in sorted_teams:
            goal_diff = teams[team]['goals_for'] - teams[team]['goals_against']
            teams[team]['goal_diff'] = goal_diff
        #sorting teams by points, goal_difference and yellow cards
        sorted_teams = dict(sorted(teams.items(), key=lambda item: (item[1]['points'], item[1]['goal_diff'], item[1]['yellow_cards']), reverse=True))
        #writing the output to the console and file
        with open(filepath, 'w', 'utf-8') as f:
            for team in sorted_teams:
                points = teams[team]['points']
                goal_diff = teams[team]['goal_diff']
                yellow_cards = teams[team]['yellow_cards']
                red_cards = teams[team]['red_cards']
                f.write('{:<12}'.format(team) + '{:<3}'.format(str(points)) + 'pts' + '\n')
                print('{:<12}'.format(team) + '{:<3}'.format(str(points)) + 'pts')

def main():
    players_func = players("WC22Footballers.txt")
    matches_func = matches("WC22GroupMatches.txt")
    cards_func = cards("WC22-YellowCards.txt")
    groups = write_groups("groups.txt", matches_func)
    knockout = knockout_stage("knockout.txt", matches_func, cards_func)
    print(players_func)
    print(matches_func)
    print(cards_func)
main()