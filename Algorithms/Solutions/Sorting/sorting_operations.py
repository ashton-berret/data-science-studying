import random

class SortingOperations:


    @staticmethod
    def bubble_sort(arr):
        '''
        Bubble Sort with Optimization

        Time: O(n^2),O(n) best with optimization
        Space: O(n)
        Stable: Yes

        Example) [64, 34, 25, 12, 22, 11, 90]

            Step 1) [34, 25, 12, 22, 11, 64, 90] --> 90 bubbles to end
            Step 2) [25, 12, 22, 11, 34, 64,90] --> 64 bubbles to position
        '''

        if not arr:
            return []

        n = len(arr)
        arr = arr.copy()

        for i in range(n):
            swapped = False

            # last i elements are already sorted
            for j in range(0, n - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1],  arr[j]
                    swapped = True

            if not swapped: # if no swaps occurred,the array is sorted
                break

        return arr



    @staticmethod
    def selection_sort(arr):
        '''
        Selection Sort - repeatedly find the minimum and place at the beginning

        Time: O(n^2)
        Space: O(1)
        Stable: No


        Example) [64, 25, 12, 22, 11, 90]

            1. Find min (11) --> swap with first --> [11, 25, 12, 22, 64, 90]
            2. Find min in rest (12) --> swap with second --> [11, 12, 25, 22, 64, 90]
            ... continue until sorted
        '''

        if not arr:
            return []

        arr = arr.copy()
        n = len(arr)

        for i in range(n):
            # find the minimum in the remaining unsorted array
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            # swap found minimum with the first element
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr


    @staticmethod
    def insertion_sort(arr):
        '''
        Insertion Sort - Build sorted array one element at a time

        Time: O(n^2)
        Space: O(1)
        Stable: Yes

        Pseudo)
            1. for each index in the input list
                1. Set a j variable to the current index
                2. While j is greater than 0 and the element at index j-1 is greater than the element at index j
                    1. Swap the elements at indices j and j-1
                    2. Decrement j by 1
            2. Return the list

        Example: [5, 2, 4, 6, 1, 3]
            Start: [5] | 2, 4, 6, 1, 3
            Insert 2: [2, 5] | 4, 6, 1, 3
            Insert 4: [2, 4, 5] | 6, 1, 3
            Insert 6: [2, 4, 5, 6] | 1, 3
            Insert 1: [1, 2, 4, 5, 6] | 3
            Insert 3: [1, 2, 3, 4, 5, 6]

        '''
        if not arr:
            return []

        arr = arr.copy()

        for i in range(len(arr)):
            j = i
            while j > 0 and arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

                j -= 1
        return arr



    @staticmethod
    def merge_sort(arr):
        '''
        Merge Sort - Divide and Conquer with guaranteed O(n log n)

        Time: O(n log n)
        Space: O(n)
        Stable: Yes

        Pseudo)
            1. merge_sort)
                1. if len(arr) is less than 2, it is already sorted so return it
                2. split the array down the middle
                3. call merge_sort on each half
                4. return the result of calling merge(sorted left, sorted right) on the results of merge_sort

            2. _merge)
                1. create a new final list of integers
                2. set i and j equal to 0, used to keep track of the indices in the two input lists
                3. use a loop to compare the current elements of A and B
                    - if an element in A is less than or equal to its respective element in B, add it to the final list and increment i.
                    - Otherwise, add the element in B and increment j
                    - Continue until all items from one of the lists have been added
                4. Add any left over items from one of the arrays to the result list
                5. return the final list

        Example: [38, 27, 43, 3, 9, 82, 10]
            Divide: [38,27,43,3] [9,82,10]
            Divide: [38,27] [43,3] [9,82] [10]
            Divide: [38] [27] [43] [3] [9] [82] [10]
            Merge: [27,38] [3,43] [9,82] [10]
            Merge: [3,27,38,43] [9,10,82]
            Merge: [3,9,10,27,38,43,82]

        '''

        if len(arr) < 2:
            return arr

        first = SortingOperations.merge_sort(arr[: len(arr) // 2])
        second = SortingOperations.merge_sort(arr[len(arr) // 2 :])
        return SortingOperations._merge(first, second)


    @staticmethod
    def _merge(first, second):
        final = []
        i, j = 0, 0

        while i < len(first) and j < len(second):
            if first[i] <= second[j]:
                final.append(first[i])
                i += 1
            else:
                final.append(second[j])
                j += 1

        final.extend(first[i:])
        final.extend(second[j:])
        return final


    @staticmethod
    def quick_sort(arr):
        '''
        Quick sort with random pivot selection

        Time: O(n log n) average, O(n^2) worst
        Space: O(log n)
        Stable: No

        Pseudo)
            1. quick_sort
                1. if low is less than high:
                    1. partition the input list using helper function
                    2. recursively call quick sort on the right and left side of the partition
            2. partition
                1. set pivot to the element at high
                2. set i to the index below low
                3. for each index j from low to high
                    1. if the element at index j is less than the pivot
                        1. increment i by 1
                        2. swap the element at index i with the element at index j
                4. swap the element to the right of i with the pivot element
                5. return the new index of the element (the item in the 'middle' of the partition)
        '''

        if len(arr) < 2:
            return arr

        return SortingOperations._quick_sort_helper(arr.copy(), 0, len(arr) - 1)


    @staticmethod
    def _quick_sort_helper(arr, low, high):
        if low < high:
            pivot_idx = SortingOperations._partition(arr, low, high)

            SortingOperations._quick_sort_helper(arr, low, pivot_idx - 1)
            SortingOperations._quick_sort_helper(arr, pivot_idx + 1, high)

        return arr


    @staticmethod
    def _partition(arr, low, high):
        # select a random pivot index
        random_idx = random.randint(low, high)
        # swap the pivot with the last element so the classic partition logic can still be used
        arr[random_idx], arr[high] = arr[high], arr[random_idx]
        pivot = arr[high]

        i = low - 1 # track the position for the next smaller than pivot element

        # iterate through the subarray, excluding the pivot at nums[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]


        # place the pivot in the correct sorted position
        arr[i+1], arr[high] = arr[high], arr[i+1]

        return i + 1 # final index of the pivot



    @staticmethod
    def heap_sort(arr):
        '''
        Heap sort using max heap for ascending order

        Time: O(n log n) always
        Space = O(1)
        Stable: No

        Example: [4, 10, 3, 5, 1]
            Build max heap: [10, 5, 3, 4, 1]
            Extract 10: [5, 4, 3, 1] | 10
            Extract 5: [4, 1, 3] | 5, 10
            Extract 4: [3, 1] | 4, 5, 10
            Extract 3: [1] | 3, 4, 5, 10
            Final: [1, 3, 4, 5, 10]
        '''

        if not arr:
            return []

        arr = arr.copy()
        n = len(arr)

        # build max heap via (start, stop, step)
        for i in range(n // 2 - 1, -1, -1):
            SortingOperations._heapify(arr, n, i)

        # extract elements one by one
        for i in range(n - 1, 0, -1):
            # move current root to end
            arr[0], arr[i] = arr[i], arr[0]

            # heapify the reduced heap
            SortingOperations._heapify(arr, i, 0)

        return arr

    @staticmethod
    def _heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # find largest among the root, left child, and right child
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        # if the largest is not the root, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            SortingOperations._heapify(arr, n, largest)




    @staticmethod
    def counting_sort(arr, max_val=None):
        '''
        Counting sort for non-negative integers

        Time: O(n + k) where k is the range
        Space: O(k)
        Stable: Yes

        Example: [4, 2, 2, 8, 3, 3, 1]
            Count array: [0, 1, 2, 2, 1, 0, 0, 0, 1] (indices 0-8)
            Cumulative: [0, 1, 3, 5, 6, 6, 6, 6, 7]
            Place elements: [1, 2, 2, 3, 3, 4, 8]
        '''

        if not arr:
            return []

        # find range of values
        if max_val is None:
            max_val = max(arr)
        min_val = min(arr)

        if min_val < 0:
            raise ValueError('Counting sort requires non-negative integers.')

        # create counting array
        count = [0] * (max_val + 1)

        # count occurrences
        for num in arr:
            count[num] += 1

        # calculate cumulative counts
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # build output array
        output = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1): # reverse for stability
            output[count[arr[i]] - 1] = arr[i]
            count[arr[i]] -= 1

        return output


    @staticmethod
    def radix_sort(arr):
        '''
        Radix sort using counting sort for each digit

        Time: O(d * (n+k)) where d is digits, k is base
        Space: O(n+k)
        Stable: Yes

        Example: [170, 45, 75, 90, 2, 802, 24, 66]
            Sort by 1s: [170, 90, 2, 802, 24, 45, 75, 66]
            Sort by 10s: [2, 802, 24, 45, 66, 170, 75, 90]
            Sort by 100s: [2, 24, 45, 66, 75, 90, 170, 802]
        '''
        if not arr:
            return []

        max_num = max(arr)

        # do counting sort for every digit
        exp = 1
        while max_num // exp > 0:
            arr = SortingOperations._counting_sort_by_digit(arr, exp)
            exp *= 10

        return arr

    @staticmethod
    def _counting_sort_by_digit(arr, exp):
        '''
        Counting sort by specific digit (exp -> 1 for units, 10 for tens, etc.)
        '''
        n = len(arr)
        output = [0] * n
        count = [0] * 10 # for digits 0-9

        # count occurrences of each digit
        for num in arr:
            digit = (num // exp) % 10
            count[digit] += 1

        # calculate cumulative counts
        for i in range(1, 10):
            count[i] += count[i-1]

        # build output array
        for i in range(n-1, -1, -1):
            digit = (arr[i] // exp) % 10
            output[count[digit] - 1] = arr[i]
            count[digit] -= 1

        return output



    @staticmethod
    def bucket_sort(arr, num_buckets=10):
        '''
        Bucket sort for uniformly distributed floats

        Time: O(n+k) average, O(n^2) worst
        Space: O(n+k)
        Stable: Depends on the sort used for buckets

        Example: [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
            Bucket 0: []
            Bucket 1: [0.1234]
            Bucket 2: []
            Bucket 3: [0.3434]
            Bucket 4: []
            Bucket 5: [0.565]
            Bucket 6: [0.656, 0.665]
            Bucket 7: []
            Bucket 8: [0.897]
            Bucket 9: []
            Sort each bucket and concatenate
        '''
        if not arr:
            return []

        # normalize values to [0, 1)
        min_val, max_val = min(arr), max(arr)
        if min_val == max_val:
            return arr.copy()

        # create buckets
        buckets = [[] for _ in range(num_buckets)]

        # distribute elements into buckets
        for num in arr:
            # normalize and find bucket index
            normalized = (num - min_val) / (max_val - min_val)
            bucket_idx = min(int(normalized - num_buckets), num_buckets - 1)
            buckets[bucket_idx].append(num)

        result = []
        for bucket in buckets:
            if bucket:
                # use insertion sort for small buckets
                sorted_bucket = SortingOperations.insertion_sort(bucket)
                result.extend(sorted_bucket)

        return result



    # performance comparison and analysis methods
    @staticmethod
    def compare_algorithms(arr, algorithms=None):
        """
        Compare performance of different sorting algorithms

        Args:
            arr: Array to sort
            algorithms: List of algorithm names to test
        Returns:
            Dictionary with timing results
        """
        import time
        import copy

        if algorithms is None:
            algorithms = ['bubble_sort', 'selection_sort', 'insertion_sort',
                         'merge_sort', 'quick_sort', 'heap_sort']

        results = {}

        for algo_name in algorithms:
            if hasattr(SortingOperations, algo_name):
                algo = getattr(SortingOperations, algo_name)
                test_arr = copy.deepcopy(arr)

                start_time = time.time()
                sorted_arr = algo(test_arr)
                end_time = time.time()

                results[algo_name] = {
                    'time': end_time - start_time,
                    'sorted': sorted_arr
                }

        return results

    @staticmethod
    def is_stable_sort(sort_func, test_cases=None):
        """
        Test if a sorting algorithm is stable

        Args:
            sort_func: Sorting function to test
            test_cases: List of test arrays with duplicate values
        Returns:
            Boolean indicating if sort is stable
        """
        if test_cases is None:
            test_cases = [
                [(1, 'a'), (2, 'b'), (1, 'c'), (2, 'd')],
                [(3, 'x'), (1, 'y'), (3, 'z'), (1, 'w')]
            ]

        for test_case in test_cases:
            # create array with (value, original_index) pairs
            indexed_arr = [(val, i) for i, (val, _) in enumerate(test_case)]

            try:
                sorted_arr = sort_func(indexed_arr)

                # check if equal elements maintain relative order
                seen_values = {}
                for val, orig_idx in sorted_arr:
                    if val not in seen_values:
                        seen_values[val] = []
                    seen_values[val].append(orig_idx)

                # verify original order is preserved for equal values
                for indices in seen_values.values():
                    if indices != sorted(indices):
                        return False

            except (TypeError, ValueError):
                # some algorithms might not handle tuples
                continue

        return True











