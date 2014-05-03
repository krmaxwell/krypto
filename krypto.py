import random


def shuffle():
    deck = []
    for n in range(1,7):
        deck.extend([n]*3)
    for n in range(7,11):
        deck.extend([n]*4)
    for n in range(11,18):
        deck.extend([n]*2)
    for n in range(18,26):
        deck.append(n)
    return deck


def main():
    deck = shuffle()
    objective = random.choice(deck)
    deck.remove(objective)
    hand = []
    for n in range(5):
        selection = random.choice(deck)
        hand.append(selection)
        deck.remove(selection)
    print "Cards: %r = %d (Objective Card)" % (hand, objective)

    entry = ""
    while True:
        entry = raw_input("Expression? ")
        expression = evaluate(entry, hand)
        if expression == objective:
            print "You win!"
            break


if __name__ == "__main__":
    main()
