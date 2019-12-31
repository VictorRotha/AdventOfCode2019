from collections import deque

def new_stack():
    cards.reverse()

def cut_n(n):
    cards.rotate(-n)

def increment_n(n, cards):
    rotation = 0
    new_cards = deque(['-']*len(cards))
    while cards:
        value = cards.popleft()
        new_cards[0] = value
        new_cards.rotate(-n)
        rotation += 1
    new_cards.rotate(n*rotation)
    return new_cards

cards = deque(range(10007))
with open('input.txt', 'r') as f:
    for line in f:
        if 'increment' in line:
            n = int(line.strip()[20:])
            cards = increment_n(n, cards.copy())
        elif 'cut' in line:
            n = int(line.strip()[4:])
            cut_n(n)
        else:
            new_stack()

print('position of card 2019: ', cards.index(2019))
# position of card 2019:  8775

