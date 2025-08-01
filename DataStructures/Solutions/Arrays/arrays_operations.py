class ArrayOperations:

    '''
        Common array operations and patterns
    '''

    @staticmethod
    def find_element(arr, target):
        '''
            Linear search in an array
                Q) What is the time complexity?
                    a) O(n)
        '''
        for i, element in enumerate(arr):
            if element == target:
                return i
        return -1

    @staticmethod
    def binary_search(arr, target):
        '''
            Search for a target in sorted array using binary search

            Args:
                arr: sotrted list of integers
                target: the integer to search for

            Returns:
                index of target if found, -1 if otherwise

            Q) What is the time and space complexity?
                a) Time complexity is O(log n)
                a) Space complexity is O(1)
        '''

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    @staticmethod
    def merge_sorted_arrays(nums1, m, nums2, n):
        '''
            Merge nums2 into nums1 in-place. nums1 has size m+n with m elements

            Args:
                num1s: List with m elements followed by n zeros
                m: number of elements in nums1
                nums2: list with n elements
                n: number of elements in nums2

            Q) What is the time and space complexity?
                a) Time complexity is O(m + n)
                a) Space complexity is O(1)
        '''

        # start from the end and work backwards
        i = m - 1 # last element in nums1
        j = n - 1 # last element in nums2
        k = m + n - 1 # last position in nums1

        # merge from the back
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

    @staticmethod
    def search_insert(nums, target):
        '''
            Find the index where the target should be inserted to keep the array sorted

            Args:
                nums: sorted list of integers
                target: the integer to insert

            Returns:
                the index where the target should be inserted

            Q) What is the space and come complexity?
                a) Time complexity is O(log n)
                a) Space complexity is O(1)
        '''

        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left


    @staticmethod
    def search_range(nums, target):
        '''
            Find the first and last position of target in a sorted array

            Args:
                nums: sorted list of integers (may have duplicates)
                target: integer to search for

            Returns:
                [first_index, last_index] or [-1, -1] if not found

            Q) What is the time and space complexity?
                a) Time complexity is O(log n)
                a) Space complexity is O(1)
        '''

        def find_first(nums, target):
            left = 0
            right = len(nums) - 1
            first_pos = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    first_pos = mid
                    right = mid - 1 # continue searching left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return first_pos

        def find_last(nums, target):
            left = 0
            right = len(nums) - 1
            last_pos = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    last_pos = mid
                    left = mid + 1 # continue searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return last_pos

        first = find_first(nums, target)
        if first == -1:
            return [-1, -1]
        last = find_last(nums, target)
        return [first, last]

    @staticmethod
    def reverse_array(arr):
        '''Reverse an array in-place.

            Q) What is the time and space complexity?
                a) O(n) time
                a) O(1) space
            Q) What two pointers do we have to instantiate?
                a) Left and right starting positions
            Q) What type of loop does this require?
                a) While loop that stops once the pointers reach the middle

        '''
        left = 0
        right = len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

    @staticmethod
    def find_max_min(arr):
        '''Find the maximum and minimum values.
            Q) What is the time complexity?
                a) O(n) time
        '''
        if not arr:
            return None, None

        max_val = min_val = arr[0]

        for i in range(1, len(arr)):
            if arr[i] > max_val:
                max_val = arr[i]
            elif arr[i] < min_val:
                min_val = arr[i]

        return max_val, min_val


    @staticmethod
    def remove_duplicates(arr):
        ''' Remove duplicates from sorted array.

            Q) What is the time complexity?
                a) O(n) time
            Q) Why is it not advised to try to remove the duplicates in place using pop()?
                a) Trying to remove the duplicates in place can cause issues with indexing.
                    When we use the pop() method, we are reducing the size of the array so keeping
                    track of i becomes difficult and inefficient.
       '''
        if not arr:
            return []

        result = [arr[0]]
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                result.append(arr[i])

        return result


    @staticmethod
    def two_sum(arr, target):
        '''find two numbers that add up to the target.
            Q) What is the time and space complexity?
                a) O(n) time
                a) O(n) space
            Q) What are the mappings in the seen dictionary?
                a) {Value, index}
            Q) What is the key variable we need to define in addition to the parameter target variable?
                a) Complement. This variable is used to determine if the indexed value has a pair that allows it to sum to the target (complement is a value in the dictionary).
        '''
        seen = {} # val -> index
        for i, num in enumerate(arr):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

    @staticmethod
    def rotate_array(arr, k):
        '''Rotate array to the right by k steps.
            Q) What is the time and space complexity?
                a) O(n) time
                a) O(1) space
            Q) What reverse method is implemented here and why?
                a) The triple reverse method.
                    This is implemented in order to set us up so that we can partition the two subarrays based on k-size shift.
                    By reversing the original array, all we have to do is slice the array into the subarrays and then reverse those to get the rotated array.
            Q) What check do we need to perform at the beginning of the function?
                a) We need to check if the number of steps to rotate is larger than the array's length.
                    If it is, this is the same as doing a full rotation plus the remainder (modulus) steps.
            Q) There are x number of key steps. How many steps are there? What is the function of each?
                a) 3
                    1) Reverse the entire array
                    2) reverse the first k elements to partition the subarrays and reorder/undo the original reversal.
                    3) reverse the second n-k elements, effectively reordering and shifting them k steps to the right.
            Q) What if we wanted to rotate to the left instead of to the right?
                a) This is the same as shifting n-k steps to the right, rather than k steps to the right. We can just change the parameter of the function from k to n-k.
        '''
        n = len(arr)

        '''
            handle cases where we rotate by more elements than are in the array since this is akin to doing a full rotation + a couple elements
                for example, if we rotate by 10 spaces but the array length is 7, this is the same as rotating by 3 spaces since 10 = 7 + 3, we get the remainder 3
                another example, if we rotate 21 spaces but the array length is 7, this is the same as a full rotation 3 times so the result is the original array
        '''
        if n == 0:
            return []

        k = k % n
        # reverse the entire array so that the order of sub arrays can be flipped from A + B to B' + A'.
        # this puts the elements in the reverse order of what we need, but sets us up for the next two reversals which 'undo' the reversal of the elements in each section
        arr.reverse()

        #reverse the first k elements - these are the k-shift number of elements that got rotated to the front, we just need to put them back in ascencding order
        arr[:k] = list(reversed(arr[:k]))

        # reverse the remaining elements - these are the n-k shift number of elements that got shifted k spots to the right, we just need to put them back in order
        arr[k:]= list(reversed(arr[k:]))

        return arr


    @staticmethod
    def kadanes_algorithm(arr):
        '''Find maximum subarray using Kadane's algorithm.
            Q) What is the time complexity?
                a) O(n) time
            Q) What are the key variables we need to track and what should they be initialized to?
                a) The current and global maxmimum values, they should be initialized to the first element in the array.
            Q) At each increment of comparison, what is the relationship between the two variables (i.e., independent, dependent, ignorant)
                a) The global and current max values are completely independent when the current_max comparison is taking place. Only after this comparison does the global max value become dependent on the current max value.
        '''
        if not arr:
            return 0

        # set the beginning values to the first element in the array and then start comparing at the second element
        current_max = global_max = arr[0]
        for i in range(1, len(arr)):
            current_max = max(arr[i], current_max + arr[i]) # compare the current element with the sum of the previous current max + new element
            global_max = max(current_max, global_max) # compare the current max with the global max

        return global_max

    @staticmethod
    def kadanes_algorithm_with_subarray(arr):
        '''find the maximum subarray and return the value, along with the start and end indicies

            Q) What are the additional variables we need to track in order to also return the indices? (Hint: 3)
                a) start, global_start, and global_end

        '''
        if not arr:
            return 0, -1, -1

        current_max = global_max = arr[0]
        start = global_start = global_end = 0

        for i in range(1, len(arr)):
            # if current element is better than extending the previous subarray
            if arr[i] > current_max + arr[i]:
                current_max = arr[i]
                start = i # start a new subarray at this position
            else:
                current_max = current_max + arr[i]

            # if we found a new global maximum
            if current_max > global_max:
                global_max = current_max
                global_start = start # update the start of the best subarray
                global_end = i # update the end of the best subarray

        return global_max, global_start, global_end









