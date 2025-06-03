import sys
import os
import argparse
import traceback

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
    print("Make sure the file exists in Solutions/LinkedLists/ or Practice/LinkedLists/")
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

def test_singly_linked_list():
    """Test SinglyLinkedList implementation with detailed logging"""
    
    print("Step 1: Creating SinglyLinkedList instance...")
    try:
        sll = LinkedListOperations.SinglyLinkedList()
        print(f"   ✓ SinglyLinkedList created: {type(sll)}")
    except Exception as e:
        print(f"   ❌ Failed to create SinglyLinkedList: {e}")
        raise
    
    print("\nStep 2: Testing empty list state...")
    get_invalid = sll.get(0)
    size = sll.size
    print(f"   get(0) on empty list returned: {get_invalid} (expected: -1)")
    print(f"   size: {size} (expected: 0)")
    assert get_invalid == -1, f"Empty list get should return -1, got {get_invalid}"
    assert size == 0, f"Empty list should have size 0, got {size}"
    print("   ✓ Empty list tests passed")
    
    print("\nStep 3: Testing add_at_head operations...")
    print("   Adding 1 at head...")
    sll.add_at_head(1)
    list_state_1 = sll.to_list()
    print(f"   List state: {list_state_1} (expected: [1])")
    print(f"   Size: {sll.size} (expected: 1)")
    assert list_state_1 == [1], f"After add_at_head(1), expected [1], got {list_state_1}"
    assert sll.size == 1, f"Size should be 1, got {sll.size}"
    
    print("   Adding 2 at head...")
    sll.add_at_head(2)
    list_state_2 = sll.to_list()
    print(f"   List state: {list_state_2} (expected: [2, 1])")
    assert list_state_2 == [2, 1], f"After add_at_head(2), expected [2, 1], got {list_state_2}"
    print("   ✓ add_at_head operations passed")
    
    print("\nStep 4: Testing add_at_tail operations...")
    print("   Adding 3 at tail...")
    sll.add_at_tail(3)
    list_state_3 = sll.to_list()
    print(f"   List state: {list_state_3} (expected: [2, 1, 3])")
    assert list_state_3 == [2, 1, 3], f"After add_at_tail(3), expected [2, 1, 3], got {list_state_3}"
    print("   ✓ add_at_tail operations passed")
    
    print("\nStep 5: Testing get operations...")
    get_0 = sll.get(0)
    get_1 = sll.get(1)
    get_2 = sll.get(2)
    get_invalid = sll.get(3)
    print(f"   get(0): {get_0} (expected: 2)")
    print(f"   get(1): {get_1} (expected: 1)")
    print(f"   get(2): {get_2} (expected: 3)")
    print(f"   get(3): {get_invalid} (expected: -1)")
    assert get_0 == 2, f"get(0) should return 2, got {get_0}"
    assert get_1 == 1, f"get(1) should return 1, got {get_1}"
    assert get_2 == 3, f"get(2) should return 3, got {get_2}"
    assert get_invalid == -1, f"get(3) should return -1, got {get_invalid}"
    print("   ✓ get operations passed")
    
    print("\nStep 6: Testing add_at_index operations...")
    print("   Adding 4 at index 1...")
    sll.add_at_index(1, 4)
    list_state_4 = sll.to_list()
    print(f"   List state: {list_state_4} (expected: [2, 4, 1, 3])")
    assert list_state_4 == [2, 4, 1, 3], f"After add_at_index(1, 4), expected [2, 4, 1, 3], got {list_state_4}"
    print("   ✓ add_at_index operations passed")
    
    print("\nStep 7: Testing delete_at_index operations...")
    print("   Deleting at index 1...")
    sll.delete_at_index(1)
    list_state_5 = sll.to_list()
    print(f"   List state: {list_state_5} (expected: [2, 1, 3])")
    assert list_state_5 == [2, 1, 3], f"After delete_at_index(1), expected [2, 1, 3], got {list_state_5}"
    
    print("   Deleting head (index 0)...")
    sll.delete_at_index(0)
    list_state_6 = sll.to_list()
    print(f"   List state: {list_state_6} (expected: [1, 3])")
    assert list_state_6 == [1, 3], f"After delete_at_index(0), expected [1, 3], got {list_state_6}"
    print("   ✓ delete_at_index operations passed")

def test_doubly_linked_list():
    """Test DoublyLinkedList implementation with detailed logging"""
    
    print("Step 1: Creating DoublyLinkedList instance...")
    try:
        dll = LinkedListOperations.DoublyLinkedList()
        print(f"   ✓ DoublyLinkedList created: {type(dll)}")
    except Exception as e:
        print(f"   ❌ Failed to create DoublyLinkedList: {e}")
        raise
    
    print("\nStep 2: Testing empty list state...")
    is_empty = dll.is_empty()
    size = dll.size
    print(f"   is_empty(): {is_empty} (expected: True)")
    print(f"   size: {size} (expected: 0)")
    assert is_empty == True, f"New list should be empty, got {is_empty}"
    assert size == 0, f"New list should have size 0, got {size}"
    print("   ✓ Empty list tests passed")
    
    print("\nStep 3: Testing add_first operations...")
    print("   Adding 1 at front...")
    dll.add_first(1)
    list_state_1 = dll.to_list()
    print(f"   List state: {list_state_1} (expected: [1])")
    print(f"   Size: {dll.size} (expected: 1)")
    assert list_state_1 == [1], f"After add_first(1), expected [1], got {list_state_1}"
    assert dll.size == 1, f"Size should be 1, got {dll.size}"
    
    print("   Adding 2 at front...")
    dll.add_first(2)
    list_state_2 = dll.to_list()
    print(f"   List state: {list_state_2} (expected: [2, 1])")
    assert list_state_2 == [2, 1], f"After add_first(2), expected [2, 1], got {list_state_2}"
    print("   ✓ add_first operations passed")
    
    print("\nStep 4: Testing add_last operations...")
    print("   Adding 3 at end...")
    dll.add_last(3)
    list_state_3 = dll.to_list()
    print(f"   List state: {list_state_3} (expected: [2, 1, 3])")
    assert list_state_3 == [2, 1, 3], f"After add_last(3), expected [2, 1, 3], got {list_state_3}"
    print("   ✓ add_last operations passed")
    
    print("\nStep 5: Testing remove_first operations...")
    print("   Removing first element...")
    first = dll.remove_first()
    list_state_4 = dll.to_list()
    print(f"   remove_first() returned: {first} (expected: 2)")
    print(f"   List state: {list_state_4} (expected: [1, 3])")
    assert first == 2, f"remove_first should return 2, got {first}"
    assert list_state_4 == [1, 3], f"After remove_first, expected [1, 3], got {list_state_4}"
    print("   ✓ remove_first operations passed")
    
    print("\nStep 6: Testing remove_last operations...")
    print("   Removing last element...")
    last = dll.remove_last()
    list_state_5 = dll.to_list()
    print(f"   remove_last() returned: {last} (expected: 3)")
    print(f"   List state: {list_state_5} (expected: [1])")
    assert last == 3, f"remove_last should return 3, got {last}"
    assert list_state_5 == [1], f"After remove_last, expected [1], got {list_state_5}"
    
    print("   Removing final element...")
    dll.remove_first()
    final_empty = dll.is_empty()
    print(f"   is_empty after removing all: {final_empty} (expected: True)")
    assert final_empty == True, f"List should be empty after removing all, got {final_empty}"
    print("   ✓ remove_last operations passed")
    
    print("\nStep 7: Testing exception handling...")
    print("   Testing remove_first from empty list...")
    try:
        dll.remove_first()
        assert False, "Should raise IndexError when removing from empty list"
    except IndexError as e:
        print(f"   ✓ Correctly raised IndexError: {e}")
    except Exception as e:
        assert False, f"Should raise IndexError, but got {type(e).__name__}: {e}"

def test_helper_methods():
    """Test helper methods with detailed logging"""
    
    print("Step 1: Testing create_linked_list...")
    test_values = [1, 2, 3, 4]
    print(f"   Creating list from {test_values}...")
    head = LinkedListOperations.create_linked_list(test_values)
    result = LinkedListOperations.linked_list_to_list(head)
    print(f"   Result: {result} (expected: {test_values})")
    assert result == test_values, f"Expected {test_values}, got {result}"
    print("   ✓ create_linked_list passed")
    
    print("\nStep 2: Testing empty list creation...")
    empty_head = LinkedListOperations.create_linked_list([])
    print(f"   Empty list head: {empty_head} (expected: None)")
    assert empty_head is None, f"Empty list should return None, got {empty_head}"
    print("   ✓ Empty list creation passed")
    
    print("\nStep 3: Testing single element list...")
    single_head = LinkedListOperations.create_linked_list([42])
    single_result = LinkedListOperations.linked_list_to_list(single_head)
    print(f"   Single element result: {single_result} (expected: [42])")
    assert single_result == [42], f"Expected [42], got {single_result}"
    print("   ✓ Single element list passed")
    
    print("\nStep 4: Testing print_linked_list...")
    head = LinkedListOperations.create_linked_list([1, 2, 3])
    print_result = LinkedListOperations.print_linked_list(head)
    expected_print = "1 -> 2 -> 3 -> None"
    print(f"   Print result: '{print_result}' (expected: '{expected_print}')")
    assert print_result == expected_print, f"Expected '{expected_print}', got '{print_result}'"
    print("   ✓ print_linked_list passed")

def test_reverse_linked_list():
    """Test reverse linked list functions with detailed logging"""
    
    print("Step 1: Testing iterative reverse...")
    test_values = [1, 2, 3, 4, 5]
    print(f"   Original list: {test_values}")
    head = LinkedListOperations.create_linked_list(test_values)
    reversed_head = LinkedListOperations.reverse_linked_list(head)
    result = LinkedListOperations.linked_list_to_list(reversed_head)
    expected = [5, 4, 3, 2, 1]
    print(f"   Reversed result: {result} (expected: {expected})")
    assert result == expected, f"Expected {expected}, got {result}"
    print("   ✓ Iterative reverse passed")
    
    print("\nStep 2: Testing recursive reverse...")
    head = LinkedListOperations.create_linked_list(test_values)
    reversed_head = LinkedListOperations.reverse_linked_list_recursive(head)
    result = LinkedListOperations.linked_list_to_list(reversed_head)
    print(f"   Recursive result: {result} (expected: {expected})")
    assert result == expected, f"Expected {expected}, got {result}"
    print("   ✓ Recursive reverse passed")
    
    print("\nStep 3: Testing edge cases...")
    # Single node
    single = LinkedListOperations.create_linked_list([1])
    reversed_single = LinkedListOperations.reverse_linked_list(single)
    single_result = LinkedListOperations.linked_list_to_list(reversed_single)
    print(f"   Single node reverse: {single_result} (expected: [1])")
    assert single_result == [1], f"Expected [1], got {single_result}"
    
    # Empty list
    empty = LinkedListOperations.reverse_linked_list(None)
    print(f"   Empty list reverse: {empty} (expected: None)")
    assert empty is None, f"Expected None, got {empty}"
    print("   ✓ Edge cases passed")

def test_cycle_detection():
    """Test cycle detection functions with detailed logging"""
    
    print("Step 1: Testing has_cycle with no cycle...")
    head = LinkedListOperations.create_linked_list([1, 2, 3, 4])
    has_cycle_result = LinkedListOperations.has_cycle(head)
    print(f"   has_cycle([1,2,3,4]): {has_cycle_result} (expected: False)")
    assert has_cycle_result == False, f"List without cycle should return False, got {has_cycle_result}"
    print("   ✓ No cycle detection passed")
    
    print("\nStep 2: Testing has_cycle with cycle...")
    # Create cycle: 1->2->3->4->2 (4 points back to 2)
    head = LinkedListOperations.create_linked_list([1, 2, 3, 4])
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    nodes[-1].next = nodes[1]  # Create cycle: 4 -> 2
    
    has_cycle_result = LinkedListOperations.has_cycle(head)
    print(f"   has_cycle with cycle: {has_cycle_result} (expected: True)")
    assert has_cycle_result == True, f"List with cycle should return True, got {has_cycle_result}"
    print("   ✓ Cycle detection passed")
    
    print("\nStep 3: Testing find_cycle_start...")
    cycle_start = LinkedListOperations.find_cycle_start(head)
    print(f"   Cycle start node value: {cycle_start.val if cycle_start else None} (expected: 2)")
    print(f"   Is same node as nodes[1]: {cycle_start is nodes[1]} (expected: True)")
    assert cycle_start is not None, f"Should find cycle start, got None"
    assert cycle_start.val == 2, f"Cycle start should have value 2, got {cycle_start.val}"
    assert cycle_start is nodes[1], f"Should return exact node where cycle starts"
    print("   ✓ Cycle start detection passed")
    
    print("\nStep 4: Testing no cycle for find_cycle_start...")
    no_cycle_head = LinkedListOperations.create_linked_list([1, 2, 3, 4])
    no_cycle_start = LinkedListOperations.find_cycle_start(no_cycle_head)
    print(f"   find_cycle_start with no cycle: {no_cycle_start} (expected: None)")
    assert no_cycle_start is None, f"No cycle should return None, got {no_cycle_start}"
    print("   ✓ No cycle start detection passed")

def test_merge_two_sorted_lists():
    """Test merge two sorted lists with detailed logging"""
    
    print("Step 1: Testing basic merge...")
    list1_values = [1, 2, 4]
    list2_values = [1, 3, 4]
    print(f"   List 1: {list1_values}")
    print(f"   List 2: {list2_values}")
    
    list1 = LinkedListOperations.create_linked_list(list1_values)
    list2 = LinkedListOperations.create_linked_list(list2_values)
    merged = LinkedListOperations.merge_two_sorted_lists(list1, list2)
    result = LinkedListOperations.linked_list_to_list(merged)
    expected = [1, 1, 2, 3, 4, 4]
    print(f"   Merged result: {result} (expected: {expected})")
    assert result == expected, f"Expected {expected}, got {result}"
    print("   ✓ Basic merge passed")
    
    print("\nStep 2: Testing merge with empty list...")
    list1 = None
    list2 = LinkedListOperations.create_linked_list([0])
    merged = LinkedListOperations.merge_two_sorted_lists(list1, list2)
    result = LinkedListOperations.linked_list_to_list(merged)
    expected = [0]
    print(f"   Merge None + [0]: {result} (expected: {expected})")
    assert result == expected, f"Expected {expected}, got {result}"
    print("   ✓ Empty list merge passed")
    
    print("\nStep 3: Testing merge both empty...")
    merged = LinkedListOperations.merge_two_sorted_lists(None, None)
    print(f"   Merge None + None: {merged} (expected: None)")
    assert merged is None, f"Merging two empty lists should return None, got {merged}"
    print("   ✓ Both empty merge passed")

def test_advanced_operations():
    """Test advanced linked list operations with detailed logging"""
    
    print("Step 1: Testing find_middle_node...")
    # Odd length
    odd_list = LinkedListOperations.create_linked_list([1, 2, 3, 4, 5])
    middle_odd = LinkedListOperations.find_middle_node(odd_list)
    print(f"   Middle of [1,2,3,4,5]: {middle_odd.val} (expected: 3)")
    assert middle_odd.val == 3, f"Middle should be 3, got {middle_odd.val}"
    
    # Even length
    even_list = LinkedListOperations.create_linked_list([1, 2, 3, 4, 5, 6])
    middle_even = LinkedListOperations.find_middle_node(even_list)
    print(f"   Middle of [1,2,3,4,5,6]: {middle_even.val} (expected: 4)")
    assert middle_even.val == 4, f"Middle should be 4, got {middle_even.val}"
    print("   ✓ find_middle_node passed")
    
    print("\nStep 2: Testing is_palindrome...")
    # Palindrome cases
    palindrome_cases = [
        ([1, 2, 3, 2, 1], "odd palindrome"),
        ([1, 2, 2, 1], "even palindrome"),
        ([1], "single node"),
        ([], "empty list")
    ]
    
    for values, description in palindrome_cases:
        head = LinkedListOperations.create_linked_list(values) if values else None
        result = LinkedListOperations.is_palindrome(head)
        print(f"   is_palindrome({values}) [{description}]: {result} (expected: True)")
        assert result == True, f"{description} should be palindrome, got {result}"
    
    # Non-palindrome
    non_palindrome = LinkedListOperations.create_linked_list([1, 2, 3, 4, 5])
    result = LinkedListOperations.is_palindrome(non_palindrome)
    print(f"   is_palindrome([1,2,3,4,5]) [non-palindrome]: {result} (expected: False)")
    assert result == False, f"Non-palindrome should return False, got {result}"
    print("   ✓ is_palindrome passed")
    
    print("\nStep 3: Testing add_two_numbers...")
    # 342 + 465 = 807
    l1 = LinkedListOperations.create_linked_list([2, 4, 3])  # 342
    l2 = LinkedListOperations.create_linked_list([5, 6, 4])  # 465
    result_head = LinkedListOperations.add_two_numbers(l1, l2)
    result = LinkedListOperations.linked_list_to_list(result_head)
    expected = [7, 0, 8]  # 807
    print(f"   add_two_numbers([2,4,3], [5,6,4]): {result} (expected: {expected})")
    assert result == expected, f"342 + 465 = 807: expected {expected}, got {result}"
    print("   ✓ add_two_numbers passed")

def run_all_tests():
    """Run all test functions with detailed reporting"""
    print("🚀 STARTING COMPREHENSIVE LINKED LISTS TESTS")
    print("="*70)
    
    tests = [
        ("SinglyLinkedList Implementation", test_singly_linked_list),
        ("DoublyLinkedList Implementation", test_doubly_linked_list),
        ("Helper Methods", test_helper_methods),
        ("Reverse Linked List", test_reverse_linked_list),
        ("Cycle Detection", test_cycle_detection),
        ("Merge Two Sorted Lists", test_merge_two_sorted_lists),
        ("Advanced Operations", test_advanced_operations),
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
        print("🎉 ALL TESTS PASSED! Your linked list implementation is working correctly!")
    else:
        print("🔧 Some tests failed. Check the detailed output above to fix the issues.")
    
    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1) 
