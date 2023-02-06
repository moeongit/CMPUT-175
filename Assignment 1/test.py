import codecs

def cards(filename):
    cards = []
    with codecs.open(filename, "r", "utf-8") as file:
        for i, line in file:
            stats = line.strip().split(";")
            if len(stats) == 5:
                match, country, name, card_type, time = stats
                cards.append({"match": match, "country": country, "name": name, "type": card_type, "time": time})
    return cards


cards_function = cards("WC22-YellowCards.txt")