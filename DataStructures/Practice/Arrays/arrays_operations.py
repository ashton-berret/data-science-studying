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
        pass

    @staticmethod
    def binary_search(arr, target):
        '''
            Search for a target in a sorted array using binary search
        '''
        pass




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
        pass

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

        pass

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

        pass





    @staticmethod
    def find_max_min(arr):
        '''Find the maximum and minimum values.

            Q) What is the time complexity?
                a) O(n)

        '''
        pass

    @staticmethod
    def remove_duplicates(arr):
        '''Remove duplicates from sorted array.

            Q) What is the time complexity?
                a) O(n)
            Q) Why is it not advised to try to remove the duplicates in place using pop()?
                a) Using pop() can cause issues with indexing since we are reducing the size of the array each time, causing tracking i to become difficult
        '''
        pass




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
        pass



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
        pass



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

        pass


    @staticmethod
    def kadanes_algorithm_with_subarray(arr):
        '''find the maximum subarray and return the value, along with the start and end indicies

            Q) What are the additional variables we need to track in order to also return the indices? (Hint: 3)
                a) start, global_start, global_end

        '''
        pass









