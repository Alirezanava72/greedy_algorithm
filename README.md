# MFT Data Analysis with Python - Greedy Algorithm

## Overview

### What is a 'Greedy algorithm'?
A greedy algorithm, as the name suggests, **always makes the choice that seems to be the best at that moment**. This means that it makes a locally-optimal choice in the hope that this choice will lead to a globally-optimal solution. In other words, it makes the best possible decision at each step without considering the consequences of those decisions on future steps. The term "greedy" is used because the algorithm appears to be making a series of choices that are advantageous at the moment, without considering the long-term impact.

In another words, the decision on which choice is considered optimal is made based on a specific criterion defined by the problem at hand. The criteria for determining the optimal choice depend on the problem's characteristics and requirements.

How can we determine which option is the most advantageous?

Determining which option is optimal involves making decisions based on a specific criterion or rule that optimizes the current situation at each step. Assume that you have an objective function that needs to be optimized (either maximized or minimized) at a given point. A Greedy algorithm makes greedy choices at each step to ensure that the objective function is optimized. The Greedy algorithm has only one shot to compute the optimal solution so that it never goes back and reverses the decision. Here are some general steps and considerations for determining the most advantageous option in a Greedy algorithm:

1.	Define the Objective Function:

Clearly define the objective or goal of the problem you are trying to solve. Understand what constitutes an optimal outcome or solution.

2.	Identify Greedy Choice Criteria:

Establish the criteria for making greedy choices at each step. This could involve selecting the option with the maximum or minimum value, highest priority, shortest distance, etc., depending on the nature of the problem.

3.	Greedy Choice at Each Step:

At each step of the algorithm, identify the available options and apply the greedy choice criteria to select the most advantageous option according to the defined criterion.

4.	Update State or Solution:

Update the current state or solution based on the chosen option. This may involve removing the chosen item, updating weights or values, or adjusting the problem state accordingly.

5.	Repeat Steps:

Repeat the process iteratively until a solution is found. In some cases, the algorithm may have a termination condition, or it may continue until all elements are processed.

6.	Verify Optimality:

Depending on the problem, you may need to verify the optimality of the solution obtained by the Greedy algorithm. In some cases, Greedy algorithms provide globally optimal solutions, while in others, they may not.

Examples:

Greedy Choice in Knapsack(backpack) Problem:

*	Criterion: Choose items with the maximum value-to-weight ratio.

*	At each step, select the item that contributes the most value while not exceeding the weight limit.

Let's solve the Knapsack Problem in Python using numPy:
```python
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
```

Greedy algorithms have some advantages and disadvantages:

* Advantages:
1.	It is quite easy to come up with a greedy algorithm (or even multiple greedy algorithms) for a problem.
2.	Analysing the run time for greedy algorithms will generally be much easier than for other techniques (like Divide (Break the original problem into smaller, more manageable subproblems) and Conquer (Solve the subproblems independently, either recursively or iteratively)). For the Divide and conquer technique, it is not clear whether the technique is fast or slow. This is because at each level of recursion the size of gets smaller and the number of sub-problems increases.

*	Disadvantage:

1. The difficult part is that for greedy algorithms you must work much harder to understand correctness issues. Even with the correct algorithm, it is hard to prove why it is correct. Proving that a greedy algorithm is correct is more of an art than a science. It involves a lot of creativity.

Another Example of Greedy algorithm for better understanding:

Imagine you have a limited amount of time (T) and a list of tasks represented by an array A, where each element indicates the time required to complete a task. The goal is to maximize the number of tasks completed within the given time constraint.
The solution follows a Greedy algorithm approach:
1.   Sort the array A in non-decreasing order.

1.	Iterate through the sorted array, selecting tasks one by one.

2.	Keep track of the number of tasks completed (numberOfThings).

3.	Repeat the process until currentTime exceeds T.

Let A = {5, 3, 4, 2, 1} and T = 6

After sorting, A = {1, 2, 3, 4, 5}

After the 1st iteration:

* currentTime = 1

* numberOfThings = 1

After the 2nd iteration:

* currentTime is 1 + 2 = 3

* numberOfThings = 2

After the 3rd iteration:

* currentTime is 3 + 3 = 6

* numberOfThings = 3

After the 4th iteration, currentTime becomes 10, which is greater than T (6). Therefore, the answer is 3, indicating that you can complete a maximum of 3 tasks within the given time limit.
