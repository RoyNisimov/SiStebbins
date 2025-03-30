# CHaSeD 0 1 2 3
def mod_no_zero(v: int, m: int) -> int:
    v %= m
    if v == 0: v = m
    return v

def find_position(value: int, suit: int, bottom_card_value: int = 13, bottom_card_suit: int = 3) -> int:
    cards_to_add = (- suit + bottom_card_suit)
    s = mod_no_zero((bottom_card_value - 3 * cards_to_add), 13)
    v = mod_no_zero((s-value), 13) * 4 - cards_to_add
    return mod_no_zero(v, 52)
print(find_position(int(input("Value: ")), int(input("Suit: ")), int(input("Value: ")), int(input("Suit: "))))