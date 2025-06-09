import sys
import os
import argparse
import traceback
import time

def setup_imports():
    """Set up imports based on the command-line argument."""
    parser = argparse.ArgumentParser(description='Test 1-D Dynamic Programming operations')
    parser.add_argument('--mode', choices=['solution', 'practice'], default='solution',
                      help='Which implementation to test (solution or practice)')
    args = parser.parse_args()

    # Get the current directory and project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))

    if args.mode == 'solution':
        # Import from Solutions
        solutions_dir = os.path.join(project_root, 'Solutions', 'DynamicProgramming')
        sys.path.insert(0, solutions_dir)
        print(f"Testing solution implementation from: {solutions_dir}")
    else:
        # Import from Practice
        practice_dir = os.path.join(project_root, 'Practice', 'DynamicProgramming')
        sys.path.insert(0, practice_dir)
        print(f"Testing practice implementation from: {practice_dir}")

# Setup the path and import
setup_imports()

try:
    from dp1_operations import DP1Operations
except ImportError as e:
    print(f"❌ Could not import DP1Operations: {e}")
    print("Make sure the file exists in Solutions/DP/ or Practice/DP/")
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

def test_fibonacci():
    """Test Fibonacci number calculation"""
    print("Step 1: Testing basic Fibonacci numbers...")

    # Test small values
    assert DP1Operations.fibonacci(0) == 0, f"F(0) should be 0"
    assert DP1Operations.fibonacci(1) == 1, f"F(1) should be 1"
    assert DP1Operations.fibonacci(2) == 1, f"F(2) should be 1"
    assert DP1Operations.fibonacci(3) == 2, f"F(3) should be 2"
    assert DP1Operations.fibonacci(4) == 3, f"F(4) should be 3"
    assert DP1Operations.fibonacci(5) == 5, f"F(5) should be 5"
    print(f"   Basic values: F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3, F(5)=5 ✓")

    print("\nStep 2: Testing larger Fibonacci numbers...")
    assert DP1Operations.fibonacci(10) == 55, f"F(10) should be 55"
    assert DP1Operations.fibonacci(15) == 610, f"F(15) should be 610"
    assert DP1Operations.fibonacci(20) == 6765, f"F(20) should be 6765"
    print(f"   Larger values: F(10)=55, F(15)=610, F(20)=6765 ✓")

    print("\nStep 3: Testing edge cases...")
    # Test performance for moderately large values
    start_time = time.time()
    result = DP1Operations.fibonacci(100)
    end_time = time.time()
    expected_f100 = 354224848179261915075  # F(100)
    assert result == expected_f100, f"F(100) should be {expected_f100}"
    print(f"   F(100) = {result} computed in {end_time - start_time:.4f} seconds ✓")

    print("✓ fibonacci tests passed")

def test_climbing_stairs():
    """Test climbing stairs problem"""
    print("Step 1: Testing basic stair combinations...")

    assert DP1Operations.climbing_stairs(1) == 1, f"1 stair should have 1 way"
    assert DP1Operations.climbing_stairs(2) == 2, f"2 stairs should have 2 ways"
    assert DP1Operations.climbing_stairs(3) == 3, f"3 stairs should have 3 ways"
    assert DP1Operations.climbing_stairs(4) == 5, f"4 stairs should have 5 ways"
    assert DP1Operations.climbing_stairs(5) == 8, f"5 stairs should have 8 ways"
    print(f"   Basic stairs: 1→1, 2→2, 3→3, 4→5, 5→8 ways ✓")

    print("\nStep 2: Testing larger values...")
    assert DP1Operations.climbing_stairs(10) == 89, f"10 stairs should have 89 ways"
    assert DP1Operations.climbing_stairs(15) == 987, f"15 stairs should have 987 ways"
    print(f"   Larger values: 10→89, 15→987 ways ✓")

    print("\nStep 3: Verifying Fibonacci relationship...")
    # climbing_stairs(n) = fibonacci(n+1)
    for n in range(1, 10):
        stairs_result = DP1Operations.climbing_stairs(n)
        fib_result = DP1Operations.fibonacci(n + 1)
        assert stairs_result == fib_result, f"climbing_stairs({n}) should equal fibonacci({n+1})"
    print(f"   Fibonacci relationship verified: climbing_stairs(n) = fibonacci(n+1) ✓")

    print("✓ climbing_stairs tests passed")

def test_house_robber():
    """Test house robber problem"""
    print("Step 1: Testing basic robbery scenarios...")

    # Simple cases
    assert DP1Operations.house_robber([1, 2, 3, 1]) == 4, f"[1,2,3,1] should yield 4"
    assert DP1Operations.house_robber([2, 7, 9, 3, 1]) == 12, f"[2,7,9,3,1] should yield 12"
    print(f"   Basic cases: [1,2,3,1]→4, [2,7,9,3,1]→12 ✓")

    print("\nStep 2: Testing edge cases...")
    assert DP1Operations.house_robber([]) == 0, f"Empty array should yield 0"
    assert DP1Operations.house_robber([5]) == 5, f"Single house should yield its value"
    assert DP1Operations.house_robber([1, 2]) == 2, f"Two houses should yield max value"
    assert DP1Operations.house_robber([2, 1]) == 2, f"Two houses should yield max value"
    print(f"   Edge cases: []→0, [5]→5, [1,2]→2, [2,1]→2 ✓")

    print("\nStep 3: Testing larger scenarios...")
    assert DP1Operations.house_robber([5, 1, 3, 9]) == 14, f"[5,1,3,9] should yield 14 (5+9)"
    assert DP1Operations.house_robber([2, 4, 1, 9, 2, 3]) == 16, f"Should yield 16"
    print(f"   Larger cases: [5,1,3,9]→14, [2,4,1,9,2,3]→16 ✓")

    print("\nStep 4: Testing alternating patterns...")
    # All even indices vs all odd indices
    houses = [10, 1, 20, 2, 30, 3, 40, 4]
    result = DP1Operations.house_robber(houses)
    # Optimal: rob indices 0,2,4,6 → 10+20+30+40 = 100
    assert result == 100, f"Alternating pattern should yield 100"
    print(f"   Alternating pattern: [10,1,20,2,30,3,40,4]→100 ✓")

    print("✓ house_robber tests passed")

def test_coin_change():
    """Test coin change problem"""
    print("Step 1: Testing basic coin combinations...")

    assert DP1Operations.coin_change([1, 3, 4], 6) == 2, f"[1,3,4] for amount 6 should need 2 coins"
    assert DP1Operations.coin_change([2], 3) == -1, f"[2] for amount 3 should be impossible"
    assert DP1Operations.coin_change([1], 0) == 0, f"Any coins for amount 0 should need 0 coins"
    print(f"   Basic cases: [1,3,4]→6 needs 2, [2]→3 impossible, [1]→0 needs 0 ✓")

    print("\nStep 2: Testing standard denominations...")
    assert DP1Operations.coin_change([1, 5, 10, 25], 30) == 2, f"Standard coins for 30 should need 2"
    assert DP1Operations.coin_change([1, 5, 10, 25], 67) == 6, f"Standard coins for 67 should need 6"
    print(f"   Standard denominations: 30→2 coins, 67→6 coins ✓")

    print("\nStep 3: Testing edge cases...")
    assert DP1Operations.coin_change([1], 1) == 1, f"Single coin for amount 1 should need 1"
    assert DP1Operations.coin_change([1], 10) == 10, f"Only 1-coins for amount 10 should need 10"
    assert DP1Operations.coin_change([5, 10], 3) == -1, f"No small coins for amount 3 should be impossible"
    print(f"   Edge cases: [1]→1 needs 1, [1]→10 needs 10, [5,10]→3 impossible ✓")

    print("\nStep 4: Testing greedy vs optimal...")
    # Greedy would pick [4,1,1] = 3 coins, but optimal is [3,3] = 2 coins
    assert DP1Operations.coin_change([1, 3, 4], 6) == 2, f"Greedy trap case should find optimal"
    assert DP1Operations.coin_change([1, 4, 5], 8) == 2, f"Another greedy trap should find optimal"
    print(f"   Greedy vs optimal: DP finds better solutions than greedy ✓")

    print("✓ coin_change tests passed")

def test_longest_increasing_subsequence():
    """Test longest increasing subsequence"""
    print("Step 1: Testing basic LIS cases...")

    assert DP1Operations.longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert DP1Operations.longest_increasing_subsequence([0, 1, 0, 3, 2, 3]) == 4
    assert DP1Operations.longest_increasing_subsequence([7, 7, 7, 7, 7]) == 1
    print(f"   Basic cases: [10,9,2,5,3,7,101,18]→4, [0,1,0,3,2,3]→4, [7,7,7,7,7]→1 ✓")

    print("\nStep 2: Testing edge cases...")
    assert DP1Operations.longest_increasing_subsequence([]) == 0, f"Empty array should return 0"
    assert DP1Operations.longest_increasing_subsequence([1]) == 1, f"Single element should return 1"
    assert DP1Operations.longest_increasing_subsequence([1, 2, 3, 4, 5]) == 5, f"Sorted array should return length"
    assert DP1Operations.longest_increasing_subsequence([5, 4, 3, 2, 1]) == 1, f"Reverse sorted should return 1"
    print(f"   Edge cases: []→0, [1]→1, [1,2,3,4,5]→5, [5,4,3,2,1]→1 ✓")

    print("\nStep 3: Testing mixed patterns...")
    assert DP1Operations.longest_increasing_subsequence([1, 3, 2, 4]) == 3, f"[1,3,2,4] should have LIS length 3"
    assert DP1Operations.longest_increasing_subsequence([4, 10, 4, 3, 8, 9]) == 3, f"Should find length 3"
    print(f"   Mixed patterns: [1,3,2,4]→3, [4,10,4,3,8,9]→3 ✓")

    print("\nStep 4: Testing longer sequences...")
    # Test a longer sequence with known LIS
    long_seq = [1, 12, 7, 0, 23, 11, 52, 31, 61, 69, 70, 2]
    result = DP1Operations.longest_increasing_subsequence(long_seq)
    # One possible LIS: [1, 7, 11, 31, 61, 69, 70] = length 7
    assert result == 7, f"Long sequence should have LIS length 7"
    print(f"   Longer sequence: length 12 array has LIS of length 7 ✓")

    print("✓ longest_increasing_subsequence tests passed")

def test_word_break():
    """Test word break problem"""
    print("Step 1: Testing basic word segmentation...")

    assert DP1Operations.word_break("leetcode", ["leet", "code"]) == True
    assert DP1Operations.word_break("applepenapple", ["apple", "pen"]) == True
    assert DP1Operations.word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    print(f"   Basic cases: 'leetcode'→True, 'applepenapple'→True, 'catsandog'→False ✓")

    print("\nStep 2: Testing edge cases...")
    assert DP1Operations.word_break("", ["a"]) == True, f"Empty string should be segmentable"
    assert DP1Operations.word_break("a", ["a"]) == True, f"Single char match should work"
    assert DP1Operations.word_break("a", ["b"]) == False, f"Single char no match should fail"
    assert DP1Operations.word_break("ab", ["a", "b"]) == True, f"Two single chars should work"
    print(f"   Edge cases: ''→True, 'a'/'a'→True, 'a'/'b'→False, 'ab'/['a','b']→True ✓")

    print("\nStep 3: Testing word reuse...")
    assert DP1Operations.word_break("aaaaaaa", ["aaaa", "aaa"]) == True, f"Should reuse words"
    assert DP1Operations.word_break("aaaaaaa", ["aaaa", "aa"]) == False, f"Should handle impossible reuse"
    print(f"   Word reuse: 'aaaaaaa' with different dictionaries ✓")

    print("\nStep 4: Testing overlapping words...")
    assert DP1Operations.word_break("abcd", ["a", "abc", "b", "cd"]) == True, f"Should handle overlapping"
    assert DP1Operations.word_break("cars", ["car", "ca", "rs"]) == True, f"Multiple segmentation paths"
    print(f"   Overlapping words: multiple valid segmentation paths ✓")

    print("\nStep 5: Testing longer strings...")
    long_string = "programming"
    word_dict = ["pro", "gram", "ming", "program"]
    assert DP1Operations.word_break(long_string, word_dict) == True, f"Should segment 'programming'"
    print(f"   Longer strings: 'programming' successfully segmented ✓")

    print("✓ word_break tests passed")

def test_buy_sell_stock1():
    """Test single buy/sell stock transaction"""
    print("Step 1: Testing basic stock transactions...")

    assert DP1Operations.buy_sell_stock1([7, 1, 5, 3, 6, 4]) == 5
    assert DP1Operations.buy_sell_stock1([7, 6, 4, 3, 1]) == 0
    print(f"   Basic cases: [7,1,5,3,6,4]→5, [7,6,4,3,1]→0 ✓")

    print("\nStep 2: Testing edge cases...")
    assert DP1Operations.buy_sell_stock1([]) == 0, f"Empty prices should return 0"
    assert DP1Operations.buy_sell_stock1([1]) == 0, f"Single price should return 0"
    assert DP1Operations.buy_sell_stock1([1, 2]) == 1, f"Two prices should return difference"
    assert DP1Operations.buy_sell_stock1([2, 1]) == 0, f"Decreasing prices should return 0"
    print(f"   Edge cases: []→0, [1]→0, [1,2]→1, [2,1]→0 ✓")

    print("\nStep 3: Testing optimal timing...")
    assert DP1Operations.buy_sell_stock1([1, 2, 3, 4, 5]) == 4, f"Increasing prices: buy first, sell last"
    assert DP1Operations.buy_sell_stock1([5, 4, 3, 2, 1]) == 0, f"Decreasing prices: no profit"
    assert DP1Operations.buy_sell_stock1([3, 3, 3, 3, 3]) == 0, f"Flat prices: no profit"
    print(f"   Optimal timing: [1,2,3,4,5]→4, [5,4,3,2,1]→0, [3,3,3,3,3]→0 ✓")

    print("\nStep 4: Testing complex patterns...")
    assert DP1Operations.buy_sell_stock1([2, 4, 1, 9]) == 8, f"Should buy at 1, sell at 9"
    assert DP1Operations.buy_sell_stock1([6, 1, 3, 2, 4, 7]) == 6, f"Should buy at 1, sell at 7"
    print(f"   Complex patterns: [2,4,1,9]→8, [6,1,3,2,4,7]→6 ✓")

    print("✓ buy_sell_stock1 tests passed")

def test_buy_sell_stock2():
    """Test multiple buy/sell stock transactions"""
    print("Step 1: Testing basic multiple transactions...")

    assert DP1Operations.buy_sell_stock2([7, 1, 5, 3, 6, 4]) == 7
    assert DP1Operations.buy_sell_stock2([1, 2, 3, 4, 5]) == 4
    assert DP1Operations.buy_sell_stock2([7, 6, 4, 3, 1]) == 0
    print(f"   Basic cases: [7,1,5,3,6,4]→7, [1,2,3,4,5]→4, [7,6,4,3,1]→0 ✓")

    print("\nStep 2: Testing edge cases...")
    assert DP1Operations.buy_sell_stock2([]) == 0, f"Empty prices should return 0"
    assert DP1Operations.buy_sell_stock2([1]) == 0, f"Single price should return 0"
    assert DP1Operations.buy_sell_stock2([1, 2]) == 1, f"Two prices should return difference"
    print(f"   Edge cases: []→0, [1]→0, [1,2]→1 ✓")

    print("\nStep 3: Testing vs single transaction...")
    # Compare with single transaction results
    prices1 = [7, 1, 5, 3, 6, 4]
    single = DP1Operations.buy_sell_stock1(prices1)  # Should be 5
    multiple = DP1Operations.buy_sell_stock2(prices1)  # Should be 7
    assert multiple >= single, f"Multiple transactions should be at least as good as single"
    assert multiple == 7 and single == 5, f"Multiple should be better: {multiple} vs {single}"
    print(f"   Multiple vs single: {multiple} >= {single} ✓")

    print("\nStep 4: Testing optimal strategy...")
    # Test case where multiple small transactions beat one large transaction
    prices = [1, 2, 1, 2, 1, 2]
    result = DP1Operations.buy_sell_stock2(prices)
    # Optimal: buy at each 1, sell at each 2 → 3 transactions of profit 1 each = 3
    assert result == 3, f"Should make 3 small transactions for profit 3"
    print(f"   Optimal strategy: [1,2,1,2,1,2]→3 (multiple small transactions) ✓")

    print("✓ buy_sell_stock2 tests passed")

def test_longest_palindromic_substring():
    """Test longest palindromic substring"""
    print("Step 1: Testing basic palindromes...")

    result1 = DP1Operations.longest_palindromic_substring("babad")
    assert result1 in ["bab", "aba"], f"'babad' should return 'bab' or 'aba', got '{result1}'"

    result2 = DP1Operations.longest_palindromic_substring("cbbd")
    assert result2 == "bb", f"'cbbd' should return 'bb', got '{result2}'"

    print(f"   Basic cases: 'babad'→'{result1}', 'cbbd'→'{result2}' ✓")

    print("\nStep 2: Testing edge cases...")
    assert DP1Operations.longest_palindromic_substring("") == "", f"Empty string should return empty"
    assert DP1Operations.longest_palindromic_substring("a") == "a", f"Single char should return itself"
    assert DP1Operations.longest_palindromic_substring("ac") == "a", f"Two different chars should return first"
    assert DP1Operations.longest_palindromic_substring("aa") == "aa", f"Two same chars should return both"
    print(f"   Edge cases: ''→'', 'a'→'a', 'ac'→'a', 'aa'→'aa' ✓")

    print("\nStep 3: Testing full palindromes...")
    assert DP1Operations.longest_palindromic_substring("racecar") == "racecar", f"Full palindrome should return itself"
    assert DP1Operations.longest_palindromic_substring("abccba") == "abccba", f"Even-length full palindrome"
    print(f"   Full palindromes: 'racecar'→'racecar', 'abccba'→'abccba' ✓")

    print("\nStep 4: Testing mixed cases...")
    result3 = DP1Operations.longest_palindromic_substring("abacabad")
    # Possible longest palindromes: "aba", "aca", "aba" (length 3)
    assert len(result3) == 7 and result3 == 'abacaba', f"Should find palindrome of length 7"

    result4 = DP1Operations.longest_palindromic_substring("bananas")
    # "anan" is longest with length 4
    assert result4 == "anana", f"'bananas' should return 'anana', got '{result4}'"
    print(f"   Mixed cases: 'abacabad'→'{result3}', 'bananas'→'{result4}' ✓")

    print("\nStep 5: Testing longer strings...")
    long_palindrome = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"
    result5 = DP1Operations.longest_palindromic_substring(long_palindrome)
    # The entire string is a palindrome
    assert result5 == long_palindrome, f"Long palindrome should return entire string"
    print(f"   Long string: found palindrome of length {len(result5)} ✓")

    print("✓ longest_palindromic_substring tests passed")

def test_performance():
    """Test performance characteristics"""
    print("Step 1: Testing algorithmic efficiency...")

    # Test Fibonacci performance
    start_time = time.time()
    DP1Operations.fibonacci(1000)
    fib_time = time.time() - start_time
    assert fib_time < 0.1, f"Fibonacci(1000) should be fast, took {fib_time:.4f}s"
    print(f"   Fibonacci(1000): {fib_time:.4f}s ✓")

    # Test Coin Change performance
    start_time = time.time()
    DP1Operations.coin_change([1, 3, 4], 1000)
    coin_time = time.time() - start_time
    assert coin_time < 0.5, f"Coin change for amount 1000 should be fast, took {coin_time:.4f}s"
    print(f"   Coin change (amount=1000): {coin_time:.4f}s ✓")

    # Test LIS performance
    start_time = time.time()
    large_array = list(range(1000, 0, -1))  # Worst case: decreasing array
    DP1Operations.longest_increasing_subsequence(large_array)
    lis_time = time.time() - start_time
    assert lis_time < 2.0, f"LIS on 1000 elements should be reasonable, took {lis_time:.4f}s"
    print(f"   LIS (1000 elements): {lis_time:.4f}s ✓")

    print("✓ performance tests passed")

def test_edge_cases():
    """Test edge cases and boundary conditions"""
    print("Step 1: Testing empty inputs...")

    # Functions that should handle empty inputs gracefully
    assert DP1Operations.house_robber([]) == 0, f"Empty house array should return 0"
    assert DP1Operations.longest_increasing_subsequence([]) == 0, f"Empty LIS array should return 0"
    assert DP1Operations.buy_sell_stock1([]) == 0, f"Empty stock prices should return 0"
    assert DP1Operations.buy_sell_stock2([]) == 0, f"Empty stock prices should return 0"
    assert DP1Operations.word_break("", ["word"]) == True, f"Empty string should be segmentable"
    assert DP1Operations.longest_palindromic_substring("") == "", f"Empty string palindrome should be empty"
    print(f"   Empty inputs handled correctly ✓")

    print("\nStep 2: Testing single element inputs...")
    assert DP1Operations.fibonacci(0) == 0, f"F(0) edge case"
    assert DP1Operations.climbing_stairs(1) == 1, f"Single stair should have 1 way"
    assert DP1Operations.house_robber([42]) == 42, f"Single house should return its value"
    assert DP1Operations.longest_increasing_subsequence([5]) == 1, f"Single element LIS should be 1"
    assert DP1Operations.buy_sell_stock1([10]) == 0, f"Single stock price should return 0"
    assert DP1Operations.longest_palindromic_substring("x") == "x", f"Single char palindrome"
    print(f"   Single element inputs handled correctly ✓")

    print("\nStep 3: Testing boundary values...")
    # Test with minimum and maximum reasonable values
    assert DP1Operations.coin_change([1], 0) == 0, f"Amount 0 should need 0 coins"
    assert DP1Operations.coin_change([1000000], 1) == -1, f"Large coin for small amount should be impossible"
    assert DP1Operations.word_break("a", []) == False, f"Empty dictionary should make segmentation impossible"
    print(f"   Boundary values handled correctly ✓")

    print("\nStep 4: Testing identical elements...")
    # Arrays with all same elements
    assert DP1Operations.house_robber([5, 5, 5, 5]) == 10, f"Identical houses should rob alternating"
    assert DP1Operations.longest_increasing_subsequence([3, 3, 3]) == 1, f"All same should have LIS 1"
    assert DP1Operations.buy_sell_stock2([4, 4, 4, 4]) == 0, f"Flat prices should yield 0 profit"
    print(f"   Identical elements handled correctly ✓")

    print("✓ edge_cases tests passed")

def run_all_tests():
    """Run all test functions with detailed reporting"""
    print("🚀 STARTING COMPREHENSIVE 1-D DYNAMIC PROGRAMMING TESTS")
    print("="*70)

    tests = [
        ("Fibonacci", test_fibonacci),
        ("Climbing Stairs", test_climbing_stairs),
        ("House Robber", test_house_robber),
        ("Coin Change", test_coin_change),
        ("Longest Increasing Subsequence", test_longest_increasing_subsequence),
        ("Word Break", test_word_break),
        ("Buy/Sell Stock I", test_buy_sell_stock1),
        ("Buy/Sell Stock II", test_buy_sell_stock2),
        ("Longest Palindromic Substring", test_longest_palindromic_substring),
        ("Performance Tests", test_performance),
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
        print("\n🎉 ALL TESTS PASSED! Your 1-D DP implementation is working correctly!")
        print("\n🔥 KEY DP CONCEPTS VALIDATED:")
        print("   • Fibonacci-style patterns (Fibonacci, Climbing Stairs)")
        print("   • Decision problems (House Robber, Word Break)")
        print("   • Optimization problems (Coin Change, LIS)")
        print("   • State machine DP (Stock problems)")
        print("   • Range DP (Longest Palindromic Substring)")
        print("   • Space and time complexity optimizations")
        print("   • Edge case handling and boundary conditions")
        print("\n💡 PATTERNS MASTERED:")
        print("   🎯 STATE: Clearly defined what dp[i] represents")
        print("   🎯 TRANSITION: Proper recurrence relations")
        print("   🎯 BASE CASE: Correct initialization")
        print("   🎯 TABULATION: Bottom-up iterative solutions")
        print("   🎯 OPTIMIZATION: Space complexity improvements")
    else:
        print("\n🔧 Some tests failed. Check the detailed output above to fix the issues.")
        print("\n💡 DEBUGGING TIPS:")
        print("   • Verify STATE definition matches what you're computing")
        print("   • Check TRANSITION logic covers all cases correctly")
        print("   • Ensure BASE CASES handle edge inputs properly")
        print("   • Test with simple examples by hand first")
        print("   • Verify array bounds and initialization")
        print("   • Check for off-by-one errors in indices")

    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
