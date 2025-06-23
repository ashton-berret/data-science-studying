import sys
import os
import argparse
import traceback

def setup_imports():
    """Set up imports based on the command-line argument."""
    parser = argparse.ArgumentParser(description='Test array operations')
    parser.add_argument('--mode', choices=['solution', 'practice'], default='solution',
                      help='Which implementation to test (solution or practice)')
    args = parser.parse_args()

    # Get the current directory and project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))

    if args.mode == 'solution':
        # Import from Solutions
        solutions_dir = os.path.join(project_root, 'Solutions', 'Arrays')
        sys.path.insert(0, solutions_dir)
        print(f"Testing solution implementation from: {solutions_dir}")
    else:
        # Import from Practice
        practice_dir = os.path.join(project_root, 'Practice', 'Arrays')
        sys.path.insert(0, practice_dir)
        print(f"Testing practice implementation from: {practice_dir}")

# Setup the path and import
setup_imports()

try:
    from arrays_operations import ArrayOperations
except ImportError as e:
    print(f"❌ Could not import ArrayOperations: {e}")
    print("Make sure the file exists in Solutions/Arrays/ or Practice/Arrays/")
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

def test_find_element():
    """Test find_element function"""
    print("Step 1: Testing basic element finding...")

    # Test basic case
    arr = [1, 3, 5, 7, 9]
    result = ArrayOperations.find_element(arr, 5)
    print(f"   find_element([1, 3, 5, 7, 9], 5) = {result} (expected: 2)")
    assert result == 2, f"Expected 2, got {result}"

    result = ArrayOperations.find_element(arr, 7)
    print(f"   find_element([1, 3, 5, 7, 9], 7) = {result} (expected: 3)")
    assert result == 3, f"Expected 3, got {result}"

    print("\nStep 2: Testing element not found...")
    result = ArrayOperations.find_element(arr, 6)
    print(f"   find_element([1, 3, 5, 7, 9], 6) = {result} (expected: -1)")
    assert result == -1, f"Expected -1, got {result}"

    print("\nStep 3: Testing empty array...")
    result = ArrayOperations.find_element([], 5)
    print(f"   find_element([], 5) = {result} (expected: -1)")
    assert result == -1, f"Expected -1, got {result}"

    print("✓ find_element tests passed")

def test_binary_search():
    """Test binary_search function"""
    print("Step 1: Testing basic binary search...")

    arr = [1, 3, 5, 7, 9, 11, 13]
    result = ArrayOperations.binary_search(arr, 7)
    print(f"   binary_search([1, 3, 5, 7, 9, 11, 13], 7) = {result} (expected: 3)")
    assert result == 3, f"Expected 3, got {result}"

    result = ArrayOperations.binary_search(arr, 1)
    print(f"   binary_search([1, 3, 5, 7, 9, 11, 13], 1) = {result} (expected: 0)")
    assert result == 0, f"Expected 0, got {result}"

    result = ArrayOperations.binary_search(arr, 13)
    print(f"   binary_search([1, 3, 5, 7, 9, 11, 13], 13) = {result} (expected: 6)")
    assert result == 6, f"Expected 6, got {result}"

    print("\nStep 2: Testing element not found...")
    result = ArrayOperations.binary_search(arr, 6)
    print(f"   binary_search([1, 3, 5, 7, 9, 11, 13], 6) = {result} (expected: -1)")
    assert result == -1, f"Expected -1, got {result}"

    print("\nStep 3: Testing empty array...")
    result = ArrayOperations.binary_search([], 5)
    print(f"   binary_search([], 5) = {result} (expected: -1)")
    assert result == -1, f"Expected -1, got {result}"

    print("✓ binary_search tests passed")

def test_merge_sorted_arrays():
    """Test merge_sorted_arrays function"""
    print("Step 1: Testing basic merge...")

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    ArrayOperations.merge_sorted_arrays(nums1, 3, nums2, 3)
    print(f"   merge_sorted_arrays([1,2,3,0,0,0], 3, [2,5,6], 3) = {nums1}")
    print(f"   Expected: [1, 2, 2, 3, 5, 6]")
    assert nums1 == [1, 2, 2, 3, 5, 6], f"Expected [1, 2, 2, 3, 5, 6], got {nums1}"

    print("\nStep 2: Testing nums1 larger...")
    nums1 = [1, 2, 3, 4, 5, 0, 0]
    nums2 = [6, 7]
    ArrayOperations.merge_sorted_arrays(nums1, 5, nums2, 2)
    print(f"   merge_sorted_arrays([1,2,3,4,5,0,0], 5, [6,7], 2) = {nums1}")
    print(f"   Expected: [1, 2, 3, 4, 5, 6, 7]")
    assert nums1 == [1, 2, 3, 4, 5, 6, 7], f"Expected [1, 2, 3, 4, 5, 6, 7], got {nums1}"

    print("\nStep 3: Testing nums2 larger...")
    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]
    ArrayOperations.merge_sorted_arrays(nums1, 3, nums2, 3)
    print(f"   merge_sorted_arrays([4,5,6,0,0,0], 3, [1,2,3], 3) = {nums1}")
    print(f"   Expected: [1, 2, 3, 4, 5, 6]")
    assert nums1 == [1, 2, 3, 4, 5, 6], f"Expected [1, 2, 3, 4, 5, 6], got {nums1}"

    print("✓ merge_sorted_arrays tests passed")

def test_search_insert():
    """Test search_insert function"""
    print("Step 1: Testing target found...")

    nums = [1, 3, 5, 6]
    result = ArrayOperations.search_insert(nums, 5)
    print(f"   search_insert([1, 3, 5, 6], 5) = {result} (expected: 2)")
    assert result == 2, f"Expected 2, got {result}"

    print("\nStep 2: Testing target not found - insert middle...")
    result = ArrayOperations.search_insert(nums, 2)
    print(f"   search_insert([1, 3, 5, 6], 2) = {result} (expected: 1)")
    assert result == 1, f"Expected 1, got {result}"

    print("\nStep 3: Testing target not found - insert end...")
    result = ArrayOperations.search_insert(nums, 7)
    print(f"   search_insert([1, 3, 5, 6], 7) = {result} (expected: 4)")
    assert result == 4, f"Expected 4, got {result}"

    print("\nStep 4: Testing target not found - insert beginning...")
    result = ArrayOperations.search_insert(nums, 0)
    print(f"   search_insert([1, 3, 5, 6], 0) = {result} (expected: 0)")
    assert result == 0, f"Expected 0, got {result}"

    print("✓ search_insert tests passed")

def test_search_range():
    """Test search_range function"""
    print("Step 1: Testing target found with duplicates...")

    nums = [5, 7, 7, 8, 8, 10]
    result = ArrayOperations.search_range(nums, 8)
    print(f"   search_range([5, 7, 7, 8, 8, 10], 8) = {result} (expected: [3, 4])")
    assert result == [3, 4], f"Expected [3, 4], got {result}"

    result = ArrayOperations.search_range(nums, 7)
    print(f"   search_range([5, 7, 7, 8, 8, 10], 7) = {result} (expected: [1, 2])")
    assert result == [1, 2], f"Expected [1, 2], got {result}"

    print("\nStep 2: Testing target found single occurrence...")
    result = ArrayOperations.search_range(nums, 5)
    print(f"   search_range([5, 7, 7, 8, 8, 10], 5) = {result} (expected: [0, 0])")
    assert result == [0, 0], f"Expected [0, 0], got {result}"

    print("\nStep 3: Testing target not found...")
    result = ArrayOperations.search_range(nums, 6)
    print(f"   search_range([5, 7, 7, 8, 8, 10], 6) = {result} (expected: [-1, -1])")
    assert result == [-1, -1], f"Expected [-1, -1], got {result}"

    print("✓ search_range tests passed")

def test_reverse_array():
    """Test reverse_array function"""
    print("Step 1: Testing odd length array...")

    arr1 = [1, 2, 3, 4, 5]
    result = ArrayOperations.reverse_array(arr1.copy())
    print(f"   reverse_array([1, 2, 3, 4, 5]) = {result} (expected: [5, 4, 3, 2, 1])")
    assert result == [5, 4, 3, 2, 1], f"Expected [5, 4, 3, 2, 1], got {result}"

    print("\nStep 2: Testing even length array...")
    arr2 = [1, 2, 3, 4]
    result = ArrayOperations.reverse_array(arr2.copy())
    print(f"   reverse_array([1, 2, 3, 4]) = {result} (expected: [4, 3, 2, 1])")
    assert result == [4, 3, 2, 1], f"Expected [4, 3, 2, 1], got {result}"

    print("\nStep 3: Testing single element array...")
    arr3 = [1]
    result = ArrayOperations.reverse_array(arr3.copy())
    print(f"   reverse_array([1]) = {result} (expected: [1])")
    assert result == [1], f"Expected [1], got {result}"

    print("\nStep 4: Testing empty array...")
    arr4 = []
    result = ArrayOperations.reverse_array(arr4.copy())
    print(f"   reverse_array([]) = {result} (expected: [])")
    assert result == [], f"Expected [], got {result}"

    print("✓ reverse_array tests passed")

def test_find_max_min():
    """Test find_max_min function"""
    print("Step 1: Testing normal case...")

    arr1 = [3, 5, 1, 7, 2]
    result = ArrayOperations.find_max_min(arr1)
    print(f"   find_max_min([3, 5, 1, 7, 2]) = {result} (expected: (7, 1))")
    assert result == (7, 1), f"Expected (7, 1), got {result}"

    print("\nStep 2: Testing with negative numbers...")
    arr2 = [-3, -5, -1, -7, -2]
    result = ArrayOperations.find_max_min(arr2)
    print(f"   find_max_min([-3, -5, -1, -7, -2]) = {result} (expected: (-1, -7))")
    assert result == (-1, -7), f"Expected (-1, -7), got {result}"

    print("\nStep 3: Testing with mixed numbers...")
    arr3 = [-3, 5, -1, 7, -2]
    result = ArrayOperations.find_max_min(arr3)
    print(f"   find_max_min([-3, 5, -1, 7, -2]) = {result} (expected: (7, -3))")
    assert result == (7, -3), f"Expected (7, -3), got {result}"

    print("\nStep 4: Testing single element array...")
    arr4 = [42]
    result = ArrayOperations.find_max_min(arr4)
    print(f"   find_max_min([42]) = {result} (expected: (42, 42))")
    assert result == (42, 42), f"Expected (42, 42), got {result}"

    print("\nStep 5: Testing empty array...")
    arr5 = []
    result = ArrayOperations.find_max_min(arr5)
    print(f"   find_max_min([]) = {result} (expected: (None, None))")
    assert result == (None, None), f"Expected (None, None), got {result}"

    print("✓ find_max_min tests passed")

def test_remove_duplicates():
    """Test remove_duplicates function"""
    print("Step 1: Testing sorted array with duplicates...")

    arr1 = [1, 1, 2, 2, 3, 4, 4, 5]
    result = ArrayOperations.remove_duplicates(arr1)
    print(f"   remove_duplicates([1, 1, 2, 2, 3, 4, 4, 5]) = {result} (expected: [1, 2, 3, 4, 5])")
    assert result == [1, 2, 3, 4, 5], f"Expected [1, 2, 3, 4, 5], got {result}"

    print("\nStep 2: Testing array with all same elements...")
    arr2 = [1, 1, 1, 1]
    result = ArrayOperations.remove_duplicates(arr2)
    print(f"   remove_duplicates([1, 1, 1, 1]) = {result} (expected: [1])")
    assert result == [1], f"Expected [1], got {result}"

    print("\nStep 3: Testing array with no duplicates...")
    arr3 = [1, 2, 3, 4, 5]
    result = ArrayOperations.remove_duplicates(arr3)
    print(f"   remove_duplicates([1, 2, 3, 4, 5]) = {result} (expected: [1, 2, 3, 4, 5])")
    assert result == [1, 2, 3, 4, 5], f"Expected [1, 2, 3, 4, 5], got {result}"

    print("\nStep 4: Testing empty array...")
    arr4 = []
    result = ArrayOperations.remove_duplicates(arr4)
    print(f"   remove_duplicates([]) = {result} (expected: [])")
    assert result == [], f"Expected [], got {result}"

    print("✓ remove_duplicates tests passed")

def test_two_sum():
    """Test two_sum function"""
    print("Step 1: Testing basic case...")

    arr1 = [2, 7, 11, 15]
    result = ArrayOperations.two_sum(arr1, 9)
    print(f"   two_sum([2, 7, 11, 15], 9) = {result} (expected: [0, 1])")
    assert result == [0, 1], f"Expected [0, 1], got {result}"

    print("\nStep 2: Testing case with target not found...")
    arr2 = [2, 7, 11, 15]
    result = ArrayOperations.two_sum(arr2, 30)
    print(f"   two_sum([2, 7, 11, 15], 30) = {result} (expected: [])")
    assert result == [], f"Expected [], got {result}"

    print("\nStep 3: Testing case with negative numbers...")
    arr3 = [3, -1, 0, 5]
    result = ArrayOperations.two_sum(arr3, 2)
    print(f"   two_sum([3, -1, 0, 5], 2) = {result} (expected: [0, 1])")
    assert result == [0, 1], f"Expected [0, 1], got {result}"

    print("\nStep 4: Testing case with duplicate numbers...")
    arr4 = [3, 3]
    result = ArrayOperations.two_sum(arr4, 6)
    print(f"   two_sum([3, 3], 6) = {result} (expected: [0, 1])")
    assert result == [0, 1], f"Expected [0, 1], got {result}"

    print("\nStep 5: Testing empty array...")
    arr5 = []
    result = ArrayOperations.two_sum(arr5, 5)
    print(f"   two_sum([], 5) = {result} (expected: [])")
    assert result == [], f"Expected [], got {result}"

    print("✓ two_sum tests passed")

def test_rotate_array():
    """Test rotate_array function"""
    print("Step 1: Testing basic rotation...")

    arr1 = [1, 2, 3, 4, 5, 6, 7]
    result = ArrayOperations.rotate_array(arr1.copy(), 3)
    print(f"   rotate_array([1, 2, 3, 4, 5, 6, 7], 3) = {result} (expected: [5, 6, 7, 1, 2, 3, 4])")
    assert result == [5, 6, 7, 1, 2, 3, 4], f"Expected [5, 6, 7, 1, 2, 3, 4], got {result}"

    print("\nStep 2: Testing rotation equal to array length...")
    arr2 = [1, 2, 3, 4, 5]
    result = ArrayOperations.rotate_array(arr2.copy(), 5)
    print(f"   rotate_array([1, 2, 3, 4, 5], 5) = {result} (expected: [1, 2, 3, 4, 5])")
    assert result == [1, 2, 3, 4, 5], f"Expected [1, 2, 3, 4, 5], got {result}"

    print("\nStep 3: Testing rotation greater than array length...")
    arr3 = [1, 2, 3, 4, 5]
    result = ArrayOperations.rotate_array(arr3.copy(), 7)  # 7 % 5 = 2
    print(f"   rotate_array([1, 2, 3, 4, 5], 7) = {result} (expected: [4, 5, 1, 2, 3])")
    assert result == [4, 5, 1, 2, 3], f"Expected [4, 5, 1, 2, 3], got {result}"

    print("\nStep 4: Testing rotation of 0 steps...")
    arr4 = [1, 2, 3, 4, 5]
    result = ArrayOperations.rotate_array(arr4.copy(), 0)
    print(f"   rotate_array([1, 2, 3, 4, 5], 0) = {result} (expected: [1, 2, 3, 4, 5])")
    assert result == [1, 2, 3, 4, 5], f"Expected [1, 2, 3, 4, 5], got {result}"

    print("\nStep 5: Testing single element array...")
    arr5 = [42]
    result = ArrayOperations.rotate_array(arr5.copy(), 3)
    print(f"   rotate_array([42], 3) = {result} (expected: [42])")
    assert result == [42], f"Expected [42], got {result}"

    print("\nStep 6: Testing empty array...")
    arr6 = []
    result = ArrayOperations.rotate_array(arr6.copy(), 3)
    print(f"   rotate_array([], 3) = {result} (expected: [])")
    assert result == [], f"Expected [], got {result}"

    print("✓ rotate_array tests passed")

def test_kadanes_algorithm():
    """Test kadanes_algorithm function"""
    print("Step 1: Testing basic case...")

    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = ArrayOperations.kadanes_algorithm(arr1)
    print(f"   kadanes_algorithm([-2, 1, -3, 4, -1, 2, 1, -5, 4]) = {result} (expected: 6)")
    assert result == 6, f"Expected 6, got {result}"

    print("\nStep 2: Testing all positive numbers...")
    arr2 = [1, 2, 3, 4, 5]
    result = ArrayOperations.kadanes_algorithm(arr2)
    print(f"   kadanes_algorithm([1, 2, 3, 4, 5]) = {result} (expected: 15)")
    assert result == 15, f"Expected 15, got {result}"

    print("\nStep 3: Testing all negative numbers...")
    arr3 = [-1, -2, -3, -4, -5]
    result = ArrayOperations.kadanes_algorithm(arr3)
    print(f"   kadanes_algorithm([-1, -2, -3, -4, -5]) = {result} (expected: -1)")
    assert result == -1, f"Expected -1, got {result}"

    print("\nStep 4: Testing single positive number...")
    arr4 = [42]
    result = ArrayOperations.kadanes_algorithm(arr4)
    print(f"   kadanes_algorithm([42]) = {result} (expected: 42)")
    assert result == 42, f"Expected 42, got {result}"

    print("\nStep 5: Testing single negative number...")
    arr5 = [-42]
    result = ArrayOperations.kadanes_algorithm(arr5)
    print(f"   kadanes_algorithm([-42]) = {result} (expected: -42)")
    assert result == -42, f"Expected -42, got {result}"

    print("\nStep 6: Testing empty array...")
    arr6 = []
    result = ArrayOperations.kadanes_algorithm(arr6)
    print(f"   kadanes_algorithm([]) = {result} (expected: 0)")
    assert result == 0, f"Expected 0, got {result}"

    print("✓ kadanes_algorithm tests passed")

def test_kadanes_algorithm_with_subarray():
    """Test kadanes_algorithm_with_subarray function"""
    print("Step 1: Testing basic case...")

    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = ArrayOperations.kadanes_algorithm_with_subarray(arr1)
    print(f"   kadanes_algorithm_with_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) = {result}")
    print(f"   Expected: (6, 3, 6) - subarray [4, -1, 2, 1]")
    assert result == (6, 3, 6), f"Expected (6, 3, 6), got {result}"

    print("\nStep 2: Testing all positive numbers...")
    arr2 = [1, 2, 3, 4, 5]
    result = ArrayOperations.kadanes_algorithm_with_subarray(arr2)
    print(f"   kadanes_algorithm_with_subarray([1, 2, 3, 4, 5]) = {result}")
    print(f"   Expected: (15, 0, 4) - entire array")
    assert result == (15, 0, 4), f"Expected (15, 0, 4), got {result}"

    print("\nStep 3: Testing all negative numbers...")
    arr3 = [-1, -2, -3, -4, -5]
    result = ArrayOperations.kadanes_algorithm_with_subarray(arr3)
    print(f"   kadanes_algorithm_with_subarray([-1, -2, -3, -4, -5]) = {result}")
    print(f"   Expected: (-1, 0, 0) - just the first element")
    assert result == (-1, 0, 0), f"Expected (-1, 0, 0), got {result}"

    print("\nStep 4: Testing single element...")
    arr4 = [42]
    result = ArrayOperations.kadanes_algorithm_with_subarray(arr4)
    print(f"   kadanes_algorithm_with_subarray([42]) = {result}")
    print(f"   Expected: (42, 0, 0)")
    assert result == (42, 0, 0), f"Expected (42, 0, 0), got {result}"

    print("\nStep 5: Testing specific subarray pattern...")
    arr5 = [3, -4, 5, -2, 1, 6, -1]
    result = ArrayOperations.kadanes_algorithm_with_subarray(arr5)
    print(f"   kadanes_algorithm_with_subarray([3, -4, 5, -2, 1, 6, -1]) = {result}")
    print(f"   Expected: (10, 2, 5) - subarray [5, -2, 1, 6]")
    assert result == (10, 2, 5), f"Expected (10, 2, 5), got {result}"

    print("\nStep 6: Testing empty array...")
    arr6 = []
    result = ArrayOperations.kadanes_algorithm_with_subarray(arr6)
    print(f"   kadanes_algorithm_with_subarray([]) = {result}")
    print(f"   Expected: (0, -1, -1)")
    assert result == (0, -1, -1), f"Expected (0, -1, -1), got {result}"

    print("✓ kadanes_algorithm_with_subarray tests passed")

def run_all_tests():
    """Run all test functions with detailed reporting"""
    print("🚀 STARTING COMPREHENSIVE ARRAYS TESTS")
    print("="*70)

    tests = [
        ("Find Element (Linear Search)", test_find_element),
        ("Binary Search", test_binary_search),
        ("Merge Sorted Arrays", test_merge_sorted_arrays),
        ("Search Insert Position", test_search_insert),
        ("Search Range", test_search_range),
        ("Reverse Array", test_reverse_array),
        ("Find Max Min", test_find_max_min),
        ("Remove Duplicates", test_remove_duplicates),
        ("Two Sum", test_two_sum),
        ("Rotate Array", test_rotate_array),
        ("Kadane's Algorithm", test_kadanes_algorithm),
        ("Kadane's with Subarray", test_kadanes_algorithm_with_subarray),
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
        print("🎉 ALL TESTS PASSED! Your implementation is working correctly!")
    else:
        print("🔧 Some tests failed. Check the detailed output above to fix the issues.")

    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
