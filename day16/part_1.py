def parse_input():
    flow_rates = {}
    neighbors_dict = {}
    for line in open('day16/00.in').read().splitlines():
        line = line.split(";")
        valve = line[0].split()[1]
        flow_rates[valve] = int(line[0].split("=")[1])
        neighbors = [v.replace(',', '') for v in line[1].split(' ')[5:]]
        neighbors_dict[valve] = neighbors
    return flow_rates, neighbors_dict


def dfs(valve, remaining_time, flow_rates, neighbors, opened, pressure_so_far, memo):
    if remaining_time < 0:
        return pressure_so_far

    state = (valve, remaining_time, frozenset(opened))
    if state in memo:
        return memo[state]

    best_pressure = pressure_so_far
    this_valves_flow_rate = flow_rates[valve]

    if valve not in opened:  # Take it
        best_pressure = max(best_pressure,
                            dfs(valve, remaining_time - 1, flow_rates, neighbors, opened | {valve}, pressure_so_far + this_valves_flow_rate * (remaining_time - 1), memo))

    for neighbor in neighbors[valve]:
        best_pressure = max(best_pressure,
                            dfs(neighbor, remaining_time - 1, flow_rates, neighbors, opened, pressure_so_far, memo))

    memo[state] = best_pressure
    return best_pressure


flow_rates, neighbors = parse_input()
print(dfs('AA', 30, flow_rates, neighbors, set(), 0, {}))
