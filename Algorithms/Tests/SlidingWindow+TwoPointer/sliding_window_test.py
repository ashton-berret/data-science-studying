# sliding_window_test.py
import unittest
import sys
import os
import argparse

def setup_imports():
    """Set up imports based on the command-line argument."""
    parser = argparse.ArgumentParser(description='Test sliding window operations')
    parser.add_argument('--mode', choices=['solution', 'practice'], default='solution',
                      help='Which implementation to test (solution or practice)')
    args = parser.parse_args()
    
    # Get the current directory and project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir,'..', '..'))
    
    if args.mode == 'solution':
        # Import from Solutions
        solutions_dir = os.path.join(project_root, 'Solutions', 'SlidingWindow+TwoPointer')
        sys.path.insert(0, solutions_dir)
        print(f"Testing solution implementation from: {solutions_dir}")
    else:
        # Import from Practice
        practice_dir = os.path.join(project_root, 'Practice', 'SlidingWindow+TwoPointer')
        sys.path.insert(0, practice_dir)
        print(f"Testing practice implementation from: {practice_dir}")
    
    # Now import the module
    try:
        global SlidingWindowOperations
        from sliding_window_solution import SlidingWindowOperations
        return True
    except ImportError as e:
        print(f"Error importing SlidingWindowOperations: {e}")
        print(f"Make sure the file exists in the appropriate directory.")
        return False

# Set up imports before defining the test cases
if not setup_imports():
    sys.exit(1)

class TestSlidingWindowOperations(unittest.TestCase):
    
    def test_max_sum_subarray_of_size_k(self):
        # Test normal case
        arr1 = [2, 1, 5, 1, 3, 2]
        self.assertEqual(SlidingWindowOperations.max_sum_subarray_of_size_k(arr1, 3), 9)
        
        # Test with all same elements
        arr2 = [1, 1, 1, 1, 1]
        self.assertEqual(SlidingWindowOperations.max_sum_subarray_of_size_k(arr2, 3), 3)
        
        # Test with negative numbers
        arr3 = [-1, -2, -3, -4, -5]
        self.assertEqual(SlidingWindowOperations.max_sum_subarray_of_size_k(arr3, 2), -3)
        
        # Test with k equal to array length
        arr4 = [1, 2, 3, 4, 5]
        self.assertEqual(SlidingWindowOperations.max_sum_subarray_of_size_k(arr4, 5), 15)
        
        # Test with k greater than array length
        arr5 = [1, 2, 3]
        self.assertEqual(SlidingWindowOperations.max_sum_subarray_of_size_k(arr5, 4), 0)
        
        # Test empty array
        arr6 = []
        self.assertEqual(SlidingWindowOperations.max_sum_subarray_of_size_k(arr6, 3), 0)
    
    def test_smallest_subarray_with_given_sum(self):
        # Test normal case
        arr1 = [2, 1, 5, 2, 3, 2]
        self.assertEqual(SlidingWindowOperations.smallest_subarray_with_given_sum(arr1, 7), 2)
        
        # Test case where the entire array is needed
        arr2 = [1, 1, 1, 1, 1]
        self.assertEqual(SlidingWindowOperations.smallest_subarray_with_given_sum(arr2, 5), 5)
        
        # Test case where no subarray exists with the given sum
        arr3 = [1, 2, 3, 4, 5]
        self.assertEqual(SlidingWindowOperations.smallest_subarray_with_given_sum(arr3, 20), 0)
        
        # Test with a single element that meets the requirement
        arr4 = [10, 2, 3]
        self.assertEqual(SlidingWindowOperations.smallest_subarray_with_given_sum(arr4, 10), 1)
        
        # Test empty array
        arr5 = []
        self.assertEqual(SlidingWindowOperations.smallest_subarray_with_given_sum(arr5, 5), 0)
    
    def test_longest_substring_with_k_distinct(self):
        # Test normal case
        self.assertEqual(SlidingWindowOperations.longest_substring_with_k_distinct("araaci", 2), 4)
        
        # Test with k equal to string length
        self.assertEqual(SlidingWindowOperations.longest_substring_with_k_distinct("abc", 3), 3)
        
        # Test with k greater than string length
        self.assertEqual(SlidingWindowOperations.longest_substring_with_k_distinct("abc", 4), 3)
        
        # Test with all same characters
        self.assertEqual(SlidingWindowOperations.longest_substring_with_k_distinct("aaaaa", 1), 5)
        
        # Test with k = 0
        self.assertEqual(SlidingWindowOperations.longest_substring_with_k_distinct("abc", 0), 0)
        
        # Test empty string
        self.assertEqual(SlidingWindowOperations.longest_substring_with_k_distinct("", 2), 0)
    
    def test_fruits_into_baskets(self):
        # Test case from problem description
        self.assertEqual(SlidingWindowOperations.fruits_into_baskets("ABCAC"), 3)
        
        # Test with all same fruits
        self.assertEqual(SlidingWindowOperations.fruits_into_baskets("AAAAA"), 5)
        
        # Test with alternating fruits
        self.assertEqual(SlidingWindowOperations.fruits_into_baskets("ABABAB"), 6)
        
        # Test with three different fruits
        self.assertEqual(SlidingWindowOperations.fruits_into_baskets("ABCBA"), 3)
        
        # Test empty array
        self.assertEqual(SlidingWindowOperations.fruits_into_baskets(""), 0)
    
    def test_longest_substring_without_repeating(self):
        # Test normal case
        self.assertEqual(SlidingWindowOperations.longest_substring_without_repeating("abcabcbb"), 3)
        
        # Test with all same characters
        self.assertEqual(SlidingWindowOperations.longest_substring_without_repeating("bbbbb"), 1)
        
        # Test with no repeating characters
        self.assertEqual(SlidingWindowOperations.longest_substring_without_repeating("abcdef"), 6)
        
        # Test empty string
        self.assertEqual(SlidingWindowOperations.longest_substring_without_repeating(""), 0)
        
        # Test with repeating pattern
        self.assertEqual(SlidingWindowOperations.longest_substring_without_repeating("pwwkew"), 3)
    
    def test_find_all_anagrams(self):
        # Test normal case
        self.assertEqual(SlidingWindowOperations.find_all_anagrams("cbaebabacd", "abc"), [0, 6])
        
        # Test with pattern longer than string
        self.assertEqual(SlidingWindowOperations.find_all_anagrams("abc", "abcd"), [])
        
        # Test with pattern equal to string
        self.assertEqual(SlidingWindowOperations.find_all_anagrams("abc", "abc"), [0])
        
        # Test with no anagrams
        self.assertEqual(SlidingWindowOperations.find_all_anagrams("hello", "world"), [])
        
        # Test with empty string
        self.assertEqual(SlidingWindowOperations.find_all_anagrams("", "abc"), [])
        
        # Test with empty pattern
        self.assertEqual(SlidingWindowOperations.find_all_anagrams("abc", ""), [])
    
    def test_longest_repeating_character_replacement(self):
        # Test normal case
        self.assertEqual(SlidingWindowOperations.longest_repeating_character_replacement("AABABBA", 1), 4)
        
        # Test with k = 0 (no replacements allowed)
        self.assertEqual(SlidingWindowOperations.longest_repeating_character_replacement("ABCDE", 0), 1)
        
        # Test with k equal to string length (all replacements allowed)
        self.assertEqual(SlidingWindowOperations.longest_repeating_character_replacement("ABCDE", 5), 5)
        
        # Test with all same characters
        self.assertEqual(SlidingWindowOperations.longest_repeating_character_replacement("AAAAA", 2), 5)
        
        # Test empty string
        self.assertEqual(SlidingWindowOperations.longest_repeating_character_replacement("", 2), 0)

if __name__ == "__main__":
    unittest.main()
