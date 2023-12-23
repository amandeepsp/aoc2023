from collections import Counter
import functools


def find_cardset_weight(cards):
    card_counter = sorted(Counter(cards).values(), reverse=True)
    if card_counter[0] == 5:
        return 6
    if card_counter[0] == 4:
        return 5
    if card_counter[0] == 3 and card_counter[1] == 2:
        return 4
    if card_counter[0] == 3:
        return 3
    if card_counter[0] == 2 and card_counter[1] == 2:
        return 2
    if card_counter[0] == 2:
        return 1
    return 0


def find_cardset_weight_with_jokers(cards: str):
    jokers = cards.count("J")
    cards = [c for c in cards if c != "J"]
    card_counter = sorted(Counter(cards).values(), reverse=True)
    if not card_counter:
        card_counter = [0]
    if card_counter[0] + jokers == 5:
        return 6
    if card_counter[0] + jokers == 4:
        return 5
    if card_counter[0] + jokers == 3 and card_counter[1] == 2:
        return 4
    if card_counter[0] + jokers == 3:
        return 3
    if card_counter[0] == 2 and (jokers or card_counter[1] == 2):
        return 2
    if card_counter[0] == 2 or jokers:
        return 1
    return 0


def cmp_cards(cards1, cards2, cards_rank, cmp_func):
    hand_rank1 = cmp_func(cards1)
    hand_rank2 = cmp_func(cards2)

    if hand_rank1 < hand_rank2:
        return -1
    elif hand_rank1 > hand_rank2:
        return 1
    else:
        for card1, card2 in zip(cards1, cards2):
            if cards_rank[card1] < cards_rank[card2]:
                return -1
            elif cards_rank[card1] > cards_rank[card2]:
                return 1
            else:
                continue
        return 0


def find_weighted_sum(cards, cards_seq, cmp_func):
    cards_rank = {card: i + 1 for i, card in enumerate(cards)}

    sorted_cards_seq = sorted(
        cards_seq,
        key=functools.cmp_to_key(
            lambda x, y: cmp_cards(x[0], y[0], cards_rank, cmp_func)
        ),
    )

    weighted_sum = 0
    for i, (_, bid) in enumerate(sorted_cards_seq, start=1):
        weighted_sum += i * bid

    return weighted_sum


with open("data/day07.txt") as infile:
    cards_seq = []
    for line in infile:
        cards, bid = line.strip().split()
        cards_seq.append((cards, int(bid)))

    wsum = find_weighted_sum("23456789TJQKA", cards_seq, find_cardset_weight)
    print(f"Part 1: {wsum}")

    wsum_joker = find_weighted_sum(
        "J23456789TQKA", cards_seq, find_cardset_weight_with_jokers
    )
    print(f"Part 2: {wsum_joker}")
