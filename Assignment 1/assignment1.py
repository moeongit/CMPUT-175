import codecs

def players(filename):
    players = []
    with codecs.open(filename, "r", "utf-8") as file:
        for line in file:
            stats = line.strip().split(";")
            country_number = stats[0].split(" ")
            country = country_number[0]
            number = country_number[1]
            position = stats[1]
            name = stats[2]
            dob, age = stats[3].split(" (")
            age = age.strip("aged ").strip(")")
            players.append({
                "country": country, "number": number, "position": position,
                "name": name, "dob": dob, "age": age})
    return players

def matches(filename):
    matches = []
    with codecs.open(filename, "r", "utf-8") as file:
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
                matches.append({"group": group, "team1": team1, "team2": team2, 
                    "team1_scores": team1_scores, "team2_scores": team2_scores, "date": date})
    return matches

def cards(filename):
    cards = []
    with codecs.open(filename, "r", "utf-8") as file:
        for i, line in enumerate(file):
            stats = line.strip().split(";")
            if len(stats) == 5:
                match, country, name, card_type, time = stats
                cards.append({"match": match, "country": country, "name": name, "type": card_type, "time": time})
    return cards

def write_groups(filename, matches):
    groups = {}
    for match in matches:
        group = match["group"]
        team1 = match["team1"]
        team2 = match["team2"]
        if group not in groups:
            groups[group] = set()
        groups[group].add(team1)
        groups[group].add(team2)
    with open(filename, "w") as file:
        for group, countries in sorted(groups.items()):
            file.write("Group {}\n".format(group))
            print("Group {}".format(group))
            for country in sorted(countries):
                file.write("{}\n".format(country))
                print("{}".format(country))
            file.write("\n")
            print("")

def write_knockout(knockout_teams, output_file):
    with open(output_file, 'w') as file:
        for team in knockout_teams:
            file.write(team[0] + ' ' + str(team[1]) + ' pts' + '\n')


def knockout_stage(filepath, matches):
    teams = {}
    for match in matches:
        team1 = match["team1"]
        team2 = match["team2"]
        team1_scores = match["team1_scores"]
        team2_scores = match["team2_scores"]

        if team1 not in teams:
            teams[team1] = {"points": 0, "goal_diff": 0, "yellow_cards": 0}
        if team2 not in teams:
            teams[team2] = {"points": 0, "goal_diff": 0, "yellow_cards": 0}

        if len(team1_scores) > len(team2_scores):
            teams[team1]["points"] += 3
            teams[team1]["goal_diff"] += len(team1_scores) - len(team2_scores)
            teams[team2]["goal_diff"] += len(team2_scores) - len(team1_scores)
        elif len(team1_scores) < len(team2_scores):
            teams[team2]["points"] += 3
            teams[team1]["goal_diff"] += len(team1_scores) - len(team2_scores)
            teams[team2]["goal_diff"] += len(team2_scores) - len(team1_scores)
        else:
            teams[team1]["points"] += 1
            teams[team2]["points"] += 1

    # Sort teams by points, goal difference, and yellow cards
    teams = {k: v for k, v in sorted(teams.items(), key=lambda item: (-item[1]["points"], item[1]["goal_diff"], item[1]["yellow_cards"]))}

    # Write teams to file
    with open(filepath, "w") as f:
        for team, stats in teams.items():
            f.write("{}    {} pts\n".format(team, stats["points"]))
    return teams




def average_age(players_function):
    teams = {}
    for player in players_function:
        team = player["country"]
        age = int(player["age"])
        if team not in teams:
            teams[team] = {"players": 0, "age": 0}
        teams[team]["players"] += 1
        teams[team]["age"] += age
    for team in teams.keys():
        teams[team]["average_age"] = round(teams[team]["age"] / teams[team]["players"], 2)
    with open("ages.txt", "w", encoding="utf-8") as f:
        total_players = 0
        total_age = 0
        for team, values in sorted(teams.items()):
            players = values["players"]
            age = values["average_age"]
            total_players += players
            total_age += age * players
            f.write("{:<12}".format(team) + "{:.2f}".format(age) + " years\n") 
            print("{:<12}".format(team) + "{:.2f}".format(age) + " years") 
        f.write("\nAverage Overall " + "{:.2f}".format(total_age/total_players) + " years")
        print("\nAverage Overall " + "{:.2f}".format(total_age/total_players) + " years\n")

def histogram(players_function):
    ages = {}
    for player in players_function:
        age = int(player["age"])
        if age not in ages:
            ages[age] = 0
        ages[age] += 1
    with open("histogram.txt", "w", encoding="utf-8") as file:
        for age in range(18, 41):
            if age in ages:
                stars = round(ages[age]/5)
                if stars == 0:
                    stars = 1
                file.write("{} years ({:2d}){}\n".format(age, ages[age],'*' * stars))
                print("{} years ({:2d}){}".format(age, ages[age],'*' * stars))

def player_most_goals(filename):
    matches = []
    goals = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            stats = line.strip().split(";")
            if stats[0] and stats[1] and stats[2] and stats[3] and stats[4]:
                team1 = stats[1]
                team2 = stats[2]
                scores = stats[3]
                team1_scores = scores.split(")(")[0].strip("(")
                team2_scores = scores.split(")(")[1].strip(")")
                matches.append({"team1": team1, "team2": team2, 
                    "team1_scores": team1_scores, "team2_scores": team2_scores})
                goals.append(team1_scores)
                goals.append(team2_scores)
    players_list = player_most_goals(goals)
    with open("scorers.txt", "w", encoding="utf-8") as f:
        goals_scored = 0
        for player in players_list:
            if player["goals"] > goals_scored:
                goals_scored = player["goals"]
                f.write("+-------+--------------+-------------------------+\n")
                f.write("|{:<5}| {:<12}  | {:<23}|\n".format(str(goals_scored) + " goals", player["country"], player["name"]))
            elif player["goals"] == goals_scored:
                f.write("|{:<5}| {:<12}  | {:<23}|\n".format("", player["country"], player["name"]))

def most_yellow_cards(cards):
    match_card_count = {}
    for card in cards:
        match = card["match"]
        country = card["country"]
        if match not in match_card_count:
            match_card_count[match] = {}
        if country not in match_card_count[match]:
            match_card_count[match][country] = 0
        match_card_count[match][country] += 1
    max_cards = 0
    max_match = ""
    for match, card_count in match_card_count.items():
        if sum(card_count.values()) > max_cards:
            max_cards = sum(card_count.values())
            max_match = match
    match_name = max_match.split("-")
    match_name = " vs ".join(match_name)
    with open("yellow.txt", "w") as file:
        file.write(match_name + "\n")
        print(f"\n{match_name}")
        for country, count in match_card_count[max_match].items():
            file.write(f"{country}: {count} YC\n")
            print(f"{country}: {count} YC")





def main():
    players_function = players("WC22Footballers.txt")
    matches_function = matches("WC22GroupMatches.txt")
    cards_function = cards("WC22-YellowCards.txt")
    groups = write_groups("groups.txt", matches_function)
    ages = average_age(players_function)
    stars = histogram(players_function)
    most_yellow_cards(cards_function)
    knockout_teams = knockout_stage("WC22GroupMatches.txt", "WC22-YellowCards.txt")
    write_knockout(knockout_teams, "knockout.txt")
main()