import random
def mod_no_zero(v: int, m: int) -> int:
    v %= m
    if v == 0: v = m
    return v
def acaan(value: int, suit: int, pos: int) -> (int, int):
    d, r = divmod(pos, 4)
    s = ["c", "h", "s", "d"]
    difference_in_suit_and_value = -3*r
    new_value = mod_no_zero(value + d + difference_in_suit_and_value, 13)
    new_suit = (suit - r) % 4
    return new_value, new_suit

def to_card(value: int, suit: int):
    t = [f"{i}" for i in range(2, 11)]
    t.insert(0, "A")
    t.insert(11, "J")
    t.insert(12, "Q")
    t.insert(13, "K")
    s = ["♣️", "♥️", "♠️", "♦️"]
    return f"{t[value - 1]} {s[suit]}"

def rand_acaan():
    value = random.randint(1, 13)
    suit = random.randint(0, 3)
    position = random.randint(1, 52)
    return to_card(value, suit), position, value, suit
i = 1
while i == 1 or input("Rand") == "":
    i = 0
    a = rand_acaan()
    print(a[0], a[1])
    if input("Solve?") == "":
        print(to_card(*acaan(a[2], a[3], a[1])))