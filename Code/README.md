# Code Module – Arc Routing Heuristic

This folder contains the full Python implementation of our custom heuristic for solving arc routing problems. The heuristic is based on a longest-path traversal strategy with a final Dijkstra-based closure step to ensure the tour forms a valid cycle.

## Components

- `graph.py`: Graph structure and node-to-edge mapping.
- `edge.py`: Edge class with source, destination, cost, and required status.
- `util.py`: Input file parsers for different problem types (DRPP, MCPP, WRPP, Additional Cases).
- `atlasCycle.py`: The core heuristic algorithm implementation.
- `mainCycle.py`: Main entry point for running the heuristic on a selected instance.

---

## How to Run

To run the heuristic on any dataset:

1. **Open `mainCycle.py`**
   - Change the `folder_path` variable to point to the dataset you want to run.
   - Example:
     ```python
     folder_path = "../test_instances/WRPP_Instances"
     ```

2. **Open `util.py`**
   - You will see **four utility classes or methods**, one for each dataset type (labeled with comments).
   - **Uncomment only the class for the dataset you're using**, and **comment the other three**, since they share the same class or method names.


3. **Run the script**
   ```bash
   python mainCycle.py

