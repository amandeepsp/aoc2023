from itertools import cycle
import math


with open("data/day08.txt") as infile:
    instructions, graph_str = infile.read().split("\n\n")
    graph = {}
    for node in graph_str.splitlines():
        node_name, adj = node.split(" = ")
        graph[node_name] = tuple(adj.strip("()").split(", "))

    inst_cycle = cycle(1 if inst == "R" else 0 for inst in instructions)
    step_count = 0
    stack = ["AAA"]

    while stack:
        curr = stack.pop()
        if curr == "ZZZ":
            break
        step_count += 1
        next_inst = next(inst_cycle)
        stack.append(graph[curr][next_inst])

    print(f"Part 1: {step_count}")

    start_nodes = [n for n in graph.keys() if n.endswith("A")]
    cycles = []

    for node in start_nodes:
        step_count = 0
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr.endswith("Z"):
                cycles.append(step_count)
                break
            step_count += 1
            next_inst = next(inst_cycle)
            stack.append(graph[curr][next_inst])

    print(f"Part2 : {math.lcm(*cycles)}")
