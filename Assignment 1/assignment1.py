# This program reads text files (data) from the 2022 World Cup and generates text files based on that data.
# The players function goes through the footballers text function and finds the info of the player
# The same is done for the matches function and the cards function
# I stuck to simple programming here so comments werent really necessary in most spots. I used split and strip and appended things to a list and made most things clean

import codecs

def players(filename):
    players = []
    with codecs.open(filename, "r", "utf-8") as file:
        for line in file:
            stats = line.strip().split(";")
            country_number = stats[0].rsplit(" ", 1) # Used r.split because the number and country would interfere if the country had a space between it like "South Korea"
            country = " ".join(country_number[:-1])
            number = country_number[-1] 
            position = stats[1]
            name = stats[2]
            birth, age = stats[3].split(" (")
            age = age.strip("aged ").strip(")")
            players.append({
                "country": country, "number": number, "position": position,
                "name": name, "birth": birth, "age": age})
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
    groups = {} # made this a dictionary (easier)
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
            print("Group {}".format(group)) # Used the format function to make everything alphabetical
            for country in sorted(countries):
                file.write("{}\n".format(country))
                print("{}".format(country))
            file.write("\n")
            print("")

def card_total(team,cardslist):
    total=0
    for card in cardslist:
        if card['country'] == team:
            if card['type'] == "Y":
                total+=1
            elif card['type'] == "R":
                total+=4
    return(total)


def match_results(matches,cardslist):
    match_points=[]
    for match in matches:
        group=match["group"]

        team1=match["team1"]
        team2=match["team2"]

        team1_goals=len(match["team1_scores"].split(","))
        team2_goals=len(match["team2_scores"].split(","))

        score_diff=team1_goals-team2_goals

        if score_diff>0:
            team1_points=3
            team2_points=0
        elif score_diff<0:
            team2_points=3
            team1_points=0
        else:
            team1_points=1
            team2_points=1
        match_points.append({"group": group, "team1": team1, "team2": team2, "score_diff":score_diff, "team1_points":team1_points, "team2_points":team2_points})
    team_points={}
    for match in match_points:
        group=match["group"]
        team1=match["team1"]
        team2=match["team2"]
        if group not in team_points:
            team_points[group]={}
        if team1 not in team_points[group]:
            team_points[group][team1]=0
        if team2 not in team_points[group]:
            team_points[group][team2]=0
        team_points[group][team1]+=match["team1_points"]
        team_points[group][team2]+=match["team2_points"]
    
    output=[]
    for group in team_points:

        groupteams_scores=team_points[group]
        sorted_teamscores = sorted(groupteams_scores.items(), key=lambda x:x[1],reverse=True)
        
        # Breaking Ties
        tiebreaker=0
        if sorted_teamscores[1][1] == sorted_teamscores[2][1]:
            for match in match_points:
                if match["team1"]==sorted_teamscores[1][0] and match["team2"]==sorted_teamscores[2][0]:
                    if score_diff>0:
                        tiebreaker=1
                    elif score_diff<0:
                        tiebreaker=2
                    else:
                        team1card=card_total(team1,cardslist)
                        team2card=card_total(team2,cardslist)
                    if team1card>team2card:
                        tiebreaker=2
                    elif team2card>team1card:
                        tiebreaker=1
                if match["team1"]==sorted_teamscores[2][0] and match["team2"]==sorted_teamscores[1][0]:
                    if score_diff>0:
                        tiebreaker=2
                    elif score_diff<0:
                        tiebreaker=1
                    else:
                        team1card=card_total(team1,cardslist)
                        team2card=card_total(team2,cardslist)
                    if team1card>team2card:
                        tiebreaker=1
                    elif team2card>team1card:
                        tiebreaker=2

        if tiebreaker==0 or tiebreaker==1:
            output.append(sorted_teamscores[0])
            output.append(sorted_teamscores[1])
        elif tiebreaker == 2:
            output.append(sorted_teamscores[0])
            output.append(sorted_teamscores[2])

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
        for age in range(18, 41): # Age range 18-40, 41 not exclusive
            if age in ages:
                stars = round(ages[age]/5)
                if stars == 0:
                    stars = 1
                file.write("{} years ({:2d}){}\n".format(age, ages[age],'*' * stars))
                print("{} years ({:2d}){}".format(age, ages[age],'*' * stars))

def most_player_goals():
    players = codecs.open("WC22Footballers.txt", "r", "utf-8")
    goals = {}
    top_scorers = {}
    with codecs.open("WC22GroupMatches.txt", "r", "utf-8") as file:
        for line in file:
            stats = line.strip().split(";")
            if stats[0] and stats[1] and stats[2] and stats[3] and stats[4]:
                team1 = stats[1]
                team2 = stats[2]
                scores = stats[3].find(")")
                score1 = stats[3][1:scores]
                score2 = stats[3][scores + 2:-1] # Slicing to find scores
                score1 = score1.split(",")
                score2 = score2.split(",")
                for num in score1:
                    player = " ".join([team1, num])
                    goals[player] = goals.get(player, 0) + 1
                for num in score2:
                    player = " ".join([team2, num])
                    goals[player] = goals.get(player, 0) + 1
    top_goals = 0 # Counter for goals
    for player, goal in goals.items():  # this loop finds the maximum goal scored
        if goal > top_goals:
            top_goals = goal
    for player, goal in goals.items():  # this loop finds if others scored the same amout
        if goal == top_goals:
            top_scorers[player] = goal
    for player in players:
        stats = player.split(";")
        player = stats[0]
        name = stats[2]
        if player in top_scorers.keys():
            top_scorers[player] = name
    with open("scorers.txt", "w", encoding="utf-8") as file:
        file.write("+ ------------ + ----------------- + ---------------------------------- +\n")
        print("+ ------------ + ----------------- + ---------------------------------- +")
        for player, name in top_scorers.items():
            player = player.split()
            team = player[0]
            number = player[1]
            file.write(f"|  {top_goals} goals     | {team: <13}     |{number: >3} {name: <32}|\n")
            print(f"|  {top_goals} goals     | {team: <13}     |{number: >3} {name: <32}|")
        file.write("+ ------------ + ----------------- + ---------------------------------- +\n")
        print("+ ------------ + ----------------- + ---------------------------------- +")
        
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
    knockout = match_results(matches_function,cards_function)
    ages = average_age(players_function)
    stars = histogram(players_function)
    most_goals = most_player_goals()
    most_yellow_cards(cards_function)
main()