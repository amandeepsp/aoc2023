with open("data/day09.txt") as infile:
    elem_sum = 0
    back_element_sum = 0

    for line in infile:
        seq = [int(elem) for elem in line.strip().split()]

        all_diffs = [seq]
        diffs = seq
        while set(diffs) != set([0]):
            curr_diffs = []
            for a, b in zip(diffs, diffs[1:]):
                curr_diffs.append(b - a)
            diffs = curr_diffs
            all_diffs.append(diffs)
            
        next_element = 0
        for diffs_seq in all_diffs[::-1]:
            next_element += diffs_seq[-1]

        elem_sum += next_element

        back_element = 0
        for diffs_seq in all_diffs[::-1]:
            back_element = diffs_seq[0] - back_element

        back_element_sum += back_element

    print(f"Part 1: {elem_sum}")
    print(f"Part 2: {back_element_sum}")
