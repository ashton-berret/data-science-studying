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



    @staticmethod
    def clone_graph(node):
        '''
        Clone/deep copy a graph given a reference to one of its nodes

        Args:
            node: a node object with val and neighbors list

        Returns:
            Node: cloned version of the input node's connected component

        Q) Why can't we just copy references?
            a) We need a completely separate graph structure
        Q) How do we handle cycles in a graph?
            a) Use the visited map to avoid infinite loops
        Q) What is the key insight?
            a) Map each original node to its clone to maintain relationships
        Q) What is the time and space complexity?
            a) Time complexity is O(V + E)
            a) Space complexity is O(V)
        '''

        if not node:
            return None

        visited = {}

        def dfs_clone(original):
            # if already cloned, return the clone
            clone = Node(original.val)
            visited[original] = clone # mark as visited before recursing

            for neighbor in original.neighbors:
                clone.neighbors.append(dfs_clone(neighbor))

            return clone

        return dfs_clone(node)



    @staticmethod
    def course_schedule(num_courses, prerequisites):
        '''
        Determine if you can finish all courses given prerequisites

        Args:
            num_courses: int number of courses (0 to numCourses - 1)
            prerequisites: list of [course, prerequisite] pairs

        Returns:
            boolean: true if can complete all, false otherwise

        Q) When is it impossible to complete a course?
            a) When there is a cycle in the prerequisite dependencies
        Q) How do we detect cycles in directed graphs?
            a) Use DFS with 3 colors: white, grey, black
        Q) What do the colors represent?
            a) unprocessed, in current path, processed
        Q) What is the time and space complexity?
            a) Time complexity is O(V + E)
            a) Space complexity is O(V)

        Example Walkthrough) num_courses = 4, prereqs = [[1,0], [2, 0], [3,1], [3,2]]
            course_dependencies = 0 -> 1 -> 3, 0->2->3
            result = True (can take in order: 0,1,2,3)
        '''

        # build adjacency list from prerequisites
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course) # prereq -> course

        WHITE, GRAY, BLACK = 0, 1, 2
        color = [WHITE] * num_courses

        def has_cycle(course):
            # gray node found, back edge indicates cycle
            if color[course] == GRAY:
                return True
            if color[course] == BLACK:
                return False

            color[course] = GRAY

            # check all dependent courses
            for dependent in graph[course]:
                if has_cycle(dependent):
                    return True

            color[course] = BLACK
            return False

        # check for cycles starting from any unvisited course
        for course in range(num_courses):
            if color[course] == WHITE:
                if has_cycle(course):
                    return False # cycle found, impossible

        return True



    @staticmethod
    def number_of_islands(grid):
        '''
        Count number of islands in a 2D binary grid

        Args:
            grid: 2D list where '1' represents land and '0' represents water

        Returns:
            int: number of islands


        Q) What represents an island?
            a) Connected group of '1's
        Q) What does connected mean?
            a) Adjacently horizontally or vertically
        Q) How do we avoid counting the same island multiple times?
            a) Mark visited cells by changing '1' to '0' or using visited set
        Q) What is the time and space complexity?
            a) Time complexity is O(rows * cols)
            a) SPace complexity is O(rows * cols)

        Example)  grid = [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ]
            Result: 3 islands
        '''

        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs_sink_island(row, col):
            # boundary check and water check
            if (row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0'):
                return

            # mark current land cell as visited by sinking it (turning it into water value)
            grid[row][col] = '0'

            # explore all 4 directions
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for dr, dc in directions:
                dfs_sink_island(row + dr, col + dc)


        # scan entire grid for land cells
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    island_count += 1
                    dfs_sink_island(row, col)

        return island_count



    @staticmethod
    def word_ladder(begin_word, end_word, word_list):
        '''
        Find the length of the shortest transformation sequence from begin_word to end_word

        Args:
            begin_word: start word
            end_word: target word
            word_list: list of valid intermediate words

        Returns:
            int: length of shortest transformation sequence, 0 if possible

        Q) What makes two words connected?
            a) Different by exactly one letter
        Q) Why use BFS instead of DFS?
            a) BFS finds shortest transformation sequence
        Q) How do we optimize neighbor finding?
            a) For each position, try all 26 letters instead of checking all words
        Q) What is the time and space complexity?
            a) Time complexity is O(M^2 * N) where M = word length, N = word list size
            a) Space complexity is O(M * N)

        Example Walkthrough)
            - begin_word = 'hit', end_word = 'cog'
            - word_list = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
            - result = 5 (hit -> hot -> dot -> dog -> cog)
        '''

        if end_word not in word_list:
            return 0


        # convert to set for O(1) lookup
        word_set = set(word_list)
        queue = deque([(begin_word, 1)]) # word, steps
        visited = {begin_word}

        while queue:
            current_word, steps = queue.popleft()

            if current_word == end_word:
                return steps

            # generate all possible one-letter transformations
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvqxyz':
                    if c == current_word[i]:
                        continue

                    # create new word by changing one letter
                    new_word = current_word[:i] + c + current_word[i+1:]

                    # check if valid transformation and not in visited
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, steps + 1))

        return 0




    @staticmethod
    def dijkstra_shortest_path(graph, start):
        '''
        Find the shortetst path from start vertex using Dijkstra's algo

        Args:
            graph: dict representing weighted adjacency list
            start: starting vertex

        Return:
            dict: distances from start to all vertices

        Q) How does Dijkstra's algorithm work?
            a) Greedily select nearerst unvisited vertex and relax its edges
        Q) What data structure is used?
            a) Priority queue (min-heap) to efficiently get minimum distance vertex
        Q) What's the limitation of Dijkstra's algorithm?
            a) Can't handle negative edge weights
        Q) What is the time and space complexity?
            a) Time complexity is O((V + E) log V)
            a) Space complexity is O(V)

        Example Walkthrough)
            graph = {"A": [("B", 4), ("C", 2)], "B": [("D", 3)], "C": [("D", 1)], "D": []}
            dijkstra_shortest_path(graph, "A")
            Result: {"A": 0, "B": 4, "C": 2, "D": 3} (shortest distances)
        '''

        # initialize distances: start=0, all others = inf
        distances = {vertex: float('inf') for vertex in graph}
        distances[start] = 0

        pq = [(0, start)] # distance, vertex
        visited = set()

        while pq:
            current_dist, current_vertex = heapq.heappop(pq)

            # skip if already processed bc of potential duplicate entries
            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            # relax all outgoing edges from current vertex
            if current_vertex in graph:
                for neighbor, weight in graph[current_vertex]:
                    new_dist = current_dist + weight

                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        # add to pq for future processing
                        heapq.heappush(pq, (new_dist, neighbor))

        return distances



    @staticmethod
    def friend_circles(is_connected):
        '''
        Find the number of circles in a social network

        Args:
            is_connected: 2D martix where is_connected[i][j] = 1 if two people are friends

        Returns:
            int: number of friend circles

        Q) What is a friend circle?
            a) A group where everyone is connected (directly or indirectly)
        Q) How is this different from the adjacency list representation?
            a) This uses adjacency matrix instead of list.
        Q) What is the relationship to connected components?
            a) Each friend circle is a connected component
        Q) What is the time and space complexity?
            a) Time complexity is O(N^2)
            a) Space complexity is O(n)

        Example)
            is_connected=  [[1,1,0], [1,1,0], [0,0,1]]
            result: 2 (circle 1: person 0 and person 1, circle 2 is person 2 alone)

                    Person:         0  1  2

                    Person 0:      [1, 1, 0]
                    Person 1:      [1, 1, 0]
                    Person 2:      [0, 0, 1]
        '''

        n = len(is_connected)
        visited = set()
        circles = 0

        def dfs_friend_circle(person):
            visited.add(person)

            for friend in range(n):
                # if they're friends and friend not in visited
                if is_connected[person][friend] == 1 and friend not in visited:
                    dfs_friend_circle(friend)

        # start DFS from each unvisited person
        for person in range(n):
            if person not in visited:
                circles += 1
                dfs_friend_circle(person)

        return circles




    @staticmethod
    def valid_tree(n, edges):
        '''
        Check if given edges will form a valid tree

        Args:
            n: number of nodes (labeled 0 to n-1)
            edges: list of undirected edges

        Returns:
            boolean: True if edges form a valid tree

        Q) What are the properties of a valid tree?
            a) Connected, has exactly n-1 edges, and no cycles
        Q) Can we check these properties efficiently?
            a) Check edge count first, the connectivity via DFS/BFS
        Q) Why exactly n-1 edges?
            a) Tree with n nodes needs exactly n-1 edges to be connected without cycles
        Q) What is the time and space complexity?
            a) Time complexity is O(V + E)
            a) Space complexity is O(V + E)
        '''

        if len(edges) != n - 1:
            return False

        # build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        stack = [0]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)


        # tree is valid if all nodes are reachable
        return len(visited) == n




    @staticmethod
    def find_path_with_obstacles(grid, start, end):
        '''
        Find path in grid with obstacles using BFS

        Args:
            grid: 2D matrix where 0 = empty, 1 = obstacle
            start: tuple (row, col) of start position
            end: tuple (row, col) of end position

        Returns:
            list: path as list of (row, col) tuples, empty if no path

        Q) Why use BFS?
            a) Guarantees shortest path in unweighted grids
        Q) How do we handle obstacles?
            a) Skip cells with value of 1 during exploration
        Q) How do we reconstruct the path?
            a) Track parent pointers using BFS then backtrack
        Q) What is the time and space complexity?
            a) Time complexity is O(rows * cols)
            a) Space complexity is O(rows * cols)

        Example)
            Grid: [[0,0,1],
                   [0,0,0],
                   [1,0,0]]

            Visual representation:
            (0,0) → (0,1) | (0,2)
              ↓       ↓   | WALL
            (1,0) → (1,1) → (1,2)
            WALL    ↓       ↓
            (2,0) → (2,1) → (2,2)
        '''

        if not grid or not grid[0]:
            return []

        rows, cols = len(grid), len(grid[0])
        start_row, start_col = start
        end_row, end_col = end

        # check if start or end positions are obstacles
        if grid[start_row][start_col] == 1 or  grid[end_row][end_col] == 1:
            return []

        # bfs setup
        queue = deque([start])
        visited = {start}
        parent = {}
        parent[start] = None
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            current_row, current_col = queue.popleft()

            if (current_row, current_col) == end:
                path = []
                current = end
                while current is not None:
                    path.append(current)
                    current = parent[current]
                return path[::-1] # reverse to get start -> end order

            # explore all four directions
            for dr, dc in directions:
                next_row, next_col = current_row + dr, current_col + dc
                next_pos = next_row, next_col

                # check bounds
                if (0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 0 and next_pos not in visited):
                    visited.add(next_pos)
                    parent[next_pos] = (current_row, current_col)
                    queue.append(next_pos)


        return []
