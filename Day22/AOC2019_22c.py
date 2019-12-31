with open('input.txt', 'r') as f:
    shuffles = f.readlines()

# f(x) = a *x + b
def parse_ab(deck, shuffles):
    a, b = 1, 0
    for shuffle in shuffles:
        if 'new stack' in shuffle:
            a = - a
            b = deck - b - 1
        elif 'cut' in shuffle:
            n = int(shuffle.strip()[4:])
            b = (b-n) % deck
        elif 'increment' in shuffle:
            n = int(shuffle.strip()[20:])
            a = (n * a)%deck
            b = (n * b)%deck
    return a, b

def parse_rev(deck, shuffles):
    a, b = 1,0
    for shuffle in shuffles[::-1]:
        if 'new stack' in shuffle:
            a = - a
            b = deck - b - 1
        elif 'cut' in shuffle:
            n = int(shuffle.strip()[4:])
            b = (b+n) % deck
        elif 'increment' in shuffle:
            n = int(shuffle.strip()[20:])
            z = pow(n, deck-2, deck)            # modinv ?!?
            a = (z * a)%deck
            b = (z * b)%deck
    return a, b

def run(a, b, deck, pos):
    pos = (pos*a + b) % deck
    return pos

def runpoly(a,b, deck, pos, n):
    pos = (pow(a, n, deck) * pos + (pow(a, n, deck) - 1) * pow(a-1, deck-2, deck) * b) % deck
    return pos

deck = 119315717514047
n = 101741582076661
pos = 2020

a, b = parse_rev(deck, shuffles)
newpos = runpoly(a, b, deck, pos, n)

print(newpos)
# PART 02 SOLUTION: 47141544607176
