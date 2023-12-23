def transform_range(elem, ranges):
    for range in ranges:
        source_range = range["src"]
        dest_range = range["dest"]

        if elem in source_range:
            return dest_range.start + (elem - source_range.start)
    return elem

def transform_range_for_range(seed_range, ranges):
    for curr_range in ranges:
        source_range = curr_range["src"]
        dest_range = curr_range["dest"]

        intersected_src_seed = range(max(seed_range.start, source_range.start), min(seed_range.stop, source_range.stop))
        if len(intersected_src_seed) > 0:
            new_ranges = []
            transformed_range =  range(
                dest_range.start + (intersected_src_seed.start - source_range.start),
                dest_range.start + (intersected_src_seed.start - source_range.start) + len(intersected_src_seed)
            )
            new_ranges.append(transformed_range)

            if seed_range.start < intersected_src_seed.start:
                new_ranges.append(range(seed_range.start, intersected_src_seed.start))
            
            if seed_range.stop > intersected_src_seed.stop:
                new_ranges.append(range(intersected_src_seed.stop, seed_range.stop))

            return new_ranges

    return [seed_range]

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


    seeds =  [range(seed, seed + range_len) for seed, range_len in zip(seeds[0::2], seeds[1::2])]

    for ranges_arr in range_maps:
        new_seeds = []
        while len(seeds) > 0:
            curr_seed_range = seeds.pop()
            new_seed = transform_range_for_range(curr_seed_range, ranges_arr)
            new_seeds.append(new_seed[0])
            if len(new_seed) > 1:
                seeds.extend(new_seed[1:])
        seeds = new_seeds
    
    min_seed = min([r.start for r in seeds])
    print(f"Part 2: {min_seed}")
