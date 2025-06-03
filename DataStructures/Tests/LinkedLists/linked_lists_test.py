import sys
import os
import argparse

def setup_imports():
    """Set up imports based on the command-line argument."""
    parser = argparse.ArgumentParser(description='Test linked lists operations')
    parser.add_argument('--mode', choices=['solution', 'practice'], default='solution',
                      help='Which implementation to test (solution or practice)')
    args = parser.parse_args()
  
    # Get the current directory and project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir,'..', '..'))
    
    if args.mode == 'solution':
        # Import from Solutions
        solutions_dir = os.path.join(project_root, 'Solutions', 'LinkedLists')
        sys.path.insert(0, solutions_dir)
        print(f"Testing solution implementation from: {solutions_dir}")
    else:
        # Import from Practice
        practice_dir = os.path.join(project_root, 'Practice', 'LinkedLists')
        sys.path.insert(0, practice_dir)
        print(f"Testing practice implementation from: {practice_dir}")
     
# Setup the path and import
setup_imports()

try:
    from linked_lists_operations import LinkedListOperations, ListNode, DoublyListNode
except ImportError as e:
    print(f"❌ Could not import LinkedListOperations: {e}")
    print("Make sure the file exists in Solutions/Linked Lists/ or Practice/Linked Lists/")
    sys.exit(1)

def test_singly_linked_list():
    """Test SinglyLinkedList implementation"""
    print("Testing SinglyLinkedList...")
    
    sll = LinkedListOperations.SinglyLinkedList()
    
    # Test empty list
    assert sll.get(0) == -1, "Empty list should return -1"
    assert sll.size == 0, "Empty list should have size 0"
    
    # Test add_at_head
    sll.add_at_head(1)
    assert sll.to_list() == [1], f"After add_at_head(1), expected [1], got {sll.to_list()}"
    assert sll.size == 1, "Size should be 1"
    
    sll.add_at_head(2)
    assert sll.to_list() == [2, 1], f"After add_at_head(2), expected [2, 1], got {sll.to_list()}"
    
    # Test add_at_tail
    sll.add_at_tail(3)
    assert sll.to_list() == [2, 1, 3], f"After add_at_tail(3), expected [2, 1, 3], got {sll.to_list()}"
    
    # Test get
    assert sll.get(0) == 2, "Get index 0 should return 2"
    assert sll.get(1) == 1, "Get index 1 should return 1"  
    assert sll.get(2) == 3, "Get index 2 should return 3"
    assert sll.get(3) == -1, "Get invalid index should return -1"
    
    # Test add_at_index
    sll.add_at_index(1, 4)  # Insert 4 at index 1
    assert sll.to_list() == [2, 4, 1, 3], f"After add_at_index(1, 4), expected [2, 4, 1, 3], got {sll.to_list()}"
    
    # Test delete_at_index
    sll.delete_at_index(1)  # Remove index 1 (value 4)
    assert sll.to_list() == [2, 1, 3], f"After delete_at_index(1), expected [2, 1, 3], got {sll.to_list()}"
    
    sll.delete_at_index(0)  # Remove head
    assert sll.to_list() == [1, 3], f"After delete_at_index(0), expected [1, 3], got {sll.to_list()}"
    
    print("✓ SinglyLinkedList tests passed")

def test_doubly_linked_list():
    """Test DoublyLinkedList implementation"""
    print("Testing DoublyLinkedList...")
    
    dll = LinkedListOperations.DoublyLinkedList()
    
    # Test empty list
    assert dll.is_empty() == True, "New list should be empty"
    assert dll.size == 0, "New list should have size 0"
    
    # Test add_first
    dll.add_first(1)
    assert dll.to_list() == [1], f"After add_first(1), expected [1], got {dll.to_list()}"
    assert dll.size == 1, "Size should be 1"
    
    dll.add_first(2)
    assert dll.to_list() == [2, 1], f"After add_first(2), expected [2, 1], got {dll.to_list()}"
    
    # Test add_last
    dll.add_last(3)
    assert dll.to_list() == [2, 1, 3], f"After add_last(3), expected [2, 1, 3], got {dll.to_list()}"
    
    # Test remove_first
    first = dll.remove_first()
    assert first == 2, f"remove_first should return 2, got {first}"
    assert dll.to_list() == [1, 3], f"After remove_first, expected [1, 3], got {dll.to_list()}"
    
    # Test remove_last
    last = dll.remove_last()
    assert last == 3, f"remove_last should return 3, got {last}"
    assert dll.to_list() == [1], f"After remove_last, expected [1], got {dll.to_list()}"
    
    # Test remove until empty
    dll.remove_first()
    assert dll.is_empty() == True, "List should be empty"
    
    # Test exception on empty remove
    try:
        dll.remove_first()
        assert False, "Should raise IndexError on empty remove"
    except IndexError:
        pass
    
    print("✓ DoublyLinkedList tests passed")

def test_helper_methods():
    """Test helper methods"""
    print("Testing helper methods...")
    
    # Test create_linked_list
    head = LinkedListOperations.create_linked_list([1, 2, 3, 4])
    result = LinkedListOperations.linked_list_to_list(head)
    assert result == [1, 2, 3, 4], f"Expected [1, 2, 3, 4], got {result}"
    
    # Test empty list
    empty_head = LinkedListOperations.create_linked_list([])
    assert empty_head is None, "Empty list should return None"
    
    # Test single element
    single_head = LinkedListOperations.create_linked_list([42])
    single_result = LinkedListOperations.linked_list_to_list(single_head)
    assert single_result == [42], f"Expected [42], got {single_result}"
    
    print("✓ Helper methods tests passed")

def test_reverse_linked_list():
    """Test reverse_linked_list functions"""
    print("Testing reverse_linked_list...")
    
    # Test iterative version
    head = LinkedListOperations.create_linked_list([1, 2, 3, 4, 5])
    reversed_head = LinkedListOperations.reverse_linked_list(head)
    result = LinkedListOperations.linked_list_to_list(reversed_head)
    assert result == [5, 4, 3, 2, 1], f"Expected [5, 4, 3, 2, 1], got {result}"
    
    # Test recursive version
    head = LinkedListOperations.create_linked_list([1, 2, 3, 4, 5])
    reversed_head = LinkedListOperations.reverse_linked_list_recursive(head)
    result = LinkedListOperations.linked_list_to_list(reversed_head)
    assert result == [5, 4, 3, 2, 1], f"Expected [5, 4, 3, 2, 1], got {result}"
    
    # Test single node
    single = LinkedListOperations.create_linked_list([1])
    reversed_single = LinkedListOperations.reverse_linked_list(single)
    result = LinkedListOperations.linked_list_to_list(reversed_single)
    assert result == [1], f"Expected [1], got {result}"
    
    # Test empty list
    empty = LinkedListOperations.reverse_linked_list(None)
    assert empty is None, "Reversed empty list should be None"
    
    print("✓ reverse_linked_list tests passed")

def test_has_cycle():
    """Test has_cycle function"""
    print("Testing has_cycle...")
    
    # Test no cycle
    head = LinkedListOperations.create_linked_list([1, 2, 3, 4])
    assert LinkedListOperations.has_cycle(head) == False, "List without cycle should return False"
    
    # Test with cycle
    head = LinkedListOperations.create_linked_list([1, 2, 3, 4])
    # Create cycle: 4 -> 2
    current = head
    second_node = head.next
    while current.next:
        current = current.next
    current.next = second_node  # Create cycle
    
    assert LinkedListOperations.has_cycle(head) == True, "List with cycle should return True"
    
    # Test single node with self cycle
    single = ListNode(1)
    single.next = single
    assert LinkedListOperations.has_cycle(single) == True, "Self-cycle should return True"
    
    # Test empty list
    assert LinkedListOperations.has_cycle(None) == False, "Empty list should return False"
    
    print("✓ has_cycle tests passed")

def test_find_cycle_start():
    """Test find_cycle_start function"""
    print("Testing find_cycle_start...")
    
    # Test no cycle
    head = LinkedListOperations.create_linked_list([1, 2, 3, 4])
    assert LinkedListOperations.find_cycle_start(head) is None, "No cycle should return None"
    
    # Test with cycle starting at node 2 (value 3)
    head = LinkedListOperations.create_linked_list([1, 2, 3, 4, 5])
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    
    # Create cycle: last node points to third node (index 2, value 3)
    nodes[-1].next = nodes[2]  # 5 -> 3, creating cycle
    
    cycle_start = LinkedListOperations.find_cycle_start(head)
    assert cycle_start is not None, "Should find cycle start"
    assert cycle_start.val == 3, f"Cycle start should be node with value 3, got {cycle_start.val}"
    assert cycle_start is nodes[2], "Should return the exact node where cycle starts"
    
    print("✓ find_cycle_start tests passed")

def test_merge_two_sorted_lists():
    """Test merge_two_sorted_lists function"""
    print("Testing merge_two_sorted_lists...")
    
    # Test basic merge
    list1 = LinkedListOperations.create_linked_list([1, 2, 4])
    list2 = LinkedListOperations.create_linked_list([1, 3, 4])
    merged = LinkedListOperations.merge_two_sorted_lists(list1, list2)
    result = LinkedListOperations.linked_list_to_list(merged)
    assert result == [1, 1, 2, 3, 4, 4], f"Expected [1, 1, 2, 3, 4, 4], got {result}"
    
    # Test empty lists
    list1 = None
    list2 = LinkedListOperations.create_linked_list([0])
    merged = LinkedListOperations.merge_two_sorted_lists(list1, list2)
    result = LinkedListOperations.linked_list_to_list(merged)
    assert result == [0], f"Expected [0], got {result}"
    
    # Test both empty
    merged = LinkedListOperations.merge_two_sorted_lists(None, None)
    assert merged is None, "Merging two empty lists should return None"
    
    print("✓ merge_two_sorted_lists tests passed")

def test_find_middle_node():
    """Test find_middle_node function"""
    print("Testing find_middle_node...")
    
    # Test odd length
    head = LinkedListOperations.create_linked_list([1, 2, 3, 4, 5])
    middle = LinkedListOperations.find_middle_node(head)
    assert middle.val == 3, f"Middle of [1,2,3,4,5] should be 3, got {middle.val}"
    
    # Test even length (returns second middle)
    head = LinkedListOperations.create_linked_list([1, 2, 3, 4, 5, 6])
    middle = LinkedListOperations.find_middle_node(head)
    assert middle.val == 4, f"Middle of [1,2,3,4,5,6] should be 4, got {middle.val}"
    
    # Test single node
    head = LinkedListOperations.create_linked_list([1])
    middle = LinkedListOperations.find_middle_node(head)
    assert middle.val == 1, f"Middle of [1] should be 1, got {middle.val}"
    
    # Test empty list
    middle = LinkedListOperations.find_middle_node(None)
    assert middle is None, "Middle of empty list should be None"
    
    print("✓ find_middle_node tests passed")

def test_remove_nth_from_end():
    """Test remove_nth_from_end function"""
    print("Testing remove_nth_from_end...")
    
    # Test remove from middle
    head = LinkedListOperations.create_linked_list([1, 2, 3, 4, 5])
    result_head = LinkedListOperations.remove_nth_from_end(head, 2)
    result = LinkedListOperations.linked_list_to_list(result_head)
    assert result == [1, 2, 3, 5], f"Remove 2nd from end: expected [1,2,3,5], got {result}"
    
    # Test remove head (nth from end where n = length)
    head = LinkedListOperations.create_linked_list([1, 2])
    result_head = LinkedListOperations.remove_nth_from_end(head, 2)
    result = LinkedListOperations.linked_list_to_list(result_head)
    assert result == [2], f"Remove head: expected [2], got {result}"
    
    # Test remove only node
    head = LinkedListOperations.create_linked_list([1])
    result_head = LinkedListOperations.remove_nth_from_end(head, 1)
    result = LinkedListOperations.linked_list_to_list(result_head)
    assert result == [], f"Remove only node: expected [], got {result}"
    
    print("✓ remove_nth_from_end tests passed")

def test_intersection_of_two_lists():
    """Test intersection_of_two_lists function"""
    print("Testing intersection_of_two_lists...")
    
    # Create intersection scenario
    # List A: 4 -> 1 -> 8 -> 4 -> 5
    # List B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
    # Intersection at node with value 8
    
    common_part = LinkedListOperations.create_linked_list([8, 4, 5])
    
    # List A
    nodeA1 = ListNode(4)
    nodeA2 = ListNode(1)
    nodeA1.next = nodeA2
    nodeA2.next = common_part
    
    # List B  
    nodeB1 = ListNode(5)
    nodeB2 = ListNode(6)
    nodeB3 = ListNode(1)
    nodeB1.next = nodeB2
    nodeB2.next = nodeB3
    nodeB3.next = common_part
    
    intersection = LinkedListOperations.intersection_of_two_lists(nodeA1, nodeB1)
    assert intersection is not None, "Should find intersection"
    assert intersection.val == 8, f"Intersection should be node with value 8, got {intersection.val}"
    assert intersection is common_part, "Should return the exact intersection node"
    
    # Test no intersection
    listA = LinkedListOperations.create_linked_list([2, 6, 4])
    listB = LinkedListOperations.create_linked_list([1, 5])
    intersection = LinkedListOperations.intersection_of_two_lists(listA, listB)
    assert intersection is None, "No intersection should return None"
    
    print("✓ intersection_of_two_lists tests passed")

def test_is_palindrome():
    """Test is_palindrome function"""
    print("Testing is_palindrome...")
    
    # Test palindrome odd length
    head = LinkedListOperations.create_linked_list([1, 2, 3, 2, 1])
    assert LinkedListOperations.is_palindrome(head) == True, "Odd palindrome should return True"
    
    # Test palindrome even length
    head = LinkedListOperations.create_linked_list([1, 2, 2, 1])
    assert LinkedListOperations.is_palindrome(head) == True, "Even palindrome should return True"
    
    # Test non-palindrome
    head = LinkedListOperations.create_linked_list([1, 2, 3, 4, 5])
    assert LinkedListOperations.is_palindrome(head) == False, "Non-palindrome should return False"
    
    # Test single node
    head = LinkedListOperations.create_linked_list([1])
    assert LinkedListOperations.is_palindrome(head) == True, "Single node should be palindrome"
    
    # Test empty list
    assert LinkedListOperations.is_palindrome(None) == True, "Empty list should be palindrome"
    
    print("✓ is_palindrome tests passed")

def test_add_two_numbers():
    """Test add_two_numbers function"""
    print("Testing add_two_numbers...")
    
    # Test basic addition: 342 + 465 = 807
    l1 = LinkedListOperations.create_linked_list([2, 4, 3])  # 342
    l2 = LinkedListOperations.create_linked_list([5, 6, 4])  # 465
    result_head = LinkedListOperations.add_two_numbers(l1, l2)
    result = LinkedListOperations.linked_list_to_list(result_head)
    assert result == [7, 0, 8], f"342 + 465 = 807: expected [7,0,8], got {result}"
    
    # Test with carry: 99 + 9 = 108
    l1 = LinkedListOperations.create_linked_list([9, 9])     # 99
    l2 = LinkedListOperations.create_linked_list([9])        # 9
    result_head = LinkedListOperations.add_two_numbers(l1, l2)
    result = LinkedListOperations.linked_list_to_list(result_head)
    assert result == [8, 0, 1], f"99 + 9 = 108: expected [8,0,1], got {result}"
    
    # Test zero
    l1 = LinkedListOperations.create_linked_list([0])
    l2 = LinkedListOperations.create_linked_list([0])
    result_head = LinkedListOperations.add_two_numbers(l1, l2)
    result = LinkedListOperations.linked_list_to_list(result_head)
    assert result == [0], f"0 + 0 = 0: expected [0], got {result}"
    
    print("✓ add_two_numbers tests passed")

def test_remove_duplicates_sorted():
    """Test remove_duplicates_sorted function"""
    print("Testing remove_duplicates_sorted...")
    
    # Test with duplicates
    head = LinkedListOperations.create_linked_list([1, 1, 2, 3, 3])
    result_head = LinkedListOperations.remove_duplicates_sorted(head)
    result = LinkedListOperations.linked_list_to_list(result_head)
    assert result == [1, 2, 3], f"Expected [1,2,3], got {result}"
    
    # Test no duplicates
    head = LinkedListOperations.create_linked_list([1, 2, 3, 4, 5])
    result_head = LinkedListOperations.remove_duplicates_sorted(head)
    result = LinkedListOperations.linked_list_to_list(result_head)
    assert result == [1, 2, 3, 4, 5], f"Expected [1,2,3,4,5], got {result}"
    
    # Test all same
    head = LinkedListOperations.create_linked_list([1, 1, 1, 1])
    result_head = LinkedListOperations.remove_duplicates_sorted(head)
    result = LinkedListOperations.linked_list_to_list(result_head)
    assert result == [1], f"Expected [1], got {result}"
    
    print("✓ remove_duplicates_sorted tests passed")

def test_partition_list():
    """Test partition_list function"""
    print("Testing partition_list...")
    
    # Test basic partition
    head = LinkedListOperations.create_linked_list([1, 4, 3, 2, 5, 2])
    result_head = LinkedListOperations.partition_list(head, 3)
    result = LinkedListOperations.linked_list_to_list(result_head)
    
    # Check that all elements < 3 come before all elements >= 3
    partition_index = -1
    for i, val in enumerate(result):
        if val >= 3:
            partition_index = i
            break
    
    if partition_index != -1:
        # Check all elements before partition_index are < 3
        for i in range(partition_index):
            assert result[i] < 3, f"Element {result[i]} at index {i} should be < 3"
        
        # Check all elements from partition_index onwards are >= 3
        for i in range(partition_index, len(result)):
            assert result[i] >= 3, f"Element {result[i]} at index {i} should be >= 3"
    
    # Test edge case: all elements less than x
    head = LinkedListOperations.create_linked_list([1, 2])
    result_head = LinkedListOperations.partition_list(head, 3)
    result = LinkedListOperations.linked_list_to_list(result_head)
    assert result == [1, 2], f"Expected [1,2], got {result}"
    
    print("✓ partition_list tests passed")

def run_all_tests():
    """Run all test functions"""
    print("Running Linked Lists Operations Tests...")
    print("=" * 50)
    
    try:
        # Test basic implementations
        test_singly_linked_list()
        test_doubly_linked_list()
        test_helper_methods()
        
        # Test core algorithms
        test_reverse_linked_list()
        test_has_cycle()
        test_find_cycle_start()
        test_merge_two_sorted_lists()
        test_find_middle_node()
        test_remove_nth_from_end()
        test_intersection_of_two_lists()
        test_is_palindrome()
        test_add_two_numbers()
        test_remove_duplicates_sorted()
        test_partition_list()
        
        print("=" * 50)
        print("🎉 All tests passed successfully!")
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1) 
