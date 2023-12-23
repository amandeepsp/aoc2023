with open("data/day06.txt") as infile:
    times, distances = infile.readlines()
    times = [int(time) for time in times.strip().split()[1:]]
    distances = [int(dist) for dist in distances.split()[1:]]
    print(times,distances)