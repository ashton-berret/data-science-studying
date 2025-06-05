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
                a) Time complexity is O(n)
                a) Space complexity is O(1) -> in place operation
            Q) What constitutes a min-heap?
                a) Every parent is <= both of its children
            Q) Why start from the last non-leaf node?
                a) Leaf nodes are already valid heaps, we can work bottom up
            Q) What is the difference between heapify and building heap by insertion?
                a) Heapify is O(n), repeated insertion is O(n log n)

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

        def heapify_down(arr, n, i):
            # i is the current element we are using as comparison in walkthrough above
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left] <= arr[smallest]:
                smallest = left
            if right < n and arr[right] <= arr[smallest]:
                smallest = right

            if smallest != i:
                arr[i], arr[smallest] = arr[smallest], arr[i]
                heapify_down(arr, n, i)

            n = len(arr)
            # start from the last non-leaf node and heapify down
            for i in range(n // 2 - 1, -1, -1):
                heapify_down(arr, n, i)



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
                a) Time complexity is O(log n) -> buble up at most height levels
                a) Space complexity is O(1) -> only using constant extra space
            Q) Why do we bubble up instead of down?
                a) New element is added at the end, may violate the heap property with parent
            Q) When do we stop bubbling up?
                a) When parent is smaller (min-heap) or we reach root

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
        heap.append(val)
        i = len(heap) - 1

        # bubble up
        while i > 0:
            parent = (i - 1) // 2
            if heap[parent] <= heap[i]:
                break
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent



    @staticmethod
    def heap_extract_min(heap):
        '''
            Extract (remove) the minimum element from the heap

            Args:
                heap: list of strings representing min-heap

            Returns:
                min element, or None if heap is empty

            Q) What is time and space complexity?
                a) Time complexity is O(log n) -> bubble down at most height levels
                a) Space complexity is O(1)
            Q) Why can't we just take heap[0]?
                a) This would work for peek, but extraction means removing the element and doing so would break the heap structure (left child would become root)
            Q) Why do we move the last element to the root?
                a) Maintains complete tree property, then we can fix the heap property

            Example Walkthrough) heap = [1, 2, 3, 5, 10, 4]
                1. save min = 1
                2. move last element to root -> [4, 2, 3, 5, 10]
                3. bubble down: compare 4 with children (2,3) -> swap 4 with 2
                    - now we have [2, 4, 3, 5, 10]
                4. bubble down: 4 vs children (5, 10) -> no swap needed
                5. return 1
        '''

        if not heap:
            return None

        min_val = heap[0]
        if len(heap) == 1:
            heap.pop()
            return min_val

        # move the last element to the root
        heap[0] = heap.pop()

        # bubble down
        i = 0
        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(heap) and heap[left] < heap[smallest]:
                smallest = left
            if right < len(heap) and heap[right] < heap[smallest]:
                smallest = right

            if smallest == i:
                break

            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest

        return min_val


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
                a) Time complexity is O(n log k) -> process n elements, maintain heap size of k
                a) Space complexity is O(k) -> heap size
            Q) Why can't we just sort the array in reverse order, convert to hashmap to remove duplicates, and use k - 1 as the index lookup?
                a) We can! Here are the pros and cons of each:
                    1. Sorted hashmap:
                        - simple
                        - time complexity is O(n log n) -> works well when k > n / 2
                    2. Heap:
                        - more complex
                        - time complexity is O(n log k) -> works well with smaller k's or when memory is more constrained
            Q) Why do we use min heap instead of max heap?
                a) Min heap of size k keeps the k largest elements, where the root is kth largest
            Q) What if k > len(nums)?
                a) Typically undefined, could return smallest element

            Example Walkthrough) nums = [3, 2, 1, 5, 6, 4], k = 2
                1. process 3 -> heap = [3]
                2. process 2 -> heap = [2,3]
                3. process 1 -> heap = [2,3] --> 1 is not added since it is < 2
                4. process 5 -> heap = [3,5]
                5. process 6 -> heap = [5,6]
                6. process 4 -> heap = [5,6] --> not added
                7. return heap[0] = 5
        '''
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heapreplace(heap, num)

        return heap[0]



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
                a) Time complexity is O(n log k) -> count frequencies (O(n)), heap operations (O(n log k))
                a) Space complexity is O(n)
            Q) Why use min-heap for most frequent?
                a) Min-heap of size k keeps k most frequent, efficiently removes least frequent
            Q) Could we use max heap instead?
                a) Yes, but we would need to process all the elements then extract k times

            Example Walkthrough) nums = [1, 1, 1, 2, 2, 3], k = 2
                1. count frequencies: {1:3, 2:2, 3:1}
                2. process (1,3): heap = [(3, 1)]
                3. process (2,2): heap = [(2,2), (3,1)]
                4. process (3,1): heap = [(2,2), (3,1)] -> (1,3) not added since 1 < 2
                5. extract values -> [2, 1]
        '''

        freq_map = Counter(nums)
        heap = []

        for num, freq in freq_map.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            elif freq > heap[0][0]:
                heapq.heapreplace(heap, (freq, num))

        return [num for freq, num in heap]


    @staticmethod
    def merge_k_sorted_lists(lists):
        '''
            Merge k sorted linked lists into one sorted list

            Args:
                lists: list of ListNode heads representing sorted lists

            Returns:
                ListNode head of merged sorted list

            Q) What is the time and space complexity?
                a) Time complexity is O(n log k) where n is total nodes, k is number of lists
                a) Space complexity is O(k)
            Q) Why is this better than merging lists one by one?
                a) Merging one by one is O(nk) compared to O(n log k)
            Q) How do we handle empty lists?
                a) Skip None heads when initializing heap

            Example Walkthrough) lists = [[1,4,5], [1,3,4], [2,6]]
                1. initialize heap with heads: [(1, list1), (1, list2), (2, list3)]
                2. extract (1, list1), add to result, push list1.next = 4
                3. extract (1, list2), add to result, push list2.next = 3
                4. continue until all nodes are processed
                5. result: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
        '''

        if not lists:
            return None

        heap = []
        dummy = ListNode(0)
        current = dummy

        # initialize heap with first node from each list
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))

        list_index = len(lists) # for unique identification

        while heap:
            val, idx, node = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, list_index, node.next))
                list_index += 1

        return dummy.next



    @staticmethod
    def meeting_rooms_ii(intervals):
        '''
            Find minimum number of meeting rooms required

            Args:
                intervals: list of [start, end] representing meeting times

            Returns:
                minimum number of meeting rooms needed

            Q) What is the time and space complexity?
                a) Time complexity is O(n log n) -> sorting + heap operations
                a) Space complxity is O(n) -> heap size in worst case
            Q) Why use min-heap for end times?
                a) Track earliest ending meeting to see if the room becomes available
            Q) When do we need a new room?
                a) When current meeting starts before earliest meeting ends

            Example Walkthrough) intervals = [[0, 30], [5,10], [15,20]]
                1. Sort by start time: [[0, 30], [5,10], [15,20]]
                2. meeting [0,30]: heap = [30], rooms = 1
                3. meeting [5,10]: 5<30, heap = [10,30], rooms = 2
                4. meeting [15,20]: 15 > 10, heap = [20,30], rooms = 2
                5. return 2
        '''

        if not intervals:
            return 0

        # sort meetings by start time
        intervals.sort(key=lambda x: x[0])
        heap = []

        for start, end in intervals:
            # if earliest meeting ends before current starts, reuse the room
            if heap and heap[0] <= start:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

        return len(heap)



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
                a) Time complexity is O(m log m) where m is unique tests
                a) Space complexity is O(m) -> heap and frequency map
            Q) Why do we use max-heap for frequencies?
                a) Execute most frequent tasks first to minimize wait time
            Q) When do we add idle time?
                a) When we can't fill all n+1 slots in a round

            Example Walkthrough) tasks = ['A', 'A', 'A', 'B', 'B', 'B'], n = 2
                1. frequencies: A:3, B:3
                2. round 1, execute A -> B -> Idle, remaining a:2, b:2
                3. round 2, execute A -> B -> Idle, remaining a:1, b:1
                4. round 3, execute A -> B -> Idle, remaining a:0, b:0
                5. total time = 8 (num tasks + idle time)
        '''

        freq_map = Counter(tasks)
        frequencies_max_heap = [-freq for freq in freq_map.values()]
        heapq.heapify(frequencies_max_heap)

        time = 0

        while frequencies_max_heap:
            cycle = []
            # try to fill n+1 time slots
            for i in range(n+1):
                if frequencies_max_heap:
                    freq = -heapq.heappop(frequencies_max_heap)
                    if freq > 1:
                        cycle.append(freq - 1)
                    time += 1
                elif cycle: # still have tasks to do but need idle time
                    time += 1

            # add remaining frequencies back to heap
            for freq in cycle:
                heapq.heappush(frequencies_max_heap, -freq)

        return time


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
                a) Time complexity is O(n log k) - each element added/removed once
                a) Space complexity is O(k)
            Q) Why store (value, index) pairs?
                a) Need to track which elements are still in the current window
            Q) How do we handle outdated maximums?
                a) Remove elements from heap that are outside the current window


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

        if not nums or k == 0:
            return []

        max_heap = []
        result = []

        for i in range(len(nums)):
            # add current element to heap
            heapq.heappush(max_heap, (-nums[i], i))

            # remove elements outside the current window
            while max_heap and max_heap[0][1] <= i - k: # using [0][1] since we are referencing first element in heap, then getting the second element(idx) in that tuple
                heapq.heappop(max_heap)

            # if window is complete, add maximum to result
            if i >= k -1:
                result.append(-max_heap[0][0])

        return result



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
                a) Time complexity is O(n log k) -> process n points, maintain heap of size k
                a) Space complexity is O(k)
            Q) Why use max-heap for closest points?
                a) Max heap of size k keeps k closes, efficiently removes farthest
            Q) How do we calculate distance?
                a) Use squared distance to avoid floating point operations

            Example Walkthrough) points = [[1,1], [2,2], [3,3]], k = 1
                1. point [1,1]: distance = 2, heap = [(2, [1,1])]
                2. point [2,2]: distance = 2*2 = 4, don't add since 4 > 2
                3. point [3,3]: distance = 18, don't add since 18 > 2
                4. return [[1,1]]
        '''

        def squared_distance(point):
            return point[0] ** 2 + point[1] ** 2

        max_heap = []
        for point in points:
            dist = squared_distance(point)

            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist, point))
            elif dist <= -max_heap[0][0]:
                heapq.heapreplace(max_heap, (-dist, point))

        return [point for dist, point, in max_heap]

class MedianFinder:
    '''
        Find the median from data stream using two heaps

        Q) What is the time and space complexity?
            a) Time complexity for addNum is O(log n), findMedian = O(1)
            a) Space complexity is O(n), storing all numbers
        Q) Why use two heaps?
            a) Max-heap for smaller half, min-heap for larger half, median is at the roots
        Q) How do we maintain balance?
            a) Keep heap sizes equal or max-heap 1 larger

        Example Walkthrough) stream = [2,3,4]
            1. add 2: max_heap = [], min_heap = [2], median = 2
            2. add 3: max_heap = [2], min_heap = [3], median = 2.5
            3. add 4: max_heap = [2], min_heap = [3,4], median = 3
    '''

    def __init__(self):
        self.max_heap = [] # for smaller half (negative values for max behavior)
        self.min_heap = [] # for larger half

    def add_num(self, num):
        ''' Add number to data structure'''

        # always add to max heap first
        heapq.heappush(self.max_heap, -num)

        # move largest from max_heap to min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # balance the heaps
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        ''' find median of all numbers added so far'''
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0








