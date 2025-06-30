class ArrayOperations:

    '''
        Common array operations and patterns
    '''

    @staticmethod
    def find_element(arr, target):
        '''Linear search in an arrays

            Q) What is the time complexity?
                a)
        '''
        for i, element in enumerate(arr):
            if element == target:
                return i

        return -1

    @staticmethod
    def binary_search(arr, target):
        '''
            Search for a target in a sorted array using binary search
        '''

        if not arr:
            return -1

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
    def reverse_array(arr):
        '''Reverse an array in-place.

            Q) What is the time and space complexity?
                a) O(n), O(1)
            Q) What two pointers do we have to instantiate?
                a) start and end
            Q) What type of loop does this require?
                a) while

        '''

        if not arr:
            return []

        left = 0
        right = len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr


    @staticmethod
    def merge_sorted_arrays(nums1, m, nums2, n):
        '''
            Merge nums2 into nums1 in place. nums1 has size m+n with m elememnts

            Args:
                num1s: List with m elements followed by n zeros
                m: number of elements in nums1
                nums2: list with n elements
                n: number of elements in nums2

            Q) What is the time and space complexity?
                a) Time is O(m+n)
                a) Space is O(1)
        '''
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        return nums1

    @staticmethod
    def search_insert(nums, target):
        '''
            Find the index where the target should be inserted to keep the array sorted

            Args:
                nums: sorted list of integers
                target: number to be inserted

            Returns:
                the index where the target should be insorted

            Q) What is the time and space complexity?
                a) O(log n)
                a) O(1)
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
                nums: sorted list of integers
                target: number to be inserted

            Returns:
                [first_index, last_index] or [-1, -1] if not found

            Q) What is the time and space complexity
                a) O(log n)
                a) O(1)

        '''

        def find_first(nums, target):
            first_pos = -1
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    first_pos = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return first_pos

        def find_last(nums, target):
            last_pos = -1
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    last_pos = mid
                    left = mid + 1
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
    def find_max_min(arr):
        '''Find the maximum and minimum values.

            Q) What is the time complexity?
                a) O(n)
            Q) Is range() inclusive or exlusive of the start and end values?
                a) [start, end) --> inclusive of start, exclusive of end (so gets to last index but not last index+1)

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
        '''Remove duplicates from sorted array.

            Q) What is the time complexity?
                a) O(n)
            Q) Why is it not advised to try to remove the duplicates in place using pop()?
                a) Using pop() can cause issues with indexing since we are reducing the size of the array each time, causing tracking i to become difficult
        '''
        if not arr:
            return []

        result = [arr[0]]

        for i in range(1, len(arr)):
            if arr[i-1] != arr[i]:
                result.append(arr[i])

        return result



    @staticmethod
    def two_sum(arr, target):
        '''find two numbers that add up to the target.

            Q) What is the time and space complexity?
                a) O(n), O(n)
            Q) What are the mappings in the seen dictionary?
                a) complement and index
            Q) What is the key variable we need to define in addition to the parameter target variable?
                a) Complement
        '''
        seen = {}

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
                a) O(n) time, O(n) space
            Q) What reverse method is implemented here and why?
                a) Triple reverse method
            Q) What check do we need to perform at the beginning of the function?
                a) To see if the number of steps to rotate is longer than the length of the array, then we just have to rotate by the remainder
            Q) There are x number of key steps. How many steps are there? What is the function of each?
                1. Reverse the array
                2. Reverse the first k-elements to partition the subarray and reorder/undo the initial reversal
                3. reverse the second n-k elements to reorder and effectively shift them k indices to the right
            Q) What if we wanted to rotate to the left instead of to the right?
                a) This is the same as shifting n-k elements instead of k elements
        '''
        n = len(arr)
        if n == 0:
            return []

        k = k % n

        arr.reverse()

        arr[:k] = list(reversed(arr[:k]))
        arr[k:] = list(reversed(arr[k:]))

        return arr

    @staticmethod
    def kadanes_algorithm(arr):
        '''Find maximum subarray using Kadane's algorithm.

            Q) What is the time complexity?
                a) O(n)
            Q) What are the key variables we need to track and what should they be initialized to?
                a) current and global maximums, both intialized to the first element in the array
            Q) At each increment of comparison, what is the relationship between the two variables (i.e., independent, dependent, ignorant)
                a)
        '''

        if not arr:
            return 0

        current_max = global_max = arr[0]

        for i in range(1, len(arr)):
            current_max = max(arr[i], arr[i] + current_max)
            global_max = max(global_max, current_max)

        return global_max

    @staticmethod
    def kadanes_algorithm_with_subarray(arr):
        '''find the maximum subarray and return the value, along with the start and end indicies

            Q) What are the additional variables we need to track in order to also return the indices? (Hint: 3)
                a) start, global_start, global_end

        '''
        if not arr:
            return 0, -1, -1

        current_max = global_max = arr[0]
        start = global_start = global_end = 0

        for i in range(1, len(arr)):
            if arr[i] > arr[i] + current_max:
                current_max = arr[i]
                start = i
            else:
                current_max = current_max + arr[i]


            if current_max > global_max:
                global_max = current_max
                global_start = start
                global_end = i

        return global_max, global_start, global_end







