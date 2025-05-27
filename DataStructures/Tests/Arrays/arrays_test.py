import unittest
import sys
import os
import argparse

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
    
    # Now import the module
    try:
        global ArrayOperations
        from array_operations import ArrayOperations
        return True
    except ImportError as e:
        print(f"Error importing ArrayOperations: {e}")
        print(f"Make sure the file exists in the appropriate directory.")
        return False

# Set up imports before defining the test cases
if not setup_imports():
    sys.exit(1)

class TestArrayOperations(unittest.TestCase):
    
    def test_find_element(self):
        # Test basic case
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(ArrayOperations.find_element(arr, 5), 2)
        self.assertEqual(ArrayOperations.find_element(arr, 7), 3)
        
        # Test element not found
        self.assertEqual(ArrayOperations.find_element(arr, 6), -1)
        
        # Test empty array
        self.assertEqual(ArrayOperations.find_element([], 5), -1)
    
    def test_reverse_array(self):
        # Test odd length array
        arr1 = [1, 2, 3, 4, 5]
        self.assertEqual(ArrayOperations.reverse_array(arr1.copy()), [5, 4, 3, 2, 1])
        
        # Test even length array
        arr2 = [1, 2, 3, 4]
        self.assertEqual(ArrayOperations.reverse_array(arr2.copy()), [4, 3, 2, 1])
        
        # Test single element array
        arr3 = [1]
        self.assertEqual(ArrayOperations.reverse_array(arr3.copy()), [1])
        
        # Test empty array
        arr4 = []
        self.assertEqual(ArrayOperations.reverse_array(arr4.copy()), [])
    
    def test_find_max_min(self):
        # Test normal case
        arr1 = [3, 5, 1, 7, 2]
        self.assertEqual(ArrayOperations.find_max_min(arr1), (7, 1))
        
        # Test with negative numbers
        arr2 = [-3, -5, -1, -7, -2]
        self.assertEqual(ArrayOperations.find_max_min(arr2), (-1, -7))
        
        # Test with mixed numbers
        arr3 = [-3, 5, -1, 7, -2]
        self.assertEqual(ArrayOperations.find_max_min(arr3), (7, -3))
        
        # Test single element array
        arr4 = [42]
        self.assertEqual(ArrayOperations.find_max_min(arr4), (42, 42))
        
        # Test empty array
        arr5 = []
        self.assertEqual(ArrayOperations.find_max_min(arr5), (None, None))
    
    def test_remove_duplicates(self):
        # Test sorted array with duplicates
        arr1 = [1, 1, 2, 2, 3, 4, 4, 5]
        self.assertEqual(ArrayOperations.remove_duplicates(arr1), [1, 2, 3, 4, 5])
        
        # Test array with all same elements
        arr2 = [1, 1, 1, 1]
        self.assertEqual(ArrayOperations.remove_duplicates(arr2), [1])
        
        # Test array with no duplicates
        arr3 = [1, 2, 3, 4, 5]
        self.assertEqual(ArrayOperations.remove_duplicates(arr3), [1, 2, 3, 4, 5])
        
        # Test empty array
        arr4 = []
        self.assertEqual(ArrayOperations.remove_duplicates(arr4), [])
    
    def test_two_sum(self):
        # Test basic case
        arr1 = [2, 7, 11, 15]
        self.assertEqual(ArrayOperations.two_sum(arr1, 9), [0, 1])
        
        # Test case with target not found
        arr2 = [2, 7, 11, 15]
        self.assertEqual(ArrayOperations.two_sum(arr2, 30), [])
        
        # Test case with negative numbers
        arr3 = [3, -1, 0, 5]
        self.assertEqual(ArrayOperations.two_sum(arr3, 2), [0, 1])
        
        # Test case with duplicate numbers that sum to target
        arr4 = [3, 3]
        self.assertEqual(ArrayOperations.two_sum(arr4, 6), [0, 1])
        
        # Test empty array
        arr5 = []
        self.assertEqual(ArrayOperations.two_sum(arr5, 5), [])
    
    def test_rotate_array(self):
        # Test basic rotation
        arr1 = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(ArrayOperations.rotate_array(arr1.copy(), 3), [5, 6, 7, 1, 2, 3, 4])
        
        # Test rotation equal to array length (no change)
        arr2 = [1, 2, 3, 4, 5]
        self.assertEqual(ArrayOperations.rotate_array(arr2.copy(), 5), [1, 2, 3, 4, 5])
        
        # Test rotation greater than array length
        arr3 = [1, 2, 3, 4, 5]
        self.assertEqual(ArrayOperations.rotate_array(arr3.copy(), 7), [4, 5, 1, 2, 3])  # 7 % 5 = 2
        
        # Test rotation of 0 steps
        arr4 = [1, 2, 3, 4, 5]
        self.assertEqual(ArrayOperations.rotate_array(arr4.copy(), 0), [1, 2, 3, 4, 5])
        
        # Test single element array
        arr5 = [42]
        self.assertEqual(ArrayOperations.rotate_array(arr5.copy(), 3), [42])
        
        # Test empty array
        arr6 = []
        self.assertEqual(ArrayOperations.rotate_array(arr6.copy(), 3), [])
    
    def test_kadanes_algorithm(self):
        # Test basic case
        arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(ArrayOperations.kadanes_algorithm(arr1), 6)  # Subarray [4, -1, 2, 1]
        
        # Test all positive numbers
        arr2 = [1, 2, 3, 4, 5]
        self.assertEqual(ArrayOperations.kadanes_algorithm(arr2), 15)  # Entire array
        
        # Test all negative numbers
        arr3 = [-1, -2, -3, -4, -5]
        self.assertEqual(ArrayOperations.kadanes_algorithm(arr3), -1)  # Just the first element
        
        # Test with a single positive number
        arr4 = [42]
        self.assertEqual(ArrayOperations.kadanes_algorithm(arr4), 42)
        
        # Test with a single negative number
        arr5 = [-42]
        self.assertEqual(ArrayOperations.kadanes_algorithm(arr5), -42)
        
        # Test empty array
        arr6 = []
        self.assertEqual(ArrayOperations.kadanes_algorithm(arr6), 0)
    
    def test_kadanes_algorithm_with_subarray(self):
        # Test basic case
        arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(ArrayOperations.kadanes_algorithm_with_subarray(arr1), (6, 3, 6))  # Subarray [4, -1, 2, 1]
        
        # Test all positive numbers
        arr2 = [1, 2, 3, 4, 5]
        self.assertEqual(ArrayOperations.kadanes_algorithm_with_subarray(arr2), (15, 0, 4))  # Entire array
        
        # Test all negative numbers
        arr3 = [-1, -2, -3, -4, -5]
        self.assertEqual(ArrayOperations.kadanes_algorithm_with_subarray(arr3), (-1, 0, 0))  # Just the first element
        
        # Test with a single element
        arr4 = [42]
        self.assertEqual(ArrayOperations.kadanes_algorithm_with_subarray(arr4), (42, 0, 0))
        
        # Test with specific subarray pattern
        arr5 = [3, -4, 5, -2, 1, 6, -1]
        self.assertEqual(ArrayOperations.kadanes_algorithm_with_subarray(arr5), (10, 2, 5))  # Subarray [5, -2, 1, 6]
        
        # Test empty array
        arr6 = []
        self.assertEqual(ArrayOperations.kadanes_algorithm_with_subarray(arr6), (0, -1, -1))

if __name__ == "__main__":
    unittest.main()
