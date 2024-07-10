# Farid Gahramanov - S023378


from typing import List, Set
from Solver import Solver, Solution
from Node import Node

class DFS(Solver):
    def solve(self) -> Solution:
        node_stack = [[self.data.depot_node]]
        marked_nodes: Set[Node] = set()
        capacity_limit = self.data.vehicle_capacity

        while node_stack:
            path = node_stack.pop()
            last_node = path[-1]

            load = sum(node.load for node in path[1:] if node.is_store)

            if last_node.is_depot and self.checkAllNodes(path):
                return path

            for node in self.data.nodes:
                if node.is_store and node not in marked_nodes:
                    new_load = load + node.load
                    if new_load <= capacity_limit:
                        extended_path = path + [node]
                        node_stack.append(extended_path)
                        marked_nodes.add(node)

        return path
    def checkAllNodes(self, path: List[Node]) -> bool:
        all_store_nodes = {node for node in self.data.nodes if node.is_store}
        visited_nodes = {node for node in path if node.is_store}
        return visited_nodes == all_store_nodes
