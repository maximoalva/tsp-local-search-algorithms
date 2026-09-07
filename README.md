# TSP Local Search Algorithms

Implementation of local search algorithms for the **Traveling Salesman Problem (TSP)**, developed as part of **Programación III** in the **Tecnicatura Universitaria en Inteligencia Artificial** at the **Universidad Nacional de Rosario (UNR)**.

The project explores and compares three local search strategies using a **2-opt neighborhood**:

- Hill Climbing
- Random Restart Hill Climbing
- Tabu Search

## Overview

The Traveling Salesman Problem consists of finding a tour that visits every city exactly once and returns to the starting city, while minimizing the total travel distance.

For this implementation, a solution is represented as a tour that starts and ends at city `0`, with every other city appearing exactly once.

The algorithms operate on a **2-opt neighborhood**, where two non-adjacent edges are selected and the intermediate segment of the tour is reversed. This provides a simple way to explore neighboring solutions while preserving a valid TSP tour.

The optimization is formulated by maximizing the negative tour distance:

```text
obj(tour) = - total_distance(tour)
```

Therefore, a higher objective value corresponds to a shorter tour.

## Algorithms

### Hill Climbing

The basic hill climbing algorithm starts from the predefined initial tour and repeatedly evaluates the available 2-opt moves.

At each iteration:

1. Compute the objective-value difference for every possible action.
2. Select the actions producing the largest improvement.
3. Randomly break ties between those actions.
4. Apply the selected move if it improves the current solution.
5. Stop when no improving neighbor exists.

The resulting solution is a local optimum with respect to the implemented neighborhood.

### Random Restart Hill Climbing

Random Restart Hill Climbing extends the basic approach by restarting the search from a randomly generated tour whenever a local optimum is reached.

This allows the algorithm to explore different regions of the search space and reduces the dependence on a single initial solution.

In this implementation, the search performs up to **5 random restarts**, keeping the best local optimum found across all runs.

### Tabu Search

Tabu Search introduces a memory mechanism to discourage repeatedly applying recently used moves.

The implementation:

- Maintains a tabu list of recently performed 2-opt actions.
- Selects the best non-tabu action at each iteration.
- Allows moves that do not improve the current solution, helping the search escape local optima.
- Keeps track of the best solution found during the entire search.
- Uses a tabu tenure of **70 moves**.
- Stops after **1000 consecutive iterations without improving the best solution**.

This strategy allows the search to move through worse intermediate solutions while preserving the best tour discovered so far.

## Search Space and Neighborhood

For a TSP instance with `n` cities, a state is a permutation of the cities that starts and ends at city `0`.

The neighborhood is generated through **2-opt moves**. An action is represented by a pair `(i, j)` identifying two non-adjacent edges of the current tour.

Applying a 2-opt move removes those two edges and reconnects the tour by reversing the segment between them.

This neighborhood is shared by the three implemented algorithms, making it possible to compare their search strategies while keeping the underlying representation and local moves consistent.

## Program Output

The main program runs all three algorithms on the selected TSP instance and reports:

| Metric | Description |
|---|---|
| `Value` | Objective value of the best tour found |
| `Time` | Execution time |
| `Iters` | Number of iterations performed |
| `Algorithm` | Algorithm used |

It also generates a graphical comparison showing:

- `Init` — the initial tour
- `Hill` — the solution found by Hill Climbing
- `Hill_reset` — the solution found by Random Restart Hill Climbing
- `Tabu` — the solution found by Tabu Search

## Project Structure

```text
.
├── instances/
│   └── *.tsp
├── load.py
├── main.py
├── parse.py
├── plot.py
├── problem.py
├── requirements.txt
├── search.py
└── README.md
```

### Main modules

- **`main.py`** — command-line entry point. Loads the instance, runs the algorithms, prints statistics, and displays the resulting tours.
- **`search.py`** — contains the local search framework and the three algorithms.
- **`problem.py`** — defines the TSP optimization problem, including states, objective values, neighborhood operations, and random resets.
- **`load.py`** — loads TSP instances.
- **`parse.py`** — handles command-line arguments.
- **`plot.py`** — visualizes the initial and final tours.
- **`instances/`** — contains TSP problem instances.

## Requirements

The assignment specifies **Python 3.10 or higher**.

Install the required dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the program by providing a TSP instance:

```bash
python3 main.py instances/ar24.tsp
```

The program will run the three algorithms sequentially, print their performance statistics, and display the corresponding tours.

## Technologies

- Python
- Graph algorithms
- Local search
- Heuristic optimization
- Traveling Salesman Problem (TSP)
- 2-opt neighborhood
- Hill Climbing
- Random Restart
- Tabu Search
- Matplotlib

## Key Concepts

This project focuses on several important concepts in heuristic optimization:

- **Local optima** and the limitations of purely greedy local search.
- **Neighborhood structures** for combinatorial optimization.
- **Random restarts** as a diversification strategy.
- **Tabu lists** as a memory-based mechanism for escaping local optima.
- **2-opt** as a tour-improvement operator for the TSP.
- The trade-off between **solution quality, exploration, and execution time**.

## Academic Context

This repository was developed for a practical assignment in **Programación III** at the **Universidad Nacional de Rosario**, focused on implementing local search techniques for combinatorial optimization problems.
