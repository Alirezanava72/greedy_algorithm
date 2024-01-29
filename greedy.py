import numpy as np

# defining the function
def greedy_knapsack(values, weights, capacity):
    n = len(values)
    ratio = [v / w for v, w in zip(values, weights)] # calculating the value-to-weight ratio for each item
    indices = np.argsort(ratio)[::-1]

    total_value = 0
    knapsack = np.zeros(n)

    for i in indices:
        if weights[i] <= capacity:
            knapsack[i] = 1
            total_value += values[i]
            capacity -= weights[i]

    return total_value, knapsack

# values
item_values = [30, 40, 35, 10, 25]
item_weights = [5, 8, 7, 2, 3]
knapsack_capacity = 10

# Solve the problem using the values via greedy algorithm
result_value, selected_items = greedy_knapsack(item_values, item_weights, knapsack_capacity)

print("Hypothetical values:")
print("Item values:", item_values)
print("Item weights:", item_weights)
print("Knapsack capacity:", knapsack_capacity)
print("\nResults:")
print("Total value:", result_value)
print("Selected items (1 indicates selection):", selected_items.astype(int))


