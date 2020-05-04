import random
# Knapsack

knapsack = {
    "V": 10,
    "R": 5,
    "NR_ITEMS": 100,    # 100, 250, 500
    # "C": 20,    # 2 * v or 0.5 * sum (weights)
}

def generate_uncor():
    weights = [random.uniform(1,knapsack["V"]) for i in range(knapsack["NR_ITEMS"])]
    values = [random.uniform(1,knapsack["V"]) for i in range(knapsack["NR_ITEMS"])]
    capacity = int(0.5 * sum(weights))
    return {'weights':weights, 'values':values, 'capacity': capacity}

def generate_weak_cor():
    weights = [random.uniform(1,knapsack["V"]) for i in range(knapsack["NR_ITEMS"])]
    values = []
    for i in range(knapsack["NR_ITEMS"]):
        value = weights[i] + random.uniform(-knapsack["R"],knapsack["R"])
        while value <= 0:
            value = weights[i] + random.uniform(-knapsack["R"],knapsack["R"])
        values.append(value)
    capacity = int(0.5 * sum(weights))
    return {'weights':weights, 'values':values, 'capacity': capacity}

def generate_strong_cor():
    weights = [random.uniform(1,knapsack["V"]) for i in range(knapsack["NR_ITEMS"])]
    values = [weights[i] + knapsack["R"] for i in range(knapsack["NR_ITEMS"])]
    capacity = int(0.5 * sum(weights))
    return {'weights':weights, 'values':values, 'capacity': capacity}

