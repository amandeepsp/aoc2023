targets = {"red": 12, "green": 13, "blue": 14}


def is_game_possible(outcome_sets):
    for outcome in outcome_sets:
        outcome_colors = outcome.split(", ")
        for outcome_color in outcome_colors:
            num, color = outcome_color.split(" ")
            if targets[color.strip()] < int(num):
                return False
    return True


def find_fewest_colors_power(outcome_sets):
    color_counts = {}

    for outcome in outcome_sets:
        outcome_colors = outcome.split(", ")
        for outcome_color in outcome_colors:
            num, color = outcome_color.split(" ")
            color = color.strip()
            if color in color_counts:
                color_counts[color].append(int(num))
            else:
                color_counts[color] = [int(num)]

    power = 1
    for count_list in color_counts.values():
        power = power * max(count_list)
    
    return power


with open("data/day02.txt") as infile:
    sum = 0
    power_sum = 0

    for line in infile:
        game_id, outcomes = line.split(": ")
        game_id = int(game_id.split(" ")[1])
        outcome_sets = outcomes.split("; ")
        if is_game_possible(outcome_sets):
            sum = sum + game_id
        
        power_sum = power_sum + find_fewest_colors_power(outcome_sets)

    print(f"Part 1: {sum}")
    print(f"Part 2: {power_sum}")
