import sys
import os
import argparse
import traceback

def setup_imports():
    """Set up imports based on the command-line argument."""
    parser = argparse.ArgumentParser(description='Test sliding window operations')
    parser.add_argument('--mode', choices=['solution', 'practice'], default='solution',
                      help='Which implementation to test (solution or practice)')
    args = parser.parse_args()
    
    # Get the current directory and project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
    
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

# Setup the path and import
setup_imports()

try:
    from sliding_window_solution import SlidingWindowOperations
except ImportError as e:
    print(f"❌ Could not import SlidingWindowOperations: {e}")
    print("Make sure the file exists in Solutions/SlidingWindow+TwoPointer/ or Practice/SlidingWindow+TwoPointer/")
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

def test_max_sum_subarray_of_size_k():
    """Test max_sum_subarray_of_size_k function"""
    print("Step 1: Testing normal case...")
    
    arr1 = [2, 1, 5, 1, 3, 2]
    result = SlidingWindowOperations.max_sum_subarray_of_size_k(arr1, 3)
    print(f"   max_sum_subarray_of_size_k([2, 1, 5, 1, 3, 2], 3) = {result} (expected: 9)")
    assert result == 9, f"Expected 9, got {result}"
    
    print("\nStep 2: Testing with all same elements...")
    arr2 = [1, 1, 1, 1, 1]
    result = SlidingWindowOperations.max_sum_subarray_of_size_k(arr2, 3)
    print(f"   max_sum_subarray_of_size_k([1, 1, 1, 1, 1], 3) = {result} (expected: 3)")
    assert result == 3, f"Expected 3, got {result}"
    
    print("\nStep 3: Testing with negative numbers...")
    arr3 = [-1, -2, -3, -4, -5]
    result = SlidingWindowOperations.max_sum_subarray_of_size_k(arr3, 2)
    print(f"   max_sum_subarray_of_size_k([-1, -2, -3, -4, -5], 2) = {result} (expected: -3)")
    assert result == -3, f"Expected -3, got {result}"
    
    print("\nStep 4: Testing k greater than array length...")
    arr4 = [1, 2, 3]
    result = SlidingWindowOperations.max_sum_subarray_of_size_k(arr4, 4)
    print(f"   max_sum_subarray_of_size_k([1, 2, 3], 4) = {result} (expected: 0)")
    assert result == 0, f"Expected 0, got {result}"
    
    print("\nStep 5: Testing empty array...")
    arr5 = []
    result = SlidingWindowOperations.max_sum_subarray_of_size_k(arr5, 3)
    print(f"   max_sum_subarray_of_size_k([], 3) = {result} (expected: 0)")
    assert result == 0, f"Expected 0, got {result}"
    
    print("✓ max_sum_subarray_of_size_k tests passed")

def test_smallest_subarray_with_given_sum():
    """Test smallest_subarray_with_given_sum function"""
    print("Step 1: Testing normal case...")
    
    arr1 = [2, 1, 5, 2, 3, 2]
    result = SlidingWindowOperations.smallest_subarray_with_given_sum(arr1, 7)
    print(f"   smallest_subarray_with_given_sum([2, 1, 5, 2, 3, 2], 7) = {result} (expected: 2)")
    assert result == 2, f"Expected 2, got {result}"
    
    print("\nStep 2: Testing entire array needed...")
    arr2 = [1, 1, 1, 1, 1]
    result = SlidingWindowOperations.smallest_subarray_with_given_sum(arr2, 5)
    print(f"   smallest_subarray_with_given_sum([1, 1, 1, 1, 1], 5) = {result} (expected: 5)")
    assert result == 5, f"Expected 5, got {result}"
    
    print("\nStep 3: Testing no valid subarray...")
    arr3 = [1, 2, 3, 4, 5]
    result = SlidingWindowOperations.smallest_subarray_with_given_sum(arr3, 20)
    print(f"   smallest_subarray_with_given_sum([1, 2, 3, 4, 5], 20) = {result} (expected: 0)")
    assert result == 0, f"Expected 0, got {result}"
    
    print("\nStep 4: Testing single element meets requirement...")
    arr4 = [10, 2, 3]
    result = SlidingWindowOperations.smallest_subarray_with_given_sum(arr4, 10)
    print(f"   smallest_subarray_with_given_sum([10, 2, 3], 10) = {result} (expected: 1)")
    assert result == 1, f"Expected 1, got {result}"
    
    print("\nStep 5: Testing empty array...")
    arr5 = []
    result = SlidingWindowOperations.smallest_subarray_with_given_sum(arr5, 5)
    print(f"   smallest_subarray_with_given_sum([], 5) = {result} (expected: 0)")
    assert result == 0, f"Expected 0, got {result}"
    
    print("✓ smallest_subarray_with_given_sum tests passed")

def test_longest_substring_with_k_distinct():
    """Test longest_substring_with_k_distinct function"""
    print("Step 1: Testing normal case...")
    
    result = SlidingWindowOperations.longest_substring_with_k_distinct("araaci", 2)
    print(f"   longest_substring_with_k_distinct('araaci', 2) = {result} (expected: 4)")
    assert result == 4, f"Expected 4, got {result}"
    
    print("\nStep 2: Testing k equal to string length...")
    result = SlidingWindowOperations.longest_substring_with_k_distinct("abc", 3)
    print(f"   longest_substring_with_k_distinct('abc', 3) = {result} (expected: 3)")
    assert result == 3, f"Expected 3, got {result}"
    
    print("\nStep 3: Testing k greater than distinct characters...")
    result = SlidingWindowOperations.longest_substring_with_k_distinct("abc", 4)
    print(f"   longest_substring_with_k_distinct('abc', 4) = {result} (expected: 3)")
    assert result == 3, f"Expected 3, got {result}"
    
    print("\nStep 4: Testing all same characters...")
    result = SlidingWindowOperations.longest_substring_with_k_distinct("aaaaa", 1)
    print(f"   longest_substring_with_k_distinct('aaaaa', 1) = {result} (expected: 5)")
    assert result == 5, f"Expected 5, got {result}"
    
    print("\nStep 5: Testing k = 0...")
    result = SlidingWindowOperations.longest_substring_with_k_distinct("abc", 0)
    print(f"   longest_substring_with_k_distinct('abc', 0) = {result} (expected: 0)")
    assert result == 0, f"Expected 0, got {result}"
    
    print("\nStep 6: Testing empty string...")
    result = SlidingWindowOperations.longest_substring_with_k_distinct("", 2)
    print(f"   longest_substring_with_k_distinct('', 2) = {result} (expected: 0)")
    assert result == 0, f"Expected 0, got {result}"
    
    print("✓ longest_substring_with_k_distinct tests passed")

def test_fruits_into_baskets():
    """Test fruits_into_baskets function"""
    print("Step 1: Testing normal case...")
    
    result = SlidingWindowOperations.fruits_into_baskets("ABCAC")
    print(f"   fruits_into_baskets('ABCAC') = {result} (expected: 3)")
    assert result == 3, f"Expected 3, got {result}"
    
    print("\nStep 2: Testing all same fruits...")
    result = SlidingWindowOperations.fruits_into_baskets("AAAAA")
    print(f"   fruits_into_baskets('AAAAA') = {result} (expected: 5)")
    assert result == 5, f"Expected 5, got {result}"
    
    print("\nStep 3: Testing alternating fruits...")
    result = SlidingWindowOperations.fruits_into_baskets("ABABAB")
    print(f"   fruits_into_baskets('ABABAB') = {result} (expected: 6)")
    assert result == 6, f"Expected 6, got {result}"
    
    print("\nStep 4: Testing three different fruits...")
    result = SlidingWindowOperations.fruits_into_baskets("ABCBA")
    print(f"   fruits_into_baskets('ABCBA') = {result} (expected: 3)")
    assert result == 3, f"Expected 3, got {result}"
    
    print("\nStep 5: Testing empty array...")
    result = SlidingWindowOperations.fruits_into_baskets("")
    print(f"   fruits_into_baskets('') = {result} (expected: 0)")
    assert result == 0, f"Expected 0, got {result}"
    
    print("✓ fruits_into_baskets tests passed")

def test_longest_substring_without_repeating():
    """Test longest_substring_without_repeating function"""
    print("Step 1: Testing normal case...")
    
    result = SlidingWindowOperations.longest_substring_without_repeating("abcabcbb")
    print(f"   longest_substring_without_repeating('abcabcbb') = {result} (expected: 3)")
    assert result == 3, f"Expected 3, got {result}"
    
    print("\nStep 2: Testing all same characters...")
    result = SlidingWindowOperations.longest_substring_without_repeating("bbbbb")
    print(f"   longest_substring_without_repeating('bbbbb') = {result} (expected: 1)")
    assert result == 1, f"Expected 1, got {result}"
    
    print("\nStep 3: Testing no repeating characters...")
    result = SlidingWindowOperations.longest_substring_without_repeating("abcdef")
    print(f"   longest_substring_without_repeating('abcdef') = {result} (expected: 6)")
    assert result == 6, f"Expected 6, got {result}"
    
    print("\nStep 4: Testing empty string...")
    result = SlidingWindowOperations.longest_substring_without_repeating("")
    print(f"   longest_substring_without_repeating('') = {result} (expected: 0)")
    assert result == 0, f"Expected 0, got {result}"
    
    print("\nStep 5: Testing repeating pattern...")
    result = SlidingWindowOperations.longest_substring_without_repeating("pwwkew")
    print(f"   longest_substring_without_repeating('pwwkew') = {result} (expected: 3)")
    assert result == 3, f"Expected 3, got {result}"
    
    print("✓ longest_substring_without_repeating tests passed")

def test_find_all_anagrams():
    """Test find_all_anagrams function"""
    print("Step 1: Testing normal case...")
    
    result = SlidingWindowOperations.find_all_anagrams("cbaebabacd", "abc")
    print(f"   find_all_anagrams('cbaebabacd', 'abc') = {result} (expected: [0, 6])")
    assert result == [0, 6], f"Expected [0, 6], got {result}"
    
    print("\nStep 2: Testing pattern longer than string...")
    result = SlidingWindowOperations.find_all_anagrams("abc", "abcd")
    print(f"   find_all_anagrams('abc', 'abcd') = {result} (expected: [])")
    assert result == [], f"Expected [], got {result}"
    
    print("\nStep 3: Testing pattern equal to string...")
    result = SlidingWindowOperations.find_all_anagrams("abc", "abc")
    print(f"   find_all_anagrams('abc', 'abc') = {result} (expected: [0])")
    assert result == [0], f"Expected [0], got {result}"
    
    print("\nStep 4: Testing no anagrams...")
    result = SlidingWindowOperations.find_all_anagrams("hello", "world")
    print(f"   find_all_anagrams('hello', 'world') = {result} (expected: [])")
    assert result == [], f"Expected [], got {result}"
    
    print("\nStep 5: Testing empty string...")
    result = SlidingWindowOperations.find_all_anagrams("", "abc")
    print(f"   find_all_anagrams('', 'abc') = {result} (expected: [])")
    assert result == [], f"Expected [], got {result}"
    
    print("\nStep 6: Testing empty pattern...")
    result = SlidingWindowOperations.find_all_anagrams("abc", "")
    print(f"   find_all_anagrams('abc', '') = {result} (expected: [])")
    assert result == [], f"Expected [], got {result}"
    
    print("✓ find_all_anagrams tests passed")

def test_longest_repeating_character_replacement():
    """Test longest_repeating_character_replacement function"""
    print("Step 1: Testing normal case...")
    
    result = SlidingWindowOperations.longest_repeating_character_replacement("AABABBA", 1)
    print(f"   longest_repeating_character_replacement('AABABBA', 1) = {result} (expected: 4)")
    assert result == 4, f"Expected 4, got {result}"
    
    print("\nStep 2: Testing k = 0 (no replacements)...")
    result = SlidingWindowOperations.longest_repeating_character_replacement("ABCDE", 0)
    print(f"   longest_repeating_character_replacement('ABCDE', 0) = {result} (expected: 1)")
    assert result == 1, f"Expected 1, got {result}"
    
    print("\nStep 3: Testing k equal to string length...")
    result = SlidingWindowOperations.longest_repeating_character_replacement("ABCDE", 5)
    print(f"   longest_repeating_character_replacement('ABCDE', 5) = {result} (expected: 5)")
    assert result == 5, f"Expected 5, got {result}"
    
    print("\nStep 4: Testing all same characters...")
    result = SlidingWindowOperations.longest_repeating_character_replacement("AAAAA", 2)
    print(f"   longest_repeating_character_replacement('AAAAA', 2) = {result} (expected: 5)")
    assert result == 5, f"Expected 5, got {result}"
    
    print("\nStep 5: Testing empty string...")
    result = SlidingWindowOperations.longest_repeating_character_replacement("", 2)
    print(f"   longest_repeating_character_replacement('', 2) = {result} (expected: 0)")
    assert result == 0, f"Expected 0, got {result}"
    
    print("✓ longest_repeating_character_replacement tests passed")

def test_min_window():
    """Test min_window function"""
    print("Step 1: Testing normal case...")
    
    result = SlidingWindowOperations.min_window("ADOBECODEBANC", "ABC")
    print(f"   min_window('ADOBECODEBANC', 'ABC') = '{result}' (expected: 'BANC')")
    assert result == "BANC", f"Expected 'BANC', got '{result}'"
    
    print("\nStep 2: Testing no valid window...")
    result = SlidingWindowOperations.min_window("a", "aa")
    print(f"   min_window('a', 'aa') = '{result}' (expected: '')")
    assert result == "", f"Expected '', got '{result}'"
    
    print("\nStep 3: Testing pattern equal to string...")
    result = SlidingWindowOperations.min_window("abc", "abc")
    print(f"   min_window('abc', 'abc') = '{result}' (expected: 'abc')")
    assert result == "abc", f"Expected 'abc', got '{result}'"
    
    print("\nStep 4: Testing pattern longer than string...")
    result = SlidingWindowOperations.min_window("ab", "abc")
    print(f"   min_window('ab', 'abc') = '{result}' (expected: '')")
    assert result == "", f"Expected '', got '{result}'"
    
    print("\nStep 5: Testing duplicate characters in pattern...")
    result = SlidingWindowOperations.min_window("aa", "aa")
    print(f"   min_window('aa', 'aa') = '{result}' (expected: 'aa')")
    assert result == "aa", f"Expected 'aa', got '{result}'"
    
    print("\nStep 6: Testing empty strings...")
    result = SlidingWindowOperations.min_window("", "abc")
    print(f"   min_window('', 'abc') = '{result}' (expected: '')")
    assert result == "", f"Expected '', got '{result}'"
    
    print("✓ min_window tests passed")

def test_max_sliding_window():
    """Test max_sliding_window function"""
    print("Step 1: Testing normal case...")
    
    result = SlidingWindowOperations.max_sliding_window([1,3,-1,-3,5,3,6,7], 3)
    print(f"   max_sliding_window([1,3,-1,-3,5,3,6,7], 3) = {result} (expected: [3,3,5,5,6,7])")
    assert result == [3,3,5,5,6,7], f"Expected [3,3,5,5,6,7], got {result}"
    
    print("\nStep 2: Testing k = 1...")
    result = SlidingWindowOperations.max_sliding_window([1,2,3,4,5], 1)
    print(f"   max_sliding_window([1,2,3,4,5], 1) = {result} (expected: [1,2,3,4,5])")
    assert result == [1,2,3,4,5], f"Expected [1,2,3,4,5], got {result}"
    
    print("\nStep 3: Testing k equal to array length...")
    result = SlidingWindowOperations.max_sliding_window([1,2,3,4,5], 5)
    print(f"   max_sliding_window([1,2,3,4,5], 5) = {result} (expected: [5])")
    assert result == [5], f"Expected [5], got {result}"
    
    print("\nStep 4: Testing negative numbers...")
    result = SlidingWindowOperations.max_sliding_window([-1,-2,-3,-4], 2)
    print(f"   max_sliding_window([-1,-2,-3,-4], 2) = {result} (expected: [-1,-2,-3])")
    assert result == [-1,-2,-3], f"Expected [-1,-2,-3], got {result}"
    
    print("\nStep 5: Testing all same elements...")
    result = SlidingWindowOperations.max_sliding_window([1,1,1,1], 2)
    print(f"   max_sliding_window([1,1,1,1], 2) = {result} (expected: [1,1,1])")
    assert result == [1,1,1], f"Expected [1,1,1], got {result}"
    
    print("\nStep 6: Testing empty array...")
    result = SlidingWindowOperations.max_sliding_window([], 3)
    print(f"   max_sliding_window([], 3) = {result} (expected: [])")
    assert result == [], f"Expected [], got {result}"
    
    print("✓ max_sliding_window tests passed")

def test_check_inclusion():
    """Test check_inclusion function"""
    print("Step 1: Testing permutation exists...")
    
    result = SlidingWindowOperations.check_inclusion("ab", "eidbaooo")
    print(f"   check_inclusion('ab', 'eidbaooo') = {result} (expected: True)")
    assert result == True, f"Expected True, got {result}"
    
    print("\nStep 2: Testing permutation doesn't exist...")
    result = SlidingWindowOperations.check_inclusion("ab", "eidboaoo")
    print(f"   check_inclusion('ab', 'eidboaoo') = {result} (expected: False)")
    assert result == False, f"Expected False, got {result}"
    
    print("\nStep 3: Testing pattern equal to substring...")
    result = SlidingWindowOperations.check_inclusion("abc", "abc")
    print(f"   check_inclusion('abc', 'abc') = {result} (expected: True)")
    assert result == True, f"Expected True, got {result}"
    
    print("\nStep 4: Testing pattern longer than string...")
    result = SlidingWindowOperations.check_inclusion("abcd", "abc")
    print(f"   check_inclusion('abcd', 'abc') = {result} (expected: False)")
    assert result == False, f"Expected False, got {result}"
    
    print("\nStep 5: Testing duplicate characters in pattern...")
    result = SlidingWindowOperations.check_inclusion("aab", "bbaac")
    print(f"   check_inclusion('aab', 'bbaac') = {result} (expected: True)")
    assert result == True, f"Expected True, got {result}"
    
    result = SlidingWindowOperations.check_inclusion("aab", "bbac")
    print(f"   check_inclusion('aab', 'bbac') = {result} (expected: False)")
    assert result == False, f"Expected False, got {result}"
    
    print("\nStep 6: Testing single character...")
    result = SlidingWindowOperations.check_inclusion("a", "ab")
    print(f"   check_inclusion('a', 'ab') = {result} (expected: True)")
    assert result == True, f"Expected True, got {result}"
    
    print("\nStep 7: Testing empty strings...")
    result = SlidingWindowOperations.check_inclusion("", "abc")
    print(f"   check_inclusion('', 'abc') = {result} (expected: False)")
    assert result == False, f"Expected False, got {result}"
    
    print("✓ check_inclusion tests passed")

def run_all_tests():
    """Run all test functions with detailed reporting"""
    print("🚀 STARTING COMPREHENSIVE SLIDING WINDOW TESTS")
    print("="*70)
    
    tests = [
        ("Max Sum Subarray of Size K", test_max_sum_subarray_of_size_k),
        ("Smallest Subarray with Given Sum", test_smallest_subarray_with_given_sum),
        ("Longest Substring with K Distinct", test_longest_substring_with_k_distinct),
        ("Fruits into Baskets", test_fruits_into_baskets),
        ("Longest Substring Without Repeating", test_longest_substring_without_repeating),
        ("Find All Anagrams", test_find_all_anagrams),
        ("Longest Repeating Character Replacement", test_longest_repeating_character_replacement),
        ("Minimum Window Substring", test_min_window),
        ("Max Sliding Window", test_max_sliding_window),
        ("Check Inclusion (Permutation in String)", test_check_inclusion),
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
