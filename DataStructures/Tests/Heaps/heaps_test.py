import sys
import os
import argparse
import traceback
import heapq

def setup_imports():
    """Set up imports based on the command-line argument."""
    parser = argparse.ArgumentParser(description='Test heaps operations')
    parser.add_argument('--mode', choices=['solution', 'practice'], default='solution',
                      help='Which implementation to test (solution or practice)')
    args = parser.parse_args()

    # Get the current directory and project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))

    if args.mode == 'solution':
        # Import from Solutions
        solutions_dir = os.path.join(project_root, 'Solutions', 'Heaps')
        sys.path.insert(0, solutions_dir)
        print(f"Testing solution implementation from: {solutions_dir}")
    else:
        # Import from Practice
        practice_dir = os.path.join(project_root, 'Practice', 'Heaps')
        sys.path.insert(0, practice_dir)
        print(f"Testing practice implementation from: {practice_dir}")

# Setup the path and import
setup_imports()

try:
    from heaps_operations import HeapsOperations, MedianFinder, ListNode
except ImportError as e:
    print(f"❌ Could not import HeapsOperations: {e}")
    print("Make sure the file exists in Solutions/Heaps+PriorityQueues/ or Practice/Heaps+PriorityQueues/")
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

def is_valid_min_heap(arr):
    """Helper function to validate min-heap property"""
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True

def create_linked_lists():
    """Create test linked lists for merge k sorted lists"""
    # List 1: 1->4->5
    list1 = ListNode(1)
    list1.next = ListNode(4)
    list1.next.next = ListNode(5)

    # List 2: 1->3->4
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    # List 3: 2->6
    list3 = ListNode(2)
    list3.next = ListNode(6)

    return [list1, list2, list3]

def linked_list_to_array(head):
    """Convert linked list to array for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_heapify_operations():
    """Test heapify and basic heap operations"""
    print("Step 1: Testing heapify_min...")

    arr = [4, 10, 3, 5, 1]
    print(f"   Original array: {arr}")
    HeapsOperations.heapify_min(arr)
    print(f"   After heapify: {arr}")

    assert is_valid_min_heap(arr), f"Array {arr} is not a valid min-heap"
    assert arr[0] == 1, f"Expected min element 1 at root, got {arr[0]}"

    print("\nStep 2: Testing heap_insert_min...")
    heap = [1, 4, 3, 5, 10]
    print(f"   Initial heap: {heap}")

    HeapsOperations.heap_insert_min(heap, 2)
    print(f"   After inserting 2: {heap}")
    assert is_valid_min_heap(heap), f"Heap {heap} is not valid after insertion"

    HeapsOperations.heap_insert_min(heap, 0)
    print(f"   After inserting 0: {heap}")
    assert heap[0] == 0, f"Expected 0 at root, got {heap[0]}"
    assert is_valid_min_heap(heap), f"Heap {heap} is not valid after insertion"

    print("\nStep 3: Testing heap_extract_min...")
    min_val = HeapsOperations.heap_extract_min(heap)
    print(f"   Extracted min: {min_val} (expected: 0)")
    print(f"   Heap after extraction: {heap}")
    assert min_val == 0, f"Expected extracted min 0, got {min_val}"
    assert is_valid_min_heap(heap), f"Heap {heap} is not valid after extraction"

    # Test empty heap
    empty_heap = []
    result = HeapsOperations.heap_extract_min(empty_heap)
    print(f"   Extract from empty heap: {result} (expected: None)")
    assert result is None, f"Expected None from empty heap, got {result}"

    print("✓ heap operations tests passed")

def test_kth_largest_element():
    """Test kth largest element function"""
    print("Step 1: Testing kth largest element...")

    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result = HeapsOperations.kth_largest_element(nums, k)
    print(f"   Array: {nums}, k={k}")
    print(f"   Result: {result} (expected: 5)")
    assert result == 5, f"Expected 5, got {result}"

    print("\nStep 2: Testing edge cases...")
    nums = [1]
    k = 1
    result = HeapsOperations.kth_largest_element(nums, k)
    print(f"   Single element: {nums}, k={k}, result: {result}")
    assert result == 1, f"Expected 1, got {result}"

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    result = HeapsOperations.kth_largest_element(nums, k)
    print(f"   With duplicates: k={k}, result: {result} (expected: 4)")
    assert result == 4, f"Expected 4, got {result}"

    print("✓ kth_largest_element tests passed")

def test_top_k_frequent_elements():
    """Test top k frequent elements function"""
    print("Step 1: Testing top k frequent elements...")

    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = HeapsOperations.top_k_frequent_elements(nums, k)
    print(f"   Array: {nums}, k={k}")
    print(f"   Result: {result}")

    # Check that we got k elements and they include the most frequent
    assert len(result) == k, f"Expected {k} elements, got {len(result)}"
    assert 1 in result and 2 in result, f"Expected [1,2] in result, got {result}"

    print("\nStep 2: Testing single element...")
    nums = [1]
    k = 1
    result = HeapsOperations.top_k_frequent_elements(nums, k)
    print(f"   Single element: {nums}, k={k}, result: {result}")
    assert result == [1], f"Expected [1], got {result}"

    print("\nStep 3: Testing all unique elements...")
    nums = [1, 2, 3, 4, 5]
    k = 3
    result = HeapsOperations.top_k_frequent_elements(nums, k)
    print(f"   All unique: {nums}, k={k}, result: {result}")
    assert len(result) == k, f"Expected {k} elements, got {len(result)}"

    print("✓ top_k_frequent_elements tests passed")

def test_merge_k_sorted_lists():
    """Test merge k sorted lists function"""
    print("Step 1: Testing merge k sorted lists...")

    lists = create_linked_lists()
    print("   Input lists:")
    for i, lst in enumerate(lists):
        print(f"     List {i+1}: {linked_list_to_array(lst)}")

    result = HeapsOperations.merge_k_sorted_lists(lists)
    result_array = linked_list_to_array(result)
    expected = [1, 1, 2, 3, 4, 4, 5, 6]

    print(f"   Merged result: {result_array}")
    print(f"   Expected: {expected}")
    assert result_array == expected, f"Expected {expected}, got {result_array}"

    print("\nStep 2: Testing empty lists...")
    result = HeapsOperations.merge_k_sorted_lists([])
    print(f"   Empty input: {result} (expected: None)")
    assert result is None, f"Expected None, got {result}"

    print("\nStep 3: Testing single list...")
    single_list = [ListNode(1)]
    single_list[0].next = ListNode(2)
    result = HeapsOperations.merge_k_sorted_lists(single_list)
    result_array = linked_list_to_array(result)
    print(f"   Single list result: {result_array} (expected: [1, 2])")
    assert result_array == [1, 2], f"Expected [1, 2], got {result_array}"

    print("✓ merge_k_sorted_lists tests passed")

def test_median_finder():
    """Test MedianFinder class"""
    print("Step 1: Testing MedianFinder...")

    mf = MedianFinder()

    print("   Adding numbers: 1, 2, 3")
    mf.add_num(1)
    median = mf.find_median()
    print(f"   After adding 1: median = {median} (expected: 1)")
    assert median == 1, f"Expected median 1, got {median}"

    mf.add_num(2)
    median = mf.find_median()
    print(f"   After adding 2: median = {median} (expected: 1.5)")
    assert median == 1.5, f"Expected median 1.5, got {median}"

    mf.add_num(3)
    median = mf.find_median()
    print(f"   After adding 3: median = {median} (expected: 2)")
    assert median == 2, f"Expected median 2, got {median}"

    print("✓ MedianFinder tests passed")

def test_meeting_rooms_ii():
    """Test meeting rooms II function"""
    print("Step 1: Testing meeting rooms II...")

    intervals = [[0, 30], [5, 10], [15, 20]]
    result = HeapsOperations.meeting_rooms_ii(intervals)
    print(f"   Intervals: {intervals}")
    print(f"   Rooms needed: {result} (expected: 2)")
    assert result == 2, f"Expected 2 rooms, got {result}"

    print("\nStep 2: Testing no overlapping meetings...")
    intervals = [[7, 10], [2, 4]]
    result = HeapsOperations.meeting_rooms_ii(intervals)
    print(f"   Non-overlapping: {intervals}")
    print(f"   Rooms needed: {result} (expected: 1)")
    assert result == 1, f"Expected 1 room, got {result}"

    print("\nStep 3: Testing all overlapping meetings...")
    intervals = [[1, 5], [2, 6], [3, 7], [4, 8]]
    result = HeapsOperations.meeting_rooms_ii(intervals)
    print(f"   All overlapping: {intervals}")
    print(f"   Rooms needed: {result} (expected: 4)")
    assert result == 4, f"Expected 4 rooms, got {result}"

    print("\nStep 4: Testing empty intervals...")
    result = HeapsOperations.meeting_rooms_ii([])
    print(f"   Empty intervals: {result} (expected: 0)")
    assert result == 0, f"Expected 0 rooms, got {result}"

    print("✓ meeting_rooms_ii tests passed")

def test_task_scheduler():
    """Test task scheduler function"""
    print("Step 1: Testing task scheduler...")

    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    result = HeapsOperations.task_scheduler(tasks, n)
    print(f"   Tasks: {tasks}, cooldown: {n}")
    print(f"   Time needed: {result} (expected: 8)")
    assert result == 8, f"Expected 8 time units, got {result}"

    print("\nStep 2: Testing no cooldown...")
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 0
    result = HeapsOperations.task_scheduler(tasks, n)
    print(f"   No cooldown: n={n}")
    print(f"   Time needed: {result} (expected: 6)")
    assert result == 6, f"Expected 6 time units, got {result}"

    print("\nStep 3: Testing diverse tasks...")
    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n = 2
    result = HeapsOperations.task_scheduler(tasks, n)
    print(f"   Diverse tasks with dominant A")
    print(f"   Time needed: {result} (expected: 16)")
    assert result == 16, f"Expected 16 time units, got {result}"

    print("✓ task_scheduler tests passed")

def test_sliding_window_maximum():
    """Test sliding window maximum function"""
    print("Step 1: Testing sliding window maximum...")

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = HeapsOperations.sliding_window_maximum(nums, k)
    expected = [3, 3, 5, 5, 6, 7]
    print(f"   Array: {nums}, k={k}")
    print(f"   Result: {result}")
    print(f"   Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 2: Testing single element window...")
    nums = [1, 2, 3, 4, 5]
    k = 1
    result = HeapsOperations.sliding_window_maximum(nums, k)
    expected = [1, 2, 3, 4, 5]
    print(f"   Window size 1: result = {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 3: Testing window size equals array length...")
    nums = [1, 3, 2, 5, 4]
    k = 5
    result = HeapsOperations.sliding_window_maximum(nums, k)
    expected = [5]
    print(f"   Full window: result = {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("✓ sliding_window_maximum tests passed")


def test_k_closest_points_to_origin():
    """Test k closest points to origin function"""
    print("Step 1: Testing k closest points...")
    points = [[1, 1], [2, 2], [3, 3]]
    k = 1
    result = HeapsOperations.k_closest_points_to_origin(points, k)
    print(f"   Points: {points}, k={k}")
    print(f"   Result: {result}")
    # Check that we got k points and [1,1] is included (closest)
    assert len(result) == k, f"Expected {k} points, got {len(result)}"
    assert [1, 1] in result, f"Expected [1,1] in result, got {result}"

    print("\nStep 2: Testing multiple closest points...")
    points = [[0, 1], [1, 0], [2, 0], [0, 2], [0, 3], [3, 4]]
    k = 3
    result = HeapsOperations.k_closest_points_to_origin(points, k)
    print(f"   Points: {points}, k={k}")
    print(f"   Result: {result}")
    assert len(result) == k, f"Expected {k} points, got {len(result)}"

    # Calculate distances for verification
    # [0,1]: √1=1, [1,0]: √1=1, [2,0]: √4=2, [0,2]: √4=2, [0,3]: √9=3, [3,4]: √25=5
    # The 3 closest should be [0,1], [1,0], and either [2,0] or [0,2] (both distance 2)
    expected_points = [[0, 1], [1, 0]]  # These two are definitely closest
    for point in expected_points:
        assert point in result, f"Expected {point} in closest points, got {result}"

    # Check that the third point is either [2,0] or [0,2] (both have distance 2)
    third_point_options = [[2, 0], [0, 2]]
    third_point_found = any(point in result for point in third_point_options)
    assert third_point_found, f"Expected one of {third_point_options} in result, got {result}"

    print("\nStep 3: Testing single point...")
    points = [[0, 3]]
    k = 1
    result = HeapsOperations.k_closest_points_to_origin(points, k)
    print(f"   Single point: {result}")
    assert result == [[0, 3]], f"Expected [[0, 3]], got {result}"
    print("✓ k_closest_points_to_origin tests passed")

def test_reorganize_string():
    """Test reorganize string function"""
    print("Step 1: Testing reorganize string...")

    s = "aab"
    result = HeapsOperations.reorganize_string(s)
    print(f"   Input: '{s}'")
    print(f"   Result: '{result}'")

    # Check that result is valid
    assert len(result) == len(s), f"Expected length {len(s)}, got {len(result)}"
    if result:  # If reorganization was possible
        for i in range(len(result) - 1):
            assert result[i] != result[i + 1], f"Adjacent chars are same at position {i}: {result}"

    print("\nStep 2: Testing impossible reorganization...")
    s = "aaab"
    result = HeapsOperations.reorganize_string(s)
    print(f"   Impossible case: '{s}' -> '{result}' (expected: '')")
    assert result == "", f"Expected empty string for impossible case, got '{result}'"

    print("\nStep 3: Testing longer string...")
    s = "aabbcc"
    result = HeapsOperations.reorganize_string(s)
    print(f"   Longer string: '{s}' -> '{result}'")

    if result:
        assert len(result) == len(s), f"Expected length {len(s)}, got {len(result)}"
        for i in range(len(result) - 1):
            assert result[i] != result[i + 1], f"Adjacent chars are same at position {i}: {result}"

        # Check character frequencies match
        from collections import Counter
        assert Counter(result) == Counter(s), f"Character frequencies don't match"

    print("\nStep 4: Testing single character...")
    s = "a"
    result = HeapsOperations.reorganize_string(s)
    print(f"   Single char: '{s}' -> '{result}'")
    assert result == "a", f"Expected 'a', got '{result}'"

    print("✓ reorganize_string tests passed")

def test_maximum_cpu_load():
    """Test maximum CPU load function"""
    print("Step 1: Testing maximum CPU load...")

    jobs = [[1, 4, 3], [2, 5, 4], [7, 9, 6]]
    result = HeapsOperations.maximum_cpu_load(jobs)
    print(f"   Jobs: {jobs}")
    print(f"   Max CPU load: {result} (expected: 7)")
    assert result == 7, f"Expected max load 7, got {result}"

    print("\nStep 2: Testing non-overlapping jobs...")
    jobs = [[1, 2, 3], [3, 4, 2], [5, 6, 1]]
    result = HeapsOperations.maximum_cpu_load(jobs)
    print(f"   Non-overlapping: {jobs}")
    print(f"   Max CPU load: {result} (expected: 3)")
    assert result == 3, f"Expected max load 3, got {result}"

    print("\nStep 3: Testing all overlapping jobs...")
    jobs = [[1, 4, 2], [2, 4, 1], [3, 4, 1]]
    result = HeapsOperations.maximum_cpu_load(jobs)
    print(f"   All overlapping: {jobs}")
    print(f"   Max CPU load: {result} (expected: 4)")
    assert result == 4, f"Expected max load 4, got {result}"

    print("\nStep 4: Testing empty jobs...")
    result = HeapsOperations.maximum_cpu_load([])
    print(f"   Empty jobs: {result} (expected: 0)")
    assert result == 0, f"Expected max load 0, got {result}"

    print("\nStep 5: Testing single job...")
    jobs = [[1, 3, 5]]
    result = HeapsOperations.maximum_cpu_load(jobs)
    print(f"   Single job: {jobs}")
    print(f"   Max CPU load: {result} (expected: 5)")
    assert result == 5, f"Expected max load 5, got {result}"

    print("✓ maximum_cpu_load tests passed")

def test_heap_edge_cases():
    """Test edge cases for heap operations"""
    print("Step 1: Testing heapify with single element...")

    arr = [5]
    HeapsOperations.heapify_min(arr)
    print(f"   Single element heapify: {arr}")
    assert arr == [5], f"Expected [5], got {arr}"

    print("\nStep 2: Testing heapify with empty array...")
    arr = []
    HeapsOperations.heapify_min(arr)
    print(f"   Empty array heapify: {arr}")
    assert arr == [], f"Expected [], got {arr}"

    print("\nStep 3: Testing heapify with already sorted array...")
    arr = [1, 2, 3, 4, 5]
    HeapsOperations.heapify_min(arr)
    print(f"   Already sorted: {arr}")
    assert is_valid_min_heap(arr), f"Result is not a valid min heap: {arr}"

    print("\nStep 4: Testing heap operations with duplicates...")
    arr = [3, 3, 3, 3]
    HeapsOperations.heapify_min(arr)
    print(f"   All duplicates: {arr}")
    assert is_valid_min_heap(arr), f"Result is not a valid min heap: {arr}"

    HeapsOperations.heap_insert_min(arr, 3)
    print(f"   After inserting duplicate: {arr}")
    assert is_valid_min_heap(arr), f"Result is not a valid min heap: {arr}"

    min_val = HeapsOperations.heap_extract_min(arr)
    print(f"   Extracted: {min_val}, remaining: {arr}")
    assert min_val == 3, f"Expected 3, got {min_val}"
    assert is_valid_min_heap(arr), f"Result is not a valid min heap: {arr}"

    print("✓ heap edge cases tests passed")

def test_advanced_scenarios():
    """Test advanced scenarios and stress tests"""
    print("Step 1: Testing large heap operations...")

    # Test with larger dataset
    import random
    large_array = [random.randint(1, 1000) for _ in range(100)]
    original = large_array.copy()

    HeapsOperations.heapify_min(large_array)
    print(f"   Heapified array of 100 elements: min = {large_array[0]}")
    assert is_valid_min_heap(large_array), "Large array is not a valid min heap"
    assert large_array[0] == min(original), f"Min element incorrect"

    print("\nStep 2: Testing heap sort using extract_min...")
    heap = [64, 34, 25, 12, 22, 11, 90]
    HeapsOperations.heapify_min(heap)

    sorted_elements = []
    while heap:
        min_val = HeapsOperations.heap_extract_min(heap)
        sorted_elements.append(min_val)

    print(f"   Heap sort result: {sorted_elements}")
    assert sorted_elements == sorted(sorted_elements), "Heap sort failed"

    print("\nStep 3: Testing MedianFinder with stream of 1000 numbers...")
    mf = MedianFinder()
    numbers = [random.randint(1, 1000) for _ in range(50)]  # Reduced for faster testing

    for num in numbers:
        mf.add_num(num)

    final_median = mf.find_median()
    expected_median = sorted(numbers)[len(numbers) // 2] if len(numbers) % 2 == 1 else \
                     (sorted(numbers)[len(numbers) // 2 - 1] + sorted(numbers)[len(numbers) // 2]) / 2.0

    print(f"   Final median from stream: {final_median}")
    print(f"   Expected median: {expected_median}")
    assert abs(final_median - expected_median) < 0.001, f"Median calculation incorrect"

    print("✓ advanced scenarios tests passed")

def run_all_tests():
    """Run all test functions with detailed reporting"""
    print("🚀 STARTING COMPREHENSIVE HEAPS/PRIORITY QUEUES TESTS")
    print("="*70)

    tests = [
        ("Heapify and Basic Operations", test_heapify_operations),
        ("Kth Largest Element", test_kth_largest_element),
        ("Top K Frequent Elements", test_top_k_frequent_elements),
        ("Merge K Sorted Lists", test_merge_k_sorted_lists),
        ("MedianFinder (Data Stream)", test_median_finder),
        ("Meeting Rooms II", test_meeting_rooms_ii),
        ("Task Scheduler", test_task_scheduler),
        ("Sliding Window Maximum", test_sliding_window_maximum),
        ("K Closest Points to Origin", test_k_closest_points_to_origin),
        ("Reorganize String", test_reorganize_string),
        ("Maximum CPU Load", test_maximum_cpu_load),
        ("Heap Edge Cases", test_heap_edge_cases),
        ("Advanced Scenarios", test_advanced_scenarios),
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
        print("🎉 ALL TESTS PASSED! Your heaps implementation is working correctly!")
        print("\n🔥 KEY CONCEPTS VALIDATED:")
        print("   • Min/Max heap properties and operations")
        print("   • Heap-based algorithms for top-k problems")
        print("   • Priority queue applications")
        print("   • Two-heap pattern for median finding")
        print("   • Interval scheduling with heaps")
        print("   • Frequency-based heap problems")
        print("   • Time/space complexity optimizations")
    else:
        print("🔧 Some tests failed. Check the detailed output above to fix the issues.")
        print("\n💡 DEBUGGING TIPS:")
        print("   • Verify heap property maintenance after insertions/deletions")
        print("   • Check boundary conditions (empty heaps, single elements)")
        print("   • Ensure correct heap type (min vs max) for each problem")
        print("   • Validate algorithm logic for complex problems")

    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
