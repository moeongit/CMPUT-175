import codecs

def parse_players(filepath):
    players = []
    with codecs.open(filepath, 'r', 'utf-8') as f:
        for line in f:
            fields = line.strip().split(";")
            country_number = fields[0]
            position = fields[1]
            name = fields[2]
            dob, age = fields[3].split(" (")
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

def parse_matches(filepath):
    matches = []
    with codecs.open(filepath, 'r', 'utf-8') as f:
        for line in f:
            fields = line.strip().split(";")
            if fields[0] and fields[1] and fields[2] and fields[3] and fields[4]:
                group = fields[0]
                team1 = fields[1]
                team2 = fields[2]
                scores = fields[3]
                date = fields[4]
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

def parse_cards(filepath):
    cards = []
    with codecs.open(filepath, 'r', 'utf-8') as f:
        for line in f:
            fields = line.strip().split(";")
            match = fields[0]
            country = fields[1]
            name = fields[2]
            card_type = fields[3]
            time = fields[4]
            cards.append({
                "match": match,
                "country": country,
                "name": name,
                "type": card_type,
                "time": time
            })
    return cards


players = parse_players("WC22Footballers.txt")
matches = parse_matches("WC22GroupMatches.txt")
cards = parse_cards("WC22-YellowCards.txt")
print(players)
print(matches)
print(cards)