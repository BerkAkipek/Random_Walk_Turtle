from random import choice


def random_walk(num_steps):
    directions = ["N", "S", "W", "E", "U", "D"]
    x, y, z = 0, 0, 0
    for step in range(num_steps):
        decision = choice(directions)
        if decision == "N": y += 1
        elif decision == "S": y -= 1
        elif decision == "W": x -= 1
        elif decision == "E": x += 1
        elif decision == "U": z += 1
        else: z -= 1
    return (x, y, z)


def random_walk_limit_distribution(step_limit, distance_limit, num_walks):
    return_list = []
    for step in range(1, step_limit + 1):
        no_transport = 0
        for walk in range(num_walks):
            simulated_walk = random_walk(step)
            distance = abs(simulated_walk[0]) + abs(simulated_walk[1]) + abs(simulated_walk[2])
            if distance <= distance_limit:
                no_transport += 1
        return_list.append(no_transport / num_walks)
    return return_list


if __name__ == "__main__":
    cache = random_walk_limit_distribution(step_limit=40, distance_limit=5, num_walks=1000)
    for value in cache:
        print(f"{cache.index(value)}:   {value}\n")

