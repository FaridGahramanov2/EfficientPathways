# Farid Gahramanov - S023378

from queue import PriorityQueue
from typing import List
from Solver import Solver, Solution
from Node import Node

class UCS(Solver):
    def solve(self) -> Solution:
        node_queue = PriorityQueue()
        node_queue.put((0, [self.data.depot_node]))
        cost_tracker = {self.data.depot_node: 0}
        capacity_limit = self.data.vehicle_capacity
        marked_nodes = set()

        while not node_queue.empty():
            total_cost, path = node_queue.get()
            last_node = path[-1]

            load_amount = sum(node.load for node in path[1:] if node.is_store)

            if last_node.is_depot and self.checkAllNodes(path):
                return path

            for node in self.data.nodes:
                if node.is_store and node not in marked_nodes:
                    new_cost = total_cost + self.data.get_distance(last_node, node)
                    new_load = load_amount + node.load

                    if new_load <= capacity_limit and new_cost < cost_tracker.get(node, float('inf')):
                        extended_path = path + [node]
                        node_queue.put((new_cost, extended_path))
                        marked_nodes.add(node)
                        cost_tracker[node] = new_cost

        return path

    def checkAllNodes(self, path: List[Node]) -> bool:
        store_nodes_set = {node for node in self.data.nodes if node.is_store}
        visited_nodes_set = {node for node in path if node.is_store}
        return visited_nodes_set == store_nodes_set
