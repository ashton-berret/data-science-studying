import heapq
from collections import defaultdict, Counter
from typing import List, Optional, Tuple
import math

class ListNode:
    '''
        Linked list node for merge K sorted lists problem later on
    '''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

class HeapsOperations:
    ''' Comprehensive heap and priority queue operations for interviews '''

    @staticmethod
    def heapify_min(arr):
        '''
            Convert an array into a min-heap in-place

            Args:
                arr: list of comparable elements

            Returns:
                None (modifies the array in place)

            Q) What is the time and space complexity?
                a)
                a)
            Q) What constitutes a min-heap?
                a)
            Q) Why start from the last non-leaf node?
                a)
            Q) What is the difference between heapify and building heap by insertion?
                a)

            Example Walkthrough) arr = [4, 10, 3, 5, 1]

                DRAW THE TREE STRUCTURE FOR THIS ARR

                            4
                           / \
                          10  3
                         /  \
                        5    1

                1. start from last non-leaf: index = (num_elements - 1) // 2 --> (5-1) // 2 = 2, element 3
                    - Element 3 at index 2
                    - left child is at index 2*2 + 1 = 5 --> doesn't exist in arr
                    - right child is 2 * 2 + 2 = 6 --> doesn't exist in arr
                    - no children, so no change needed
                    - arr = [4, 10, 3, 5, 1]
                2. heapify down -> element 10 at index 1:
                    - left child is at index 2 * 1 + 1 = 3 = 5
                    - right child is at index 2 * 1 + 2 = 4 = 1
                    - compare 10 and min(5,1) -> 1 is min, so swap 1 and 10
                    - arr = [4, 1, 3, 5, 10]
                3. heapify down -> element 4 at index 0:
                    - left child is at index 2 * 0 + 1 = 1
                    - right child is at index 2 * 0 + 2 = 2
                    - compare 4 and min(1, 3) -> 1 is min, so swap 4 and 1
                    - arr = [1, 4, 3, 5, 10]
                    - tree is now:

                            1
                           / \
                          4   3
                         / \
                        5   10

                4. since we swapped 4, we need to check that it doesn't violate the heap property with its new children
                    - element 4 at index 1
                    - left child is at index 2 * 1 + 1 = 3 = 5
                    - right child is at index 2 * 1 + 2 = 4 = 10
                    - compare 4 and min(5, 10) -> 4 is min, no swap needed

                5. final result is
                            1
                           / \
                          4   3
                         / \
                        5   10

                    - arr = [1, 4, 3, 5, 10]
        '''
        # Implement heapify_min here
        pass


    @staticmethod
    def heap_insert_min(heap, val):
        '''
            Insert a value into a min-heap and maintain heap property

            Args:
                heap: list representing a min-heap
                val: value to insert

            Returns:
                none, modifies the heap in place

            Q) What is the time and space complexity?
                a)
                a)
            Q) Why do we bubble up instead of down?
                a)
            Q) When do we stop bubbling up?
                a)

            Example Walkthrough) heap = [1, 4, 3, 5, 10], insert 2
                    TREE)
                                1
                               / \
                              4   3
                             / \
                            5   10
                1. add 2 to the end -> [1, 4, 3, 5, 10, 2]
                    TREE)
                                1
                               / \
                              4    3
                             / \  /
                            5  10 2

                2. bubble up, 2 vs parent 3 at index 2
                    - since 2 < 3, swap
                    - heap = [1, 4, 2, 5, 10, 3]
                    TREE)
                                1
                               / \
                              4    2
                             / \  /
                             5 10 3
                3. bubble up, 2 vs parent 1 at index 0, no swap needed
                4. final is [1, 4, 2, 5, 10, 3]
        '''
        # Implement heap_insert_min here
        pass


    @staticmethod
    def heap_extract_min(heap):
        '''
            Extract (remove) the minimum element from the heap

            Args:
                heap: list of strings representing min-heap

            Returns:
                min element, or None if heap is empty

            Q) What is time and space complexity?
                a)
                a)
            Q) Why can't we just take heap[0]?
                a)
            Q) Why do we move the last element to the root?
                a)

            Example Walkthrough) heap = [1, 2, 3, 5, 10, 4]
                1. save min = 1
                2. move last element to root -> [4, 2, 3, 5, 10]
                3. bubble down: compare 4 with children (2,3) -> swap 4 with 2
                    - now we have [2, 4, 3, 5, 10]
                4. bubble down: 4 vs children (5, 10) -> no swap needed
                5. return 1
        '''
        # Implement heap_extract_min here
        pass


    @staticmethod
    def kth_largest_element(nums, k):
        '''
            Find the kth largest element in the array.

            Args:
                nums: list of integers
                k: integer representing which largest element to find

            Returns:
                kth largest element

            Q) What is the time and space complexity?
                a)
                a)
            Q) Why can't we just sort the array in reverse order, convert to hashmap to remove duplicates, and use k - 1 as the index lookup?
                a)
            Q) Why do we use min heap instead of max heap?
                a)
            Q) What if k > len(nums)?
                a)

            Example Walkthrough) nums = [3, 2, 1, 5, 6, 4], k = 2
                1. process 3 -> heap = [3]
                2. process 2 -> heap = [2,3]
                3. process 1 -> heap = [2,3] --> 1 is not added since it is < 2
                4. process 5 -> heap = [3,5]
                5. process 6 -> heap = [5,6]
                6. process 4 -> heap = [5,6] --> not added
                7. return heap[0] = 5
        '''
        # Implement kth_largest_element here
        pass


    @staticmethod
    def top_k_frequent_elements(nums, k):
        '''
            Find k most frequent elements in array

            Args:
                nums: list of integers
                k: integer representing how many frequent elements to return

            Returns:
                list of k most frequent elements

            Q) What is the time and space complexity?
                a)
                a)
            Q) Why use min-heap for most frequent?
                a)
            Q) Could we use max heap instead?
                a)

            Example Walkthrough) nums = [1, 1, 1, 2, 2, 3], k = 2
                1. count frequencies: {1:3, 2:2, 3:1}
                2. process (1,3): heap = [(3, 1)]
                3. process (2,2): heap = [(2,2), (3,1)]
                4. process (3,1): heap = [(2,2), (3,1)] -> (1,3) not added since 1 < 2
                5. extract values -> [2, 1]
        '''
        # Implement top_k_frequent_elements here
        pass


    @staticmethod
    def merge_k_sorted_lists(lists):
        '''
            Merge k sorted linked lists into one sorted list

            Args:
                lists: list of ListNode heads representing sorted lists

            Returns:
                ListNode head of merged sorted list

            Q) What is the time and space complexity?
                a)
                a)
            Q) Why is this better than merging lists one by one?
                a)
            Q) How do we handle empty lists?
                a)

            Example Walkthrough) lists = [[1,4,5], [1,3,4], [2,6]]
                1. initialize heap with heads: [(1, list1), (1, list2), (2, list3)]
                2. extract (1, list1), add to result, push list1.next = 4
                3. extract (1, list2), add to result, push list2.next = 3
                4. continue until all nodes are processed
                5. result: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
        '''
        # Implement merge_k_sorted_lists here
        pass


    @staticmethod
    def meeting_rooms_ii(intervals):
        '''
            Find minimum number of meeting rooms required

            Args:
                intervals: list of [start, end] representing meeting times

            Returns:
                minimum number of meeting rooms needed

            Q) What is the time and space complexity?
                a)
                a)
            Q) Why use min-heap for end times?
                a)
            Q) When do we need a new room?
                a)

            Example Walkthrough) intervals = [[0, 30], [5,10], [15,20]]
                1. Sort by start time: [[0, 30], [5,10], [15,20]]
                2. meeting [0,30]: heap = [30], rooms = 1
                3. meeting [5,10]: 5<30, heap = [10,30], rooms = 2
                4. meeting [15,20]: 15 > 10, heap = [20,30], rooms = 2
                5. return 2
        '''
        # Implement meeting_rooms_ii here
        pass


    @staticmethod
    def task_scheduler(tasks, n):
        '''
            Minimum time to execute all tasks with cooldown period

            Args:
                tasks: list of characters representing tasks types
                n: integer representing cooldown period between task types

            Returns:
                minimum time to complete all tasks

            Q) What is the time and space complexity?
                a)
                a)
            Q) Why do we use max-heap for frequencies?
                a)
            Q) When do we add idle time?
                a)

            Example Walkthrough) tasks = ['A', 'A', 'A', 'B', 'B', 'B'], n = 2
                1. frequencies: A:3, B:3
                2. round 1, execute A -> B -> Idle, remaining a:2, b:2
                3. round 2, execute A -> B -> Idle, remaining a:1, b:1
                4. round 3, execute A -> B -> Idle, remaining a:0, b:0
                5. total time = 8 (num tasks + idle time)
        '''
        # Implement task_scheduler here
        pass


    @staticmethod
    def sliding_window_maximum(nums, k):
        '''
            Find maximum in each sliding window of size k

            Args:
                nums: a list of integers
                k: sliding window size

            Returns:
                list of maximum values in each window

            Q) What is the time and space complexity?
                a)
                a)
            Q) Why store (value, index) pairs?
                a)
            Q) How do we handle outdated maximums?
                a)

            Q) Example Walkthrough) nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3

                ----+-------+-------------+---------------+-------------------+------------------------+------------
                 i  |nums[i]| Add to heap | Window range  | Cleanup: remove   | Heap after cleanup     | Window max
                    |       |             | (indices)     | index <= i-k      | (elements present)     |
                ----+-------+-------------+---------------+-------------------+------------------------+------------
                 0  |   1   | (-1,0)      |     [0]       | i-k = -3: none   | [(-1,0)]                |     -
                ----+-------+-------------+---------------+-------------------+------------------------+------------
                 1  |   3   | (-3,1)      |    [0,1]      | i-k = -2: none   | [(-3,1), (-1,0)]        |     -
                ----+-------+-------------+---------------+-------------------+------------------------+------------
                 2  |  -1   | (1,2)       |   [0,1,2]     | i-k = -1: none   | [(-3,1), (-1,0), (1,2)] |    3
                ----+-------+-------------+---------------+-------------------+------------------------+------------
                 3  |  -3   | (3,3)       |   [1,2,3]     | i-k = 0: remove  | [(-3,1), (1,2), (3,3)]  |    3
                    |       |             |               | elements ≤ idx 0 |                         |
                    |       |             |               | remove: (-1,0)   |                         |
                ----+-------+-------------+---------------+-------------------+------------------------+------------
                 4  |   5   | (-5,4)      |   [2,3,4]     | i-k = 1: remove  | [(-5,4), (1,2), (3,3)]  |    5
                    |       |             |               | elements ≤ idx 1 |                         |
                    |       |             |               | remove: (-3,1)   |                         |
                ----+-------+-------------+---------------+-------------------+------------------------+------------
                 5  |   3   | (-3,5)      |   [3,4,5]     | i-k = 2: remove  | [(-5,4), (-3,5), (3,3)] |   5
                    |       |             |               | elements ≤ idx 2 |                         |
                    |       |             |               | remove: (1,2)    |                         |
                ----+-------+-------------+---------------+-------------------+------------------------+------------
                 6  |   6   | (-6,6)      |   [4,5,6]     | i-k = 3: remove  | [(-6,6), (-5,4), (-3,5)]|  6
                    |       |             |               | elements ≤ idx 3 |                         |
                    |       |             |               | remove: (3,3)    |                         |
                ----+-------+-------------+---------------+-------------------+------------------------+------------
                 7  |   7   | (-7,7)      |   [5,6,7]     | i-k = 4: remove  | [(-7,7), (-6,6), (-3,5)]|  7
                    |       |             |               | elements ≤ idx 4 |                         |
                    |       |             |               | remove: (-5,4)   |                         |
                ----+-------+-------------+---------------+-------------------+------------------------+------------

                Key Verification:
                - Each heap state has exactly 3 elements when window is complete ✓
                - Window max is always -heap[0][0] (the most negative = largest positive) ✓
                - Elements removed are exactly those outside the current window ✓

                Final result: [3, 3, 5, 5, 6, 7]
        '''
        # Implement sliding_window_maximum here
        pass


    @staticmethod
    def k_closest_points_to_origin(points, k):
        '''
            Find k closest points to origin

            Args:
                points: list of [x,y] coordinates
                k: integer representing the number of closest points to return

            Returns:
                list of k closest points

            Q) What is the time and space complexity?
                a)
                a)
            Q) Why use max-heap for closest points?
                a)
            Q) How do we calculate distance?
                a)

            Example Walkthrough) points = [[1,1], [2,2], [3,3]], k = 1
                1. point [1,1]: distance = 2, heap = [(2, [1,1])]
                2. point [2,2]: distance = 2*2 = 4, don't add since 4 > 2
                3. point [3,3]: distance = 18, don't add since 18 > 2
                4. return [[1,1]]
        '''
        # Implement k_closest_points_to_origin here
        pass


    @staticmethod
    def reorganize_string(s):
        '''
            Reorganize string so no two adjacent characters are same

            Args:
                s: string to reorganize

            Returns:
                reorganized string, or empty string if impossible

            Q) What is the time and space complexity?
                a)
                a)
            Q) When is reorganization impossible?
                a)
            Q) Why use max heap for frequencies?
                a)

            Example Walkthrough) s = 'aab'
                1. Frequencies = a:2, b:1
                2. Place 'a': result = 'a', remaining: a=1, b=1
                3. Place 'b': result = 'ab', remaining a=1
                4. Place 'a': result 'aba', remaining=0
                5. return 'aba'
        '''
        # Implement reorganize_string here
        pass


    @staticmethod
    def maximum_cpu_load(jobs):
        '''
            Find the maximum CPU load at any  time

            Args:
                jobs: list of [start, end, cpu_load] representing jobs

            Returns:
                maximum CPU load at any point in time

            Q) What is the time and space complexity?
                a)
                a)
            Q) How do we keep track of overlapping jobs?
                a)
            Q) When do we update maximum load?
                a)

            Example Walkthrough) jobs = [[1,4,3], [2,5,4], [7,9,6]]
                1. sort by start: -> already sorted
                2. job [1,4,3]: heap = [(4,3)], current_load = 3, max_load = 3
                3. job [2,5,4]: heap = [(4,3), (5,4)], current load = 7, max load = 7
                4. job [7,9,6]: remove expired, heap = [(9,6)], current load = 6, max_load = 7
                5. return 7
        '''
        # Implement maximum_cpu_load here
        pass


    @staticmethod
    def print_heap_structure(heap, heap_type='min'):
        '''
            Print heap for debugging/visualization

            Args:
                heap: list
                heap_type: str indicating min or max

            Returns:
                None, prints to console

            Q) What do the levels represent?
                a)

            Example Output) heap = [1, 3, 2, 7, 4, 5, 6]
                - Level 0: 1
                - Level 1: [3, 2]
                - Level 2: [7,4, 5,6]
        '''
        # Implement print_heap_structure here
        pass


class MedianFinder:
    '''
        The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

        For example, for arr = [2,3,4], the median is 3.
        For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
        Implement the MedianFinder class:

        MedianFinder() initializes the MedianFinder object.
        void addNum(int num) adds the integer num from the data stream to the data structure.
        double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


        Example 1:

            Input
            ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
            [[], [1], [2], [], [3], []]
            Output
            [null, null, null, 1.5, null, 2.0]

            Explanation
            MedianFinder medianFinder = new MedianFinder();
            medianFinder.addNum(1);    // arr = [1]
            medianFinder.addNum(2);    // arr = [1, 2]
            medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
            medianFinder.addNum(3);    // arr[1, 2, 3]
            medianFinder.findMedian(); // return 2.0


        Q) What is the time and space complexity?
            a)
            a)
        Q) Why use two heaps?
            a)
        Q) How do we maintain balance?
            a)

    '''

    def __init__(self):
        # Initialize data structures here
        pass

    def add_num(self, num):
        ''' Add number to data structure'''
        # Implement add_num here
        pass

    def find_median(self):
        ''' find median of all numbers added so far'''
        # Implement find_median here
        pass
