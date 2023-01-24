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

# def knockout_teams(filename):
#     knockout_teams = []
#     with codecs.open(filename, )


players = players("WC22Footballers.txt")
matches = matches("WC22GroupMatches.txt")
cards = cards("WC22-YellowCards.txt")
groups = write_groups("groups.txt", matches)
print(players)
print(matches)
print(cards)