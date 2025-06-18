from collections import defaultdict, deque
import heapq
from types import GeneratorType


class GraphOperations:

    @staticmethod
    def create_adjacency_list(edges, directed=True):
        '''
        Create adjacency list representation from edge list

        Args:
            edges: list of tuples (u, v) or (u, v, weight) representing edges
            directed: boolean indicating if graph is directed

        Returns:
            dict: adjacency list representation

        Q) What is the time and space complexity?
            a) Time complexity is O(E) --> process each edge once
            a) Space complexity is O(V+E) --> store vertices and edges
        Q) How do we handle weighted v unweighted edges?
            a) CHeck tuple length (2 for unweighted, 3 for weighted)
        Q) What's the difference between directed and undirected?
            a) Undirected adds edge in both directions
        Q) How can you potentially think of u and v?
            a) Source and destination
        Q) How can you visualize weights?
            a) Number assigned to an edge that represents some cost, distance, or value of that connection (if cities are nodes, the edge weight could be miles)

        Example)
            edges = [('A' ,'B'), ('B', 'C', 5)]
            directed = False
            result = {'A': [('B', 1)], 'B':[('A', 1), ('C', 5)], 'C': [('B', 5)]}
        '''

        graph = defaultdict(list)

        for edge in edges:
            if len(edge) == 2:
                u, v = edge
                weight = 1
            else:
                u, v, weight = edge

            # add edge from u to v with weight
            graph[u].append((v, weight))

            # for undirected graphs, add the reverse edge as well
            if not directed:
                graph[v].append((u, weight))

        return dict(graph)


    @staticmethod
    def add_vertex(graph, vertex):
        '''
        Add a vertex to the graph

        Args:
            graph: dict representing adjacency list
            vertex: vertex to add

        Returns:
            dict: updated graph

        Q) What happens if the vertex already exists?
            a) No change
        Q) What is the time and space complexity?
            a) Time and space is O(1) -> dictionary lookup and assignment

        Example)
            graph = {'A': [('B', 1)]}
            add_vertex(graph, 'C')
            result = {'A': [('B', 1)], 'C': []}
        '''

        if vertex not in graph:
            graph[vertex] = [] # add an empty list just to ensure the vertex exists, even though it has no outgoing edge or weight (no destination)

        return graph


    @staticmethod
    def add_edge(graph, u, v, weight=1, directed=True):
        '''
        Add an edge to the graph

        Args:
            graph: dict representing adjacency list
            u: source vertex
            v: edge vertex
            weight: edge weight (default 1)
            directed: boolean indicating if edge is directed

        Returns:
            dict: updated graph

        Q) What if the vertices don't exist?
            a) Create them automatically
        Q) How do we handle duplicate edges?
            a) Allow duplicates
        Q) What is the time and space complexity?
            a) Time and space complexity are O(1)

        Example)
            graph = {}
            add_edge(graph, 'A', 'B', 5, directed=False)
            result = {'A': [('B', 5)], 'B':[('A', 5)]}
        '''

        # ensure vertices exist
        GraphOperations.add_vertex(graph, u)
        GraphOperations.add_vertex(graph, v)

        # add the edge from u to v with specified weight
        graph[u].append((v, weight))

        if not directed:
            graph[v].append((u, weight))

        return graph

    @staticmethod
    def remove_vertex(graph, vertex):
        '''
        Remove a vertex and all its edges from the graph

        Args:
            graph: dict representing adjacency list
            vertex: vertex to remove

        Returns:
            dict: updated graph

        Q) What is the time and space complexity?
            a) O(V + E) -> must check all vertices for edges to removed vertex
            a) Space complexity is O(1)
        Q) What if vertex doesn't exist?
            a) No change to graph
        '''

        if vertex not in graph:
            return graph

        # remove the vertex and its adjacency list
        del graph[vertex]

        # keep only neighbors that are not the removed vertex
        for v in graph:
            graph[v] = [(neighbor, weight) for neighbor, weight in graph[v] if neighbor != vertex]


        return graph


    @staticmethod
    def remove_edge(graph, u, v, directed=True):
        '''
        Remove an edge from the graph

        Args:
            graph: dict representing adjacency list
            u: source vertex
            v: destination vertex
            directed: boolean indicating if edge is directed

        Returns:
            dict: updated graph

        Q) What if edge doesn't exist?
            a) No change
        Q) How do we handle multiple edges between same vertices?
            a) Remove the first occurrence only
        Q) What is the time and space complexity?
            a) Time complexity is O(degree(u)) where degree(u) is the number of neighbors of graph[u] (i.e., the length of graph[u])
            a) Space complexity is O(1)
        '''

        if u in graph:
            # for each (neighbor, weight) pair in graph[u], include it only if the neighbor != v
            graph[u] = [(neighbor, weight) for neighbor, weight in graph[u] if neighbor != v]

        if v in graph and not directed:
            graph[v] = [(neighbor, weight) for neighbor, weight in graph[v] if neighbor != u]

        return graph


    @staticmethod
    def dfs_recursive(graph, start, visited=None):
        '''
        Perform depth first search recursively

        Args:
            graph: dict representing adjacency list
            start: starting vertex
            visited: set of visited vertices

        Returns:
            list: vertices in dfs order

        Q) What is the time and space complexity?
            a) Time complexity is is O(V + E)
            a) Space complexity is O(V) - recursion stack and visited set
        Q) How does DFS work?
            a) Go as deep as possible before backtracking
        Q) What is the difference from BFS?
            a) DFS uses stack (recursion), BFS uses queue

        Example Walkthrough) graph = {0: [1,2], 1: [3], 2:[3], 3:[]}
            0 → 1 → 3
            ↓
            → 2 → 3

            1. Start at 0, mark visited, add to result
            2. visit neighbor 1, mark visited, add to result
            3. visit neighbor 3, mark visited, add to result
            4. backtrack to 0, visit neighbor 2, already visited 3
            5. result = [0, 1, 3, 2]
        '''
        # initialized visited set on first call
        if visited ==  None:
            visited = set()

        # if vertex already visited, return empty list to prevent duplicate processing/infinite recursion
        if start in visited:
            return []

        visited.add(start)
        result = [start]

        if start in graph:
            for neighbor, _ in graph[start]: # unpack (neighbor, weight) tuple
                result.extend(GraphOperations.dfs_recursive(graph, neighbor, visited))

        return result



    @staticmethod
    def dfs_iterative(graph, start):
        '''
        Perform depth-first search iteratively using a stack

        Args:
            graph: dict representing adjacency list
            start: starting vertex

        Returns:
            list: vertices in DFS order

        Q) How does iterative DFS simulate recursion?
            a) Use explicit stack to track vertices to visit
        Q) What is the order of adding neighbors?
            a) Add in reverse order since stack is LIFO
        Q) What is time and space complexity?
            a) Time complexity is O(V + E)
            a) Space complexity is O(V)

        Example Walkthrough) graph = {0: [1,2], 1:[3], 2:[3], 3:[]}
            1. stack = [0], visited = {}, result: []
            2. pop 0, mark visited, add to result, push neighbors [2,1]
            3. stack = [2,1], visited = {0}, result: [0]
            4. pop 1, mark visited, add to result, push neighbor 3
            5. stack = [2,3], visited = {0, 1}, result = [0,1]
            6. continue until stack is empty
        '''

        if start not in graph:
            return []

        visited = set()
        stack = [start]
        result = []

        while stack:
            vertex = stack.pop() # LIFO

            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)

                # add neighbors to stack for future processing
                if vertex in graph:
                    # reverse order to maintain consistent traversal order, since stack reverses order when popping
                    for neighbor, _ in reversed(graph[vertex]):
                        if neighbor not in visited:
                            stack.append(neighbor)

        return result



    @staticmethod
    def bfs(graph, start):
        '''
        Perform breadth-first search using queue

        Args:
            graph: dict representing adjacency list
            start: starting vertex

        Returns:
            list: vertices in BFS order

        Q) How does BFS work?
            a) Visit all neighbors at current level before going deeper
        Q) What data structure does BFS use?
            a) Queue to ensure level-order traversal
        Q) What are BFS applications?
            a) Shortest path in unweighted graphs, level-order traversal
        Q) What is the time and space complexity?
            a) Time complexity is O(V + E)
            a) Space complexity is O(V)

        Example Walkthrough) {0: [1, 2], 1: [3], 2: [3], 3: []}
            1. queue = [0], visited = {}, result = []
            2. deque 0, mark visited, add to result, enqueue neighbors [1,2]
            3. queue = [1,2], visited = {0}, result = [0]
            4. deque 1, mark visited, add to result, enqueue neighbor 3
            5. queue = [2,3], visited = {0,1}, result = [0,1]
            6. Continue until queue empty
        '''

        if start not in graph:
            return []

        visited = set()
        queue = deque([start]) # initialize queue with starting vertex
        result = []

        while queue:
            vertex = queue.popleft() # FIFO

            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)

                # add all unvisited neighbors to queue for next level processing
                if vertex in graph:
                    for neighbor, _ in graph[vertex]:
                        if neighbor not in visited:
                            queue.append(neighbor)


        return result



    @staticmethod
    def has_cycle_directed(graph):
        '''
        Detect a cycle in a directed graph using DFS and recursion stack

        Args:
            graph: dict representing adjacency list

        Returns:
            bool: True if cycle exists, False otherwise


        Q) How do we detect cycles in directed graphs?
            a) Track nodes in current recursion path - back edge indicates cycle
        Q) What are the three states of a vertex?
            a) White (unvisited), grey (in current path), black (processed)
        Q) When do we detect a cycle?
            a) When we encounter a grey vertex
        Q) What is the time and space complexity?
            a) Time complexity is O(V + E)
            a) Space complexity is O(V)

        Example Walkthrough) graph = {0: [1], 1:[2], 2:[0]}
            1. start dfs from 0, mark as grey
            2. visit 1, mark as grey
            3. visit 2, mark as grey,
            4. visit 0, already grey -> cycle detected
        '''

        # create categorical tag
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {vertex: WHITE for vertex in graph}

        def dfs_visit(vertex):
            # back edge detected, found vertex already in current recursion path
            if color[vertex] == GRAY:
                return True

            # already fully processed this vertex and its subtree
            if color[vertex] == BLACK:
                return False

            # mark vertex as being in current path
            color[vertex] = GRAY

            # recursively visit all neighbors
            if vertex in graph:
                for neighbor, _ in graph[vertex]:
                    # ensure each neighbor has a color
                    if neighbor not in color:
                        color[neighbor] = WHITE
                    if dfs_visit(neighbor):
                        return True

            color[vertex] = BLACK # mark as processed
            return False

        # start DFS from every univisited vertex (handles disconnected components)
        for vertex in graph:
            if color[vertex] == WHITE:
                if dfs_visit(vertex):
                    return True

        return False



    @staticmethod
    def dijkstra_shortest_path(graph, start):
        '''
        Find shortest paths from start vertex using djikstra's algorithm

        Args:
            graph: dict representing weighted adjacency lists
            start: starting vertex

        Returns:
            dict: distances from start to all vertices

        Q) How does Dijkstra's algorithm work?
            a) Greedily select the nearest unvisited vertex and relax its edges
        Q) What data structure is used?
            a) Priority queue (min-heap) to efficiently get minimum distance vertex
        Q) What is the limitation?
            a) Doesn't work with negative edge weights
        Q) What is the time and space complexity?
            a) Time complexity is O((V + E) log V)
            a) Space complexity is O(V)

        Example Walkthrough) graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
            1. start = 0
            2. initial distances: {0: 0, others = inf)
            3. process 0: update dist[1] = 4, dist[2] = 1
            4. process 2: update dist[1] = min(4, (dist[2] + 2) -> dist[1] = 3 (going from 0->2->1 vs just 0->1)
            5. process 1: update dist[3] = dist[1] + 1 = 4
            6. process 3: no updates
        '''

        # initialize distances
        distances = {vertex: float('inf') for vertex in graph}
        distances[start] = 0

        # priority queue: (distance, vertex) tuples, min-heap by distance
        pq = [(0, start)]
        visited = set()

        while pq:
            # extract vertex with minimum distance
            current_dist, current_vertex = heapq.heappop(pq)

            # skip if already processed
            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            # relax all outgoing edges from current vertex
            if current_vertex in graph:
                for neighbor, weight in graph[current_vertex]:
                    # calculate new distance through current vertex
                    new_dist = current_dist + weight

                    # update distance if shorter than path found
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        # add to pq for future processing
                        heapq.heappush(pq, (new_dist, neighbor))

        return distances


    @staticmethod
    def bellman_ford(graph, start):
        '''
        Find the shortest paths from start vertex using bellman ford algorithm

        Args:
            graph: dict representing weighted adjacency list
            start: starting vertex

        Returns:
            tuple: (distances dict, boolean indicating if negative cycle exists)

        Q) How does bellman-ford differ from djiskstra?
            a) Bellman-Ford can handle negative weights and detect negative cycles
        Q) How many iterations does it need?
            a) V-1 iterations to find shortest paths, V to detect negative cycles
        Q) What is edge relaxation?
            a) Update distance if shorter path found: dist[v] = min(dist[v], dist[u] + weight(u,v))
        Q) What is time and space complexity?
            a) Time complexity is O(VE)
            a) Space complexity is O(V)

        Example Walkthrough) Graph with negative edge: {0: [(1, 1), (2, 4)], 1: [(2, -3), (3, 2)], 2: [(3, 3)], 3: []}
            1. iteration 1: dist[1] = 1, dist[2] = 4
            2. iteration 2: dist[2] = min(4, -2) = -2, dist[3] = dist[1] + 2 = 3
            3. iteration 3. dist[3] = min(3, dist[2] + 3) = min(3, 1) = 1
        '''

        # collect all vertices (including those that only appear as destinations)
        vertices = set(graph.keys())
        for vertex in graph:
            for neighbor, _ in graph[vertex]:
                vertices.add(neighbor)

        distances = {vertex: float('inf') for vertex in vertices}
        distances[start] = 0

        # relax all edges v-1 times to find shortest paths
        for _ in range(len(vertices) - 1):
            # check every edge in graph
            for vertex in graph:
                # only relax edges from reachable vertices
                if distances[vertex] != float('inf'):
                    for neighbor, weight in graph[vertex]:
                        if distances[vertex] + weight < distances[neighbor]:
                            distances[neighbor] = distances[vertex] + weight

        # check for negative cycles
        for vertex in graph:
            if distances[vertex] != float('inf'):
                for neighbor, weight in graph[vertex]:
                    # if we can still relax an edge, negative cycle exists
                    if distances[vertex] + weight < distances[neighbor]:
                        return distances, True

        return distances, False


    @staticmethod
    def floyd_warshall(graph):
        '''
        Find shortest paths between all pairs of vertices

        Args:
            graph: dict representing weighted adjacency list

        Returns:
            dict: distances between all pairs of vertices

        Q) What is the Floyd-Warshall algo?
            a) Dynamic programming approach for all-pairs shortest path
        Q) What is the recurrence relation?
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) for all k
        Q) When to use Floyd-Warshall vs Dijkstra V number of times?
            a) Floyd-Warshall for dense graphs, Dijkstra for sparse graphs
        Q) What is the time and space complexity?
            a) Time complexity is O(V^3)
            a) Space Complexity is O(V^2)

        Example Walkthrough) 3 vertices, k=1
            dist[0][2] = min(dist[0,2], dist[0][1] + dist[1][2])
            consider path 0->1->2 vs direct path 0->2
        '''

        # get all vertices
        vertices = set(graph.keys())
        for vertex in graph:
            for neighbor, _ in graph[vertex]:
                vertices.add(neighbor)

        vertices = list(vertices)
        n = len(vertices)

        # init distance matrix
        dist = {}
        for i in vertices:
            dist[i] = {}
            for j in vertices:
                if i == j:
                    dist[i][j] = 0
                else:
                    dist[i][j] = float('inf')

        # fill in direct edges
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                dist[vertex][neighbor] = weight

        # floyd warshall algorithm
        for k in vertices:
            for i in vertices:
                for j in vertices:
                    if dist[i][k]  + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[j][k]


        return dist



    @staticmethod
    def find_connected_components(graph):
        '''
        Find all connected components in undirected graph

        Args:
            graph: dict representing adjacency list

        Returns:
            list: list of connected components (each component is a list of vertices)

        Q) What is a connected component?
            a) Maximal set of vertices where there's a path between any two
        Q) How do we find all components?
            a) Run DFS from each unvisited vertex
        Q) What's the difference from strongly connected components?
            a) Connected components are for undirected graphs
        Q) What is the time and space complexity?
            a) Time complexity is O(V + E)
            a) Space complexity is O(V)

        Example Walkthrough) Graph: {0: [1], 1: [0], 2:[3], 3:[2], 4:[]}
            1. DFS from 0: visits {0, 1} - component 1
            2. DFS from 2: visits {2, 3} - component 2
            3. DFS from 4: visits {4} - component 3
            4. Result: [[0,1], [2,3], [4]]
        '''

        visited = set()


