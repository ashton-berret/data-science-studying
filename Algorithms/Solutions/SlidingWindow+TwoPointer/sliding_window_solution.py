class SlidingWindowOperations:
    ''' common SlidingWindowOperations and patterns'''


    @staticmethod
    def max_sum_subarray_of_size_k(arr, k):
        '''
            Find the maximum sum of a subarray of size k 

            Args:
                arr: input array of integers
                k: Size of subarray 
            Returns:
                maximum sum of a subarray of size k 
        
            Q) What is the time and space complexity?
                a) O(n) time complexity
                a) O(1) space complexity 
            Q) In the for loop, what pointers interact? What is the operation that occurs during the window sliding? 
                a) i and k(size of sub array)
                a) arr[i-k] is subtracted to
            Q) What do we initialize the first window sum to? How does this affect our calculations as the window moves?
                a) The first sum is initialized to the sum of all elements starting at 0 up to k. This is important since in the for loop, we start i at value k, allowing for the i-k to remove the 0th element. 
        

            Example Walkthrough) arr = [2, 1, 5, 1, 3, 2], k = 3
                1. intialize window sum to 2 + 1 + 5 = 8, max_sum = 8
                2. for i = k = 3:
                    - remove arr[0] = 2
                    - add arr[3] = 1
                    - window_sum = 1 + 5 + 1 = 7
                    - max_sum does not change, = 8
                3. for i = 4
                    - remove arr[1] = 1
                    - add arr[4] = 3
                    - window sum = 5 + 1 + 3 = 9
                    - max_sum = 9
                4. for i = 5:
                    - remove arr[2] = 5
                    - add arr[5] = 2
                    - window_sum = 1 + 3 + 2 = 6
                    - max_sum does not change, = 9
                5. return max_sum  = 9

        '''

        if not arr or k <= 0 or k > len(arr):
            return 0

        # sum of the first window 
        window_sum = sum(arr[:k])
        max_sum = window_sum

        # slide the window from left to right
        for i in range(k, len(arr)):
            # add the next element and remove the first element from the array (i-k).
            # IMPORTANT - Realize i starts at k, not 0. so the first i-k is the same as k-k, removing the 0-index element. the next pass is removing the 1-index element, etc.  
            window_sum = window_sum + arr[i] - arr[i-k]
            max_sum = max(max_sum, window_sum)

        return max_sum 

    @staticmethod
    def smallest_subarray_with_given_sum(arr, target_sum):
        '''
            Find the lenght of the smallest contiguous subarray with sum >= target_sum 

            Args:
                arr: input array of positive integers 
                target_sum: target sum to achieve
            Returns:
                length of the smallest subarray with sum >= target sum or float(inf) if no such subarray exists

            Q) What is the time and space complexity?
                a) O(n) time complexity - each element is processed at most two times, so O(2n) but O drops constants so O(2n) = O(n)
                a) O(1) space complexity

            
            Example Walkthrough) arr = [2, 1, 5, 2, 3, 2], target_sum = 7
                1. initialize window_start = 0, window_sum = 0, min_length = inf 
                2. window_end = 0 (length 1)
                    - window_sum = 2
                    - 2 <= 7 (target_sum)
                3. window_end = 1 (length 2)
                    - window_sum = 2 + 1 = 3
                    - 3 <= 7
                4. window_end = 2 (length 3)
                    - window_sum = 2 + 1 + 5 = 8 
                    - 8 > 7 --> enter inner loop 
                    - update min_length = 3
                    - remove arr[0]
                    - window_sum = 1 + 5 = 6 --> exit inner loop 
                5. window_end = 3 (length 3)
                    - window_sum = 1 + 5 + 2 = 8
                    - 8 > 7 --> enter inner loop 
                    - min_length = min(3,3) = 3
                    - remove arr[1] = 1
                    - window_sum = 5 + 2 = 7
                    - min_length = 2
                    - remove arr[2] = 5
                    - window_sum = 2 --> exit inner loop
                6. window_end = 4 (length 2)
                    - window_sum = 2 + 3 = 5
                7. window_end = 5 (length 3)
                    - window_sum = 2 + 3 + 2 = 7 --> enter inner loop
                    - min_length = min(2, 3) = 2 --> doesn't change 
                    - remove arr[4] = 3
                    - window_sum = 2 --> exit inner loop
                8. return 2 (from window end 3, subarray [5,2])



        '''
        if not arr or target_sum <= 0:
            return 0

        window_start = 0
        window_sum = 0
        min_length = float('inf')
        
        # initialize window_end at 0 so that the first pass only takes the first element as the subarray. this expands the loop by adding one element at a time.
        for window_end in range(len(arr)):
            # add the next element
            window_sum += arr[window_end]
            
            # shrink the window, from the left, as small as possible while maintaining sum >= target sum, this prevents the starting point from passing the ending point. 
            while window_sum >= target_sum:
                # update the minimum length found so far 
                min_length = min(min_length, window_end - window_start + 1) # add one to get the number of elements in the subarray (i.e., arr[2] to arr[4] contains 3 elements)
                # remove the first value in the window from the calculation and slide the window starting position forward, effectively shrinking the window since the end point didn't change.  
                window_sum -= arr[window_start] 
                window_start += 1
        
        return min_length if min_length != float('inf') else 0

        


    @staticmethod 
    def longest_substring_with_k_distinct(s, k):
        '''
            Find the length of the longest substring with at most k distinct characters.
        
            Args:
                s: input string 
                k: maximum number of distinct characters
            Returns:
                Length of the longest substring 
            Q) What is the time and space complexity
                a) O(n) time complexity
                a) O(k) space complexity
            Q) What are the key-value mappings in the char_frequency dictionary? How do you access the character? How do you access the frequency?
                a) the character is the key and the value is the frequency
            Q) When building the frequency dictionary, why do we use 0 as the value in the char_frequency.get() method? 
                a)


            Example Walkthrough) s = 'araaci', k = 2
            1. initialize window_start = 0, max_length = 0, char_frequency = {}
            2. start with window_end = 0 (char = 'a')
                - char_frequency = { a:1 }
                - 1 distinct char < 2
                - max_length = max(0, 1) -> update to 1
            3. move to window_end = 1 (chars ['a', 'r']
                - char_frequency  = { a:1, r:1 }
                - 2 distinct chars <= 2
                - max_length = max(1, 2) --> update to 2
            4. move to window_end = 2 (chars ['a', 'r', 'a']
                - char frequency = { a:2, r:1 }
                - 2 distinct chars <= 2
                - max_length = max(2, 3) --> update to 3
            5. move to window_end = 3 (chars ['a', 'r', 'a', 'a']
                - char_frequency = { a:3, r:1 }
                - 2 distinct chars <= 2
                - max_length = max(3, 4) --> update to 4
            6. move to window_end = 4 (chars ['a', 'r', 'a', 'a', 'c']
                - char_frequency = { a:3, r:1, c:1 }
                - 3 distinct chars >= k --> remove first ['a'] from window 
                - distinct still = 3 >= k --> remove 'r' from window 
                - distinct = 2
                - char_frequency = { a:2, c:1 }
                - increment start window to 2
                - max_length = max(4, 3) --> doesn't update 
                - current window = ['a', 'a', 'c']
            7. move to window_end = 5 (chars ['a', 'a', 'c', 'i']
                - char_frequency = { a:2, c:1, i:1 }
                - 3 distinct chars > k --> remove ['a'] from window 
                - char_frequency = { a:1, c:1, i:1 }
                - 3 distinct chars > k --> remove ['a'] from window
                - char_frequency = { c:1, i:1 }
                - 2 distinct chars 
                - max_length = max(4, 2) --> doesn't update
            8. return 4 (from substring 'araa', window ending at pos 3)
        '''

        if not s or k <= 0:
            return 0

        window_start = 0
        max_length = 0
        char_frequency = {}

        for window_end in range(len(s)):
            right_char = s[window_end] # initialize the rightmost character at position 0
            char_frequency[right_char] = char_frequency.get(right_char, 0) + 1 # add the character to the dictionary and add 1 to its count value

            # shrink the window until we have at most k distinct characters
            # len(char_frequency) tells us how many distinct characters 
            while len(char_frequency) > k:
                left_char = s[window_start] 
                char_frequency[left_char] -= 1 # remove the leftmost character from the window 
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)
        return max_length


    @staticmethod
    def fruits_into_baskets(fruits):
        '''
            Find the maximum number of fruits you can collect using two baskets, where each basket can only hold one type of fruit.
            This is the same as finding the longest substring with at most two distinct characters.

            Args:
                fruits: input array of characters representing fruits
            Returns:
                maximum number of fruits you can collect with two baskets

            Q) What is the time and space complexity?
                a) O(n) time complexity -> each fruit is processed at most twice
                a) O(1) space complexity -> we store at most 3 fruits in the hash map
        '''

        return SlidingWindowOperations.longest_substring_with_k_distinct(fruits, 2)




    @staticmethod
    def longest_substring_without_repeating(s):
        '''
            Find the length of the longest substring without repeating characters
            Args:
                s: input string
            Returns:
                length of the longest substring without repeating characters 

            Q) What is the time and space complexity?
                a) O(n) time complexity, each character is processed once
                a) O(min(m,n)) where m is the size of the character set 
            

            Example Walkthrough) s = 'abcabcbb'
            1. initialize window_start, max_length = 0. char_index_map = {} (where it is {char, index}
            2. window_end = 0 (char = 'a')
                - haven't seen char yet
                - char_index_map = { a:0 }
                - current_window = ['a']
                - max_length = (0,1) --> update to 1
            3. window_end = 1 (chars = ['a', 'b'])
                - haven't seen char yet
                - char_index_map = { a:0, b:1 }
                - current_window = ['a', 'b']
                - max_length = max(1,2) --> update to 2
            4. window_end = 2 (chars = ['a', 'b', 'c'])
                - haven't seen char yet
                - char_index_map = { a:0, b:1, c:2 }
                - current_window = ['a', 'b', 'c']
                - max_length = max(2, 3) --> update to 3
            5. window_end = 3 (chars = ['a', 'b', 'c', 'a'])
                - have seen char (found at index 0 previously)
                - previous found at 0 >= start_window=0, so increment start_window 0 + 1 = 1
                - char_index_map = { a:3, b:1, c:2 }
                - current_window = ['b', 'c', 'a']
                - max_length = max(3,3) = 3 --> doesn't update
            6. window_end = 4 (chars = ['b', 'c', 'a', 'b'])
                - have seen char (found at index 1 previously)
                - previous found at 1 >= start_window = 1, so increment start window 1 + 1 = 2
                - char_index_map = { a:3, b:4, c:2 }
                - current_window = ['c', 'a', 'b']
                - max_length = max(3,3) --> doesn't update
            7. window_end = 5 (chars ['c', 'a', 'b', 'c'])
                - have seen char (previously found at index 2)
                - previous found at 2 >= start_window = 2, so increment start_window 2 + 1 = 3
                - char_index_map = { a:3, b:4, c:5 }
                - current_window = ['a', 'b', 'c']
                - max_length = max(3,3) --> doesn't update
            8. window_end = 6 (chars ['a', 'b', 'c', 'b'])
                - have seen char (previously found at index 4)
                - previous found at 4 >= start_window = 3, so increment start window 4 (previous index) + 1 = 5
                - char_index_map { a:3, b:6, c:5 }
                - current_window = ['c', 'b']
                - max_length = max(3,3) --> doesn't update 
            9. window_end = 7 (chars ['c', 'b', 'b'])
                - have seen char (previously found at index 6)
                - previous found at 6 >= 5, so increment start_window to 6 + 1 = 7
                - char_index_map = { a:3, b:7, c:5 }
                - current_window = ['b']
                - max_length = max(3,1) --> doesn't update
            10. return 3
        '''

        if not s:
            return 0

        window_start = 0
        max_length = 0
        char_index_map = {} # map characters to their most recent index 

        # expand the window by adding one character at a time 
        for window_end in range(len(s)):
            right_char = s[window_end]

            # if we've seen this character before and it is in the current window, we need to shrink the window to exclude the previous occurrence
            if right_char in char_index_map and char_index_map[right_char] >= window_start:
                # move the window start to past the previous occurrence's index, effectively removing the occurrence from the window 
                window_start = char_index_map[right_char] + 1

            # update the most recent index of the current character 
            char_index_map[right_char] = window_end 

            # update the max length if the current window is larger
            max_length = max(max_length, window_end - window_start + 1)

        return max_length


    @staticmethod
    def find_all_anagrams(s, p):
        '''
            Find all start indicies of anagrams of pattern p in string s. 
            An anagram is a string formed by rearranging the letters of another string.

            Args:
                s: input string 
                p: pattern string 
            Returns: list of all start indicies of p's anagrams in s 

            Q) What is the time and space complexity?
                a) O(n) time complexity
                a) O(m) space complexity where m is the letter of distinct characters in p 
        

            Example Walkthrough) s = 'cbaebabacd', p = 'abc'
            1. initialize pattern_freq, window_freq = {}, result = [], window_start, matched = 0
            2. window_end = 0 (char 'c')
                - add to window frequency, window_freq = { c:1 }
                - c matches pattern, increment matched = 1
                - current window = 'c'
                - window_size != pattern size, no action
            3. window_end = 1 (chars ['c', 'b'])
                - add to window frequency, window_freq = { c:1, b:1 }
                - b matches pattern, increment matched = 2
                - current_window = ['c', 'b']
                - window_size != pattern size, no action 
            4. window_end = 2 (chars ['c','b', 'a'])
                - add to window frequency, window_freq = { c:1, b:1, a:1 }
                - a matches pattern, increment matched = 3
                - current window = ['c',  'b', 'a']
                - window size == pattern size --> matched = pattern_freq (3 == 3)
                - add index 0 to result list 
            5. window_end = 3 (chars ['c', 'b', 'a', 'e'])
                - add to window frequency, window_freq = { c:1, b:1, a:1, e:1 }
                - matched = 3
                - e does not match pattern 
                - window size 4 > pattern size 3 --> remove first element from window
                - remove 'c' --> c was matched --> decrement matched = 2
                - increment window_start to 1
                - current window = ['b', 'a', 'e']
                - window size == pattern size --> matched != pattern_freq, no action 
            6. window_end = 4 (chars ['b', 'a', 'e', 'b'])
                - add to window frequency, window_freq = { c:0, b:2, a:1, e:1 }
                - matched = 1 (just the 'a:1') 
                - window size 4 > pattern size 3 --> remove first element from window 
                - remove b --> b now matches, matched = 2
                - increment window_start to 2
                - current window = ['a', 'e', 'b']
                - window size == pattern size but matched != pattern_freq, no action 
            7. window_end = 5 (chars ['a', 'e', 'b', 'a'])
                - add to window frequency, window_freq = { c:0, b:1, a:2, e:1 }
                - matched = 1 (just b:1)
                - window size 4 > pattern size 3 --> remove first element from window 
                - remove a --> a now matches, increment matched to 2
                - increment window start to 3
                - current window = ['e', 'b', 'a']
                - window size == pattern size but matched != pattern_freq, no action
            8. window_end = 6 (chars ['e', 'b', 'a', 'b'])
                - add to window frequency, window_freq = { c:0, b:2, a:1, e:1 }
                - matched = 1
                - window size 4 > pattern size 3, remove first element from window 
                - remove e, e was not matched, matched = 1
                - increment window start to 4
                - current window ['b', 'a', 'b']
                - window size == pattern size but matched != pattern_freq, no action 
            9. window_end = 7 (chars ['b', 'a', 'b', 'a'])
                - add to window frequency, window_freq = { c:0, b:2, a:2, e:0 }
                - matched = 0
                - window size 4 > pattern size 3, remove first element from window 
                - remove b, b now matches --> matched = 1
                - increment start window to 5
                - current window ['a', 'b', 'a']
            10. window_end = 8 chars( ['a', 'b', 'a', 'c'])
                - add to window frequency, window_freq = { c:1, b:1, a:2, e:0 }
                - matched = 2
                - window size 4 > pattern size 3, remove first element from window
                - a removed, now matches --> matched = 3
                - window = ['b', 'a', 'c'] (where these are indices 6,7,8)
                - increment start window to 6
                - add index 6 to result, result = [0,6]
            11. window_end = 9, chars( ['b', 'a', 'c', 'd'])
                - add to window frequency, window_freq = { c:1, b:1, a:1, d:1 }
                - matched = 3
                - window size 4 > pattern size 3, remove first element from window
                - b removed, now matched = 2
                - incremement start window to 7
                - current window = ['a', 'c', 'd']
            12. return result = [0, 6]


        '''
        if not s or not p or len(s) < len(p):
            return []

        # initialize the frequency maps for pattern and current window
        pattern_freq = {} # store frequencies for pattern characters 
        window_freq = {} # store frequencies for characters in the current window 
        result = []
        
        # build the frequency map for pattern characters
        for char in p:
            pattern_freq[char] = pattern_freq.get(char, 0) + 1 # character is key, value is frequency
        
        # intialize variables for the sliding window
        window_start = 0
        matched = 0 # counter for matched characters between pattern and window 

        # expand the window by adding one character at a time 
        for window_end in range(len(s)):
            right_char = s[window_end]

            # add the current character to the window frequency map 
            window_freq[right_char] = window_freq.get(right_char, 0) + 1

            # if the current character matches in frequency with the pattern, increment the matched counter 
            if right_char in pattern_freq and window_freq[right_char] == pattern_freq[right_char]:
                matched += 1

            # if the window size is greater than the pattern length, shrink from the left
            if window_end - window_start + 1 > len(p):
                left_char = s[window_start]

                # if the character leaving the window was a match, decrement the matched counter 
                if left_char in pattern_freq and window_freq[left_char] == pattern_freq[left_char]:
                    matched -= 1

                # update the window frequency map and shrink the window 
                window_freq[left_char] -= 1
                if window_freq[left_char] == 0:
                    del window_freq[left_char]
                window_start += 1

            # just for debugging/visualizing
            # i = 0
            # print(f'-----{i}-------')
            # print(f'Window start: {window_start}')
            # print(f'Window end: {window_end}')
            # print(f'Window freq: {window_freq}')
            # print(f'Matched: {matched}')
            # i += 1
            # print('------------')
            # if all characters match in frequency, an anagram is found, add the start index to the result 
            if matched == len(pattern_freq):
                result.append(window_start)
        
        print(result)
        return result

    @staticmethod
    def longest_repeating_character_replacement(s, k):
        '''
            Find the length of the longest substring with the same character after replacing at most k characters
            
            Args: 
                k: the max number of characters to replace
                s: input string 

            Q) What is the time and space complexity?
                a) O(n) time complexity
                a) O(1) space complexity (only store at most 26 characters)
        
            Example Walkthrough) s='AABABBA', k = 1
                1. start with window_start = 0, max_length = 0, char_frequency = {}
                2. process A, char_frequency = { A:1 }, max_repeat_count = 1
                    - characters to remove: 1 (window_size) - 1(max_repeat_count) = 0 <= k, remove nothing
                    - max_length = 1 (window_size)
                    - current_window = ['A'] 
                    - incrememnt window_end to 1 (window_size is now 2)
                3. process A, char_frequency = { A:2 }, max_repeat_count = 2
                    - characters to remove: 2 - 2 = 0 <=k, remove nothing 
                    - max_length = 2
                    - current_window = ['A', 'A']
                    - increment window_end to 2 (window_size now 3)
                4. process B, char_frequency = { A:2, B:1 }, max_repeat_count = 2
                    - characters to remove: 3 - 2 = 1 <= k(1), remove nothing 
                    - max_length = max(2,3) = 3
                    - current_window = ['A', 'A', 'B']
                    - increment window_end to 3 (window_size now 4)
                5. process A, char_frequency = { A:3, B:1 }, max_repeat_count = 3
                    - characters to remove = 4 - 3 = 1 <= k, remove nothing 
                    - max_length = max(3, 4) = 4
                    - current_window = ['A', 'A', 'B', 'A']
                    - increment window_end to 4 (window_size now 5)
                6. process B, char_frequency = { A:3, B:2 }, max_repeat_count = 3
                    - characters to remove = 5 - 3 = 2 >= k, remove char 'A' --> new char_frequency = { A:2, B:2 }
                        - increment window_start to 1 
                    - max_length = max(4,4) = 4
                    - current_window = ['A', 'B', 'A', 'B']
                    - increment window_end to 5 (window_size now 5)
                7. process B, char_frequency = { A:2, B:3 }, max_repeat_count = 3
                    - characters to remove = 5 - 3 = 2 >= k, remove char 'A' --> new char_frequency = { A:1, B:3 }
                        - increment window_start = 2
                    - max_length = max(4,4) = 4
                    - current_window = ['B', 'A', 'B', 'B']
                    - increment window_end to 6 (window_size now 5)
                8. process A, char_frequency = { A:2, B:3 }, max_repeat_count = 3
                    - characters to remove = 5 - 3 = 2 >= k, remove char 'B' --> new char_frequency = { A:2, B:2 }
                        - increment window_start = 3
                    - max_length = max(4,4) = 4
                    - current_window = ['A', 'B', 'B', 'A']
                9. return max_length = 4 (from 'AABA' or 'BABB') 
        '''
        if not s or k < 0:
            return 0

        window_start = 0
        max_length = 0
        max_repeat_count = 0 # count the most frequent character in the window
        char_frequency = {}

        # expand the window by adding one character at a time 
        for window_end in range(len(s)):
            right_char = s[window_end]
            
            # add current char to the frequency map
            char_frequency[right_char] = char_frequency.get(right_char, 0) + 1
            
            max_repeat_count = max(max_repeat_count, char_frequency[right_char])
            # if more than k characters need to be replaced, shrink the window size 
            # the number of characters to be replaced is given by: (window_end - window_start + 1) - max_repeat_count 
            '''
            '''
            if window_end - window_start + 1 - max_repeat_count > k:
                # remove the leftmost character and shrink the window 
                left_char = s[window_start]
                char_frequency[left_char] -= 1
                window_start += 1

            # update the max length with the current window size
            max_length = max(max_length, window_end - window_start + 1)

        return max_length
















