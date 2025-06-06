import sys
import os
import argparse
import traceback

def setup_imports():
    """Set up imports based on the command-line argument."""
    parser = argparse.ArgumentParser(description='Test backtracking operations')
    parser.add_argument('--mode', choices=['solution', 'practice'], default='solution',
                      help='Which implementation to test (solution or practice)')
    args = parser.parse_args()

    # Get the current directory and project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))

    if args.mode == 'solution':
        # Import from Solutions
        solutions_dir = os.path.join(project_root, 'Solutions', 'Backtracking')
        sys.path.insert(0, solutions_dir)
        print(f"Testing solution implementation from: {solutions_dir}")
    else:
        # Import from Practice
        practice_dir = os.path.join(project_root, 'Practice', 'Backtracking')
        sys.path.insert(0, practice_dir)
        print(f"Testing practice implementation from: {practice_dir}")

# Setup the path and import
setup_imports()

try:
    from backtracking_operations import BacktrackingOperations
except ImportError as e:
    print(f"❌ Could not import BacktrackingOperations: {e}")
    print("Make sure the file exists in Solutions/Backtracking/ or Practice/Backtracking/")
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

def test_generate_permutations():
    """Test permutation generation"""
    print("Step 1: Testing basic permutations...")

    nums = [1, 2, 3]
    result = BacktrackingOperations.generate_permutations(nums)
    expected = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

    print(f"   Input: {nums}")
    print(f"   Result: {result}")
    print(f"   Expected: {expected}")

    assert len(result) == 6, f"Expected 6 permutations, got {len(result)}"

    # Check all expected permutations are present
    for perm in expected:
        assert perm in result, f"Missing permutation: {perm}"

    print("\nStep 2: Testing single element...")
    nums = [5]
    result = BacktrackingOperations.generate_permutations(nums)
    expected = [[5]]
    print(f"   Single element {nums} -> {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 3: Testing empty array...")
    nums = []
    result = BacktrackingOperations.generate_permutations(nums)
    expected = [[]]
    print(f"   Empty array -> {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 4: Testing two elements...")
    nums = [1, 2]
    result = BacktrackingOperations.generate_permutations(nums)
    expected = [[1,2], [2,1]]
    print(f"   Two elements {nums} -> {result}")
    assert len(result) == 2, f"Expected 2 permutations, got {len(result)}"
    for perm in expected:
        assert perm in result, f"Missing permutation: {perm}"

    print("✓ generate_permutations tests passed")

def test_generate_combinations():
    """Test combination generation"""
    print("Step 1: Testing C(4,2)...")

    n, k = 4, 2
    result = BacktrackingOperations.generate_combinations(n, k)
    expected = [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]

    print(f"   Input: n={n}, k={k}")
    print(f"   Result: {result}")
    print(f"   Expected: {expected}")

    assert len(result) == 6, f"Expected 6 combinations, got {len(result)}"
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 2: Testing C(3,1)...")
    n, k = 3, 1
    result = BacktrackingOperations.generate_combinations(n, k)
    expected = [[1], [2], [3]]
    print(f"   C(3,1): {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 3: Testing C(3,3)...")
    n, k = 3, 3
    result = BacktrackingOperations.generate_combinations(n, k)
    expected = [[1,2,3]]
    print(f"   C(3,3): {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 4: Testing C(5,0)...")
    n, k = 5, 0
    result = BacktrackingOperations.generate_combinations(n, k)
    expected = [[]]
    print(f"   C(5,0): {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("✓ generate_combinations tests passed")

def test_generate_subsets():
    """Test subset generation"""
    print("Step 1: Testing subsets of [1,2,3]...")

    nums = [1, 2, 3]
    result = BacktrackingOperations.generate_subsets(nums)
    expected = [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

    print(f"   Input: {nums}")
    print(f"   Result: {result}")
    print(f"   Expected length: {len(expected)}")

    assert len(result) == 8, f"Expected 8 subsets, got {len(result)}"

    # Check all expected subsets are present
    for subset in expected:
        assert subset in result, f"Missing subset: {subset}"

    print("\nStep 2: Testing subsets of [1,2]...")
    nums = [1, 2]
    result = BacktrackingOperations.generate_subsets(nums)
    expected = [[], [1], [2], [1,2]]
    print(f"   Subsets of [1,2]: {result}")
    assert len(result) == 4, f"Expected 4 subsets, got {len(result)}"
    for subset in expected:
        assert subset in result, f"Missing subset: {subset}"

    print("\nStep 3: Testing subsets of []...")
    nums = []
    result = BacktrackingOperations.generate_subsets(nums)
    expected = [[]]
    print(f"   Subsets of []: {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 4: Testing subsets of [1]...")
    nums = [1]
    result = BacktrackingOperations.generate_subsets(nums)
    expected = [[], [1]]
    print(f"   Subsets of [1]: {result}")
    assert len(result) == 2, f"Expected 2 subsets, got {len(result)}"
    for subset in expected:
        assert subset in result, f"Missing subset: {subset}"

    print("✓ generate_subsets tests passed")

def test_solve_n_queens():
    """Test N-Queens solver"""
    print("Step 1: Testing 4-Queens...")

    n = 4
    result = BacktrackingOperations.solve_n_queens(n)
    print(f"   4-Queens solutions count: {len(result)}")
    print(f"   First solution:")
    if result:
        for row in result[0]:
            print(f"     {row}")

    # 4-Queens has exactly 2 solutions
    assert len(result) == 2, f"Expected 2 solutions for 4-Queens, got {len(result)}"

    # Validate first solution structure
    if result:
        solution = result[0]
        assert len(solution) == 4, f"Expected 4 rows, got {len(solution)}"
        for row in solution:
            assert len(row) == 4, f"Expected 4 columns, got {len(row)}"
            assert row.count('Q') == 1, f"Expected exactly 1 Queen per row, got {row.count('Q')}"

    print("\nStep 2: Testing 1-Queen...")
    n = 1
    result = BacktrackingOperations.solve_n_queens(n)
    expected = [["Q"]]
    print(f"   1-Queen: {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 3: Testing 2-Queens (no solution)...")
    n = 2
    result = BacktrackingOperations.solve_n_queens(n)
    print(f"   2-Queens: {result} (should be empty)")
    assert result == [], f"Expected no solutions for 2-Queens, got {result}"

    print("\nStep 4: Testing 3-Queens (no solution)...")
    n = 3
    result = BacktrackingOperations.solve_n_queens(n)
    print(f"   3-Queens: {result} (should be empty)")
    assert result == [], f"Expected no solutions for 3-Queens, got {result}"

    print("✓ solve_n_queens tests passed")

def test_solve_sudoku():
    """Test Sudoku solver"""
    print("Step 1: Testing solvable Sudoku...")

    # Easy Sudoku puzzle
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    print("   Initial board:")
    for row in board:
        print(f"     {' '.join(row)}")

    result = BacktrackingOperations.solve_sudoku(board)
    print(f"\n   Solvable: {result}")
    assert result == True, f"Expected True for solvable puzzle, got {result}"

    print("   Solved board:")
    for row in board:
        print(f"     {' '.join(row)}")

    # Verify solution - check no dots remain
    for row in board:
        for cell in row:
            assert cell != '.', f"Found unsolved cell: {cell}"

    print("\nStep 2: Testing unsolvable Sudoku...")
    # Create unsolvable puzzle (two 5s in same row)
    unsolvable_board = [
        ["5","5",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    result = BacktrackingOperations.solve_sudoku(unsolvable_board)
    print(f"   Unsolvable puzzle result: {result}")
    assert result == False, f"Expected False for unsolvable puzzle, got {result}"

    print("✓ solve_sudoku tests passed")

def test_generate_parentheses():
    """Test parentheses generation"""
    print("Step 1: Testing n=3...")

    n = 3
    result = BacktrackingOperations.generate_parentheses(n)
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]

    print(f"   Input: n={n}")
    print(f"   Result: {result}")
    print(f"   Expected: {expected}")

    assert len(result) == 5, f"Expected 5 combinations, got {len(result)}"
    for combo in expected:
        assert combo in result, f"Missing combination: {combo}"

    print("\nStep 2: Testing n=1...")
    n = 1
    result = BacktrackingOperations.generate_parentheses(n)
    expected = ["()"]
    print(f"   n=1: {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 3: Testing n=2...")
    n = 2
    result = BacktrackingOperations.generate_parentheses(n)
    expected = ["(())", "()()"]
    print(f"   n=2: {result}")
    assert len(result) == 2, f"Expected 2 combinations, got {len(result)}"
    for combo in expected:
        assert combo in result, f"Missing combination: {combo}"

    print("\nStep 4: Testing n=0...")
    n = 0
    result = BacktrackingOperations.generate_parentheses(n)
    expected = [""]
    print(f"   n=0: {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("✓ generate_parentheses tests passed")

def test_letter_combinations():
    """Test phone letter combinations"""
    print("Step 1: Testing digits '23'...")

    digits = "23"
    result = BacktrackingOperations.letter_combinations(digits)
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    print(f"   Input: {digits}")
    print(f"   Result: {result}")
    print(f"   Expected: {expected}")

    assert len(result) == 9, f"Expected 9 combinations, got {len(result)}"
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 2: Testing single digit '2'...")
    digits = "2"
    result = BacktrackingOperations.letter_combinations(digits)
    expected = ["a", "b", "c"]
    print(f"   Single digit '2': {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 3: Testing empty digits...")
    digits = ""
    result = BacktrackingOperations.letter_combinations(digits)
    expected = []
    print(f"   Empty digits: {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 4: Testing digit '7' (4 letters)...")
    digits = "7"
    result = BacktrackingOperations.letter_combinations(digits)
    expected = ["p", "q", "r", "s"]
    print(f"   Digit '7': {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("✓ letter_combinations tests passed")

def test_word_search():
    """Test word search in grid"""
    print("Step 1: Testing word 'ABCCED'...")

    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word = "ABCCED"

    print("   Board:")
    for row in board:
        print(f"     {row}")
    print(f"   Word: {word}")

    result = BacktrackingOperations.word_search(board, word)
    print(f"   Found: {result}")
    assert result == True, f"Expected True for word {word}, got {result}"

    print("\nStep 2: Testing word 'SEE'...")
    word = "SEE"
    result = BacktrackingOperations.word_search(board, word)
    print(f"   Word 'SEE' found: {result}")
    assert result == True, f"Expected True for word {word}, got {result}"

    print("\nStep 3: Testing word 'ABCB' (impossible)...")
    word = "ABCB"
    result = BacktrackingOperations.word_search(board, word)
    print(f"   Word 'ABCB' found: {result}")
    assert result == False, f"Expected False for word {word}, got {result}"

    print("\nStep 4: Testing single character word...")
    word = "A"
    result = BacktrackingOperations.word_search(board, word)
    print(f"   Word 'A' found: {result}")
    assert result == True, f"Expected True for word {word}, got {result}"

    print("\nStep 5: Testing empty board...")
    empty_board = []
    word = "A"
    result = BacktrackingOperations.word_search(empty_board, word)
    print(f"   Empty board with word 'A': {result}")
    assert result == False, f"Expected False for empty board, got {result}"

    print("✓ word_search tests passed")

def test_palindrome_partitioning():
    """Test palindrome partitioning"""
    print("Step 1: Testing string 'aab'...")

    s = "aab"
    result = BacktrackingOperations.palindrome_partitioning(s)
    expected = [["a","a","b"], ["aa","b"]]

    print(f"   Input: '{s}'")
    print(f"   Result: {result}")
    print(f"   Expected: {expected}")

    assert len(result) == 2, f"Expected 2 partitions, got {len(result)}"
    for partition in expected:
        assert partition in result, f"Missing partition: {partition}"

    print("\nStep 2: Testing string 'racecar'...")
    s = "racecar"
    result = BacktrackingOperations.palindrome_partitioning(s)
    print(f"   String 'racecar' partitions: {len(result)} found")

    # Check that "raceacar" itself is included (it's a palindrome)
    full_palindrome_found = False
    for partition in result:
        if partition == ["racecar"]:
            full_palindrome_found = True
            break
    assert full_palindrome_found, "Expected full string 'raceacar' as one partition"

    print("\nStep 3: Testing single character...")
    s = "a"
    result = BacktrackingOperations.palindrome_partitioning(s)
    expected = [["a"]]
    print(f"   Single char 'a': {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 4: Testing string 'aba'...")
    s = "aba"
    result = BacktrackingOperations.palindrome_partitioning(s)
    expected_partitions = [["a","b","a"], ["aba"]]
    print(f"   String 'aba': {result}")
    assert len(result) == 2, f"Expected 2 partitions, got {len(result)}"
    for partition in expected_partitions:
        assert partition in result, f"Missing partition: {partition}"

    print("✓ palindrome_partitioning tests passed")

def test_combination_sum():
    """Test combination sum"""
    print("Step 1: Testing candidates=[2,3,6,7], target=7...")

    candidates = [2, 3, 6, 7]
    target = 7
    result = BacktrackingOperations.combination_sum(candidates, target)
    expected = [[2,2,3], [7]]

    print(f"   Candidates: {candidates}")
    print(f"   Target: {target}")
    print(f"   Result: {result}")
    print(f"   Expected: {expected}")

    assert len(result) == 2, f"Expected 2 combinations, got {len(result)}"
    for combo in expected:
        # Check if combination exists (order might differ)
        found = False
        for res_combo in result:
            if sorted(combo) == sorted(res_combo):
                found = True
                break
        assert found, f"Missing combination: {combo}"

    print("\nStep 2: Testing candidates=[2,3,5], target=8...")
    candidates = [2, 3, 5]
    target = 8
    result = BacktrackingOperations.combination_sum(candidates, target)
    print(f"   Target 8 combinations: {result}")

    # Verify all combinations sum to target
    for combo in result:
        assert sum(combo) == target, f"Combination {combo} doesn't sum to {target}"

    print("\nStep 3: Testing no solution case...")
    candidates = [2]
    target = 3
    result = BacktrackingOperations.combination_sum(candidates, target)
    expected = []
    print(f"   No solution case: {result}")
    assert result == expected, f"Expected no solutions, got {result}"

    print("✓ combination_sum tests passed")

def test_subset_sum_exists():
    """Test subset sum existence"""
    print("Step 1: Testing nums=[3,34,4,12,5,2], target=9...")

    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    result = BacktrackingOperations.subset_sum_exists(nums, target)

    print(f"   Input: {nums}")
    print(f"   Target: {target}")
    print(f"   Exists: {result}")

    assert result == True, f"Expected True (subset [4,5] sums to 9), got {result}"

    print("\nStep 2: Testing impossible target...")
    nums = [1, 2, 3]
    target = 10
    result = BacktrackingOperations.subset_sum_exists(nums, target)
    print(f"   Impossible target 10 with [1,2,3]: {result}")
    assert result == False, f"Expected False for impossible target, got {result}"

    print("\nStep 3: Testing target=0...")
    nums = [1, 2, 3]
    target = 0
    result = BacktrackingOperations.subset_sum_exists(nums, target)
    print(f"   Target 0 (empty subset): {result}")
    assert result == True, f"Expected True for target 0 (empty subset), got {result}"

    print("\nStep 4: Testing single element match...")
    nums = [5]
    target = 5
    result = BacktrackingOperations.subset_sum_exists(nums, target)
    print(f"   Single element [5] with target 5: {result}")
    assert result == True, f"Expected True for exact match, got {result}"

    print("✓ subset_sum_exists tests passed")

def test_restore_ip_addresses():
    """Test IP address restoration"""
    print("Step 1: Testing '25525511135'...")

    s = "25525511135"
    result = BacktrackingOperations.restore_ip_addresses(s)
    expected = ["255.255.11.135", "255.255.111.35"]

    print(f"   Input: '{s}'")
    print(f"   Result: {result}")
    print(f"   Expected: {expected}")

    assert len(result) == 2, f"Expected 2 IP addresses, got {len(result)}"
    for ip in expected:
        assert ip in result, f"Missing IP address: {ip}"

    print("\nStep 2: Testing '0000'...")
    s = "0000"
    result = BacktrackingOperations.restore_ip_addresses(s)
    expected = ["0.0.0.0"]
    print(f"   Input '0000': {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 3: Testing '101023' (multiple solutions)...")
    s = "101023"
    result = BacktrackingOperations.restore_ip_addresses(s)
    print(f"   Input '101023': {result}")

    # Verify all results are valid IP addresses
    for ip in result:
        parts = ip.split('.')
        assert len(parts) == 4, f"IP {ip} doesn't have 4 parts"
        for part in parts:
            num = int(part)
            assert 0 <= num <= 255, f"Invalid IP part: {part}"
            if len(part) > 1:
                assert part[0] != '0', f"Leading zero in IP part: {part}"

    print("\nStep 4: Testing impossible case '1111'...")
    s = "1111"
    result = BacktrackingOperations.restore_ip_addresses(s)
    print(f"   Input '1111': {result}")
    # Should have some valid IPs like "1.1.1.1"
    assert len(result) > 0, f"Expected some valid IPs for '1111', got none"

    print("✓ restore_ip_addresses tests passed")

def test_find_all_paths():
    """Test maze pathfinding"""
    print("Step 1: Testing basic maze...")

    maze = [
        [0, 0, 1],
        [0, 0, 0],
        [0, 1, 0]
    ]
    start = (0, 0)
    end = (2, 2)

    print("   Maze:")
    for row in maze:
        print(f"     {row}")
    print(f"   Start: {start}, End: {end}")

    result = BacktrackingOperations.find_all_paths(maze, start, end)
    print(f"   Paths found: {len(result)}")
    for i, path in enumerate(result):
        print(f"     Path {i+1}: {path}")

    assert len(result) >= 1, f"Expected at least 1 path, got {len(result)}"

    # Verify all paths start and end correctly
    for path in result:
        assert path[0] == start, f"Path doesn't start at {start}: {path}"
        assert path[-1] == end, f"Path doesn't end at {end}: {path}"

    print("\nStep 2: Testing no path maze...")
    blocked_maze = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    result = BacktrackingOperations.find_all_paths(blocked_maze, (0, 0), (2, 2))
    print(f"   Blocked maze paths: {len(result)}")
    assert len(result) == 0, f"Expected no paths in blocked maze, got {len(result)}"

    print("\nStep 3: Testing single path...")
    single_path_maze = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    result = BacktrackingOperations.find_all_paths(single_path_maze, (0, 0), (2, 2))
    print(f"   Single path maze: {len(result)} path(s)")
    assert len(result) >= 1, f"Expected at least 1 path, got {len(result)}"

    print("✓ find_all_paths tests passed")

def test_partition_equal_subset_sum():
    """Test equal subset sum partitioning"""
    print("Step 1: Testing [1,5,11,5]...")

    nums = [1, 5, 11, 5]
    result = BacktrackingOperations.partition_equal_subset_sum(nums)

    print(f"   Input: {nums}")
    print(f"   Can partition: {result}")
    print(f"   Sum: {sum(nums)} (subsets would sum to {sum(nums)//2} each)")

    assert result == True, f"Expected True for [1,5,11,5], got {result}"

    print("\nStep 2: Testing [1,2,3,5] (impossible)...")
    nums = [1, 2, 3, 5]
    result = BacktrackingOperations.partition_equal_subset_sum(nums)
    print(f"   Input [1,2,3,5]: {result}")
    assert result == False, f"Expected False for [1,2,3,5], got {result}"

    print("\nStep 3: Testing [1,1,1,1]...")
    nums = [1, 1, 1, 1]
    result = BacktrackingOperations.partition_equal_subset_sum(nums)
    print(f"   Input [1,1,1,1]: {result}")
    assert result == True, f"Expected True for [1,1,1,1], got {result}"

    print("\nStep 4: Testing single element [2]...")
    nums = [2]
    result = BacktrackingOperations.partition_equal_subset_sum(nums)
    print(f"   Single element [2]: {result}")
    assert result == False, f"Expected False for single element, got {result}"

    print("✓ partition_equal_subset_sum tests passed")

def test_generate_unique_permutations():
    """Test unique permutation generation with duplicates"""
    print("Step 1: Testing [1,1,2]...")

    nums = [1, 1, 2]
    result = BacktrackingOperations.generate_unique_permutations(nums)
    expected = [[1,1,2], [1,2,1], [2,1,1]]

    print(f"   Input: {nums}")
    print(f"   Result: {result}")
    print(f"   Expected: {expected}")

    assert len(result) == 3, f"Expected 3 unique permutations, got {len(result)}"
    for perm in expected:
        assert perm in result, f"Missing permutation: {perm}"

    print("\nStep 2: Testing [1,2,1,1]...")
    nums = [1, 2, 1, 1]
    result = BacktrackingOperations.generate_unique_permutations(nums)
    print(f"   Input [1,2,1,1]: {len(result)} unique permutations")

    # Should have 4!/3! = 4 unique permutations
    expected_count = 4
    assert len(result) == expected_count, f"Expected {expected_count} permutations, got {len(result)}"

    # Check no duplicates in result
    result_set = set(tuple(perm) for perm in result)
    assert len(result_set) == len(result), f"Found duplicate permutations in result"

    print("\nStep 3: Testing [1,2,3] (no duplicates)...")
    nums = [1, 2, 3]
    result = BacktrackingOperations.generate_unique_permutations(nums)
    print(f"   Input [1,2,3]: {len(result)} permutations")
    assert len(result) == 6, f"Expected 6 permutations for [1,2,3], got {len(result)}"

    print("✓ generate_unique_permutations tests passed")

def test_edge_cases():
    """Test edge cases and boundary conditions"""
    print("Step 1: Testing empty inputs...")

    # Empty permutations
    result = BacktrackingOperations.generate_permutations([])
    assert result == [[]], f"Empty permutations failed: {result}"

    # Empty subsets
    result = BacktrackingOperations.generate_subsets([])
    assert result == [[]], f"Empty subsets failed: {result}"

    # Empty letter combinations
    result = BacktrackingOperations.letter_combinations("")
    assert result == [], f"Empty letter combinations failed: {result}"

    print("\nStep 2: Testing single element inputs...")

    # Single permutation
    result = BacktrackingOperations.generate_permutations([42])
    assert result == [[42]], f"Single permutation failed: {result}"

    # Single subset
    result = BacktrackingOperations.generate_subsets([42])
    assert result == [[], [42]], f"Single subsets failed: {result}"

    print("\nStep 3: Testing large inputs (performance check)...")

    # Should complete quickly
    import time
    start_time = time.time()
    result = BacktrackingOperations.generate_subsets([1,2,3,4,5])
    end_time = time.time()

    print(f"   Generated {len(result)} subsets in {end_time - start_time:.4f} seconds")
    assert len(result) == 32, f"Expected 32 subsets for 5 elements, got {len(result)}"
    assert end_time - start_time < 1.0, f"Subset generation too slow: {end_time - start_time:.4f}s"

    print("✓ edge_cases tests passed")

def run_all_tests():
    """Run all test functions with detailed reporting"""
    print("🚀 STARTING COMPREHENSIVE BACKTRACKING TESTS")
    print("="*70)

    tests = [
        ("Generate Permutations", test_generate_permutations),
        ("Generate Combinations", test_generate_combinations),
        ("Generate Subsets", test_generate_subsets),
        ("Solve N-Queens", test_solve_n_queens),
        ("Solve Sudoku", test_solve_sudoku),
        ("Generate Parentheses", test_generate_parentheses),
        ("Letter Combinations", test_letter_combinations),
        ("Word Search", test_word_search),
        ("Palindrome Partitioning", test_palindrome_partitioning),
        ("Combination Sum", test_combination_sum),
        ("Subset Sum Exists", test_subset_sum_exists),
        ("Restore IP Addresses", test_restore_ip_addresses),
        ("Find All Paths", test_find_all_paths),
        ("Partition Equal Subset Sum", test_partition_equal_subset_sum),
        ("Generate Unique Permutations", test_generate_unique_permutations),
        ("Edge Cases", test_edge_cases),
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
        print("🎉 ALL TESTS PASSED! Your backtracking implementation is working correctly!")
        print("\n🔥 KEY CONCEPTS VALIDATED:")
        print("   • Permutations and combinations generation")
        print("   • Constraint satisfaction problems (N-Queens, Sudoku)")
        print("   • Path finding and maze traversal")
        print("   • String manipulation with backtracking")
        print("   • Subset and partition problems")
        print("   • Optimization through pruning")
        print("   • Handling duplicates in backtracking")
    else:
        print("🔧 Some tests failed. Check the detailed output above to fix the issues.")
        print("\n💡 DEBUGGING TIPS:")
        print("   • Verify the three-step framework: Choice → Constraint → Goal")
        print("   • Check that backtracking (undo) is implemented correctly")
        print("   • Ensure constraints are checked before making recursive calls")
        print("   • Validate that base cases are handled properly")
        print("   • Test with simple inputs first, then scale up")

    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
