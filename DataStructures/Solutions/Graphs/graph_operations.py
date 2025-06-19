from collections import defaultdict, deque
import heapq
from types import GeneratorType

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f'Node({self.val})'

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
    def has_path(graph, start, end):
        '''
        Check if there is a path between two vertices

        Args:
            graph: dict representing adjacency list
            start: starting vertex
            end: target vertex

        Returns:
            boolean: True if path exists, false otherwise

        Q) Which traversal algorithm should we use?
            a) Either DFS or BFS works - we just need to check reachability
        Q) Can we optimize the search?
            a) Yes, just return early when target is found
        Q) What if start equals end?
            a) Return True (trivial path of length 0)
        Q) What is the time and space complexity?
            a) Time complexity is O(V + E)
            a) Space complexity is O(V)

        Example Walkthrough) graph = {"A": [("B", 1)], "B": [("C", 1)], "C": [], "D": []}
            1. has_path(graph, 'A', 'C') -> True
            2. has_path(graph, 'A', 'D') -> False
        '''

        # trivial case where start and end are the same
        if start == end:
            return True

        if start not in graph:
            return False

        visited = set()
        stack = [start] # use DFS with the stack

        while stack:
            vertex = stack.pop()

            if vertex == end:
                return True

            if vertex not in visited:
                visited.add(vertex)

                if vertex in graph:
                    for neighbor, _ in graph[vertex]:
                        stack.append(neighbor)

        return False


    @staticmethod
    def find_connected_components(graph):
        '''
        Find all connected components in an undirected graph

        Args:
            graph: dict representing adjacency list

        Returns:
            list: list of connected components (each component is a list of vertices)

        Q) What is a connected component?
            a) Maximal set of vertices where there's a path between any two
        Q) How do we find all components?
            a) Run DFS from each unvisited vertex
        Q) Why is this useful?
            a) Network analysis, clustering, finding isolated groups
        Q) What is the time and space complexity?
            a) Time complexity is O(V + E)
            a) Space complexity is O(V)

        Example Walkthrough) graph = {"A": [("B", 1)], "B": [("A", 1)], "C": [("D", 1)], "D": [("C", 1)], "E": []}
            Result: [["A", "B"], ["C", "D"], ["E"]]
        '''

        visited = set()
        components = []

        def dfs_component(vertex, component):
            visited.add(vertex)
            component.append(vertex)

            # recursively visit all unvisited neighbors
            if vertex in graph:
                for neighbor, _ in graph[vertex]:
                    if neighbor not in visited:
                        dfs_component(neighbor, component)

        # start DFS from each unvisited vertex
        for vertex in graph:
            if vertex not in visited:
                component = []
                dfs_component(vertex, component)
                components.append(component)

        return components



    @staticmethod
    def shortest_path_unweighted(graph, start, end):
        '''
        Find shortest path in unweighted graph using BFS

        Args:
            graph: dict representing unweighted graph using BFS
            start: starting vertex
            end: target vertex

        Returns:
            list: path from start to end, empty if no path exists

        Q) Why does BFS find shortest path?
            a) BFS explores vertices level by level, guaranteeing shortest distance
        Q) How do we reconstruct the path?
            a) Track parent pointers during BFS, then backtrack from end to start
        Q) What if multiple shortest paths exist?
            a) Return the one found first by BFS
        Q) What is the time and space complexity?
            a) Time complexity is O(V + E)
            a) Space complexity is O(V)

        Example Walkthrough) graph = {"A": [("B", 1), ("C", 1)], "B": [("D", 1)], "C": [("D", 1)], "D": []}
            1. shortest_path_unweighted(graph, 'A', 'D')
            2. result = ['A', 'B', 'D'] or ['A', 'C', 'D']
        '''

        # handle edge cases
        if start == end:
            return [start]
        if start not in graph:
            return []

        visited = set()
        queue = deque([start])
        parent = {start: None} # track parent pointers for path reconstruction

        while queue:
            vertex = queue.popleft()

            if vertex not in visited:
                visited.add(vertex)

            # check if we reached the target
            if vertex == end:
                # reconstruct path by following parent pointers
                path = []
                current = end
                while current is not None:
                    path.append(current)
                    current = parent[current]
                return path[::-1]

            if vertex in graph:
                for neighbor, _ in graph[vertex]:
                    if neighbor not in visited and neighbor not in parent:
                        parent[neighbor] = vertex
                        queue.append(neighbor)


        return []




