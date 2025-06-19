import sys
import os
import argparse
import traceback

def setup_imports():
    """Set up imports based on the command-line argument."""
    parser = argparse.ArgumentParser(description='Test graph operations')
    parser.add_argument('--mode', choices=['solution', 'practice'], default='solution',
                      help='Which implementation to test (solution or practice)')
    args = parser.parse_args()

    # Get the current directory and project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))

    if args.mode == 'solution':
        # Import from Solutions
        solutions_dir = os.path.join(project_root, 'Solutions', 'Graphs')
        sys.path.insert(0, solutions_dir)
        print(f"Testing solution implementation from: {solutions_dir}")
    else:
        # Import from Practice
        practice_dir = os.path.join(project_root, 'Practice', 'Graphs')
        sys.path.insert(0, practice_dir)
        print(f"Testing practice implementation from: {practice_dir}")

# Setup the path and import
setup_imports()

try:
    from graph_operations import GraphOperations, Node
except ImportError as e:
    print(f"❌ Could not import GraphOperations: {e}")
    print("Make sure the file exists in Solutions/Graphs/ or Practice/Graphs/")
    sys.exit(1)

def safe_test(test_name, test_func):
    """Wrapper to safely run tests with detailed error reporting"""
    print(f"\n{'='*60}")
    print(f"🧪 TESTING: {test_name}")
    print('='*60)

    try:
        test_func()
        print(f"✅ {test_name} - ALL TESTS PASSED!")
        return True
    except AssertionError as e:
        print(f"❌ {test_name} - ASSERTION FAILED:")
        print(f"   Error: {e}")
        print(f"   Location: {traceback.format_exc().splitlines()[-2].strip()}")
        return False
    except Exception as e:
        print(f"❌ {test_name} - UNEXPECTED ERROR:")
        print(f"   Error Type: {type(e).__name__}")
        print(f"   Error Message: {e}")
        print(f"   Full Traceback:")
        traceback.print_exc()
        return False

def create_simple_graph():
    """Create simple test graph: A-B-C, A-D"""
    edges = [("A", "B"), ("B", "C"), ("A", "D")]
    return GraphOperations.create_adjacency_list(edges, directed=False)

def create_weighted_graph():
    """Create weighted test graph"""
    edges = [("A", "B", 4), ("A", "C", 2), ("B", "D", 3), ("C", "D", 1)]
    return GraphOperations.create_adjacency_list(edges, directed=False)

def create_directed_graph():
    """Create directed test graph"""
    edges = [("A", "B"), ("B", "C"), ("C", "D"), ("A", "D")]
    return GraphOperations.create_adjacency_list(edges, directed=True)

def create_test_node_graph():
    """Create node-based graph for clone test"""
    # Create nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    # Set up connections
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2]
    node4.neighbors = [node1]

    return node1

def test_create_adjacency_list():
    """Test create_adjacency_list function"""
    print("Step 1: Testing unweighted undirected graph...")

    edges = [("A", "B"), ("B", "C"), ("A", "C")]
    graph = GraphOperations.create_adjacency_list(edges, directed=False)
    expected = {
        "A": [("B", 1), ("C", 1)],
        "B": [("A", 1), ("C", 1)],
        "C": [("B", 1), ("A", 1)]
    }

    print(f"   Created graph: {graph}")
    print(f"   Expected structure: {expected}")

    # Check that all vertices exist
    assert "A" in graph and "B" in graph and "C" in graph

    # Check that edges are bidirectional
    assert ("B", 1) in graph["A"] and ("A", 1) in graph["B"]

    print("\nStep 2: Testing weighted directed graph...")

    weighted_edges = [("X", "Y", 5), ("Y", "Z", 3)]
    weighted_graph = GraphOperations.create_adjacency_list(weighted_edges, directed=True)

    print(f"   Weighted graph: {weighted_graph}")

    assert weighted_graph["X"] == [("Y", 5)]
    assert weighted_graph["Y"] == [("Z", 3)]
    if 'Z' in weighted_graph:
        assert weighted_graph["Z"] == []
    else:
        print(" Note: Z is not in graph (appears only as destination)")
        assert True
    print("\nStep 3: Testing mixed weighted/unweighted edges...")

    mixed_edges = [("A", "B"), ("B", "C", 10)]
    mixed_graph = GraphOperations.create_adjacency_list(mixed_edges, directed=False)

    print(f"   Mixed graph: {mixed_graph}")

    assert ("B", 1) in mixed_graph["A"]  # Unweighted gets weight 1
    assert ("C", 10) in mixed_graph["B"]  # Weighted keeps its weight

    print("✓ create_adjacency_list tests passed")

def test_dfs_recursive():
    """Test dfs_recursive function"""
    print("Step 1: Testing DFS on simple graph...")

    graph = create_simple_graph()
    result = GraphOperations.dfs_recursive(graph, "A")

    print(f"   DFS from A: {result}")
    print(f"   Graph: {graph}")

    # Check that all reachable nodes are visited
    assert "A" in result
    assert "B" in result
    assert "C" in result
    assert "D" in result
    assert len(result) == 4

    # Check that A is first (starting node)
    assert result[0] == "A"

    print("\nStep 2: Testing DFS on empty graph...")

    empty_result = GraphOperations.dfs_recursive({}, "A")
    print(f"   DFS on empty graph: {empty_result}")
    assert empty_result == [] or empty_result == ['A']

    print("\nStep 3: Testing DFS with single node...")

    single_graph = {"X": []}
    single_result = GraphOperations.dfs_recursive(single_graph, "X")
    print(f"   DFS on single node: {single_result}")
    assert single_result == ["X"]

    print("✓ dfs_recursive tests passed")

def test_bfs():
    """Test bfs function"""
    print("Step 1: Testing BFS on simple graph...")

    graph = create_simple_graph()
    result = GraphOperations.bfs(graph, "A")

    print(f"   BFS from A: {result}")
    print(f"   Graph: {graph}")

    # Check that all reachable nodes are visited
    assert "A" in result
    assert "B" in result
    assert "C" in result
    assert "D" in result
    assert len(result) == 4

    # Check that A is first (starting node)
    assert result[0] == "A"

    # BFS should visit neighbors before going deeper
    a_index = result.index("A")
    b_index = result.index("B")
    d_index = result.index("D")
    c_index = result.index("C")

    # B and D should come before C (they're closer to A)
    assert b_index < c_index
    assert d_index < c_index

    print("\nStep 2: Testing BFS on disconnected components...")

    disconnected = {"A": [("B", 1)], "B": [("A", 1)], "C": []}
    result = GraphOperations.bfs(disconnected, "A")
    print(f"   BFS from A on disconnected: {result}")

    # Should only visit A and B, not C
    assert "A" in result and "B" in result
    assert "C" not in result

    print("✓ bfs tests passed")

def test_has_path():
    """Test has_path function"""
    print("Step 1: Testing path existence...")

    graph = create_simple_graph()

    # Test existing path
    result = GraphOperations.has_path(graph, "A", "C")
    print(f"   Path A->C exists: {result} (expected: True)")
    assert result == True

    # Test path to same node
    result = GraphOperations.has_path(graph, "A", "A")
    print(f"   Path A->A exists: {result} (expected: True)")
    assert result == True

    print("\nStep 2: Testing non-existent path...")

    disconnected = {"A": [("B", 1)], "B": [("A", 1)], "C": []}
    result = GraphOperations.has_path(disconnected, "A", "C")
    print(f"   Path A->C in disconnected: {result} (expected: False)")
    assert result == False

    print("\nStep 3: Testing non-existent start node...")

    result = GraphOperations.has_path(graph, "Z", "A")
    print(f"   Path from non-existent Z->A: {result} (expected: False)")
    assert result == False

    print("✓ has_path tests passed")

def test_find_connected_components():
    """Test find_connected_components function"""
    print("Step 1: Testing connected components...")

    # Create graph with 3 components: {A,B,C}, {D,E}, {F}
    disconnected = {
        "A": [("B", 1)], "B": [("A", 1), ("C", 1)], "C": [("B", 1)],
        "D": [("E", 1)], "E": [("D", 1)],
        "F": []
    }

    components = GraphOperations.find_connected_components(disconnected)
    print(f"   Connected components: {components}")

    # Should find 3 components
    assert len(components) == 3

    # Check that each component has the right vertices
    component_sets = [set(comp) for comp in components]

    assert {"A", "B", "C"} in component_sets
    assert {"D", "E"} in component_sets
    assert {"F"} in component_sets

    print("\nStep 2: Testing fully connected graph...")

    connected = create_simple_graph()
    components = GraphOperations.find_connected_components(connected)
    print(f"   Components in connected graph: {components}")

    # Should be only 1 component
    assert len(components) == 1
    assert set(components[0]) == {"A", "B", "C", "D"}

    print("✓ find_connected_components tests passed")

def test_shortest_path_unweighted():
    """Test shortest_path_unweighted function"""
    print("Step 1: Testing shortest path...")

    graph = create_simple_graph()
    path = GraphOperations.shortest_path_unweighted(graph, "A", "C")

    print(f"   Path A->C: {path}")
    print(f"   Graph: {graph}")

    # Should find a path
    assert len(path) > 0
    assert path[0] == "A"
    assert path[-1] == "C"

    # Check path length (should be 2: A->B->C)
    assert len(path) == 3

    print("\nStep 2: Testing path to same node...")

    path = GraphOperations.shortest_path_unweighted(graph, "A", "A")
    print(f"   Path A->A: {path} (expected: ['A'])")
    assert path == ["A"]

    print("\nStep 3: Testing no path...")

    disconnected = {"A": [("B", 1)], "B": [("A", 1)], "C": []}
    path = GraphOperations.shortest_path_unweighted(disconnected, "A", "C")
    print(f"   Path A->C (no connection): {path} (expected: [])")
    assert path == []

    print("✓ shortest_path_unweighted tests passed")

def test_clone_graph():
    """Test clone_graph function"""
    print("Step 1: Testing graph cloning...")

    original = create_test_node_graph()
    cloned = GraphOperations.clone_graph(original)

    print(f"   Original node value: {original.val}")
    print(f"   Cloned node value: {cloned.val}")

    # Values should be the same
    assert cloned.val == original.val

    # But objects should be different
    assert cloned is not original

    # Check that structure is preserved
    assert len(cloned.neighbors) == len(original.neighbors)

    # Check that neighbor values match but objects are different
    original_neighbor_vals = [n.val for n in original.neighbors]
    cloned_neighbor_vals = [n.val for n in cloned.neighbors]

    assert sorted(original_neighbor_vals) == sorted(cloned_neighbor_vals)

    # Ensure no shared references
    for orig_neighbor, cloned_neighbor in zip(original.neighbors, cloned.neighbors):
        assert orig_neighbor is not cloned_neighbor

    print("\nStep 2: Testing empty graph cloning...")

    result = GraphOperations.clone_graph(None)
    print(f"   Clone of None: {result} (expected: None)")
    assert result is None

    print("✓ clone_graph tests passed")

def test_course_schedule():
    """Test course_schedule function"""
    print("Step 1: Testing valid course schedule...")

    # 4 courses: 1 depends on 0, 2 depends on 0, 3 depends on 1 and 2
    result = GraphOperations.course_schedule(4, [[1,0],[2,0],[3,1],[3,2]])
    print(f"   Can finish courses [[1,0],[2,0],[3,1],[3,2]]: {result} (expected: True)")
    assert result == True

    print("\nStep 2: Testing impossible course schedule (cycle)...")

    # Cycle: 1 depends on 0, 0 depends on 1
    result = GraphOperations.course_schedule(2, [[1,0],[0,1]])
    print(f"   Can finish courses [[1,0],[0,1]]: {result} (expected: False)")
    assert result == False

    print("\nStep 3: Testing no prerequisites...")

    result = GraphOperations.course_schedule(3, [])
    print(f"   Can finish 3 courses with no prereqs: {result} (expected: True)")
    assert result == True

    print("✓ course_schedule tests passed")

def test_number_of_islands():
    """Test number_of_islands function"""
    print("Step 1: Testing island counting...")

    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    result = GraphOperations.number_of_islands(grid)
    print(f"   Number of islands: {result} (expected: 3)")
    assert result == 3

    print("\nStep 2: Testing no islands...")

    water_grid = [
        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]
    ]

    result = GraphOperations.number_of_islands(water_grid)
    print(f"   Islands in all water: {result} (expected: 0)")
    assert result == 0

    print("\nStep 3: Testing single large island...")

    land_grid = [
        ["1","1"],
        ["1","1"]
    ]

    result = GraphOperations.number_of_islands(land_grid)
    print(f"   Single large island: {result} (expected: 1)")
    assert result == 1

    print("\nStep 4: Testing empty grid...")

    result = GraphOperations.number_of_islands([])
    print(f"   Empty grid: {result} (expected: 0)")
    assert result == 0

    print("✓ number_of_islands tests passed")

def test_word_ladder():
    """Test word_ladder function"""
    print("Step 1: Testing word transformation...")

    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot","dot","dog","lot","log","cog"]

    result = GraphOperations.word_ladder(begin_word, end_word, word_list)
    print(f"   Transformation length hit->cog: {result} (expected: 5)")
    print("   → Path: hit->hot->dot->dog->cog")
    assert result == 5

    print("\nStep 2: Testing impossible transformation...")

    result = GraphOperations.word_ladder("hit", "cog", ["hot","dot","dog","lot","log"])
    print(f"   Impossible transformation: {result} (expected: 0)")
    assert result == 0

    print("\nStep 3: Testing same word...")

    result = GraphOperations.word_ladder("hit", "hit", ["hit"])
    print(f"   Same word transformation: {result} (expected: 1)")
    assert result == 1

    print("✓ word_ladder tests passed")

def test_dijkstra_shortest_path():
    """Test dijkstra_shortest_path function"""
    print("Step 1: Testing Dijkstra's algorithm...")

    graph = create_weighted_graph()
    distances = GraphOperations.dijkstra_shortest_path(graph, "A")

    print(f"   Distances from A: {distances}")
    print(f"   Graph: {graph}")

    # Check expected distances
    assert distances["A"] == 0
    assert distances["B"] == 4  # Direct path A->B
    assert distances["C"] == 2  # Direct path A->C
    assert distances["D"] == 3  # Path A->C->D (2+1)

    print("\nStep 2: Testing with different start...")

    distances = GraphOperations.dijkstra_shortest_path(graph, "C")
    print(f"   Distances from C: {distances}")

    assert distances["C"] == 0
    assert distances["D"] == 1  # Direct path C->D

    print("✓ dijkstra_shortest_path tests passed")

def test_friend_circles():
    """Test friend_circles function"""
    print("Step 1: Testing friend circles...")

    # 3 people: 0-1 are friends, 2 is alone
    is_connected = [[1,1,0],[1,1,0],[0,0,1]]
    result = GraphOperations.friend_circles(is_connected)

    print(f"   Friend circles in {is_connected}: {result} (expected: 2)")
    assert result == 2

    print("\nStep 2: Testing all friends...")

    # Everyone is friends with everyone
    all_friends = [[1,1,1],[1,1,1],[1,1,1]]
    result = GraphOperations.friend_circles(all_friends)
    print(f"   All friends: {result} (expected: 1)")
    assert result == 1

    print("\nStep 3: Testing no friendships...")

    # No one is friends
    no_friends = [[1,0,0],[0,1,0],[0,0,1]]
    result = GraphOperations.friend_circles(no_friends)
    print(f"   No friendships: {result} (expected: 3)")
    assert result == 3

    print("✓ friend_circles tests passed")

def test_valid_tree():
    """Test valid_tree function"""
    print("Step 1: Testing valid tree...")

    # Valid tree: 4 nodes, 3 edges, connected, no cycles
    result = GraphOperations.valid_tree(5, [[0,1],[0,2],[0,3],[1,4]])
    print(f"   Valid tree structure: {result} (expected: True)")
    assert result == True

    print("\nStep 2: Testing invalid tree (too many edges)...")

    # Too many edges -> cycle
    result = GraphOperations.valid_tree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])
    print(f"   Too many edges: {result} (expected: False)")
    assert result == False

    print("\nStep 3: Testing disconnected graph...")

    # Right number of edges but disconnected
    result = GraphOperations.valid_tree(4, [[0,1],[2,3]])
    print(f"   Disconnected: {result} (expected: False)")
    assert result == False

    print("\nStep 4: Testing single node...")

    result = GraphOperations.valid_tree(1, [])
    print(f"   Single node: {result} (expected: True)")
    assert result == True

    print("✓ valid_tree tests passed")

def test_find_path_with_obstacles():
    """Test find_path_with_obstacles function"""
    print("Step 1: Testing pathfinding with obstacles...")

    grid = [[0,0,1],[0,0,0],[1,0,0]]
    start = (0,0)
    end = (2,2)

    path = GraphOperations.find_path_with_obstacles(grid, start, end)

    print(f"   Path from {start} to {end}: {path}")
    print("   Grid layout:")
    for i, row in enumerate(grid):
        print(f"   {i}: {row}")

    # Should find a path
    assert len(path) > 0
    assert path[0] == start
    assert path[-1] == end

    # Check path is valid (no obstacles)
    for row, col in path:
        assert grid[row][col] == 0, f"Path goes through obstacle at {(row, col)}"

    print("\nStep 2: Testing impossible path...")

    blocked_grid = [[0,1],[1,0]]
    path = GraphOperations.find_path_with_obstacles(blocked_grid, (0,0), (1,1))
    print(f"   Blocked path: {path} (expected: [])")
    assert path == []

    print("\nStep 3: Testing start equals end...")

    path = GraphOperations.find_path_with_obstacles(grid, (0,0), (0,0))
    print(f"   Same start/end: {path} (expected: [(0,0)])")
    assert path == [(0,0)]

    print("\nStep 4: Testing obstacle at start...")

    path = GraphOperations.find_path_with_obstacles([[1,0],[0,0]], (0,0), (1,1))
    print(f"   Obstacle at start: {path} (expected: [])")
    assert path == []

    print("✓ find_path_with_obstacles tests passed")

def run_all_tests():
    """Run all test functions with detailed reporting"""
    print("🚀 STARTING COMPREHENSIVE GRAPH OPERATIONS TESTS")
    print("="*70)

    tests = [
        ("Create Adjacency List", test_create_adjacency_list),
        ("DFS Recursive", test_dfs_recursive),
        ("BFS", test_bfs),
        ("Has Path", test_has_path),
        ("Find Connected Components", test_find_connected_components),
        ("Shortest Path Unweighted", test_shortest_path_unweighted),
        ("Clone Graph", test_clone_graph),
        ("Course Schedule", test_course_schedule),
        ("Number of Islands", test_number_of_islands),
        ("Word Ladder", test_word_ladder),
        ("Dijkstra Shortest Path", test_dijkstra_shortest_path),
        ("Friend Circles", test_friend_circles),
        ("Valid Tree", test_valid_tree),
        ("Find Path with Obstacles", test_find_path_with_obstacles),
    ]

    passed = 0
    failed = 0

    for test_name, test_func in tests:
        if safe_test(test_name, test_func):
            passed += 1
        else:
            failed += 1

    print(f"\n{'='*70}")
    print(f"📊 FINAL RESULTS:")
    print(f"   ✅ Passed: {passed}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📈 Success Rate: {passed}/{passed + failed} ({100 * passed / (passed + failed):.1f}%)")

    if failed == 0:
        print("🎉 ALL TESTS PASSED! Your graph implementation is working correctly!")
    else:
        print("🔧 Some tests failed. Check the detailed output above to fix the issues.")

    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
