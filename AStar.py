# Farid Gahramanov - S023378


from queue import PriorityQueue
from typing import List
from Solver import Solver, Solution
from Node import Node

class AStar(Solver):
    def __init__(self, data):
        super().__init__(data)
        self.heuristics = {
            node.id: self.heuristic(node) for node in data.nodes
        }

    def solve(self) -> Solution:
        open_paths = PriorityQueue()
        open_paths.put((0, [self.data.depot_node]))
        node_costs = {self.data.depot_node: 0}

        while not open_paths.empty():
            current_cost, current_path = open_paths.get()
            current_node = current_path[-1]

            if current_node.is_depot and self.checkAllNodes(current_path):
                return current_path
            path_load = sum(node.load for node in current_path if node.is_store)
            for neighbor in self.data.nodes:
                if neighbor not in current_path and neighbor.is_store:
                    new_cost = current_cost + self.data.get_distance(current_node, neighbor)
                    new_load = path_load + neighbor.load

                    if new_load <= self.data.vehicle_capacity and new_cost < node_costs.get(neighbor, float('inf')):
                        new_path = current_path + [neighbor]
                        open_paths.put((new_cost + self.heuristics[neighbor.id], new_path))
                        node_costs[neighbor] = new_cost

        return current_path
    def heuristic(self, node: Node) -> float:
        return self.data.get_distance(node, self.data.depot_node)
    def checkAllNodes(self, path: List[Node]) -> bool:
        # Ensure all store nodes are visited in the path
        store_nodes = {node for node in self.data.nodes if node.is_store}
        visited_store_nodes = {node for node in path if node.is_store}
        return visited_store_nodes == store_nodes
