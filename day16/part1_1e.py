def parse_input():
    flow_rates = {}
    neighbors = {}
    valves_to_consider = set()

    for line in open('day16/00.in').read().splitlines():
        line = line.split(";")
        valve = line[0].split()[1]
        rate = int(line[0].split("=")[1])
        flow_rates[valve] = rate

        curr_neighbors = [v.replace(',', '') for v in line[1].split(' ')[5:]]
        neighbors[valve] = curr_neighbors
        if rate:
            valves_to_consider.add(valve)

    return neighbors, flow_rates, valves_to_consider


def part_1(neighbors, rates):
    open_valves = set()
    visited = {}
    max_so_far = 0

    def dfs(valve, time, cum_pressure):
        nonlocal max_so_far

        if visited.get((valve, time), -1) >= cum_pressure:  # If we've already been here with more pressure, don't bother
            return

        visited[valve, time] = cum_pressure  # Update the max pressure we've seen at this time and valve

        if time >= 30:  # If we're out of time, update the max pressure we've seen so far
            max_so_far = max(max_so_far, cum_pressure)
            return

        add_pressure = sum(rates[valve] for valve in open_valves)  # Calculate the additional pressure we get from all open valves

        if (valve not in open_valves) and (rates[valve] > 0):  # If we're at a closed valve and it has a non-zero flow rate, open it
            open_valves.add(valve)
            dfs(valve, time + 1, cum_pressure + add_pressure + rates[valve])  # Recurse with the new valve opened
            open_valves.remove(valve)  # Close the valve so we can try other options

        for neighbor in neighbors[valve]:
            dfs(neighbor, time + 1, cum_pressure + add_pressure)

    dfs(valve='AA', time=1, cum_pressure=0)
    print(max_so_far)


neighbors, rates, valves_to_consider = parse_input()
part_1(neighbors, rates)
