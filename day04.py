from collections import Counter


with open("data/day04.txt") as infile:

    points = 0
    cards_counter = Counter()

    for card_num, line in enumerate(infile):
        card = line.strip().split(":")[1]
        winning_str, curr_str = card.split("| ")
        winning_nums = set(int(num) for num in winning_str.split(" ") if num)
        current_nums = [int(num) for num in curr_str.split(" ") if num]

        winning_cnt = 0
        for num in current_nums:
            if num in winning_nums:
                winning_cnt = winning_cnt + 1
    
        if winning_cnt > 0:
            points = points + 2**(winning_cnt - 1)

        cards_counter[card_num] += 1
        for i in range(card_num + 1, card_num + winning_cnt + 1):
            cards_counter[i] += cards_counter[card_num]

    print(f"Part 1: {points}")
    print(f"Part 2: {sum(cards_counter.values())}")
        
