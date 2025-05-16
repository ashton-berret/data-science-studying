class ArrayOperations:

    '''
        Common array operations and patterns
    '''

    @staticmethod
    def find_element(arr, target):
        '''Linear search in an array 
            Q) What is the time complexity?
                a) O(n)
        '''
        for i, element in enumerate(arr):
            if element == target:
                return i 
        return -1

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

        for num in arr:
            if num > max_val:
                max_val = num
            if num < min_val:
                min_val = num

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
        k = k % n
        # reverse the entire array so that the order of sub arrays can be flipped from A + B to B' + A'.
        # this puts the elements in the reverse order of what we need, but sets us up for the next two reversals which 'undo' the reversal of the elements in each section
        arr.reverse()

        #reverse the first k elements - these are the k-shift number of elements that got rotated to the front, we just need to put them back in ascencding order 
        arr[:k].reversed(arr[:k])

        # reverse the remaining elements - these are the n-k shift number of elements that got shifted k spots to the right, we just need to put them back in order 
        arr[k:].reversed(arr[k:])

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









