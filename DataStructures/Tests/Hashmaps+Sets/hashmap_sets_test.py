import sys
import os
import argparse
import traceback

def setup_imports():
    """Set up imports based on the command-line argument."""
    parser = argparse.ArgumentParser(description='Test hashmap+set operations')
    parser.add_argument('--mode', choices=['solution', 'practice'], default='solution',
                      help='Which implementation to test (solution or practice)')
    args = parser.parse_args()
    
    # Get the current directory and project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
    
    if args.mode == 'solution':
        # Import from Solutions
        solutions_dir = os.path.join(project_root, 'Solutions', 'Hashmaps+Sets')
        sys.path.insert(0, solutions_dir)
        print(f"Testing solution implementation from: {solutions_dir}")
    else:
        # Import from Practice
        practice_dir = os.path.join(project_root, 'Practice', 'Hashmaps+Sets')
        sys.path.insert(0, practice_dir)
        print(f"Testing practice implementation from: {practice_dir}")

# Setup the path and import
setup_imports()

try:
    from hashmap_sets_operations import HashMapSetOperations
except ImportError as e:
    print(f"❌ Could not import HashMapSetOperations: {e}")
    print("Make sure the file exists in Solutions/Hashmaps+Sets/ or Practice/Hashmaps+Sets/")
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

def test_two_sum():
    """Test two_sum function"""
    print("Step 1: Testing basic case...")
    
    nums = [2, 7, 11, 15]
    target = 9
    result = HashMapSetOperations.two_sum(nums, target)
    print(f"   two_sum([2, 7, 11, 15], 9) = {result} (expected: [0, 1])")
    print(f"   → indices 0 and 1: nums[0] + nums[1] = 2 + 7 = 9")
    assert result == [0, 1], f"Expected [0, 1], got {result}"
    
    print("\nStep 2: Testing target at end...")
    nums = [3, 2, 4]
    target = 6
    result = HashMapSetOperations.two_sum(nums, target)
    print(f"   two_sum([3, 2, 4], 6) = {result} (expected: [1, 2])")
    print(f"   → indices 1 and 2: nums[1] + nums[2] = 2 + 4 = 6")
    assert result == [1, 2], f"Expected [1, 2], got {result}"
    
    print("\nStep 3: Testing same number twice...")
    nums = [3, 3]
    target = 6
    result = HashMapSetOperations.two_sum(nums, target)
    print(f"   two_sum([3, 3], 6) = {result} (expected: [0, 1])")
    print(f"   → indices 0 and 1: nums[0] + nums[1] = 3 + 3 = 6")
    assert result == [0, 1], f"Expected [0, 1], got {result}"
    
    print("\nStep 4: Testing no solution...")
    nums = [1, 2, 3]
    target = 7
    result = HashMapSetOperations.two_sum(nums, target)
    print(f"   two_sum([1, 2, 3], 7) = {result} (expected: [])")
    print(f"   → no two numbers sum to 7")
    assert result == [], f"Expected [], got {result}"
    
    print("✓ two_sum tests passed")

def test_contains_duplicate():
    """Test contains_duplicate function"""
    print("Step 1: Testing array with duplicates...")
    
    nums = [1, 2, 3, 1]
    result = HashMapSetOperations.contains_duplicate(nums)
    print(f"   contains_duplicate([1, 2, 3, 1]) = {result} (expected: True)")
    print(f"   → number 1 appears twice")
    assert result == True, f"Expected True, got {result}"
    
    print("\nStep 2: Testing array without duplicates...")
    nums = [1, 2, 3, 4]
    result = HashMapSetOperations.contains_duplicate(nums)
    print(f"   contains_duplicate([1, 2, 3, 4]) = {result} (expected: False)")
    print(f"   → all numbers are unique")
    assert result == False, f"Expected False, got {result}"
    
    print("\nStep 3: Testing empty array...")
    nums = []
    result = HashMapSetOperations.contains_duplicate(nums)
    print(f"   contains_duplicate([]) = {result} (expected: False)")
    print(f"   → empty array has no duplicates")
    assert result == False, f"Expected False, got {result}"
    
    print("\nStep 4: Testing single element...")
    nums = [1]
    result = HashMapSetOperations.contains_duplicate(nums)
    print(f"   contains_duplicate([1]) = {result} (expected: False)")
    print(f"   → single element cannot duplicate itself")
    assert result == False, f"Expected False, got {result}"
    
    print("✓ contains_duplicate tests passed")

def test_find_all_duplicates():
    """Test find_all_duplicates function"""
    print("Step 1: Testing multiple duplicates...")
    
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    result = HashMapSetOperations.find_all_duplicates(nums)
    print(f"   find_all_duplicates([4, 3, 2, 7, 8, 2, 3, 1]) = {result} (expected: [2, 3])")
    print(f"   → numbers 2 and 3 each appear twice")
    assert sorted(result) == sorted([2, 3]), f"Expected [2, 3], got {result}"
    
    print("\nStep 2: Testing no duplicates...")
    nums = [1, 2, 3, 4]
    result = HashMapSetOperations.find_all_duplicates(nums)
    print(f"   find_all_duplicates([1, 2, 3, 4]) = {result} (expected: [])")
    print(f"   → all numbers are unique")
    assert result == [], f"Expected [], got {result}"
    
    print("\nStep 3: Testing all same elements...")
    nums = [1, 1, 1, 1]
    result = HashMapSetOperations.find_all_duplicates(nums)
    print(f"   find_all_duplicates([1, 1, 1, 1]) = {result} (expected: [1])")
    print(f"   → number 1 appears multiple times")
    assert result == [1], f"Expected [1], got {result}"
    
    print("✓ find_all_duplicates tests passed")

def test_intersection_of_arrays():
    """Test intersection_of_arrays function"""
    print("Step 1: Testing basic intersection...")
    
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = HashMapSetOperations.intersection_of_arrays(nums1, nums2)
    print(f"   intersection_of_arrays([1, 2, 2, 1], [2, 2]) = {result} (expected: [2])")
    print(f"   → only number 2 appears in both arrays")
    assert sorted(result) == sorted([2]), f"Expected [2], got {result}"
    
    print("\nStep 2: Testing multiple intersections...")
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    result = HashMapSetOperations.intersection_of_arrays(nums1, nums2)
    print(f"   intersection_of_arrays([4, 9, 5], [9, 4, 9, 8, 4]) = {result} (expected: [4, 9])")
    print(f"   → numbers 4 and 9 appear in both arrays")
    assert sorted(result) == sorted([4, 9]), f"Expected [4, 9], got {result}"
    
    print("\nStep 3: Testing no intersection...")
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    result = HashMapSetOperations.intersection_of_arrays(nums1, nums2)
    print(f"   intersection_of_arrays([1, 2, 3], [4, 5, 6]) = {result} (expected: [])")
    print(f"   → no numbers appear in both arrays")
    assert result == [], f"Expected [], got {result}"
    
    print("✓ intersection_of_arrays tests passed")

def test_union_of_arrays():
    """Test union_of_arrays function"""
    print("Step 1: Testing basic union...")
    
    nums1 = [1, 2, 3]
    nums2 = [3, 4, 5]
    result = HashMapSetOperations.union_of_arrays(nums1, nums2)
    print(f"   union_of_arrays([1, 2, 3], [3, 4, 5]) = {result} (expected: [1, 2, 3, 4, 5])")
    print(f"   → union contains all unique numbers from both arrays")
    assert sorted(result) == sorted([1, 2, 3, 4, 5]), f"Expected [1, 2, 3, 4, 5], got {result}"
    
    print("\nStep 2: Testing union with duplicates...")
    nums1 = [1, 1, 2, 2]
    nums2 = [2, 2, 3, 3]
    result = HashMapSetOperations.union_of_arrays(nums1, nums2)
    print(f"   union_of_arrays([1, 1, 2, 2], [2, 2, 3, 3]) = {result} (expected: [1, 2, 3])")
    print(f"   → duplicates are removed in union")
    assert sorted(result) == sorted([1, 2, 3]), f"Expected [1, 2, 3], got {result}"
    
    print("✓ union_of_arrays tests passed")

def test_character_frequency():
    """Test character_frequency function"""
    print("Step 1: Testing basic string...")
    
    s = "hello"
    result = HashMapSetOperations.character_frequency(s)
    expected = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(f"   character_frequency('hello') = {result} (expected: {expected})")
    print(f"   → 'l' appears twice, others once")
    assert result == expected, f"Expected {expected}, got {result}"
    
    print("\nStep 2: Testing empty string...")
    s = ""
    result = HashMapSetOperations.character_frequency(s)
    expected = {}
    print(f"   character_frequency('') = {result} (expected: {expected})")
    print(f"   → empty string has no characters")
    assert result == expected, f"Expected {expected}, got {result}"
    
    print("\nStep 3: Testing single character repeated...")
    s = "aaaa"
    result = HashMapSetOperations.character_frequency(s)
    expected = {'a': 4}
    print(f"   character_frequency('aaaa') = {result} (expected: {expected})")
    print(f"   → 'a' appears 4 times")
    assert result == expected, f"Expected {expected}, got {result}"
    
    print("✓ character_frequency tests passed")

def test_longest_consecutive_sequence():
    """Test longest_consecutive_sequence function"""
    print("Step 1: Testing normal case with mixed numbers...")
    
    nums = [100, 4, 200, 1, 3, 2]
    result = HashMapSetOperations.longest_consecutive_sequence(nums)
    print(f"   longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) = {result} (expected: 4)")
    print(f"   → Sequence: [1, 2, 3, 4] has length 4")
    assert result == 4, f"Expected 4, got {result}"
    
    print("\nStep 2: Testing longer consecutive sequence...")
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    result = HashMapSetOperations.longest_consecutive_sequence(nums)
    print(f"   longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) = {result} (expected: 9)")
    print(f"   → Sequence: [0, 1, 2, 3, 4, 5, 6, 7, 8] has length 9")
    assert result == 9, f"Expected 9, got {result}"
    
    print("\nStep 3: Testing empty array...")
    nums = []
    result = HashMapSetOperations.longest_consecutive_sequence(nums)
    print(f"   longest_consecutive_sequence([]) = {result} (expected: 0)")
    print(f"   → Empty array has no consecutive sequence")
    assert result == 0, f"Expected 0, got {result}"
    
    print("\nStep 4: Testing array with duplicates...")
    nums = [1, 2, 0, 1]
    result = HashMapSetOperations.longest_consecutive_sequence(nums)
    print(f"   longest_consecutive_sequence([1, 2, 0, 1]) = {result} (expected: 3)")
    print(f"   → Sequence: [0, 1, 2] has length 3 (duplicate 1 ignored)")
    assert result == 3, f"Expected 3, got {result}"
    
    print("\nStep 5: Testing single element...")
    nums = [42]
    result = HashMapSetOperations.longest_consecutive_sequence(nums)
    print(f"   longest_consecutive_sequence([42]) = {result} (expected: 1)")
    print(f"   → Single element forms sequence of length 1")
    assert result == 1, f"Expected 1, got {result}"
    
    print("\nStep 6: Testing no consecutive elements...")
    nums = [1, 3, 5, 7, 9]
    result = HashMapSetOperations.longest_consecutive_sequence(nums)
    print(f"   longest_consecutive_sequence([1, 3, 5, 7, 9]) = {result} (expected: 1)")
    print(f"   → No consecutive numbers, longest sequence is 1")
    assert result == 1, f"Expected 1, got {result}"
    
    print("\nStep 7: Testing negative numbers...")
    nums = [-1, -2, 0, 1]
    result = HashMapSetOperations.longest_consecutive_sequence(nums)
    print(f"   longest_consecutive_sequence([-1, -2, 0, 1]) = {result} (expected: 4)")
    print(f"   → Sequence: [-2, -1, 0, 1] has length 4")
    assert result == 4, f"Expected 4, got {result}"
    
    print("\nStep 8: Testing all same elements...")
    nums = [5, 5, 5, 5]
    result = HashMapSetOperations.longest_consecutive_sequence(nums)
    print(f"   longest_consecutive_sequence([5, 5, 5, 5]) = {result} (expected: 1)")
    print(f"   → All duplicates form sequence of length 1")
    assert result == 1, f"Expected 1, got {result}"
    
    print("✓ longest_consecutive_sequence tests passed")

def test_is_anagram():
    """Test is_anagram function"""
    print("Step 1: Testing valid anagrams...")
    
    s1, s2 = "listen", "silent"
    result = HashMapSetOperations.is_anagram(s1, s2)
    print(f"   is_anagram('listen', 'silent') = {result} (expected: True)")
    print(f"   → both strings have same character frequencies")
    assert result == True, f"Expected True, got {result}"
    
    print("\nStep 2: Testing non-anagrams...")
    s1, s2 = "hello", "world"
    result = HashMapSetOperations.is_anagram(s1, s2)
    print(f"   is_anagram('hello', 'world') = {result} (expected: False)")
    print(f"   → strings have different character frequencies")
    assert result == False, f"Expected False, got {result}"
    
    print("\nStep 3: Testing different lengths...")
    s1, s2 = "abc", "abcd"
    result = HashMapSetOperations.is_anagram(s1, s2)
    print(f"   is_anagram('abc', 'abcd') = {result} (expected: False)")
    print(f"   → strings of different lengths cannot be anagrams")
    assert result == False, f"Expected False, got {result}"
    
    print("\nStep 4: Testing empty strings...")
    s1, s2 = "", ""
    result = HashMapSetOperations.is_anagram(s1, s2)
    print(f"   is_anagram('', '') = {result} (expected: True)")
    print(f"   → empty strings are anagrams of each other")
    assert result == True, f"Expected True, got {result}"
    
    print("✓ is_anagram tests passed")

def test_group_anagrams():
    """Test group_anagrams function"""
    print("Step 1: Testing multiple anagram groups...")
    
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = HashMapSetOperations.group_anagrams(strs)
    print(f"   group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']) = {result}")
    print(f"   → should group anagrams together")
    
    # Sort each group and the list of groups for comparison
    result_sorted = [sorted(group) for group in result]
    result_sorted.sort()
    expected = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    expected_sorted = [sorted(group) for group in expected]
    expected_sorted.sort()
    assert result_sorted == expected_sorted, f"Expected {expected}, got {result}"
    
    print("\nStep 2: Testing no anagrams...")
    strs = ["abc", "def", "ghi"]
    result = HashMapSetOperations.group_anagrams(strs)
    print(f"   group_anagrams(['abc', 'def', 'ghi']) = {result}")
    print(f"   → each string forms its own group")
    assert len(result) == 3, f"Expected 3 groups, got {len(result)}"
    
    print("\nStep 3: Testing all same anagrams...")
    strs = ["abc", "bca", "cab"]
    result = HashMapSetOperations.group_anagrams(strs)
    print(f"   group_anagrams(['abc', 'bca', 'cab']) = {result}")
    print(f"   → all strings are anagrams, should form one group")
    assert len(result) == 1, f"Expected 1 group, got {len(result)}"
    assert len(result[0]) == 3, f"Expected group of 3, got {len(result[0])}"
    
    print("✓ group_anagrams tests passed")

def test_first_non_repeating_character():
    """Test first_non_repeating_character function"""
    print("Step 1: Testing string with non-repeating character...")
    
    s = "leetcode"
    result = HashMapSetOperations.first_non_repeating_character(s)
    print(f"   first_non_repeating_character('leetcode') = {result} (expected: 0)")
    print(f"   → 'l' at index 0 is first non-repeating character")
    assert result == 0, f"Expected 0, got {result}"
    
    print("\nStep 2: Testing all characters repeat...")
    s = "aabb"
    result = HashMapSetOperations.first_non_repeating_character(s)
    print(f"   first_non_repeating_character('aabb') = {result} (expected: -1)")
    print(f"   → all characters repeat, no non-repeating character")
    assert result == -1, f"Expected -1, got {result}"
    
    print("\nStep 3: Testing single character...")
    s = "a"
    result = HashMapSetOperations.first_non_repeating_character(s)
    print(f"   first_non_repeating_character('a') = {result} (expected: 0)")
    print(f"   → single character is non-repeating")
    assert result == 0, f"Expected 0, got {result}"
    
    print("\nStep 4: Testing non-repeating at end...")
    s = "aabbc"
    result = HashMapSetOperations.first_non_repeating_character(s)
    print(f"   first_non_repeating_character('aabbc') = {result} (expected: 4)")
    print(f"   → 'c' at index 4 is first non-repeating character")
    assert result == 4, f"Expected 4, got {result}"
    
    print("✓ first_non_repeating_character tests passed")

def test_subarray_sum_equals_k():
    """Test subarray_sum_equals_k function"""
    print("Step 1: Testing multiple subarrays...")
    
    nums = [1, 1, 1]
    k = 2
    result = HashMapSetOperations.subarray_sum_equals_k(nums, k)
    print(f"   subarray_sum_equals_k([1, 1, 1], 2) = {result} (expected: 2)")
    print(f"   → subarrays [1,1] appear at positions (0,1) and (1,2)")
    assert result == 2, f"Expected 2, got {result}"
    
    print("\nStep 2: Testing multiple ways to reach sum...")
    nums = [1, 2, 3]
    k = 3
    result = HashMapSetOperations.subarray_sum_equals_k(nums, k)
    print(f"   subarray_sum_equals_k([1, 2, 3], 3) = {result} (expected: 2)")
    print(f"   → subarrays: [3] and [1,2] both sum to 3")
    assert result == 2, f"Expected 2, got {result}"
    
    print("\nStep 3: Testing no valid subarrays...")
    nums = [1, 2, 3]
    k = 7
    result = HashMapSetOperations.subarray_sum_equals_k(nums, k)
    print(f"   subarray_sum_equals_k([1, 2, 3], 7) = {result} (expected: 0)")
    print(f"   → no subarray sums to 7")
    assert result == 0, f"Expected 0, got {result}"
    
    print("\nStep 4: Testing with negative numbers...")
    nums = [1, -1, 0]
    k = 0
    result = HashMapSetOperations.subarray_sum_equals_k(nums, k)
    print(f"   subarray_sum_equals_k([1, -1, 0], 0) = {result} (expected: 3)")
    print(f"   → subarrays: [1,-1], [0], [1,-1,0] all sum to 0")
    assert result == 3, f"Expected 3, got {result}"
    
    print("✓ subarray_sum_equals_k tests passed")

def test_longest_substring_without_repeating_chars_hashmap():
    """Test longest_substring_without_repeating_chars_hashmap function"""
    print("Step 1: Testing basic case...")
    
    s = "abcabcbb"
    result = HashMapSetOperations.longest_substring_without_repeating_chars_hashmap(s)
    print(f"   longest_substring_without_repeating_chars_hashmap('abcabcbb') = {result} (expected: 3)")
    print(f"   → longest substring without repeating chars is 'abc' (length 3)")
    assert result == 3, f"Expected 3, got {result}"
    
    print("\nStep 2: Testing all same characters...")
    s = "bbbbb"
    result = HashMapSetOperations.longest_substring_without_repeating_chars_hashmap(s)
    print(f"   longest_substring_without_repeating_chars_hashmap('bbbbb') = {result} (expected: 1)")
    print(f"   → longest substring is single 'b' (length 1)")
    assert result == 1, f"Expected 1, got {result}"
    
    print("\nStep 3: Testing mixed repeating pattern...")
    s = "pwwkew"
    result = HashMapSetOperations.longest_substring_without_repeating_chars_hashmap(s)
    print(f"   longest_substring_without_repeating_chars_hashmap('pwwkew') = {result} (expected: 3)")
    print(f"   → longest substring is 'wke' (length 3)")
    assert result == 3, f"Expected 3, got {result}"
    
    print("\nStep 4: Testing empty string...")
    s = ""
    result = HashMapSetOperations.longest_substring_without_repeating_chars_hashmap(s)
    print(f"   longest_substring_without_repeating_chars_hashmap('') = {result} (expected: 0)")
    print(f"   → empty string has no substrings")
    assert result == 0, f"Expected 0, got {result}"
    
    print("✓ longest_substring_without_repeating_chars_hashmap tests passed")

def test_four_sum_count():
    """Test four_sum_count function"""
    print("Step 1: Testing basic case...")
    
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    result = HashMapSetOperations.four_sum_count(nums1, nums2, nums3, nums4)
    print(f"   four_sum_count([1,2], [-2,-1], [-1,2], [0,2]) = {result} (expected: 2)")
    print(f"   → 2 combinations sum to 0")
    assert result == 2, f"Expected 2, got {result}"
    
    print("\nStep 2: Testing no valid combinations...")
    nums1 = [1]
    nums2 = [1]
    nums3 = [1]
    nums4 = [1]
    result = HashMapSetOperations.four_sum_count(nums1, nums2, nums3, nums4)
    print(f"   four_sum_count([1], [1], [1], [1]) = {result} (expected: 0)")
    print(f"   → 1+1+1+1 = 4, not 0")
    assert result == 0, f"Expected 0, got {result}"
    
    print("\nStep 3: Testing all zeros...")
    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]
    result = HashMapSetOperations.four_sum_count(nums1, nums2, nums3, nums4)
    print(f"   four_sum_count([0], [0], [0], [0]) = {result} (expected: 1)")
    print(f"   → 0+0+0+0 = 0, valid combination")
    assert result == 1, f"Expected 1, got {result}"
    
    print("✓ four_sum_count tests passed")

def test_top_k_frequent_elements():
    """Test top_k_frequent_elements function"""
    print("Step 1: Testing basic case...")
    
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = HashMapSetOperations.top_k_frequent_elements(nums, k)
    print(f"   top_k_frequent_elements([1,1,1,2,2,3], 2) = {result} (expected: [1,2])")
    print(f"   → 1 appears 3 times, 2 appears 2 times (most frequent)")
    assert sorted(result) == sorted([1, 2]), f"Expected [1, 2], got {result}"
    
    print("\nStep 2: Testing single element...")
    nums = [1]
    k = 1
    result = HashMapSetOperations.top_k_frequent_elements(nums, k)
    print(f"   top_k_frequent_elements([1], 1) = {result} (expected: [1])")
    print(f"   → only one element, so it's the most frequent")
    assert result == [1], f"Expected [1], got {result}"
    
    print("\nStep 3: Testing all elements same frequency...")
    nums = [1, 2, 3]
    k = 2
    result = HashMapSetOperations.top_k_frequent_elements(nums, k)
    print(f"   top_k_frequent_elements([1,2,3], 2) = {result}")
    print(f"   → all elements appear once, return any 2")
    assert len(result) == 2, f"Expected 2 elements, got {len(result)}"
    assert all(num in nums for num in result), f"Result contains invalid elements: {result}"
    
    print("✓ top_k_frequent_elements tests passed")

def test_valid_sudoku():
    """Test valid_sudoku function"""
    print("Step 1: Testing valid sudoku board...")
    
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
    result = HashMapSetOperations.valid_sudoku(board)
    print(f"   valid_sudoku(valid_board) = {result} (expected: True)")
    print(f"   → no duplicates in rows, columns, or 3x3 boxes")
    assert result == True, f"Expected True, got {result}"
    
    print("\nStep 2: Testing invalid sudoku board (duplicate in row)...")
    board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    result = HashMapSetOperations.valid_sudoku(board)
    print(f"   valid_sudoku(invalid_board) = {result} (expected: False)")
    print(f"   → duplicate '8' in first row violates sudoku rules")
    assert result == False, f"Expected False, got {result}"
    
    print("✓ valid_sudoku tests passed")

def run_all_tests():
    """Run all test functions with detailed reporting"""
    print("🚀 STARTING COMPREHENSIVE HASHMAP AND SET TESTS")
    print("="*70)
    
    tests = [
        ("Two Sum", test_two_sum),
        ("Contains Duplicate", test_contains_duplicate),
        ("Find All Duplicates", test_find_all_duplicates),
        ("Intersection of Arrays", test_intersection_of_arrays),
        ("Union of Arrays", test_union_of_arrays),
        ("Character Frequency", test_character_frequency),
        ("Longest Consecutive Sequence", test_longest_consecutive_sequence),
        ("Is Anagram", test_is_anagram),
        ("Group Anagrams", test_group_anagrams),
        ("First Non-Repeating Character", test_first_non_repeating_character),
        ("Subarray Sum Equals K", test_subarray_sum_equals_k),
        ("Longest Substring Without Repeating Chars", test_longest_substring_without_repeating_chars_hashmap),
        ("Four Sum Count", test_four_sum_count),
        ("Top K Frequent Elements", test_top_k_frequent_elements),
        ("Valid Sudoku", test_valid_sudoku),
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
