import random
def mod_no_zero(v: int, m: int) -> int:
    v %= m
    if v == 0: v = m
    return v
def acaan(value: int, suit: int, pos: int) -> (int, int):
    d, r = divmod(pos, 4)
    difference_in_suit_and_value = -3*r
    new_value = mod_no_zero(value + d + difference_in_suit_and_value, 13)
    new_suit = (suit - r) % 4
    return new_value, new_suit
def acaan_plus(value: int, suit: int, pos: int) -> (int, int, int):
    d, r = divmod(pos, 4)
    new_value = mod_no_zero(value + d, 13)
    return new_value, suit, r


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

def find_position(value: int, suit: int, bottom_card_value: int = 13, bottom_card_suit: int = 3) -> int:
    cards_to_add = (- suit + bottom_card_suit)
    s = mod_no_zero((bottom_card_value - 3 * cards_to_add), 13)
    v = mod_no_zero((s-value), 13) * 4 - cards_to_add
    return mod_no_zero(v, 52)

if __name__ == "__main__":

    i = 1
    while i == 1 or input("Rand") == "":
        i = 0
        a = rand_acaan()
        print(a[0], a[1])
        if input("Solve?") == "":
            print(to_card(*(c := acaan(a[2], a[3], a[1]))), end="")
            print(f"which is in position {find_position(c[0], c[1], 13, 3)}")
            c = acaan_plus(a[2], a[3], a[1])
            print(f"or at the {to_card(c[0], c[1])} plus {c[2]} cards. (at position {find_position(c[0], c[1], 13, 3)})\n\n")