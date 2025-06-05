import sys
import os
import argparse
import traceback

def setup_imports():
    """Set up imports based on the command-line argument."""
    parser = argparse.ArgumentParser(description='Test binary tree operations')
    parser.add_argument('--mode', choices=['solution', 'practice'], default='solution',
                      help='Which implementation to test (solution or practice)')
    args = parser.parse_args()

    # Get the current directory and project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))

    if args.mode == 'solution':
        # Import from Solutions
        solutions_dir = os.path.join(project_root, 'Solutions', 'Trees')
        sys.path.insert(0, solutions_dir)
        print(f"Testing solution implementation from: {solutions_dir}")
    else:
        # Import from Practice
        practice_dir = os.path.join(project_root, 'Practice', 'Trees')
        sys.path.insert(0, practice_dir)
        print(f"Testing practice implementation from: {practice_dir}")

# Setup the path and import
setup_imports()

try:
    from binary_tree_operations import BinaryTreeOperations, TreeNode
except ImportError as e:
    print(f"❌ Could not import BinaryTreeOperations: {e}")
    print("Make sure the file exists in Solutions/Trees/ or Practice/Trees/")
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

def create_test_tree_1():
    """
    Create test tree:
        1
       / \
      2   3
     / \
    4   5
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root

def create_test_tree_2():
    """
    Create test tree:
        3
       / \
      9  20
        /  \
       15   7
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

def create_bst_tree():
    """
    Create BST:
        5
       / \
      3   7
     / \ / \
    2  4 6  8
    """
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    return root

def test_inorder_traversal():
    """Test inorder traversal functions"""
    print("Step 1: Testing recursive inorder traversal...")

    root = create_test_tree_1()
    result = BinaryTreeOperations.inorder_traversal_recursive(root)
    print(f"   inorder_recursive: {result} (expected: [4, 2, 5, 1, 3])")
    assert result == [4, 2, 5, 1, 3], f"Expected [4, 2, 5, 1, 3], got {result}"

    print("\nStep 2: Testing iterative inorder traversal...")
    result = BinaryTreeOperations.inorder_traversal_iterative(root)
    print(f"   inorder_iterative: {result} (expected: [4, 2, 5, 1, 3])")
    assert result == [4, 2, 5, 1, 3], f"Expected [4, 2, 5, 1, 3], got {result}"

    print("\nStep 3: Testing empty tree...")
    result = BinaryTreeOperations.inorder_traversal_recursive(None)
    print(f"   inorder_recursive(None): {result} (expected: [])")
    assert result == [], f"Expected [], got {result}"

    print("\nStep 4: Testing single node...")
    single = TreeNode(42)
    result = BinaryTreeOperations.inorder_traversal_recursive(single)
    print(f"   inorder_recursive(single): {result} (expected: [42])")
    assert result == [42], f"Expected [42], got {result}"

    print("✓ inorder_traversal tests passed")

def test_preorder_traversal():
    """Test preorder traversal functions"""
    print("Step 1: Testing recursive preorder traversal...")

    root = create_test_tree_1()
    result = BinaryTreeOperations.preorder_traversal_recursive(root)
    print(f"   preorder_recursive: {result} (expected: [1, 2, 4, 5, 3])")
    assert result == [1, 2, 4, 5, 3], f"Expected [1, 2, 4, 5, 3], got {result}"

    print("\nStep 2: Testing iterative preorder traversal...")
    result = BinaryTreeOperations.preorder_traversal_iterative(root)
    print(f"   preorder_iterative: {result} (expected: [1, 2, 4, 5, 3])")
    assert result == [1, 2, 4, 5, 3], f"Expected [1, 2, 4, 5, 3], got {result}"

    print("\nStep 3: Testing empty tree...")
    result = BinaryTreeOperations.preorder_traversal_recursive(None)
    print(f"   preorder_recursive(None): {result} (expected: [])")
    assert result == [], f"Expected [], got {result}"

    print("✓ preorder_traversal tests passed")

def test_postorder_traversal():
    """Test postorder traversal functions"""
    print("Step 1: Testing recursive postorder traversal...")

    root = create_test_tree_1()
    result = BinaryTreeOperations.postorder_traversal_recursive(root)
    print(f"   postorder_recursive: {result} (expected: [4, 5, 2, 3, 1])")
    assert result == [4, 5, 2, 3, 1], f"Expected [4, 5, 2, 3, 1], got {result}"

    print("\nStep 2: Testing iterative postorder traversal...")
    result = BinaryTreeOperations.postorder_traversal_iterative(root)
    print(f"   postorder_iterative: {result} (expected: [4, 5, 2, 3, 1])")
    assert result == [4, 5, 2, 3, 1], f"Expected [4, 5, 2, 3, 1], got {result}"

    print("\nStep 3: Testing empty tree...")
    result = BinaryTreeOperations.postorder_traversal_recursive(None)
    print(f"   postorder_recursive(None): {result} (expected: [])")
    assert result == [], f"Expected [], got {result}"

    print("✓ postorder_traversal tests passed")

def test_level_order_traversal():
    """Test level-order traversal function"""
    print("Step 1: Testing level-order traversal...")

    root = create_test_tree_2()
    result = BinaryTreeOperations.level_order_traversal(root)
    expected = [[3], [9, 20], [15, 7]]
    print(f"   level_order: {result} (expected: {expected})")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 2: Testing single node...")
    single = TreeNode(1)
    result = BinaryTreeOperations.level_order_traversal(single)
    expected = [[1]]
    print(f"   level_order(single): {result} (expected: {expected})")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 3: Testing empty tree...")
    result = BinaryTreeOperations.level_order_traversal(None)
    expected = []
    print(f"   level_order(None): {result} (expected: {expected})")
    assert result == expected, f"Expected {expected}, got {result}"

    print("✓ level_order_traversal tests passed")

def test_tree_depth():
    """Test max_depth and min_depth functions"""
    print("Step 1: Testing max_depth...")

    root = create_test_tree_2()
    result = BinaryTreeOperations.max_depth(root)
    print(f"   max_depth: {result} (expected: 3)")
    assert result == 3, f"Expected 3, got {result}"

    print("\nStep 2: Testing min_depth...")
    result = BinaryTreeOperations.min_depth(root)
    print(f"   min_depth: {result} (expected: 2)")
    assert result == 2, f"Expected 2, got {result}"

    print("\nStep 3: Testing empty tree depths...")
    max_result = BinaryTreeOperations.max_depth(None)
    min_result = BinaryTreeOperations.min_depth(None)
    print(f"   max_depth(None): {max_result} (expected: 0)")
    print(f"   min_depth(None): {min_result} (expected: 0)")
    assert max_result == 0, f"Expected 0, got {max_result}"
    assert min_result == 0, f"Expected 0, got {min_result}"

    print("\nStep 4: Testing single node depths...")
    single = TreeNode(1)
    max_result = BinaryTreeOperations.max_depth(single)
    min_result = BinaryTreeOperations.min_depth(single)
    print(f"   max_depth(single): {max_result} (expected: 1)")
    print(f"   min_depth(single): {min_result} (expected: 1)")
    assert max_result == 1, f"Expected 1, got {max_result}"
    assert min_result == 1, f"Expected 1, got {min_result}"

    print("✓ tree_depth tests passed")

def test_is_balanced():
    """Test is_balanced function"""
    print("Step 1: Testing balanced tree...")

    root = create_test_tree_2()
    result = BinaryTreeOperations.is_balanced(root)
    print(f"   is_balanced(balanced_tree): {result} (expected: True)")
    assert result == True, f"Expected True, got {result}"

    print("\nStep 2: Testing unbalanced tree...")
    # Create unbalanced tree: 1 -> 2 -> 3 -> 4
    unbalanced = TreeNode(1)
    unbalanced.left = TreeNode(2)
    unbalanced.left.left = TreeNode(3)
    unbalanced.left.left.left = TreeNode(4)

    result = BinaryTreeOperations.is_balanced(unbalanced)
    print(f"   is_balanced(unbalanced_tree): {result} (expected: False)")
    assert result == False, f"Expected False, got {result}"

    print("\nStep 3: Testing empty tree...")
    result = BinaryTreeOperations.is_balanced(None)
    print(f"   is_balanced(None): {result} (expected: True)")
    assert result == True, f"Expected True, got {result}"

    print("✓ is_balanced tests passed")

def test_invert_binary_tree():
    """Test invert_binary_tree function"""
    print("Step 1: Testing tree inversion...")

    # Create tree: 4 -> (2,7) -> (1,3),(6,9)
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    # Get original inorder
    original_inorder = BinaryTreeOperations.inorder_traversal_recursive(root)
    print(f"   Original inorder: {original_inorder}")

    # Invert the tree
    inverted_root = BinaryTreeOperations.invert_binary_tree(root)

    # Get inverted inorder (should be reversed)
    inverted_inorder = BinaryTreeOperations.inorder_traversal_recursive(inverted_root)
    print(f"   Inverted inorder: {inverted_inorder}")

    # Check that it's properly inverted
    expected_inverted = [9, 7, 6, 4, 3, 2, 1]
    assert inverted_inorder == expected_inverted, f"Expected {expected_inverted}, got {inverted_inorder}"

    print("\nStep 2: Testing empty tree inversion...")
    result = BinaryTreeOperations.invert_binary_tree(None)
    print(f"   invert_binary_tree(None): {result} (expected: None)")
    assert result is None, f"Expected None, got {result}"

    print("✓ invert_binary_tree tests passed")

def test_lowest_common_ancestor():
    """Test lowest_common_ancestor function"""
    print("Step 1: Testing LCA in tree...")

    # Create tree: 3 -> (5,1) -> (6,2),(0,8) where 2 -> (7,4)
    root = TreeNode(3)
    node5 = TreeNode(5)
    node1 = TreeNode(1)
    node6 = TreeNode(6)
    node2 = TreeNode(2)
    node0 = TreeNode(0)
    node8 = TreeNode(8)
    node7 = TreeNode(7)
    node4 = TreeNode(4)

    root.left = node5
    root.right = node1
    node5.left = node6
    node5.right = node2
    node1.left = node0
    node1.right = node8
    node2.left = node7
    node2.right = node4

    print("\nStep 2: Testing LCA of nodes 5 and 1...")
    lca = BinaryTreeOperations.lowest_common_ancestor(root, node5, node1)
    print(f"   LCA(5, 1): {lca.val} (expected: 3)")
    assert lca.val == 3, f"Expected 3, got {lca.val}"

    print("\nStep 3: Testing LCA of nodes 5 and 4...")
    lca = BinaryTreeOperations.lowest_common_ancestor(root, node5, node4)
    print(f"   LCA(5, 4): {lca.val} (expected: 5)")
    assert lca.val == 5, f"Expected 5, got {lca.val}"

    print("\nStep 4: Testing LCA of nodes 6 and 7...")
    lca = BinaryTreeOperations.lowest_common_ancestor(root, node6, node7)
    print(f"   LCA(6, 7): {lca.val} (expected: 5)")
    assert lca.val == 5, f"Expected 5, got {lca.val}"

    print("✓ lowest_common_ancestor tests passed")

def test_has_path_sum():
    """Test has_path_sum function"""
    print("Step 1: Testing path sum existence...")

    # Create tree: 5 -> (4,8) -> (11,null),(13,4) where 11 -> (7,2) and right 4 -> (null,1)
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    print("\nStep 2: Testing existing path sum...")
    result = BinaryTreeOperations.has_path_sum(root, 22)
    print(f"   has_path_sum(22): {result} (expected: True)")
    print("   → Path: 5->4->11->2 = 22")
    assert result == True, f"Expected True, got {result}"

    print("\nStep 3: Testing non-existing path sum...")
    result = BinaryTreeOperations.has_path_sum(root, 100)
    print(f"   has_path_sum(100): {result} (expected: False)")
    assert result == False, f"Expected False, got {result}"

    print("\nStep 4: Testing empty tree...")
    result = BinaryTreeOperations.has_path_sum(None, 10)
    print(f"   has_path_sum(None, 10): {result} (expected: False)")
    assert result == False, f"Expected False, got {result}"

    print("✓ has_path_sum tests passed")

def test_path_sum_all_paths():
    """Test path_sum_all_paths function"""
    print("Step 1: Testing all paths with target sum...")

    # Create tree with multiple paths summing to 22
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    result = BinaryTreeOperations.path_sum_all_paths(root, 22)
    print(f"   path_sum_all_paths(22): {result}")
    print("   → Expected paths with sum 22")

    # Check that we found the correct paths
    expected_paths = [[5, 4, 11, 2], [5, 8, 4, 5]]
    assert len(result) == 2, f"Expected 2 paths, got {len(result)}"

    # Sort both expected and result for comparison
    result_sorted = [sorted(path) for path in result]
    expected_sorted = [sorted(path) for path in expected_paths]

    for path in expected_sorted:
        assert path in result_sorted, f"Expected path {path} not found in result"

    print("\nStep 2: Testing no paths with target sum...")
    result = BinaryTreeOperations.path_sum_all_paths(root, 1000)
    print(f"   path_sum_all_paths(1000): {result} (expected: [])")
    assert result == [], f"Expected [], got {result}"

    print("✓ path_sum_all_paths tests passed")

def test_build_tree_from_preorder_inorder():
    """Test build_tree_from_preorder_inorder function"""
    print("Step 1: Testing tree construction from traversals...")

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    root = BinaryTreeOperations.build_tree_from_preorder_inorder(preorder, inorder)

    # Verify by checking traversals of constructed tree
    result_preorder = BinaryTreeOperations.preorder_traversal_recursive(root)
    result_inorder = BinaryTreeOperations.inorder_traversal_recursive(root)

    print(f"   Constructed tree preorder: {result_preorder}")
    print(f"   Original preorder: {preorder}")
    print(f"   Constructed tree inorder: {result_inorder}")
    print(f"   Original inorder: {inorder}")

    assert result_preorder == preorder, f"Preorder mismatch: expected {preorder}, got {result_preorder}"
    assert result_inorder == inorder, f"Inorder mismatch: expected {inorder}, got {result_inorder}"

    print("\nStep 2: Testing empty arrays...")
    result = BinaryTreeOperations.build_tree_from_preorder_inorder([], [])
    print(f"   build_tree([], []): {result} (expected: None)")
    assert result is None, f"Expected None, got {result}"

    print("✓ build_tree_from_preorder_inorder tests passed")

def test_serialize_deserialize():
    """Test serialize_tree and deserialize_tree functions"""
    print("Step 1: Testing tree serialization...")

    root = create_test_tree_1()
    serialized = BinaryTreeOperations.serialize_tree(root)
    print(f"   Serialized: {serialized}")

    print("\nStep 2: Testing tree deserialization...")
    deserialized_root = BinaryTreeOperations.deserialize_tree(serialized)

    # Verify by comparing traversals
    original_inorder = BinaryTreeOperations.inorder_traversal_recursive(root)
    deserialized_inorder = BinaryTreeOperations.inorder_traversal_recursive(deserialized_root)

    print(f"   Original inorder: {original_inorder}")
    print(f"   Deserialized inorder: {deserialized_inorder}")

    assert original_inorder == deserialized_inorder, f"Inorder mismatch: expected {original_inorder}, got {deserialized_inorder}"

    print("\nStep 3: Testing empty tree serialization...")
    serialized_empty = BinaryTreeOperations.serialize_tree(None)
    deserialized_empty = BinaryTreeOperations.deserialize_tree(serialized_empty)
    print(f"   serialize(None): {serialized_empty}")
    print(f"   deserialize(serialized_empty): {deserialized_empty}")
    assert deserialized_empty is None, f"Expected None, got {deserialized_empty}"

    print("✓ serialize/deserialize tests passed")

def test_is_valid_bst():
    """Test is_valid_bst function"""
    print("Step 1: Testing valid BST...")

    bst = create_bst_tree()
    result = BinaryTreeOperations.is_valid_bst(bst)
    print(f"   is_valid_bst(valid_bst): {result} (expected: True)")
    assert result == True, f"Expected True, got {result}"

    print("\nStep 2: Testing invalid BST...")
    # Create invalid BST: 5 -> (1,4) -> (null,null),(3,6)
    invalid_bst = TreeNode(5)
    invalid_bst.left = TreeNode(1)
    invalid_bst.right = TreeNode(4)
    invalid_bst.right.left = TreeNode(3)
    invalid_bst.right.right = TreeNode(6)

    result = BinaryTreeOperations.is_valid_bst(invalid_bst)
    print(f"   is_valid_bst(invalid_bst): {result} (expected: False)")
    print("   → Node 4 is in right subtree of 5 but 4 < 5")
    assert result == False, f"Expected False, got {result}"

    print("\nStep 3: Testing empty tree...")
    result = BinaryTreeOperations.is_valid_bst(None)
    print(f"   is_valid_bst(None): {result} (expected: True)")
    assert result == True, f"Expected True, got {result}"

    print("✓ is_valid_bst tests passed")

def test_bst_operations():
    """Test BST insert, search, and delete functions"""
    print("Step 1: Testing BST insertion...")

    root = TreeNode(5)
    root = BinaryTreeOperations.bst_insert(root, 3)
    root = BinaryTreeOperations.bst_insert(root, 7)
    root = BinaryTreeOperations.bst_insert(root, 2)
    root = BinaryTreeOperations.bst_insert(root, 4)

    inorder = BinaryTreeOperations.inorder_traversal_recursive(root)
    print(f"   After insertions inorder: {inorder} (expected: [2, 3, 4, 5, 7])")
    assert inorder == [2, 3, 4, 5, 7], f"Expected [2, 3, 4, 5, 7], got {inorder}"

    print("\nStep 2: Testing BST search...")
    found_node = BinaryTreeOperations.bst_search(root, 4)
    print(f"   search(4): {found_node.val if found_node else None} (expected: 4)")
    assert found_node and found_node.val == 4, f"Expected to find node with value 4"

    not_found = BinaryTreeOperations.bst_search(root, 10)
    print(f"   search(10): {not_found} (expected: None)")
    assert not_found is None, f"Expected None, got {not_found}"

    print("\nStep 3: Testing BST deletion...")
    # Delete leaf node
    root = BinaryTreeOperations.bst_delete(root, 2)
    inorder = BinaryTreeOperations.inorder_traversal_recursive(root)
    print(f"   After deleting 2: {inorder} (expected: [3, 4, 5, 7])")
    assert inorder == [3, 4, 5, 7], f"Expected [3, 4, 5, 7], got {inorder}"

    # Delete node with one child
    root = BinaryTreeOperations.bst_delete(root, 3)
    inorder = BinaryTreeOperations.inorder_traversal_recursive(root)
    print(f"   After deleting 3: {inorder} (expected: [4, 5, 7])")
    assert inorder == [4, 5, 7], f"Expected [4, 5, 7], got {inorder}"

    print("✓ bst_operations tests passed")

def test_binary_tree_paths():
    """Test binary_tree_paths function"""
    print("Step 1: Testing all root-to-leaf paths...")

    # Create tree: 1 -> (2,3) -> (null,5),null
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    result = BinaryTreeOperations.binary_tree_paths(root)
    expected = ["1->2->5", "1->3"]
    print(f"   binary_tree_paths: {result}")
    print(f"   Expected: {expected}")

    assert sorted(result) == sorted(expected), f"Expected {expected}, got {result}"

    print("\nStep 2: Testing single node...")
    single = TreeNode(1)
    result = BinaryTreeOperations.binary_tree_paths(single)
    expected = ["1"]
    print(f"   binary_tree_paths(single): {result} (expected: {expected})")
    assert result == expected, f"Expected {expected}, got {result}"

    print("✓ binary_tree_paths tests passed")

def test_diameter_of_binary_tree():
    """Test diameter_of_binary_tree function"""
    print("Step 1: Testing tree diameter...")

    # Create tree: 1 -> (2,3) -> (4,5),null
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = BinaryTreeOperations.diameter_of_binary_tree(root)
    print(f"   diameter: {result} (expected: 3)")
    print("   → Longest path: 4->2->5 (3 edges)")
    assert result == 3, f"Expected 3, got {result}"

    print("\nStep 2: Testing single node...")
    single = TreeNode(1)
    result = BinaryTreeOperations.diameter_of_binary_tree(single)
    print(f"   diameter(single): {result} (expected: 0)")
    assert result == 0, f"Expected 0, got {result}"

    print("\nStep 3: Testing empty tree...")
    result = BinaryTreeOperations.diameter_of_binary_tree(None)
    print(f"   diameter(None): {result} (expected: 0)")
    assert result == 0, f"Expected 0, got {result}"

    print("✓ diameter_of_binary_tree tests passed")

def test_count_nodes():
    """Test count_nodes function"""
    print("Step 1: Testing node count...")

    root = create_test_tree_1()
    result = BinaryTreeOperations.count_nodes(root)
    print(f"   count_nodes: {result} (expected: 5)")
    assert result == 5, f"Expected 5, got {result}"

    print("\nStep 2: Testing empty tree...")
    result = BinaryTreeOperations.count_nodes(None)
    print(f"   count_nodes(None): {result} (expected: 0)")
    assert result == 0, f"Expected 0, got {result}"

    print("\nStep 3: Testing single node...")
    single = TreeNode(1)
    result = BinaryTreeOperations.count_nodes(single)
    print(f"   count_nodes(single): {result} (expected: 1)")
    assert result == 1, f"Expected 1, got {result}"

    print("✓ count_nodes tests passed")

def test_is_symmetric():
    """Test is_symmetric function"""
    print("Step 1: Testing symmetric tree...")

    # Create symmetric tree: 1 -> (2,2) -> (3,4),(4,3)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    result = BinaryTreeOperations.is_symmetric(root)
    print(f"   is_symmetric(symmetric_tree): {result} (expected: True)")
    assert result == True, f"Expected True, got {result}"

    print("\nStep 2: Testing asymmetric tree...")
    # Create asymmetric tree: 1 -> (2,2) -> (null,3),(null,3)
    asymmetric = TreeNode(1)
    asymmetric.left = TreeNode(2)
    asymmetric.right = TreeNode(2)
    asymmetric.left.right = TreeNode(3)
    asymmetric.right.right = TreeNode(3)

    result = BinaryTreeOperations.is_symmetric(asymmetric)
    print(f"   is_symmetric(asymmetric_tree): {result} (expected: False)")
    assert result == False, f"Expected False, got {result}"

    print("\nStep 3: Testing empty tree...")
    result = BinaryTreeOperations.is_symmetric(None)
    print(f"   is_symmetric(None): {result} (expected: True)")
    assert result == True, f"Expected True, got {result}"

    print("✓ is_symmetric tests passed")

def test_build_tree_from_array():
    """Test build_tree_from_array function"""
    print("Step 1: Testing tree construction from array...")

    arr = [3, 9, 20, None, None, 15, 7]
    root = BinaryTreeOperations.build_tree_from_array(arr)

    # Verify by level-order traversal
    result = BinaryTreeOperations.level_order_traversal(root)
    expected = [[3], [9, 20], [15, 7]]
    print(f"   Level-order of constructed tree: {result}")
    print(f"   Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 2: Testing empty array...")
    result = BinaryTreeOperations.build_tree_from_array([])
    print(f"   build_tree_from_array([]): {result} (expected: None)")
    assert result is None, f"Expected None, got {result}"

    print("\nStep 3: Testing array with None root...")
    result = BinaryTreeOperations.build_tree_from_array([None])
    print(f"   build_tree_from_array([None]): {result} (expected: None)")
    assert result is None, f"Expected None, got {result}"

    print("✓ build_tree_from_array tests passed")

def run_all_tests():
    """Run all test functions with detailed reporting"""
    print("🚀 STARTING COMPREHENSIVE BINARY TREE TESTS")
    print("="*70)

    tests = [
        ("Inorder Traversal", test_inorder_traversal),
        ("Preorder Traversal", test_preorder_traversal),
        ("Postorder Traversal", test_postorder_traversal),
        ("Level Order Traversal", test_level_order_traversal),
        ("Tree Depth (Max/Min)", test_tree_depth),
        ("Is Balanced", test_is_balanced),
        ("Invert Binary Tree", test_invert_binary_tree),
        ("Lowest Common Ancestor", test_lowest_common_ancestor),
        ("Has Path Sum", test_has_path_sum),
        ("Path Sum All Paths", test_path_sum_all_paths),
        ("Build Tree from Preorder/Inorder", test_build_tree_from_preorder_inorder),
        ("Serialize/Deserialize", test_serialize_deserialize),
        ("Is Valid BST", test_is_valid_bst),
        ("BST Operations (Insert/Search/Delete)", test_bst_operations),
        ("Binary Tree Paths", test_binary_tree_paths),
        ("Diameter of Binary Tree", test_diameter_of_binary_tree),
        ("Count Nodes", test_count_nodes),
        ("Is Symmetric", test_is_symmetric),
        ("Build Tree from Array", test_build_tree_from_array),
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
        print("🎉 ALL TESTS PASSED! Your binary tree implementation is working correctly!")
    else:
        print("🔧 Some tests failed. Check the detailed output above to fix the issues.")

    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
