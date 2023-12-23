def transform_range(elem, ranges):
    for range in ranges:
        source_range = range["src"]
        dest_range = range["dest"]

        if elem in source_range:
            return dest_range.start + (elem - source_range.start)
    return elem

with open("data/day05.txt") as infile:
    data = infile.read().split("\n\n")
    seeds = [int(seed) for seed in data[0].split(": ")[1].split(" ")]
    range_maps = []
    for map_item in data[1:]:
        ranges_arr = []
        for ranges in map_item.split(":\n")[1].splitlines():
            range_arr = [int(range_elem) for range_elem in ranges.split(" ")]
            range_item = {
                "dest": range(range_arr[0], range_arr[0] + range_arr[2]),
                "src": range(range_arr[1], range_arr[1] + range_arr[2])
            }
            ranges_arr.append(range_item)
        range_maps.append(ranges_arr)

    min_final = float("inf")
    for seed in seeds:
        curr_seed = seed
        for ranges_arr in range_maps:
            curr_seed = transform_range(curr_seed, ranges_arr)
        min_final = min(min_final, curr_seed)

    print(f"Part 1: {min_final}")


    
