import collections
import itertools


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


def part_1():
    neighbors, rates, _ = parse_input()
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


def part_2():
    neighbors, rates, valves_to_open = parse_input()

    open_valves = set()
    visited = {}
    max_so_far = 0

    def search(time, me, elephant, pressure):
        nonlocal max_so_far

        if visited.get((time, me, elephant), -1) >= pressure:
            return

        visited[time, me, elephant] = pressure

        if time == 26:
            max_so_far = max(max_so_far, pressure)
            return

        pressure += sum(rates[valve] for valve in open_valves)

        # If all valves are open, just stay here
        if len(open_valves) == len(valves_to_open):
            search(time + 1, me, elephant, pressure)
            return

        # I could open the valve
        if me not in open_valves and rates[me]:
            open_valves.add(me)

            # Elephant could open the valve
            if elephant not in open_valves and rates[elephant]:
                open_valves.add(elephant)
                search(
                    time + 1,
                    me,
                    elephant,
                    pressure + rates[me] + rates[elephant]
                )
                open_valves.remove(elephant)

            # Elephant could just move
            for neighbor in neighbors[elephant]:
                search(
                    time + 1,
                    me,
                    neighbor,
                    pressure + rates[me]
                )

            open_valves.remove(me)

        # I could just move
        for me_neighbor in neighbors[me]:
            # Elephant could open the valve
            if elephant not in open_valves and rates[elephant]:
                open_valves.add(elephant)
                search(
                    time + 1,
                    me_neighbor,
                    elephant,
                    pressure + rates[elephant]
                )
                open_valves.remove(elephant)

            # Elephant could just move
            for elephant_neighbor in neighbors[elephant]:
                search(
                    time + 1,
                    me_neighbor,
                    elephant_neighbor,
                    pressure,
                )

    search(1, 'AA', 'AA', 0)
    print(max_so_far)


def bfs_search():
    neighbors, rates, valves_to_open = parse_input()
    states = {}
    valves = {valve: 1 << i for i, valve in enumerate(valves_to_open)}

    def next_states(current_states):
        for me, open_valves, flow, pressure in current_states:
            candidate_states = []

            # If at a valve of interest and it's closed, open it
            if me in valves and ~open_valves & valves[me]:
                candidate_states.append((me, open_valves | valves[me], flow + rates[me]))

            # Alternatively, move to another valve
            for neighbor in neighbors[me]:
                candidate_states.append((neighbor, open_valves, flow))

            for state in candidate_states:
                if state not in states or states[state] < pressure + flow:
                    states[state] = pressure + flow
                    yield (*state, pressure + flow)

    current_states = [('AA', 0, 0, 0)]

    for _ in range(26):
        current_states = list(next_states(current_states))

    return states


def part_2_bfs_disjoint():
    """
    Somewhat of a more clever/simpler solution here than doing 2D DFS, where the idea is that you
    use BFS to compile a list of all possible 1-player states at the end of 26 minutes, with
    a bitset to represent open valves.

    Then you group them by the open valves at the end and select the state for maximal pressure
    for that given set of final open valves.

    Then, noting that you and the elephant operate on disjoint sets of open valves, we simply
    take all distinct pairs of final states with disjoint open valves and try to find the pair
    with maximal total pressure.
    """
    states = bfs_search()
    grouped_states = collections.defaultdict(list)

    for state, pressure in states.items():
        open_valves = state[1]
        grouped_states[open_valves].append(pressure)

    best_states = {
        open_valves: max(pressures)
        for open_valves, pressures in grouped_states.items()
    }

    print(max(
        me_pressure + elephant_pressure
        for (me_open_valves, me_pressure), (elephant_open_valves, elephant_pressure)
        in itertools.combinations(best_states.items(), 2)
        if not me_open_valves & elephant_open_valves
    ))


def all_shortest_paths(adj):
    """Floyd-Warshall implementation"""
    valves = sorted(adj.keys())
    distances = {u: {v: float('inf') for v in valves} for u in valves}

    for u in valves:
        distances[u][u] = 0

        for v in adj[u]:
            distances[u][v] = 1

    for k, i, j in itertools.product(valves, repeat=3):
        if distances[i][j] > distances[i][k] + distances[k][j]:
            distances[i][j] = distances[i][k] + distances[k][j]

    return distances


def compressed_bfs_search():
    """
    This performs a BFS search on the possible 1-player states, but on a compressed weighted graph
    that whose nodes are only those with positive flow rates, and the edge weights represent
    the amount of time it takes to travel to the next valve and open it.
    """
    neighbors, rates, valves_to_open = parse_input()
    masks = {valve: 1 << i for i, valve in enumerate(valves_to_open)}
    distances = all_shortest_paths(neighbors)

    # Compress the graph to only valves with a positive flow rate
    neighbors = {
        valve_1: [valve_2 for valve_2 in valves_to_open if valve_2 != valve_1]
        for valve_1 in valves_to_open
    }

    states = {}

    # Initialize queue with 1 valve already opened
    queue = collections.deque([
        (
            valve,
            masks[valve],
            # We store the total pressure that this opened valve will contribute for the entire 26 minutes instead
            # of just simulating each individual minute
            rates[valve] * (26 - distances['AA'][valve] - 1),
            distances['AA'][valve] + 1,
        )
        for valve in valves_to_open
    ])

    while queue:
        me, open_valves, pressure, time = queue.popleft()
        state = (me, open_valves)

        if state not in states or states[state] < pressure:
            states[state] = pressure

        for neighbor in neighbors[me]:
            # New time elapsed after traveling to the valve and opening it
            new_time = time + distances[me][neighbor] + 1

            # If valve is closed, we can get to it and open it, and we can get at least 1 minute of positive flow,
            # consider it a candidate next state
            if ~open_valves & masks[neighbor] and new_time < 26:
                new_state = (neighbor, open_valves | masks[neighbor])
                new_pressure = pressure + (26 - new_time) * rates[neighbor]

                if new_state not in states or states[new_state] < new_pressure:
                    states[new_state] = new_pressure
                    queue.append((*new_state, new_pressure, new_time))

    return states


def part_2_compressed_bfs_disjoint():
    """
    This is a variant on the other BFS disjoint solution, but instead we "compress" the graph.

    0-valves are completely useless and only serve as connection points to the actual valves that
    add pressure, so we can remove them entirely and form a new weighted graph using Floyd-Warshall
    to calculate the minimum distances between valves of interest.
    """
    states = compressed_bfs_search()
    grouped_states = collections.defaultdict(list)

    for state, pressure in states.items():
        open_valves = state[1]
        grouped_states[open_valves].append(pressure)

    best_states = {
        open_valves: max(pressures)
        for open_valves, pressures in grouped_states.items()
    }

    print(max(
        me_pressure + elephant_pressure
        for (me_open_valves, me_pressure), (elephant_open_valves, elephant_pressure)
        in itertools.combinations(best_states.items(), 2)
        if not me_open_valves & elephant_open_valves
    ))


part_1()
