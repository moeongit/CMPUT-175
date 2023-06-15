
import codecs

# What are our main goals?
# There are 8 functions we have to create
# Break them down step by step

def players(filename):
    players = []
    with codecs.open(filename, "r", "utf-8") as file:
        for line in file:
            stats = line.strip().split(";")
            country_and_number = stats[0].split(" ")
            country = " ".join(country_and_number[:-1])
            number = country_and_number[-1]
            position = stats[1]
            name = stats[2]
            dob, age = stats[3].split(" (")
            age = age.strip("aged ").strip(")")
            players.append({
                "country": country, "number": number, "position": position,
                "name": name, "birth": dob, "age": age
            })
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
                team1_goals = scores.split(")(")[0].strip("(")
                team2_goals = scores.split(")(")[1].strip(")")
                matches.append({
                    "group": group, "team1": team1, "team2": team2,
                    "team1_goals": team1_goals, "team2_goals": team2_goals,
                    "date": date
                })
    return matches

def cards(filename):
    cards = []
    with codecs.open(filename, "r", "utf-8") as file:
        for line in file:
    

def main():
    players_function = players("WC22Footballers.txt")
    matches_function = matches("WC22GroupMatches.txt")
main()