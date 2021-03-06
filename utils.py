import random
import json
"""
Knapsack problem generator
"""

kp = {
    "V": 10,
    "R": 5,
    "NR_ITEMS": 250,    # 100, 250, 500
    "PERTURBATION": 10
}

def generate_uncor():
    weights = [random.uniform(1,kp["V"]) for i in range(kp["NR_ITEMS"])]
    values = [random.uniform(1,kp["V"]) for i in range(kp["NR_ITEMS"])]
    capacity = int(0.5 * sum(weights))
    return {'weights':weights, 'values':values, 'capacity': capacity}

def generate_weak_cor():
    weights = [random.uniform(1,kp["V"]) for i in range(kp["NR_ITEMS"])]
    values = []
    for i in range(kp["NR_ITEMS"]):
        value = weights[i] + random.uniform(-kp["R"],kp["R"])
        while value <= 0:
            value = weights[i] + random.uniform(-kp["R"],kp["R"])
        values.append(value)
    capacity = int(0.5 * sum(weights))
    return {'weights':weights, 'values':values, 'capacity': capacity}

def generate_strong_cor():
    weights = [random.uniform(1,kp["V"]) for i in range(kp["NR_ITEMS"])]
    values = [weights[i] + kp["R"] for i in range(kp["NR_ITEMS"])]
    capacity = int(0.5 * sum(weights))
    return {'weights':weights, 'values':values, 'capacity': capacity}


if __name__ == "__main__":
    datasets = []
    for _ in range(kp["PERTURBATION"]):
        datasets.append(generate_weak_cor())
    open("datasets/dataset1.json", 'w').write(json.dumps(datasets))