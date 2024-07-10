import time
from Data import Data
from AStar import AStar
from UCS import UCS
from DFS import DFS
from RandomSolver import RandomSolver


if __name__ == "__main__":
    # TODO: Edit this variable
    FILE_PATH = "small.pkl"  # Such as "small.pkl", "medium.pkl", "large.pkl"

    # Load data
    data = Data(FILE_PATH)

    # Random Solution
    print("Random")
    random_solver = RandomSolver(data)
    start_time = time.time()
    random_solution = random_solver.solve()
    end_time = time.time()

    print("Feasibility:", data.is_feasible(random_solution))
    print("Objective Value:", data.calculate_objective(random_solution))
    print("Elapsed Time (sec):", end_time - start_time)
    print()

    # dfs
    print("DFS")
    dfs = DFS(data)
    start_time = time.time()
    solution_dfs = dfs.solve()
    end_time = time.time()

    print("Feasibility:", data.is_feasible(solution_dfs))
    print("Objective Value:", data.calculate_objective(solution_dfs))
    print("Elapsed Time (sec):", end_time - start_time)
    print()

    # UCS
    print("UCS")
    ucs = UCS(data)
    start_time = time.time()
    solution_ucs = ucs.solve()
    end_time = time.time()

    print("Feasibility:", data.is_feasible(solution_ucs))
    print("Objective Value:", data.calculate_objective(solution_ucs))
    print("Elapsed Time (sec):", end_time - start_time)
    print()

    # A*
    print("A*")
    a_star = AStar(data)
    start_time = time.time()
    solution_a_star = a_star.solve()
    end_time = time.time()

    print("Feasibility:", data.is_feasible(solution_a_star))
    print("Objective Value:", data.calculate_objective(solution_a_star))
    print("Elapsed Time (sec):", end_time - start_time)
    print()