class HashMapSetOperations:
    ''' Common hashmap and set operations and patterns for interviews '''

    @staticmethod
    def two_sum(nums, target):  # Note: two_sum not two_sums
        '''
            Find two numbers in the array that add up to the target value.
            
            Args:
                nums: list of integers
                target: target sum value
            Returns:
                list of two indices whose values sum to target, or empty list if no solution
            
            Q) What is the time and space complexity?
                a) O(n) time complexity - single pass through the array
                a) O(n) space complexity - hash map can store up to n elements
            Q) What are the key-value mappings in the seen dictionary?
                a) Key is the number value, value is its index in the array
            Q) Why do we calculate complement first before checking if it exists?
                a) We need to find if there's already a number that, when added to current number, equals target
            Q) Why don't we store the current number in the hash map before checking for complement?
                a) We want to avoid using the same element twice (same index)
            Q) Why do we use enumerate instead of a for loop?
                a) Enumerate is iterative just like a for loop, but it keeps track of the item's index while iterating (idx, item)
            
            Example Walkthrough) nums = [2, 7, 11, 15], target = 9
                1. Initialize seen = {}
                2. i=0, num=2:
                    - complement = 9 - 2 = 7
                    - 7 not in seen
                    - seen = {2: 0}
                3. i=1, num=7:
                    - complement = 9 - 7 = 2
                    - 2 is in seen at index 0
                    - return [0, 1]
        '''
        seen = {}  # Fixed indentation
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i 
        return [] 

    @staticmethod
    def contains_duplicate(nums):
        '''
            Check if any value appears at least twice in the array

            Args: 
                nums: list of integers
            
            Returns:
                True if duplicates exist, false otherwise
            
            Q) What is the time and space complexity?
                a) O(n) time complexity, single pass through the array
                a) O(n) space complexity, store n unique elements 
            Q) Why is using a set more efficient than nested loop?
                a) Set lookup is O(1) time complexity, vs average case of O(n) for scanning the remaining array 
            Q) What happens when we try to add a duplicate value to the set?
                a) The set remains unchanged since only unique values are stored
            Q) What are the two major ways to initialize an empty set?
                a) {} and set()...{} creates an empty dictionary but in Python 3 support was added so that python can determine dict/set based on what is added to it 
            Example Walkthrough) nums = [1, 2, 3, 1]
                1. Initialize seen = set()
                2. num = 1
                    - 1 not in seen, seen = {1}
                3. num = 2
                    - 2 not in seen, seen = {1, 2}
                4. num = 3
                    - 3 not in seen, seen = {1, 2, 3}
                5. num = 1
                    - 1 in seen, return true 
        '''

        seen = set()
        for i in nums:
            if i in seen:
                return True 
            seen.add(i)

        return False 


    @staticmethod 
    def find_all_duplicates(nums):
        '''
            Find all elements that appear more than once in the array

            Args:
                nums: list of integers

            Returns:
                a list of all duplicate numbers

            Q) What is the time and space complexity?
                a) O(n) time complexity, single pass through array
                b) O(n) frequency map and result list 
            Q) How do we differentiate between first occurrences and duplicates?
                a) Track frequency count, when count becomes 2 it is the first duplicate occurrences
            Q) What does .get() do? How does it handle unseen values in this case?
                a) .get() operates similar to an in-else statement such that if a key already exists within the dict, return its value. else, initialize the value to 0 (adding 1 here for first seen) 
            Example Walkthrough) nums = [4, 3, 2, 7, 8, 2, 3, 1]
                1. initialize freq = {}, duplicates = []
                2. num = 4
                    - freq = { 4:1 }
                    - duplicates = []
                3. num = 3
                    - freq = { 4:1, 3:1 }
                    - duplicates = []
                4. num = 2
                    - freq = { 4:1, 3:1, 2:1 }
                    - duplicates = []
                5. num = 7
                    - freq = { 4:1, 3:1, 2:1, 7:1 }
                    - duplicates = []
                6. num = 8
                    - freq = { 4:1, 3:1, 2:1, 7:1, 8:1 }
                    - duplicates = []
                7. num = 2
                    - freq = { 4:1, 3:1, 2:2, 7:1, 8:1 }
                    - duplicates = [2]
                8. num = 3
                    - freq = { 4:1, 3:2, 2:2, 7:1, 8:1 }
                    - duplicatves = [2, 3]
                9. num = 1
                    - freq = { 4:1, 3:2, 2:2, 7:1, 8:1, 1:1 }
                    - duplicates = [2, 3]
                10. return [2, 3]
        '''
        
        freq = {}
        duplicates = []

        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            if freq[i] == 2:
                duplicates.append(i)

        return duplicates

    

    @staticmethod
    def intersection_of_arrays(nums1, nums2):
        '''
            Find the intersion of two arrays (common elements)

            Args:
                nums1: first array
                nums2: second array 

            Returns:
                a list of common elements present in both arrays

            Q) What is the time and space complexity?
                a) O(n + m) time complexity, where n and m are the length of the arrays 
                b) O(min(n, m)) space complexity, storing the smaller set
            Q) Why convert to sets before finding intersection?
                a) Set intersection is O(min(m, n)) compared to O(m*n) for nested loops
            Q) Why convert the smaller array to a set first?
                a) More memory efficient

            Example Walkthrough) nums1 = [1, 2, 2, 1], nums2 = [2, 2]
                1. set1 = {1, 2}, set2 = {2}
                2. intersection {1, 2} & {2} = {2}
                3. return [2]
        '''

        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)

    
    @staticmethod
    def union_of_arrays(nums1, nums2):
        '''
            Find the union of two arrays

            Args:
                nums1: first array
                nums2: second array

            Returns:
                a list of all unique elements in the arrays

            Q) What is time and space complexity?
                a) O(n + m) time complexity
                b) O(n + m) space complexity for storing both arrays 
        '''

        return list(set(nums1) | set(nums2))



    @staticmethod
    def character_frequency(s):
        '''
            Count the frequency of each character in a string 

            Args:
                s: string
            
            Return: dictionary mapping each character to its frequency

            Q) What is the time and space complexity?
                a) O(n) time complexity where n is length of string 
                a) O(k) space complexity where k is the number of unique characters

            Example Walkthrough) s = "hello"
                1. Initialize freq = {}
                2. Process 'h' 
                    - freq = { h:1 }
                3. Process 'e' 
                    - freq = { h:1, e:1 }
                4. Process 'l'
                    - freq = { h:1, e:1, l:1 }
                5. Process 'l'
                    - freq = { h:1, e:1, l:2 }
                6. Process 'o'
                    - freq = { h:1, e:1, l:2, 0:2 }
                7. Return freq
        '''

        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1 

        return freq 
    

    @staticmethod
    def is_anagram(s1, s2):
        '''
            Check if two strings are anagrams of each other

            Args: 
                s1: first string
                s2: second string 

            Returns:
                True if strings are anagrams, false otherwise

            Q) What is the time and space complexity?
                a) Time complexity is O(n) where n is the length of strings (since they must have same length to be anagrams)
                a) Space complexity is O(k) where k is number of unique characters
            Q) What is the first check we should perform?
                a) To see if the strings are the same length 
            Q) What are two approaches to solve this problem?
                a) Count character frequencies and compare or sort both strings and compare 
            
            Example Walkthrough) s1 = "listen", s2 = "silent"
                1. len("listen") == len("silent") = 6, continue
                2. freq1 = {'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1}
                3. freq2 = {'s': 1, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1}
                4. freq1 == freq2, return True

        '''

        if len(s1) != len(s2):
            return False

        return HashMapSetOperations.character_frequency(s1) == HashMapSetOperations.character_frequency(s2)


    @staticmethod
    def group_anagrams(strs):
        '''
            Group strings that are anagrams of each other 

            Args:
                strs: list of strings 

            Returns:
                list of lists, where each inner list contains the anagrams 

            Q) What is the time and space complexity?
                a) Time complexity is O(n*k*log(k)) where n is the number of strings and k is the max string length
                a) Space complexity is O(n*k) for storing all strings and keys
            Q) What do we use as the key for storing anagrams?
                a) The sorted version of each string, since each anagram has the same sorted strings

            Example Walkthrough) strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
                1. anagram_groups = {}
                2. "eat": key = "aet", anagram_groups = {"aet": ["eat"]}
                3. "tea": key = "aet", anagram_groups = {"aet": ["eat", "tea"]}
                4. "tan": key = "ant", anagram_groups = {"aet": ["eat", "tea"], "ant": ["tan"]}
                5. "ate": key = "aet", anagram_groups = {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}
                6. "nat": key = "ant", anagram_groups = {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"]}
                7. "bat": key = "abt", anagram_groups = {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"], "abt": ["bat"]}
                8. return [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]] 
        '''

        anagram_groups = {}
        for str in strs:
            # sort the string to create a key for anagrams 
            key = ''.join(sorted(str))
            if key not in anagram_groups:
                anagram_groups[key] = []
            anagram_groups[key].append(str)

        return list(anagram_groups.values())

    

    @staticmethod
    def first_non_repeating_character(s):
        '''
            Find the first non-repeating character in a string

            Args:
                s: string 

            Returns:
                the index of the first non-repeating character or -1 if all characters are non-repeating

            Q) What is the time and space complexity?
                a) Time complexity is O(n) since we just have two passes through the string 
                a) O(k) space complexity where k is the number of unique characters
            Q) How many passes through the string do we need and why do we need them?
                a) 2 passes
                a) One for getting the frequency of each char, the second to find the first char with a frequency of 1 
            Q) Why can't we solve this in one pass? 
                a) We need to know the full frequency count before determining first non-repeating 

            Example Walkthrough) s = 'leetcode'
                1. First pass -> freq = { l:1, e:e, t:1, c:1, o:1, d:1 }
                2. Second pass -> index 0, char 'l', freq[l] = 1, return 0
        '''

        freq = HashMapSetOperations.character_frequency(s)

        for i, char in enumerate(s):
            if freq[char] == 1: 
                return i 
        return -1




    @staticmethod
    def subarray_sum_equals_k(nums, k):
        '''
                Count the number of continuous subarrays whose sum equals k 
            Args:
                nums: the array of integers
                k: target value 
        
            Returns:
                the number of subarrays with sum equal to k 
            Q) What is the time and space complexity?
                a) Time complexity is O(n) for a single pass through the array 
                a) Space Complexity is O(n) for a hashmap for prefix sums 
            Q) What is the key insight for using prefix sums?
                a) If prefix_sum[j] - prefix_sum[i-1] = k, then subarray from i to j has sum k
                    - "Have we seen another prefix sum that is smaller by exactly k? If so, that means the subarray between that earlier prefix and now sums to k."
            Q) Why do we initialize prefix_sum_count with { 0:1 }?
                a) To handle subarrays starting from index 0 (when current_sum == k)
            Q) What does prefix_sum_count store?
                a) Key: cumulative sum, value: how many times this sum has occurred 
            Example Walkthrough) nums = [1, 1, 1], k = 2 
                1. initialize count = 0, current_sum = 0, prefix_sum_count = {0:1}
                2. i = 0, num = 1:
                    - current_sum = 1
                    - target = current_sum - k = 1 - 2 = -1, which is not a key in prefix_sum_count, so we don't increment count  
                    - prefix_sum_count = {0:1, 1:1}
                3. i = 1, num = 1
                    - current_sum = 2
                    - target = current_sum - k = 2 - 2 = 0, 0 is a key found in prefix_sum_count with count 1, so we increment count by 1
                    - count = 1 (subarray [1,1] from index 0 to 1)
                    - prefix_sum_count = {0:1, 1:1, 2:1}
                4. i = 2, num = 1:
                    - current_sum = 3
                    - target = current_sum - k = 3 - 2 = 1, 1 is a key found in prefix_sum_count with count 1, so we increment count by 1
                    - count = 2 (subarray [1,1] from index 1 to 2)
                    - prefix_sum_count = {0:1, 1:1, 2:1, 3:1}
                5. return 2
            
            Advanced Example) nums = [1, 0, 1, 0, 1], k = 1 - demonstrates why we need count += prefix_sum_count[target]
                1. initialize count = 0, current_sum = 0, prefix_sum_count = {0:1}
                2. i = 0, num = 1:
                    - current_sum = 1
                    - target = 1 - 1 = 0, found in prefix_sum_count with count 1
                    - count += 1 = 1 (subarray [1] from index 0 to 0)
                    - prefix_sum_count = {0:1, 1:1}
                3. i = 1, num = 0:
                    - current_sum = 1
                    - target = 1 - 1 = 0, found in prefix_sum_count with count 1
                    - count += 1 = 2 (subarray [0] from index 1 to 1? NO! This is wrong logic)
                    - Actually: subarray [1,0] from index 0 to 1 has sum 1
                    - prefix_sum_count = {0:1, 1:2}  # Note: prefix sum 1 now appears TWICE
                4. i = 2, num = 1:
                    - current_sum = 2
                    - target = 2 - 1 = 1, found in prefix_sum_count with count 2
                    - count += 2 = 4 (because there are 2 different positions where prefix sum was 1)
                    - This gives us 2 subarrays: [1] from index 1-2 and [0,1] from index 0-2
                    - prefix_sum_count = {0:1, 1:2, 2:1}
                5. Continue... return 6 total subarrays
        '''   
    
        count = 0
        current_sum = 0
        prefix_sum_count = {0: 1}  # Initialize with 0 sum occurring once (handles subarrays from index 0)
    
        for num in nums:
            current_sum += num
        
            # If we've seen a prefix sum that is exactly k smaller than our current prefix sum,
            # that means there's a subarray between that earlier position and our current position 
            # that sums to exactly k. We add the COUNT of how many times we've seen that prefix sum
            # because each occurrence represents a different starting position for a valid subarray.
            if current_sum - k in prefix_sum_count:
                # WHY NOT count += 1? Because the same prefix sum might have occurred multiple times
                # at different positions. Each occurrence gives us a different valid subarray ending
                # at the current position. For example, if prefix sum X occurred at positions 2 and 5,
                # and we're now at position 8 with current_sum = X + k, then we have TWO valid subarrays:
                # one from position 3 to 8, and another from position 6 to 8.
                count += prefix_sum_count[current_sum - k]
        
            # Add the current sum to prefix_sum_count (THIS MUST BE OUTSIDE THE IF STATEMENT)
            # We do this after checking to avoid using the same element twice in a subarray
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
        
        return count 


    @staticmethod
    def longest_substring_without_repeating_chars_hashmap(s):
        '''
            Find the length of the longest substring without repeating characters using HashMap.
            This is an alternative implementation to the sliding window approach.
            
            Args:
                s: input string
            Returns:
                length of longest substring without repeating characters
            
            Q) What is the time and space complexity?
                a) O(n) time complexity - single pass through string
                a) O(min(m, n)) space complexity where m is charset size
            Q) How does this differ from the sliding window approach?
                a) We store the actual index of each character, allowing us to jump directly
            Q) Why do we use max(start, char_index[char] + 1)?
                a) To ensure start never moves backward (handles overlapping characters)
            
            Example Walkthrough) s = "abcabcbb"
                1. start = 0, max_length = 0, char_index = {}
                2. i=0, char='a': char_index = {'a': 0}, max_length = 1
                3. i=1, char='b': char_index = {'a': 0, 'b': 1}, max_length = 2
                4. i=2, char='c': char_index = {'a': 0, 'b': 1, 'c': 2}, max_length = 3
                5. i=3, char='a': 'a' seen at index 0, start = max(0, 0+1) = 1
                   char_index = {'a': 3, 'b': 1, 'c': 2}, max_length = max(3, 3-1+1) = 3
                6. Continue similar process...
                7. return 3
        ''' 

        if not s:
            return 0

        start = 0
        max_length = 0
        char_index = {}

        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                # move start to after the previous occurrence 
                start = char_index[char] + 1 

            char_index[char] = i
            max_length = max(max_length, i - start + 1)

        return max_length


    @staticmethod
    def four_sum_count(nums1, nums2, nums3, nums4):
       '''
            Count tuples (i, j, k, l) such that nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

            Args:
                nums1, nums2, nums3, nums4: four arrays of integers 

            Returns:
                number of tuples with sum == 0

            Q) What is the time and space complexity?
                a) Time complexity is O(n^2) since we have to iterate through two pairs of arrays 
                a) Space complexity is O(n^2) since we have to store all possible sums of the first two arrays 
            Q) How do we optimize from O(n^4) brute force to O(n^2)?
                a) Pre-compute all the sums of the first two arrays to see if a complement exists 
            Q) What does the sum_count dictionary store?
                a) Key: sum of two numbers, Value: how many ways to achieve this sum 

            Example Walkthrough) nums1 = [1,2], nums2 = [-2, -1], nums3 = [-1,2], nums4 = [0, 2]
                1. initialize sum_count = {}
                2. For nums1 and nums2:
                    1. 1 + (-2) = -1, sum_count = { -1:1 }
                    2. 1 + (-1) = 0, sum_count = { -1:1, 0:1 }
                    3. 2 + (-2) = 0, sum_count = { -1:1, 0:2 }
                    4. 2 + (-1) = 1, sum_count = { -1:1, 0:2, 1:1 }
                3. For nums3 and nums4:
                    1. -1 + 0 = -1, need complement 1, found one previous occurrence, count = 1 
                    2. -1 + 2 = 1, need complement -1, found one previous occurrence, count = 2 
                    3. 2 + 0 = 2, need complement -2, not found 
                    4. 2 + 2 = 4, need complement -4, not found 
                4. return 2 
       '''
       sum_count = {}
       for num1 in nums1:
            for num2 in nums2:
                sum_ab = num1 + num2
                sum_count[sum_ab] = sum_count.get(sum_ab, 0) + 1
       
       count = 0 
       for num3 in nums3:
            for num4 in nums4:
                complement = -(num3 + num4)
                if complement in sum_count:
                    count += sum_count[complement]
       
       return count 

    @staticmethod
    def top_k_frequent_elements(nums, k):
        '''
           Find the k most frequent elements in an array.

           Args:
               nums: an array of integers 
               k: number of most frequent elements to return 

            Returns:
                list of k most frequent elements 

            Q) What is the time and space complexity?
                a) Time complexity O(n log n) if using sorting, O(n log k) if using min-heap
                a) Space complexity is O(n) to store frequency map 
            Q) What are alternative approaches aside from sorting?
                a) Min-heap of size k, or bucket sort of O(n) time 
            Q) Why might heap be better than sorting for large arrays?
                a) Heap approach is O(n log k) and sorting is O(n log n)

            Example Walkthrough) nums = [1, 1, 1, 2, 2, 3], k = 2:
                1. freq = {1:3, 2:2, 3:1}
                2. sort by frequency -> [(3,1), (2, 2), (1, 3)]
                3. take first k=2 elements --> [1,2]
                4. return [1,2]
            
        '''
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 
            
        # sort freq by descending and take the first k elements 
        sorted_by_freq = sorted(freq.keys(), key = lambda x: freq[x], reverse=True)
    
        return sorted_by_freq[:k]

    
    
    @staticmethod 
    def valid_sudoku(board):
        '''
            Determine if a 9x9 board is valid via sudoku rules

            Args:
                board: a 2D list representing sudoku cells, with '.' for blanks 

            Returns:
                true if valid, false otherwise 

            Q) What is the time and space complexity?
                a) Time complexity is O(1) since the board is a static 9x9
                a) Space complexity is O(1) - fixed number of sets 
            Q) What three conditions must be met for a valid sudoku?
                1. Each row contains unique digits 1-9
                2. Each column contains unique digits 1-9
                3. Each 3x3 sub-box contains unique digits 1-9
            Q) How do we identify which 3x3 box a cell belongs to?
                a) Box index = (row // 3) * 3 + (col // 3)
                    // --> floor division, divides and rounds down.
                    the formula outputs an integer that is the label of the box, working from left to right and then up to down, i.e.,:
                        0 1 2 
                        3 4 5
                        6 7 8
                    where box 0 contains cells (zero-indexed):
                        (0,0)   (0,1)   (0,2)
                        (1,0)   (1,1)   (1,2)
                        (2,0)   (2,1)   (2,2)
                    and box 4 contains cells:
                        (3,3)   (3,4)   (3,5)
                        (4,3)   (4,4)   (4,5)
                        (5,3)   (5,4)   (5,5)
                    and box 8 contains cells:
                        (6,6)   (6,7)   (6,8)
                        (7,6)   (7,7)   (7,8)
                        (8,6)   (8,7)   (8,8)
                    Formula Examples)
                        1. cell 0,0 -> (0 // 3) * 3 + (0 // 3) = 0 + 0 = 0 (top leftmost box)
                        2. cell 4,5 = (4 // 3) * 3 + (5 // 3) = 3 + 1 = 4 
            Example Walkthrough) Check if board[0][0] = 5 is valid:
                1. Check row 0, add 5 to row_sets[0]
                2. check col 0, add 5 to col_sets[0]
                3. check box 0, add 5 to box_sets[0]
                4. if any set already contains 5, return false 
                5. continue for all cells..
        '''
        
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell == '.':
                    continue
                
                # calculate which 3x3 box this cell belongs to 
                box_index = (row // 3) * 3 + (col // 3)
                
                # check if the number already exists in the row, column, or box set 
                if (cell in row_sets[row] or cell in col_sets[col] or cell in box_sets[box_index]):
                    return False 

                # add the number to the sets if since it doesn't currently exist 
                row_sets[row].add(cell)
                col_sets[col].add(cell)
                box_sets[box_index].add(cell)

        return True




