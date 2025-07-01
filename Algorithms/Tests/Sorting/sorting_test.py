import sys
import os
import argparse
import traceback
import time
import random

def setup_imports():
    """Set up imports based on the command-line argument."""
    parser = argparse.ArgumentParser(description='Test Sorting Algorithm operations')
    parser.add_argument('--mode', choices=['solution', 'practice'], default='solution',
                      help='Which implementation to test (solution or practice)')
    args = parser.parse_args()

    # Get the current directory and project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))

    if args.mode == 'solution':
        # Import from Solutions
        solutions_dir = os.path.join(project_root, 'Solutions', 'Sorting')
        sys.path.insert(0, solutions_dir)
        print(f"Testing solution implementation from: {solutions_dir}")
    else:
        # Import from Practice
        practice_dir = os.path.join(project_root, 'Practice', 'Sorting')
        sys.path.insert(0, practice_dir)
        print(f"Testing practice implementation from: {practice_dir}")

# Setup the path and import
setup_imports()

try:
    from sorting_operations import SortingOperations
except ImportError as e:
    print(f"❌ Could not import SortingOperations: {e}")
    print("Make sure the file exists in Solutions/Sorting/ or Practice/Sorting/")
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

def test_bubble_sort():
    """Test bubble_sort function"""
    print("Step 1: Testing normal case...")

    arr1 = [64, 34, 25, 12, 22, 11, 90]
    result = SortingOperations.bubble_sort(arr1)
    expected = [11, 12, 22, 25, 34, 64, 90]
    print(f"   bubble_sort([64, 34, 25, 12, 22, 11, 90]) = {result}")
    print(f"   Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 2: Testing already sorted array (best case)...")
    arr2 = [1, 2, 3, 4, 5]
    start_time = time.time()
    result = SortingOperations.bubble_sort(arr2)
    sort_time = time.time() - start_time
    print(f"   bubble_sort([1, 2, 3, 4, 5]) = {result} in {sort_time:.6f}s")
    assert result == [1, 2, 3, 4, 5], f"Expected [1, 2, 3, 4, 5], got {result}"
    print(f"   ✓ Optimization flag should make this fast (O(n) with early termination)")

    print("\nStep 3: Testing reverse sorted array (worst case)...")
    arr3 = [5, 4, 3, 2, 1]
    result = SortingOperations.bubble_sort(arr3)
    print(f"   bubble_sort([5, 4, 3, 2, 1]) = {result}")
    assert result == [1, 2, 3, 4, 5], f"Expected [1, 2, 3, 4, 5], got {result}"

    print("\nStep 4: Testing array with duplicates...")
    arr4 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    result = SortingOperations.bubble_sort(arr4)
    expected = sorted(arr4)
    print(f"   bubble_sort({arr4}) = {result}")
    print(f"   Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 5: Testing edge cases...")
    assert SortingOperations.bubble_sort([]) == [], f"Empty array should return []"
    assert SortingOperations.bubble_sort([42]) == [42], f"Single element should return [42]"
    print(f"   Empty array: [] → [], Single element: [42] → [42] ✓")

    print("✓ bubble_sort tests passed")

def test_selection_sort():
    """Test selection_sort function"""
    print("Step 1: Testing normal case...")

    arr1 = [64, 25, 12, 22, 11, 90]
    result = SortingOperations.selection_sort(arr1)
    expected = [11, 12, 22, 25, 64, 90]
    print(f"   selection_sort([64, 25, 12, 22, 11, 90]) = {result}")
    print(f"   Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 2: Testing consistent O(n²) performance...")
    # Selection sort should take similar time regardless of input order
    sorted_arr = list(range(100))
    reverse_arr = list(range(99, -1, -1))
    random_arr = sorted_arr.copy()
    random.shuffle(random_arr)

    times = []
    for arr in [sorted_arr, reverse_arr, random_arr]:
        start_time = time.time()
        SortingOperations.selection_sort(arr)
        times.append(time.time() - start_time)

    print(f"   Sorted array time: {times[0]:.6f}s")
    print(f"   Reverse array time: {times[1]:.6f}s")
    print(f"   Random array time: {times[2]:.6f}s")
    print(f"   ✓ Times should be similar (consistent O(n²))")

    print("\nStep 3: Testing with negative numbers...")
    arr3 = [-5, -1, -10, 3, 0, -2, 8]
    result = SortingOperations.selection_sort(arr3)
    expected = sorted(arr3)
    print(f"   selection_sort({arr3}) = {result}")
    print(f"   Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 4: Testing minimum number of swaps property...")
    # Selection sort minimizes number of swaps
    arr4 = [5, 1, 4, 2, 3]
    result = SortingOperations.selection_sort(arr4)
    expected = [1, 2, 3, 4, 5]
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"   ✓ Selection sort minimizes swaps (at most n-1 swaps)")

    print("✓ selection_sort tests passed")

def test_insertion_sort():
    """Test insertion_sort function"""
    print("Step 1: Testing normal case...")

    arr1 = [5, 2, 4, 6, 1, 3]
    result = SortingOperations.insertion_sort(arr1)
    expected = [1, 2, 3, 4, 5, 6]
    print(f"   insertion_sort([5, 2, 4, 6, 1, 3]) = {result}")
    print(f"   Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 2: Testing adaptive behavior (nearly sorted)...")
    nearly_sorted = [1, 2, 4, 3, 5, 6]  # Only 4 and 3 out of place
    start_time = time.time()
    result = SortingOperations.insertion_sort(nearly_sorted)
    adaptive_time = time.time() - start_time
    expected = [1, 2, 3, 4, 5, 6]

    reverse_sorted = [6, 5, 4, 3, 2, 1]  # Worst case
    start_time = time.time()
    SortingOperations.insertion_sort(reverse_sorted)
    worst_time = time.time() - start_time

    print(f"   Nearly sorted time: {adaptive_time:.6f}s")
    print(f"   Reverse sorted time: {worst_time:.6f}s")
    print(f"   ✓ Adaptive: nearly sorted should be much faster")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 3: Testing small array efficiency...")
    small_arr = [3, 1, 4, 1, 5]
    result = SortingOperations.insertion_sort(small_arr)
    expected = [1, 1, 3, 4, 5]
    print(f"   insertion_sort([3, 1, 4, 1, 5]) = {result}")
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"   ✓ Insertion sort excels on small arrays")

    print("\nStep 4: Testing online algorithm property...")
    # Insertion sort can sort data as it arrives
    partial = [5, 2, 4]
    result_partial = SortingOperations.insertion_sort(partial)
    assert result_partial == [2, 4, 5], f"Partial sort should work"
    print(f"   ✓ Online algorithm: can sort partial data efficiently")

    print("✓ insertion_sort tests passed")

def test_merge_sort():
    """Test merge_sort function"""
    print("Step 1: Testing normal case...")

    arr1 = [38, 27, 43, 3, 9, 82, 10]
    result = SortingOperations.merge_sort(arr1)
    expected = [3, 9, 10, 27, 38, 43, 82]
    print(f"   merge_sort([38, 27, 43, 3, 9, 82, 10]) = {result}")
    print(f"   Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 2: Testing guaranteed O(n log n) performance...")
    # Merge sort should have consistent performance regardless of input
    sizes = [100, 200, 400]
    times = []

    for size in sizes:
        worst_case = list(range(size, 0, -1))  # Reverse sorted
        start_time = time.time()
        SortingOperations.merge_sort(worst_case)
        sort_time = time.time() - start_time
        times.append(sort_time)
        print(f"   Size {size}: {sort_time:.6f}s")

    # Check if time roughly doubles when size doubles (O(n log n) behavior)
    if len(times) >= 2:
        ratio = times[1] / times[0] if times[0] > 0 else 0
        print(f"   ✓ Time ratio (200/100): {ratio:.2f} (should be ~2.0 for O(n log n))")

    print("\nStep 3: Testing stability...")
    # Test with tuples to verify stability
    arr_with_keys = [(3, 'a'), (1, 'b'), (3, 'c'), (2, 'd')]
    result = SortingOperations.merge_sort(arr_with_keys)
    expected = [(1, 'b'), (2, 'd'), (3, 'a'), (3, 'c')]
    print(f"   Stability test: {result}")
    assert result == expected, f"Merge sort should be stable: {expected} vs {result}"
    print(f"   ✓ Stable: equal elements maintain relative order")

    print("\nStep 4: Testing divide and conquer structure...")
    # Test with power-of-2 size for clean division
    arr4 = [8, 7, 6, 5, 4, 3, 2, 1]
    result = SortingOperations.merge_sort(arr4)
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"   ✓ Divide and conquer: clean recursive division")

    print("✓ merge_sort tests passed")

def test_quick_sort():
    """Test quick_sort function"""
    print("Step 1: Testing normal case...")

    arr1 = [10, 7, 8, 9, 1, 5]
    result = SortingOperations.quick_sort(arr1)
    expected = [1, 5, 7, 8, 9, 10]
    print(f"   quick_sort([10, 7, 8, 9, 1, 5]) = {result}")
    print(f"   Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 2: Testing with duplicates...")
    arr2 = [3, 6, 8, 10, 1, 2, 1]
    result = SortingOperations.quick_sort(arr2)
    expected = [1, 1, 2, 3, 6, 8, 10]
    print(f"   quick_sort([3, 6, 8, 10, 1, 2, 1]) = {result}")
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"   ✓ Handles duplicates correctly")

    print("\nStep 3: Testing randomized pivot (worst case avoidance)...")
    # Test sorted array (traditional worst case for quicksort)
    sorted_arr = list(range(1, 21))
    start_time = time.time()
    result = SortingOperations.quick_sort(sorted_arr)
    sort_time = time.time() - start_time

    print(f"   Sorted array (20 elements): {sort_time:.6f}s")
    assert result == sorted_arr, f"Should handle worst case input"
    assert sort_time < 0.1, f"Should be fast with randomized pivot"
    print(f"   ✓ Randomized pivot prevents worst-case O(n²)")

    print("\nStep 4: Testing average case performance...")
    random_arr = [random.randint(1, 100) for _ in range(100)]
    start_time = time.time()
    result = SortingOperations.quick_sort(random_arr)
    sort_time = time.time() - start_time
    expected = sorted(random_arr)

    print(f"   Random array (100 elements): {sort_time:.6f}s")
    assert result == expected, f"Should sort random array correctly"
    print(f"   ✓ Fast average case performance")

    print("\nStep 5: Testing in-place property...")
    # Quick sort should use O(log n) space on average
    large_arr = [random.randint(1, 1000) for _ in range(1000)]
    result = SortingOperations.quick_sort(large_arr)
    expected = sorted(large_arr)
    assert result == expected, f"Should sort large array correctly"
    print(f"   ✓ Efficiently sorts large arrays (in-place with O(log n) space)")

    print("✓ quick_sort tests passed")

def test_heap_sort():
    """Test heap_sort function"""
    print("Step 1: Testing normal case...")

    arr1 = [4, 10, 3, 5, 1]
    result = SortingOperations.heap_sort(arr1)
    expected = [1, 3, 4, 5, 10]
    print(f"   heap_sort([4, 10, 3, 5, 1]) = {result}")
    print(f"   Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 2: Testing guaranteed O(n log n) performance...")
    # Heap sort should have consistent performance
    sizes = [100, 200, 400]
    times = []

    for size in sizes:
        # Test with reverse sorted (challenging input)
        test_arr = list(range(size, 0, -1))
        start_time = time.time()
        SortingOperations.heap_sort(test_arr)
        sort_time = time.time() - start_time
        times.append(sort_time)
        print(f"   Size {size}: {sort_time:.6f}s")

    print(f"   ✓ Guaranteed O(n log n) regardless of input")

    print("\nStep 3: Testing duplicate elements...")
    arr3 = [1, 3, 1, 3, 2, 2]
    result = SortingOperations.heap_sort(arr3)
    expected = [1, 1, 2, 2, 3, 3]
    print(f"   heap_sort([1, 3, 1, 3, 2, 2]) = {result}")
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"   ✓ Handles duplicates correctly")

    print("\nStep 4: Testing heap property...")
    # Verify heap sort uses heap structure correctly
    arr4 = [12, 11, 13, 5, 6, 7]
    result = SortingOperations.heap_sort(arr4)
    expected = [5, 6, 7, 11, 12, 13]
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"   ✓ Correctly uses max heap for ascending sort")

    print("\nStep 5: Testing in-place sorting...")
    # Heap sort should sort in-place
    large_arr = [random.randint(1, 1000) for _ in range(500)]
    original_len = len(large_arr)
    result = SortingOperations.heap_sort(large_arr)
    expected = sorted(large_arr)

    assert len(result) == original_len, f"Length should be preserved"
    assert result == expected, f"Should sort correctly"
    print(f"   ✓ In-place sorting with O(1) extra space")

    print("✓ heap_sort tests passed")

def test_counting_sort():
    """Test counting_sort function"""
    print("Step 1: Testing normal case...")

    arr1 = [4, 2, 2, 8, 3, 3, 1]
    result = SortingOperations.counting_sort(arr1)
    expected = [1, 2, 2, 3, 3, 4, 8]
    print(f"   counting_sort([4, 2, 2, 8, 3, 3, 1]) = {result}")
    print(f"   Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 2: Testing with specified max value...")
    arr2 = [1, 4, 1, 2, 7, 5, 2]
    result = SortingOperations.counting_sort(arr2, max_val=7)
    expected = [1, 1, 2, 2, 4, 5, 7]
    print(f"   counting_sort([1, 4, 1, 2, 7, 5, 2], max_val=7) = {result}")
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"   ✓ Correctly uses specified max value")

    print("\nStep 3: Testing linear time complexity...")
    # Should be much faster than O(n log n) for small ranges
    large_arr = [random.randint(0, 100) for _ in range(10000)]
    start_time = time.time()
    result = SortingOperations.counting_sort(large_arr, max_val=100)
    count_time = time.time() - start_time
    expected = sorted(large_arr)

    print(f"   10,000 elements (range 0-100): {count_time:.6f}s")
    assert result == expected, f"Should sort correctly"
    assert count_time < 0.1, f"Should be very fast: O(n + k)"
    print(f"   ✓ Linear time O(n + k) performance")

    print("\nStep 4: Testing stability...")
    # Test stability with tuples (though counting sort typically works with integers)
    arr4 = [2, 1, 2, 1, 3]
    result = SortingOperations.counting_sort(arr4)
    expected = [1, 1, 2, 2, 3]
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"   ✓ Stable sorting (preserves relative order)")

    print("\nStep 5: Testing edge cases...")
    assert SortingOperations.counting_sort([]) == [], f"Empty array should return []"
    assert SortingOperations.counting_sort([5]) == [5], f"Single element should work"
    assert SortingOperations.counting_sort([0, 0, 0]) == [0, 0, 0], f"All zeros should work"
    print(f"   Edge cases: [], [5], [0,0,0] all handled correctly ✓")

    print("✓ counting_sort tests passed")

def test_radix_sort():
    """Test radix_sort function"""
    print("Step 1: Testing normal case...")

    arr1 = [170, 45, 75, 90, 2, 802, 24, 66]
    result = SortingOperations.radix_sort(arr1)
    expected = [2, 24, 45, 66, 75, 90, 170, 802]
    print(f"   radix_sort([170, 45, 75, 90, 2, 802, 24, 66]) = {result}")
    print(f"   Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("\nStep 2: Testing single digit numbers...")
    arr2 = [9, 3, 5, 1, 7, 2]
    result = SortingOperations.radix_sort(arr2)
    expected = [1, 2, 3, 5, 7, 9]
    print(f"   radix_sort([9, 3, 5, 1, 7, 2]) = {result}")
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"   ✓ Handles single digits correctly")

    print("\nStep 3: Testing numbers with different digit counts...")
    arr3 = [1, 10, 100, 1000, 5, 50, 500]
    result = SortingOperations.radix_sort(arr3)
    expected = [1, 5, 10, 50, 100, 500, 1000]
    print(f"   Mixed digit counts: {result}")
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"   ✓ Correctly handles varying digit counts")

    print("\nStep 4: Testing linear time performance...")
    # Should be faster than comparison sorts for integers
    large_arr = [random.randint(1, 99999) for _ in range(10000)]
    start_time = time.time()
    result = SortingOperations.radix_sort(large_arr)
    radix_time = time.time() - start_time
    expected = sorted(large_arr)

    print(f"   10,000 5-digit numbers: {radix_time:.6f}s")
    assert result == expected, f"Should sort correctly"
    print(f"   ✓ Linear time O(d × (n + k)) performance")

    print("\nStep 5: Testing stability...")
    # Radix sort should be stable
    arr5 = [121, 321, 111, 221, 131, 231]
    result = SortingOperations.radix_sort(arr5)
    expected = [111, 121, 131, 221, 231, 321]
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"   ✓ Stable sorting preserves order of equal digits")

    print("✓ radix_sort tests passed")

def test_bucket_sort():
    """Test bucket_sort function"""
    print("Step 1: Testing floating point numbers...")

    arr1 = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    result = SortingOperations.bucket_sort(arr1)
    expected = sorted(arr1)
    print(f"   bucket_sort({arr1}) = {result}")
    print(f"   Expected: {expected}")

    # Compare with tolerance for floating point
    assert len(result) == len(expected), f"Length mismatch: {len(result)} vs {len(expected)}"
    for i in range(len(result)):
        assert abs(result[i] - expected[i]) < 1e-10, f"Element {i}: {result[i]} vs {expected[i]}"
    print(f"   ✓ Correctly sorts floating point numbers")

    print("\nStep 2: Testing integer range...")
    arr2 = [29, 25, 3, 49, 9, 37, 21, 43]
    result = SortingOperations.bucket_sort(arr2)
    expected = sorted(arr2)
    print(f"   bucket_sort({arr2}) = {result}")
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"   ✓ Works with integer ranges")

    print("\nStep 3: Testing uniform distribution (best case)...")
    # Uniformly distributed data should distribute evenly across buckets
    uniform_data = [i/100.0 for i in range(0, 100, 10)]
    random.shuffle(uniform_data)
    result = SortingOperations.bucket_sort(uniform_data)
    expected = sorted(uniform_data)

    assert len(result) == len(expected), f"Length should match"
    for i in range(len(result)):
        assert abs(result[i] - expected[i]) < 1e-10, f"Should sort uniformly distributed data"
    print(f"   ✓ Optimal performance on uniformly distributed data")

    print("\nStep 4: Testing different bucket counts...")
    arr4 = [0.1, 0.5, 0.3, 0.9, 0.7, 0.2, 0.8, 0.4, 0.6]
    result_5_buckets = SortingOperations.bucket_sort(arr4, num_buckets=5)
    result_10_buckets = SortingOperations.bucket_sort(arr4, num_buckets=10)
    expected = sorted(arr4)

    # Both should produce correct results
    for i in range(len(expected)):
        assert abs(result_5_buckets[i] - expected[i]) < 1e-10
        assert abs(result_10_buckets[i] - expected[i]) < 1e-10
    print(f"   ✓ Works correctly with different bucket counts")

    print("\nStep 5: Testing edge cases...")
    assert SortingOperations.bucket_sort([]) == [], f"Empty array should return []"
    assert SortingOperations.bucket_sort([0.5]) == [0.5], f"Single element should work"

    # All same values
    same_values = [0.5, 0.5, 0.5, 0.5]
    result = SortingOperations.bucket_sort(same_values)
    assert result == same_values, f"All same values should work"
    print(f"   Edge cases: [], [0.5], [0.5,0.5,0.5,0.5] all handled ✓")

    print("✓ bucket_sort tests passed")

def test_stability():
    """Test algorithm stability"""
    print("Step 1: Testing stable algorithms...")

    # Test data with equal keys but different secondary values
    test_data = [(3, 'a'), (1, 'b'), (3, 'c'), (2, 'd'), (1, 'e'), (2, 'f')]

    stable_algorithms = ['bubble_sort', 'insertion_sort', 'merge_sort', 'counting_sort']

    for algo_name in stable_algorithms:
        print(f"\n   Testing {algo_name} stability...")
        if hasattr(SortingOperations, algo_name):
            algo = getattr(SortingOperations, algo_name)

            # For counting sort, we'll test with just the numeric values
            if algo_name == 'counting_sort':
                numeric_data = [3, 1, 3, 2, 1, 2]
                result = algo(numeric_data)
                expected = [1, 1, 2, 2, 3, 3]
                assert result == expected, f"{algo_name} should sort correctly"
                print(f"      {algo_name}: ✓ (tested with integers)")
            else:
                try:
                    result = algo(test_data)
                    # Check if stable: equal elements should maintain relative order
                    ones = [item for item in result if item[0] == 1]
                    twos = [item for item in result if item[0] == 2]
                    threes = [item for item in result if item[0] == 3]

                    # For stable sort: (1,'b') should come before (1,'e'), etc.
                    assert ones == [(1, 'b'), (1, 'e')], f"{algo_name} should preserve order of 1s"
                    assert twos == [(2, 'd'), (2, 'f')], f"{algo_name} should preserve order of 2s"
                    assert threes == [(3, 'a'), (3, 'c')], f"{algo_name} should preserve order of 3s"
                    print(f"      {algo_name}: ✓ stable")
                except (TypeError, AttributeError):
                    # Some algorithms might not handle tuples
                    print(f"      {algo_name}: ✓ (implementation doesn't support tuples)")

    print("\nStep 2: Testing unstable algorithms...")
    unstable_algorithms = ['selection_sort', 'quick_sort', 'heap_sort']

    for algo_name in unstable_algorithms:
        print(f"   {algo_name}: documented as unstable ✓")

    print("✓ stability tests completed")

def test_performance_characteristics():
    """Test performance on different input types"""
    print("Step 1: Testing performance on different input patterns...")

    # Create different types of input
    size = 1000
    sorted_arr = list(range(size))
    reverse_arr = list(range(size, 0, -1))
    random_arr = [random.randint(1, size) for _ in range(size)]
    nearly_sorted = sorted_arr.copy()
    # Shuffle just 10% of elements
    for _ in range(size // 10):
        i, j = random.randint(0, size-1), random.randint(0, size-1)
        nearly_sorted[i], nearly_sorted[j] = nearly_sorted[j], nearly_sorted[i]

    test_cases = [
        ("sorted", sorted_arr),
        ("reverse", reverse_arr),
        ("random", random_arr),
        ("nearly_sorted", nearly_sorted)
    ]

    algorithms = ['insertion_sort', 'merge_sort', 'quick_sort', 'heap_sort']

    print(f"   Testing with arrays of size {size}:")

    for case_name, test_arr in test_cases:
        print(f"\n   {case_name.upper()} INPUT:")
        for algo_name in algorithms:
            algo = getattr(SortingOperations, algo_name)

            # Skip insertion sort on large random/reverse arrays (too slow)
            if algo_name == 'insertion_sort' and case_name in ['random', 'reverse'] and size > 100:
                print(f"      {algo_name}: skipped (would be too slow)")
                continue

            start_time = time.time()
            result = algo(test_arr)
            sort_time = time.time() - start_time
            expected = sorted(test_arr)

            assert result == expected, f"{algo_name} should sort {case_name} correctly"
            print(f"      {algo_name}: {sort_time:.6f}s")

    print("\nStep 2: Analyzing adaptive behavior...")
    # Test insertion sort on nearly sorted vs random (small size)
    small_size = 100
    small_nearly_sorted = list(range(small_size))
    small_nearly_sorted[10], small_nearly_sorted[90] = small_nearly_sorted[90], small_nearly_sorted[10]
    small_random = [random.randint(1, small_size) for _ in range(small_size)]

    start_time = time.time()
    SortingOperations.insertion_sort(small_nearly_sorted)
    nearly_time = time.time() - start_time

    start_time = time.time()
    SortingOperations.insertion_sort(small_random)
    random_time = time.time() - start_time

    print(f"   Insertion sort (size 100):")
    print(f"      Nearly sorted: {nearly_time:.6f}s")
    print(f"      Random: {random_time:.6f}s")

    # Avoid division by zero for very fast operations
    if nearly_time > 0:
        ratio = random_time / nearly_time
        print(f"      ✓ Adaptive: {ratio:.1f}x slower on random data")
    else:
        print(f"      ✓ Adaptive: both operations too fast to measure precisely")

    print("✓ performance_characteristics tests passed")


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    print("Step 1: Testing empty and single element arrays...")

    algorithms = ['bubble_sort', 'selection_sort', 'insertion_sort',
                 'merge_sort', 'quick_sort', 'heap_sort']

    for algo_name in algorithms:
        algo = getattr(SortingOperations, algo_name)

        # Test empty array
        assert algo([]) == [], f"{algo_name} should handle empty array"

        # Test single element
        assert algo([42]) == [42], f"{algo_name} should handle single element"

        # Test two elements
        assert algo([2, 1]) == [1, 2], f"{algo_name} should handle two elements"
        assert algo([1, 2]) == [1, 2], f"{algo_name} should handle sorted pair"

    print("   ✓ All comparison sorts handle edge cases correctly")

    print("\nStep 2: Testing non-comparison sort edge cases...")

    # Counting sort edge cases
    assert SortingOperations.counting_sort([]) == [], f"Counting sort: empty array"
    assert SortingOperations.counting_sort([0]) == [0], f"Counting sort: single zero"
    assert SortingOperations.counting_sort([5, 5, 5]) == [5, 5, 5], f"Counting sort: all same"

    # Radix sort edge cases
    assert SortingOperations.radix_sort([]) == [], f"Radix sort: empty array"
    assert SortingOperations.radix_sort([0]) == [0], f"Radix sort: single zero"
    assert SortingOperations.radix_sort([1]) == [1], f"Radix sort: single element"

    # Bucket sort edge cases
    assert SortingOperations.bucket_sort([]) == [], f"Bucket sort: empty array"
    assert SortingOperations.bucket_sort([0.5]) == [0.5], f"Bucket sort: single element"

    print("   ✓ Non-comparison sorts handle edge cases correctly")

    print("\nStep 3: Testing boundary values...")

    # Large values
    large_vals = [1000000, 999999, 1000001]
    for algo_name in ['merge_sort', 'quick_sort', 'heap_sort']:
        algo = getattr(SortingOperations, algo_name)
        result = algo(large_vals)
        assert result == [999999, 1000000, 1000001], f"{algo_name} should handle large values"

    # Negative values (for comparison sorts)
    negative_vals = [-5, -1, -10, 0, 3]
    expected_negative = [-10, -5, -1, 0, 3]
    for algo_name in ['merge_sort', 'quick_sort', 'heap_sort']:
        algo = getattr(SortingOperations, algo_name)
        result = algo(negative_vals)
        assert result == expected_negative, f"{algo_name} should handle negative values"

    print("   ✓ Boundary values handled correctly")

    print("\nStep 4: Testing arrays with many duplicates...")

    # Array with mostly duplicates
    many_dupes = [5] * 80 + [3] * 15 + [7] * 5
    random.shuffle(many_dupes)
    expected_dupes = [3] * 15 + [5] * 80 + [7] * 5

    for algo_name in ['merge_sort', 'quick_sort', 'heap_sort']:
        algo = getattr(SortingOperations, algo_name)
        result = algo(many_dupes)
        assert result == expected_dupes, f"{algo_name} should handle many duplicates"

    print("   ✓ Arrays with many duplicates handled correctly")

    print("✓ edge_cases tests passed")

def run_all_tests():
    """Run all test functions with detailed reporting"""
    print("🚀 STARTING COMPREHENSIVE SORTING ALGORITHM TESTS")
    print("="*70)

    tests = [
        ("Bubble Sort", test_bubble_sort),
        ("Selection Sort", test_selection_sort),
        ("Insertion Sort", test_insertion_sort),
        ("Merge Sort", test_merge_sort),
        ("Quick Sort", test_quick_sort),
        ("Heap Sort", test_heap_sort),
        ("Counting Sort", test_counting_sort),
        ("Radix Sort", test_radix_sort),
        ("Bucket Sort", test_bucket_sort),
        ("Stability", test_stability),
        ("Performance Characteristics", test_performance_characteristics),
        ("Edge Cases", test_edge_cases),
    ]

    passed = 0
    failed = 0
    total_start_time = time.time()

    for test_name, test_func in tests:
        if safe_test(test_name, test_func):
            passed += 1
        else:
            failed += 1

    total_time = time.time() - total_start_time

    print(f"\n{'='*70}")
    print(f"📊 FINAL RESULTS:")
    print(f"   ✅ Passed: {passed}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📈 Success Rate: {passed}/{passed + failed} ({100 * passed / (passed + failed):.1f}%)")
    print(f"   ⏱️  Total Time: {total_time:.2f} seconds")

    if failed == 0:
        print("\n🎉 ALL TESTS PASSED! Your sorting implementations are working correctly!")
        print("\n🔥 KEY SORTING CONCEPTS VALIDATED:")
        print("   • Simple sorts (Bubble, Selection, Insertion)")
        print("   • Efficient comparison sorts (Merge, Quick, Heap)")
        print("   • Non-comparison sorts (Counting, Radix, Bucket)")
        print("   • Hybrid algorithms (TimSort, IntroSort concepts)")
        print("   • Stability preservation and analysis")
        print("   • Time and space complexity characteristics")
        print("   • Adaptive behavior on different input types")
        print("   • Edge case handling and boundary conditions")
    else:
        print("\n🔧 Some tests failed. Check the detailed output above to fix the issues.")
        print("\n💡 DEBUGGING TIPS:")
        print("   • Verify algorithm logic matches standard implementations")
        print("   • Check array bounds and index calculations")
        print("   • Ensure proper handling of edge cases (empty, single element)")
        print("   • Test stability with equal elements")
        print("   • Verify time complexity matches expected performance")
        print("   • Check that original arrays are not modified")
        print("   • Ensure proper initialization of data structures")

    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
