"""Optimal solution for shortest path.

single-source

unweighted          bfs             O(V+E)          linear
non-neg weighted    dijkstra        O(Vlog(V+E))
weighted            bellman-ford    O(VE)
acyclic             (sorted + 1     O(V+E)
                    iteration of
                    bellman-ford)
all-paths 

unweighted          bfs             O(V**2+VE) = O(VE)
non-neg weighted    dijkstra        O(V**2log(VE))
weighted            bellman-ford    O(V**2E)

"""

from collections import deque, defaultdict


class Graph(object):
    def __init__(self, vertex_count, adjacency_list=[]):
        self.V = vertex_count
        self.graph = []
        self.shortest_path = float('inf')
        self.neighbors = defaultdict(list)
        self.adjacency_list = adjacency_list
        if adjacency_list:
            for u in range(len(adjacency_list)):
                for v in range(len(adjacency_list[u])):
                    w = adjacency_list[u][v]
                    if w == float('inf'):
                        continue
                    self.add_edge(u, v, w)

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
        self.neighbors[u].append(v)

    def print_graph(self):
        print('Graph:')
        for edge in self.graph:
            self.print_a_to_b(src=edge[0], dest=edge[1], weight=edge[2])
        print('')

    def print_adjacency_list(self):
        print('Adjacency List:')
        for row in range(len(self.adjacency_list)):
            print(self.adjacency_list[row])
        print('')

    def print_a_to_b(self, src, dest, weight):
        print('({a}) -- {w} --> ({b})'.format(a=src, b=dest, w=weight))

    def print_a_to_all_b(self, src, shortest_paths):
        for i in range(self.V):
            self.print_a_to_b(src=src, dest=i, weight=shortest_paths[i])

    def bfs_a_to_b(self, src, dest, edge_weight=1):
        print('Shortest path from src to dest using bfs')
        print('Setting all weights to {} for bfs...'.format(edge_weight))
        queue = deque()
        queue.append(src)
        shortest_paths = [-1] * self.V
        shortest_paths[src] = 0
        while queue:
            node = queue.popleft()
            for neighbor in self.neighbors[node]:
                if shortest_paths[neighbor] >= 0:  # already visited 
                    continue
                queue.append(neighbor)
                shortest_paths[neighbor] = shortest_paths[node] + edge_weight
                if neighbor == dest:
                    self.print_a_to_b(src, dest, shortest_paths[neighbor])
                    print('')
                    return shortest_paths[neighbor]

    def bfs_a_to_all_b(self, src, edge_weight=1):
        print('Shortest path from src to all nodes using bfs')
        """Find shortest distance from src to all other vertices.
        """
        print('Setting all weights to {} for bfs...'.format(edge_weight))
        queue = deque()
        queue.append(src)
        shortest_paths = [-1] * self.V
        shortest_paths[src] = 0
        while queue:
            node = queue.popleft()
            for neighbor in self.neighbors[node]:
                if shortest_paths[neighbor] >= 0: # the neighbor has been visited
                    continue
                queue.append(neighbor)
                shortest_paths[neighbor] = shortest_paths[node] + edge_weight

        self.print_a_to_all_b(src, shortest_paths)
        print('')
        return shortest_paths

    def bellman_ford_a_to_b(self, src, dest):
        print('Shortest path from src to dest using bellman_ford')
        shortest_paths = [float('inf')] * self.V
        shortest_paths[src] = 0

        for i in range(self.V - 1):
            for u, v, w in self.graph:
                if shortest_paths[u] == float('inf'):
                    continue # this node hasn't been discovered yet
                if shortest_paths[u] + w < shortest_paths[v]:
                    shortest_paths[v] = shortest_paths[u] + w

            # check for negative weight cycles
            for u, v, w in self.graph:
                if shortest_paths[u] == float('inf'):
                    continue # this node hasn't been discovered yet
                if shortest_paths[u] + w < shortest_paths[v]:
                    print('negative weight cycle exists in the graph')
                    return
        self.print_a_to_b(src, dest, shortest_paths[dest])
        print('')
        return shortest_paths[dest]


    def bellman_ford(self, src):
        """Find shortest distance from src to all other vertices.
        """

        print('Shortest path from src to all nodes using bellman_ford')

        # Shortest paths holds the shortest distance from the src node to each 
        # node in the graph. Each index in the array represents a corresponding 
        # node in the graph, e.g. node 2's shortest distance from src will be 
        # stored at shortest_paths[2].
        shortest_paths = [float('inf')] * self.V
        # Distance from src to src is 0
        shortest_paths[src] = 0

        for i in range(self.V - 1): # Loop through V - 1 edges
            # Rexation Formula: update the distance between u and v if it is 
            # shorter than what's current stored
            for u, v, w in self.graph:
                # To start, only the distance to the src node is not infinity, 
                # so skip nodes until you reach the src node
                if shortest_paths[u] == float('inf'):
                    continue
                if shortest_paths[u] + w < shortest_paths[v]:
                    shortest_paths[v] = shortest_paths[u] + w

        # The above loop gets the shortest path if there are no negative
        # weight cycles. If we get a shorter path then there is a negative
        # weight cycle.
        for u, v, w in self.graph:
            if shortest_paths[u] == float('inf'):
                continue
            if shortest_paths[u] + w < shortest_paths[v]:
                print('negative weight cycle exists in the graph')
                return
        self.print_a_to_all_b(src, shortest_paths)
        print('')
        return shortest_paths

    def dijkstra(self, src):
        print('Shortest path from src to all nodes using dijkstra')

        dist = [float('inf')] * self.V
        dist[src] = 0
        shortest_path_set = [False] * self.V
        for v in range(self.V):
            # Pick the minimum distance vertex from 
            # the set of vertices not yet processed. 
            # nearest_neighbor is always equal to src in first iteration
            # Initilaize minimum distance for next node
            min = float('inf')
            # Search not nearest vertex not in the 
            # shortest path tree
            for v in range(self.V):
                if dist[v] < min and shortest_path_set[v] == False:
                    min = dist[v]
                    min_index = v
            nearest_neighbor = min_index

            # Put the minimum distance vertex in the 
            # shotest path tree
            shortest_path_set[nearest_neighbor] = True

            # Update dist value of the adjacent vertices 
            # of the picked vertex only if the current 
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if (self.adjacency_list[nearest_neighbor][v] > 0 and shortest_path_set[v] == False and dist[v] > dist[nearest_neighbor] + self.adjacency_list[nearest_neighbor][v]):
                    dist[v] = dist[nearest_neighbor] + self.adjacency_list[nearest_neighbor][v]
        self.print_a_to_all_b(src, dist)


if __name__ == '__main__':
    """
    Graph g

    adjacency_list: 
    [
        [INF,  -1,   4, INF, INF],
        [INF, INF,   3,   2,   2],
        [INF, INF, INF, INF, INF],
        [INF,   1,   5, INF, INF],
        [INF, INF, INF,  -3, INF]
    ]

    Setting the graph with the above adjacency list does the following:

    g.add_edge(u=0, v=1, w=-1)
    g.add_edge(u=0, v=2, w=4)
    g.add_edge(u=1, v=2, w=3)
    g.add_edge(u=1, v=3, w=2)
    g.add_edge(u=1, v=4, w=2)
    g.add_edge(u=3, v=2, w=5)
    g.add_edge(u=3, v=1, w=1)
    g.add_edge(u=4, v=3, w=-3)
    """
    INF = float('inf')
    adjacency_list = [
        [INF,  -1,   4, INF, INF],
        [INF, INF,   3,   2,   2],
        [INF, INF, INF, INF, INF],
        [INF,   1,   5, INF, INF],
        [INF, INF, INF,  -3, INF]]
    g = Graph(5, adjacency_list)
    g.print_graph()
    g.print_adjacency_list()
    g.bellman_ford(src=0)
    g.bellman_ford_a_to_b(src=0, dest=4)
    g.bfs_a_to_all_b(src=0)
    g.bfs_a_to_b(src=0, dest=4)
    g.dijkstra(src=0)

