import sys
import os
import argparse

def setup_imports():
    """Set up imports based on the command-line argument."""
    parser = argparse.ArgumentParser(description='Test hashmap+set operations')
    parser.add_argument('--mode', choices=['solution', 'practice'], default='solution',
                      help='Which implementation to test (solution or practice)')
    args = parser.parse_args()
  
    # Get the current directory and project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir,'..', '..'))
    
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
except ImportError:
    print("Could not import HashMapSetOperations. Make sure the file exists in Solutions/Hashmaps+Sets/ or Practice/Hashmaps+Sets/")
    sys.exit(1)

def test_two_sum():
    """Test two_sum function"""
    print("Testing two_sum...")
    
    # Test case 1: Basic case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = HashMapSetOperations.two_sum(nums1, target1)
    expected1 = [0, 1]
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test case 2: Target at end
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = HashMapSetOperations.two_sum(nums2, target2)
    expected2 = [1, 2]
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test case 3: Same number twice
    nums3 = [3, 3]
    target3 = 6
    result3 = HashMapSetOperations.two_sum(nums3, target3)
    expected3 = [0, 1]
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    # Test case 4: No solution
    nums4 = [1, 2, 3]
    target4 = 7
    result4 = HashMapSetOperations.two_sum(nums4, target4)
    expected4 = []
    assert result4 == expected4, f"Expected {expected4}, got {result4}"
    
    print("✓ two_sum tests passed")

def test_contains_duplicate():
    """Test contains_duplicate function"""
    print("Testing contains_duplicate...")
    
    # Test case 1: Has duplicates
    nums1 = [1, 2, 3, 1]
    result1 = HashMapSetOperations.contains_duplicate(nums1)
    assert result1 == True, f"Expected True, got {result1}"
    
    # Test case 2: No duplicates
    nums2 = [1, 2, 3, 4]
    result2 = HashMapSetOperations.contains_duplicate(nums2)
    assert result2 == False, f"Expected False, got {result2}"
    
    # Test case 3: Empty array
    nums3 = []
    result3 = HashMapSetOperations.contains_duplicate(nums3)
    assert result3 == False, f"Expected False, got {result3}"
    
    # Test case 4: Single element
    nums4 = [1]
    result4 = HashMapSetOperations.contains_duplicate(nums4)
    assert result4 == False, f"Expected False, got {result4}"
    
    print("✓ contains_duplicate tests passed")

def test_find_all_duplicates():
    """Test find_all_duplicates function"""
    print("Testing find_all_duplicates...")
    
    # Test case 1: Multiple duplicates
    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
    result1 = HashMapSetOperations.find_all_duplicates(nums1)
    expected1 = [2, 3]
    assert sorted(result1) == sorted(expected1), f"Expected {expected1}, got {result1}"
    
    # Test case 2: No duplicates
    nums2 = [1, 2, 3, 4]
    result2 = HashMapSetOperations.find_all_duplicates(nums2)
    expected2 = []
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test case 3: All same elements
    nums3 = [1, 1, 1, 1]
    result3 = HashMapSetOperations.find_all_duplicates(nums3)
    expected3 = [1]
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    print("✓ find_all_duplicates tests passed")

def test_intersection_of_arrays():
    """Test intersection_of_arrays function"""
    print("Testing intersection_of_arrays...")
    
    # Test case 1: Basic intersection
    nums1_1 = [1, 2, 2, 1]
    nums2_1 = [2, 2]
    result1 = HashMapSetOperations.intersection_of_arrays(nums1_1, nums2_1)
    expected1 = [2]
    assert sorted(result1) == sorted(expected1), f"Expected {expected1}, got {result1}"
    
    # Test case 2: Multiple intersections
    nums1_2 = [4, 9, 5]
    nums2_2 = [9, 4, 9, 8, 4]
    result2 = HashMapSetOperations.intersection_of_arrays(nums1_2, nums2_2)
    expected2 = [4, 9]
    assert sorted(result2) == sorted(expected2), f"Expected {expected2}, got {result2}"
    
    # Test case 3: No intersection
    nums1_3 = [1, 2, 3]
    nums2_3 = [4, 5, 6]
    result3 = HashMapSetOperations.intersection_of_arrays(nums1_3, nums2_3)
    expected3 = []
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    print("✓ intersection_of_arrays tests passed")

def test_union_of_arrays():
    """Test union_of_arrays function"""
    print("Testing union_of_arrays...")
    
    # Test case 1: Basic union
    nums1_1 = [1, 2, 3]
    nums2_1 = [3, 4, 5]
    result1 = HashMapSetOperations.union_of_arrays(nums1_1, nums2_1)
    expected1 = [1, 2, 3, 4, 5]
    assert sorted(result1) == sorted(expected1), f"Expected {expected1}, got {result1}"
    
    # Test case 2: With duplicates
    nums1_2 = [1, 1, 2, 2]
    nums2_2 = [2, 2, 3, 3]
    result2 = HashMapSetOperations.union_of_arrays(nums1_2, nums2_2)
    expected2 = [1, 2, 3]
    assert sorted(result2) == sorted(expected2), f"Expected {expected2}, got {result2}"
    
    print("✓ union_of_arrays tests passed")

def test_character_frequency():
    """Test character_frequency function"""
    print("Testing character_frequency...")
    
    # Test case 1: Basic string
    s1 = "hello"
    result1 = HashMapSetOperations.character_frequency(s1)
    expected1 = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test case 2: Empty string
    s2 = ""
    result2 = HashMapSetOperations.character_frequency(s2)
    expected2 = {}
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test case 3: Single character repeated
    s3 = "aaaa"
    result3 = HashMapSetOperations.character_frequency(s3)
    expected3 = {'a': 4}
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    print("✓ character_frequency tests passed")

def test_is_anagram():
    """Test is_anagram function"""
    print("Testing is_anagram...")
    
    # Test case 1: Valid anagrams
    s1_1, s2_1 = "listen", "silent"
    result1 = HashMapSetOperations.is_anagram(s1_1, s2_1)
    assert result1 == True, f"Expected True, got {result1}"
    
    # Test case 2: Not anagrams
    s1_2, s2_2 = "hello", "world"
    result2 = HashMapSetOperations.is_anagram(s1_2, s2_2)
    assert result2 == False, f"Expected False, got {result2}"
    
    # Test case 3: Different lengths
    s1_3, s2_3 = "abc", "abcd"
    result3 = HashMapSetOperations.is_anagram(s1_3, s2_3)
    assert result3 == False, f"Expected False, got {result3}"
    
    # Test case 4: Empty strings
    s1_4, s2_4 = "", ""
    result4 = HashMapSetOperations.is_anagram(s1_4, s2_4)
    assert result4 == True, f"Expected True, got {result4}"
    
    print("✓ is_anagram tests passed")

def test_group_anagrams():
    """Test group_anagrams function"""
    print("Testing group_anagrams...")
    
    # Test case 1: Multiple anagram groups
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = HashMapSetOperations.group_anagrams(strs1)
    # Sort each group and the list of groups for comparison
    result1_sorted = [sorted(group) for group in result1]
    result1_sorted.sort()
    expected1 = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    expected1_sorted = [sorted(group) for group in expected1]
    expected1_sorted.sort()
    assert result1_sorted == expected1_sorted, f"Expected {expected1}, got {result1}"
    
    # Test case 2: No anagrams
    strs2 = ["abc", "def", "ghi"]
    result2 = HashMapSetOperations.group_anagrams(strs2)
    assert len(result2) == 3, f"Expected 3 groups, got {len(result2)}"
    
    # Test case 3: All same anagrams
    strs3 = ["abc", "bca", "cab"]
    result3 = HashMapSetOperations.group_anagrams(strs3)
    assert len(result3) == 1, f"Expected 1 group, got {len(result3)}"
    assert len(result3[0]) == 3, f"Expected group of 3, got {len(result3[0])}"
    
    print("✓ group_anagrams tests passed")

def test_first_non_repeating_character():
    """Test first_non_repeating_character function"""
    print("Testing first_non_repeating_character...")
    
    # Test case 1: Has non-repeating character
    s1 = "leetcode"
    result1 = HashMapSetOperations.first_non_repeating_character(s1)
    expected1 = 0  # 'l' at index 0
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test case 2: All characters repeat
    s2 = "aabb"
    result2 = HashMapSetOperations.first_non_repeating_character(s2)
    expected2 = -1
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test case 3: Single character
    s3 = "a"
    result3 = HashMapSetOperations.first_non_repeating_character(s3)
    expected3 = 0
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    # Test case 4: Non-repeating at end
    s4 = "aabbc"
    result4 = HashMapSetOperations.first_non_repeating_character(s4)
    expected4 = 4  # 'c' at index 4
    assert result4 == expected4, f"Expected {expected4}, got {result4}"
    
    print("✓ first_non_repeating_character tests passed")

def test_subarray_sum_equals_k():
    """Test subarray_sum_equals_k function"""
    print("Testing subarray_sum_equals_k...")
    
    # Test case 1: Multiple subarrays
    nums1 = [1, 1, 1]
    k1 = 2
    result1 = HashMapSetOperations.subarray_sum_equals_k(nums1, k1)
    expected1 = 2  # [1,1] appears twice
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test case 2: Single element equals k
    nums2 = [1, 2, 3]
    k2 = 3
    result2 = HashMapSetOperations.subarray_sum_equals_k(nums2, k2)
    expected2 = 2  # [3] and [1,2]
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test case 3: No valid subarrays
    nums3 = [1, 2, 3]
    k3 = 7
    result3 = HashMapSetOperations.subarray_sum_equals_k(nums3, k3)
    expected3 = 0
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    # Test case 4: With negative numbers
    nums4 = [1, -1, 0]
    k4 = 0
    result4 = HashMapSetOperations.subarray_sum_equals_k(nums4, k4)
    expected4 = 3  # [1,-1], [0], [1,-1,0]
    assert result4 == expected4, f"Expected {expected4}, got {result4}"
    
    print("✓ subarray_sum_equals_k tests passed")

def test_longest_substring_without_repeating_chars_hashmap():
    """Test longest_substring_without_repeating_chars_hashmap function"""
    print("Testing longest_substring_without_repeating_chars_hashmap...")
    
    # Test case 1: Basic case
    s1 = "abcabcbb"
    result1 = HashMapSetOperations.longest_substring_without_repeating_chars_hashmap(s1)
    expected1 = 3  # "abc"
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test case 2: All same characters
    s2 = "bbbbb"
    result2 = HashMapSetOperations.longest_substring_without_repeating_chars_hashmap(s2)
    expected2 = 1  # "b"
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test case 3: No repeating characters
    s3 = "pwwkew"
    result3 = HashMapSetOperations.longest_substring_without_repeating_chars_hashmap(s3)
    expected3 = 3  # "wke"
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    # Test case 4: Empty string
    s4 = ""
    result4 = HashMapSetOperations.longest_substring_without_repeating_chars_hashmap(s4)
    expected4 = 0
    assert result4 == expected4, f"Expected {expected4}, got {result4}"
    
    print("✓ longest_substring_without_repeating_chars_hashmap tests passed")

def test_four_sum_count():
    """Test four_sum_count function"""
    print("Testing four_sum_count...")
    
    # Test case 1: Basic case
    nums1_1 = [1, 2]
    nums2_1 = [-2, -1]
    nums3_1 = [-1, 2]
    nums4_1 = [0, 2]
    result1 = HashMapSetOperations.four_sum_count(nums1_1, nums2_1, nums3_1, nums4_1)
    expected1 = 2
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test case 2: No valid combinations
    nums1_2 = [1]
    nums2_2 = [1]
    nums3_2 = [1]
    nums4_2 = [1]
    result2 = HashMapSetOperations.four_sum_count(nums1_2, nums2_2, nums3_2, nums4_2)
    expected2 = 0  # 1+1+1+1 = 4, not 0
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test case 3: All zeros
    nums1_3 = [0]
    nums2_3 = [0]
    nums3_3 = [0]
    nums4_3 = [0]
    result3 = HashMapSetOperations.four_sum_count(nums1_3, nums2_3, nums3_3, nums4_3)
    expected3 = 1  # 0+0+0+0 = 0
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    print("✓ four_sum_count tests passed")

def test_top_k_frequent_elements():
    """Test top_k_frequent_elements function"""
    print("Testing top_k_frequent_elements...")
    
    # Test case 1: Basic case
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    result1 = HashMapSetOperations.top_k_frequent_elements(nums1, k1)
    expected1 = [1, 2]  # 1 appears 3 times, 2 appears 2 times
    assert sorted(result1) == sorted(expected1), f"Expected {expected1}, got {result1}"
    
    # Test case 2: Single element
    nums2 = [1]
    k2 = 1
    result2 = HashMapSetOperations.top_k_frequent_elements(nums2, k2)
    expected2 = [1]
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test case 3: All elements same frequency
    nums3 = [1, 2, 3]
    k3 = 2
    result3 = HashMapSetOperations.top_k_frequent_elements(nums3, k3)
    assert len(result3) == 2, f"Expected 2 elements, got {len(result3)}"
    assert all(num in nums3 for num in result3), f"Result contains invalid elements: {result3}"
    
    print("✓ top_k_frequent_elements tests passed")

def test_valid_sudoku():
    """Test valid_sudoku function"""
    print("Testing valid_sudoku...")
    
    # Test case 1: Valid board
    board1 = [
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
    result1 = HashMapSetOperations.valid_sudoku(board1)
    assert result1 == True, f"Expected True, got {result1}"
    
    # Test case 2: Invalid board (duplicate in row)
    board2 = [
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
    result2 = HashMapSetOperations.valid_sudoku(board2)
    assert result2 == False, f"Expected False, got {result2}"
    
    print("✓ valid_sudoku tests passed")

def run_all_tests():
    """Run all test functions"""
    print("Running HashMap and Set Operations Tests...")
    print("=" * 50)
    
    try:
        test_two_sum()
        test_contains_duplicate()
        test_find_all_duplicates()
        test_intersection_of_arrays()
        test_union_of_arrays()
        test_character_frequency()
        test_is_anagram()
        test_group_anagrams()
        test_first_non_repeating_character()
        test_subarray_sum_equals_k()
        test_longest_substring_without_repeating_chars_hashmap()
        test_four_sum_count()
        test_top_k_frequent_elements()
        test_valid_sudoku()
        
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
