# Rubik's Cube Solver
This Python script is a Rubik's Cube solver using the IDA* (Iterative Deepening A*) algorithm. It includes functions for cube manipulation, movement application, and solving. The solver generates pruning tables for piece orientation and permutation, then searches for the solution with increasing depth.

# Getting Started
Prerequisites

Make sure you have the following installed:

Python (>=3.6)

NumPy

-> pip install numpy

# Usage
1. Open the rubiks_cube_solver.py file.
2. Modify the cube_state variable in the __main__ block to set the initial cube state.
3. Run the script: python rubiks_cube_solver.py
   
The script will display the initial cube state, normalize the stickers, generate pruning tables, and start the search for the optimal solution using IDA*.
# Example
Here's an example of how to use the solver:

from rubiks_cube_solver import apply_algorithm_string, solve_cube

#Initialize cube state and apply an algorithm

cube_state = initialize_state()

cube_state = apply_algorithm_string(cube_state, "R U2 R2 F2 R' F2 R F R")

#Solve the cube

solve_cube(cube_state)

