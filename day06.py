
from functools import reduce
from math import ceil, floor, sqrt
from operator import mul

def solns(t_max, d_max):
    term1 = sqrt(t_max**2 - 4*d_max) / 2.0
    term2 = t_max / 2.0
    return [ceil(term2 - term1), floor(term2 + term1)]

with open("data/day06.txt") as infile:
    times, distances = infile.readlines()
    times = [int(time) for time in times.strip().split()[1:]]
    distances = [int(dist) for dist in distances.split()[1:]]

    counts_record_break = []

    for i in range(len(times)):
        d_max = distances[i]
        t_max = times[i]
        soln = solns(t_max, d_max)
        counts_record_break.append(soln[1] - soln[0] + 1)

    print(f"Part 1: {reduce(mul, counts_record_break)}")

    infile.seek(0)
    times, distances = infile.readlines()
    time = int(times.replace(" ", "").split(":")[1].strip())
    distance = int(distances.replace(" ", "").split(":")[1].strip())
    soln = solns(time, distance)
    print(f"Part 2: {soln[1] - soln[0] + 1}")
