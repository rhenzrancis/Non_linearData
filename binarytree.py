"""
Assessment 3.4 - Program for Diagram 2: Graph
Last name: MABIDA

The letters of the last name are the nodes. The two A's are labeled
A1 and A2 so they can be told apart. The graph is undirected and
stored as an adjacency list. Prints the BFS and DFS traversals.
"""

from collections import deque


class Graph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node):
        self.adj.setdefault(node, [])

    def add_edge(self, a, b):
        self.add_node(a)
        self.add_node(b)
        self.adj[a].append(b)
        self.adj[b].append(a)

    def bfs(self, start):
        """Breadth-First Search using a queue."""
        visited = {start}
        queue = deque([start])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start):
        """Depth-First Search using recursion."""
        visited = set()
        order = []

        def visit(node):
            visited.add(node)
            order.append(node)
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visit(neighbor)

        visit(start)
        return order

    def show(self):
        for node, neighbors in self.adj.items():
            print(f"{node}: {', '.join(neighbors)}")


if __name__ == "__main__":
    g = Graph()
    g.add_edge("M", "A1")
    g.add_edge("A1", "A2")
    g.add_edge("A1", "B")
    g.add_edge("B", "I")
    g.add_edge("I", "D")

    print("Graph for MABIDA (adjacency list)")
    g.show()

    print("\nBFS from M:", " -> ".join(g.bfs("M")))
    print("DFS from M:", " -> ".join(g.dfs("M")))