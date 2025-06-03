from collections import deque

class StackQueueOperations:
    ''' Common stack and queue operations and patterns for coding interviews '''

    # ======================= Stack Implementations ============================

    class ArrayStack:
        ''' stack implementation using python list'''
        def __init__(self):
            '''
                Initialize an empty stack using a list 

                Q) What is the time complexity of stack operations using a list?
                    a) Push: O(1) amortized - list append is O(1) in the average case 
                    a) Pop: O(1) - list pop from end is O(1)
                    a) Peek: O(1) - accessing last element is O(1)
                Q) What is the space complexity?
                    a) O(n)
                Q) Why do we use the end of the list as the top of the stack?
                    a) Because appending/removing fro the end of the list is O(1) while inserting removing from the beginning is O(n) (have to shift everything to the end once)

            '''

            self.items = []



        def push(self, item):
            '''
                Add an element to the top of the stack 

                Args:
                    item: element to add to stack 
                
                Example Stack) 
                    stack = [1, 2, 3], push(4) --> stack = [1, 2, 3, 4]
            '''
            
            self.items.append(item)


        def pop(self):
            '''
                Remove and return the top element from the stack 

                Returns:
                    top element from the statck

                Raises:
                    index error if stack is empty
            '''
            if self.is_empty():
                raise IndexError('Pop from empty stack')
            return self.items.pop()

        def peek(self):
            '''
                Return the element at the top of the stack without removing it 

                Returns:
                    top element in stack 

                Raises:
                    IndexError if empty stack 
            '''
            if self.is_empty():
                raise IndexError('Peek from empty stack')
            return self.items[-1]

        
        def is_empty(self):
            '''
                Checks if the stack is empty 

                Returns:
                    true if empty, false otherwise
            '''
            return len(self.items) == 0

        def size(self):
            '''
                Returns the number of elements in the stack 

                Returns:
                    number of elements in the stack 
            '''
            return len(self.items)

    class ArrayQueue:
        ''' Queue implementation using a python list (this is inefficient, this is just for demo) '''

        def __init__(self):
            '''
                Initialize an empty queue using a list 

                Q) Why is this implementation inefficient?
                    a) Removing from the front of the list requires shifting all the elements, making dequeue O(n)
                Q) What is the time complexity of queue operations using a list?
                    a) Enqueue: O(1) --> adding to end of list 
                    b) Dequeue: O(n)
                Q) When could you use this?
                    a) When queue size is small and simplicity is more important than performance
            '''
            self.items = []

        def enqueue(self, item):
            '''
                Add an element to the rear of the queue 
            '''
            self.items.append(item)

        def dequeue(self):
            '''
                Remove an element from the front of the queue 
            '''
            if self.is_empty():
                raise IndexError('dequeue from an empty queue')
            return self.items.pop(0)

        def front(self):
            '''
                Return the front element without removing it 
            '''
            if self.is_empty():
                raise IndexError('Front of queue is empty')
            return self.items[0]

        def is_empty(self):
            '''
                Check if queue is empty 
            '''
            return len(self.items) == 0

        def size(self):
            '''
                Return the number of elements in the queue 
            '''
            return len(self.items)

    class DequeQueue:
        ''' Efficient implementation using collections.deque (pronounced deck) '''

        def __init__(self):
            '''
                Initialize an empty queue

                Q) What is the time complexity of deque operations?
                    a) Enqueue (append): O(1)
                    a) Dequeue (pop): O(1)
                    a) All operations are O(1)
                Q) What is deque optimized for?
                    a) Fast appends and pops from both ends of the container
                Q) What are the differences between deque and list implementation?
                    a) Memory structure: Lists contains contiguous block of memory, Deque contains doubly linked fixed size blocks of memory 
                    a) Access: Lists use index-based access (direct memory address calculations (base_address + (index * element size)), Deques use L and R pointers (initialized at middle element))
                Q) What are the differences in performance for the given operations?
                    a) Right appends: 
                        List -> O(1) (amortized)
                        Deque -> O(1)
                    a) Right pops:
                        List -> O(1)
                        Deque -> O(1)
                    a) Insert/Pop (Left):
                        List -> O(n)
                        Deque -> O(1)
                    a) Random Access:
                        List -> O(1)
                        Deque -> O(n)
                    a) Memory usage:
                        List -> Lower
                        Deque -> Higher

            '''
            self.items = deque()


        def enqueue(self, item):
            '''
                Add an element to the rear of the queue 
            '''
            self.items.append(item)

        def dequeue(self):
            '''
                Remove and return the front element from the queue 
            '''
            if self.is_empty():
                raise IndexError('Removing from empty queue')
            return self.items.popleft()

        def front(self):
            '''
                Return the front element in the queue without removing items
            '''
            if self.is_empty():
                raise IndexError('Peeking from empty queue')
            return self.items[0]

        def rear(self):
            '''
                Return the back element in the queue without removing it 
            '''
            if self.is_empty():
                raise IndexError('Peeking from empty queue')
            return self.items[-1]

        def is_empty(self):
            '''
                Check if the queue is empty 
            '''
            return len(self.items) == 0

        def size(self):
            '''
                Return the number of elements in the queue 
            '''
            return len(self.items)


    #===================Stack Applications =================
    @staticmethod
    def valid_parentheses(s):
        '''
            Check if a string of parentheses is valid (valid if each bracket has a matching closing bracket and is closed in the correct order)

            Args:
                s: string containing only '(', ')', '{', '}'. '[', ']'

            Returns:
                True if valid, false otherwise 

            Q) What is the time and space complexity?
                a) Time complexity is O(n) -> single pass through the array 
                a) Space complexity is O(n)
            Q) Why is a stack the perfect data structure for this problem?
                a) LIFO property matches the nested structure of the valid parenthesis

        '''
        stack = []
        mapping = {')':'(', '}':'{', ']':'['} 
        for i in s:
            if i in mapping: # if it is a closing bracket
                if not stack or stack.pop() != mapping[i]:
                    return False 
            else: # if it is an opening bracket 
                stack.append(i) 
        return len(stack) == 0

    @staticmethod 
    def evaluate_postfix(expression):
        '''
            Evaluate a postfix expression 

            Args:
                expression: list of strings representing a postfix expression 
                    - postfix notation is reverse polish notation, where operators come after operands (i.e., "3 4 +" means 3 + 4)

            Returns:
                result of expression evaluation 

            Q) What is the time and space complexity?
                a) Time is O(n), single pass through the expression 
                a) Space is O(n), stack holds up to n operands 
            Q) Why is a stack ideal for this?
                a) We need to store operands until we encounter an operator, then apply the operator to the most recent operand 

            Example Walkthrough) expression = ["2", "1", "+", "3", "*"]
                1. Initialize stack = []
                2. token = "2", number, push to stack, stack = [2]
                3. token = "1", number, push to stack, stack = [2, 1]
                4. token = "+", operator, pop 1 and 2, compute 2 + 1 = 3, push stack [3]
                5. token = "3", number, push to stack [3,3]
                6. token = "*", operator, pop 1 and 2, compute 3*3, push to stack, 9
                7. return stack[0] = 9

        '''

        stack = []
        operators = ['+', '-', '*', '/']
        for i in expression:
            if i in operators:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    result = a + b 
                elif token == '-':
                    result = a - b 
                elif token == '*':
                    result = a * b 
                else:
                 result = a / b 

                stack.append(result)
            else:
                stack.append(i)
        return stack[0]


    @staticmethod
    def daily_temperatures(temperatures):
        '''
            Find the number of days until a warmer temperature for each day

            Args:
                temperatures: list of daily temperatures 

            Returns:
                an array where array[i] is the number of days after i until a warmer temperature 

            Q) What is the time and space complexity?
                a) Time complexity is O(n), each element is pushed and popped at most once 
                a) Space complexity is O(n), stack holds up to n indices
            Q) What pattern does this problem follow?
                a) Monotonic stack pattern - stack maintains element in monotonic order.
                    - A stack is monotonic if when starting at the bottom of the stack, each element is either in increasing or decreasing order  
            Q) What do we store in the stack?
                a) Indices (not temperatures) so we can calculate the distance between days 
            Q) In this problem, why is the stack always in decreasing order? What does this mean about the comparison between the most recent waiting day and the previous days?
                a) The stack is always decreasing, because if the value at i + 1 could solve i, i would be automatically removed. It is impossible to have an out of order stack.
                a) This means that the most recent day is always the point of the comparison with the lowest requirement (i.e., the lowest barrier to being solved)

            Example Walkthrough) temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
                1. Initialize result = [0]*8 (num of temps), stack = []
                2. i = 0, temp = 73, stack empty, push i=0, stack = [0]
                3. i = 1, temp = 74, 74>73, pop stack[0], result[0] = 1-0 = 1, push 1, stack = [1]
                4. i = 2, temp = 75, 75>74, pop stack[0], result[1] = 2-1 = 1, push 2, stack = [2]
                5. i = 3, temp = 71, push to stack, stack = [2,3]
                6. i = 4, temp = 69, push to stack, stack = [2,3,4]
                7. i = 5, temp = 72:
                    - 72 > 69, pop stack[4], result[4] = 5-4 = 1, result[4] = 1
                    - 72 > 71, pop stack[3], result[3] = 5 - 3 = 2, result[3] = 2
                    - 72 < 75, push to stack, stack = [2, 5]
                8. i = 6, temp = 76:
                    - 76 > 72, pop stack[5], result[5] = 6 - 5 = 1, result[5] = 1
                    - 76 > 75, pop stack[2], result[2] = 6 - 2 = 4, result[2] = 4
                    - push to stack, stack = [6]
                9. i = 7, temp = 73, push to stack, stack = [6,7]
                10. return result = [1, 1, 4, 2, 1, 1, 0, 0]
        '''
        result = [0] * len(temperatures)
        waiting_days = []
        

        for current_day, current_temp in enumerate(temperatures):
            while waiting_days and temperatures[waiting_days[-1]] < current_temp: # while there are days in the waiting stack and the temperature today is > than the last/easiest day's temp 
                most_recent_waiting_day = waiting_days.pop() # get the index of the last/easiest waiting day 
                result[most_recent_waiting_day] = current_day = most_recent_waiting_day # the respective index's value is the number of days waited 

            stack.append(current_day) # if there are no days waiting or if the current temperature does not satisfy the requirements, we add the current day's index to the waiting stack at the end 

        return result



    @staticmethod
    def implement_stack_using_queues():
        '''
            Implement a stack using only queue operations 

            Q) What is the time complexity of stack operations using two queues?
                a) Push: O(n) -> need to move all elements between queues 
                a) Pop: O(1) -> just deque from the main queue 
            Q) What is the key insight for this implementation?
                a) To maintain LIFO order with FIFO operations, we need to just need to reverse the order of the elements
        '''

        class MyStack():
            def __init__(self):
                '''
                    Example walkthrough) Push operations push(1), push(2), push(3)
                        1. push(1):
                            q1 = [1], q2 = []
                        2. push(2):
                            add 2 to q2 -> q2 = [2]
                            move all from q1 to q2 -> q1 = [], q2 = [2,1]
                            swap q1 and q2 -> q1 = [2,1], q2 = []
                        3. push(3):
                            add 3 to q2
                            move all from q1 to q2, q1 = [], q2 = [3, 2, 1]
                            swap q1 and q2 = q1 = [3,2,1], q2 = []
                        4. pop(): dequeues 3 from q1 in LIFO order (just to be super clear, we have to pop from the left to mimic lifo, popping from right would be fifo)
                '''

                self.q1 = deque()
                self.q2 = deque()

            def push(self, x):
                '''
                    Push element onto stack 
                '''
                self.q2.append(x)
                
                # move items from q1 to q2
                while self.q1:
                    self.q2.append(self.q1.popleft())

                # swap the queues 
                self.q1, self.q2 = self.q2, self.q1

            def pop(self):
                '''
                    Remove the leftmost element 
                '''
                if not self.q1:
                    raise IndexError('Popping from empty stack')
                return self.q1.popleft()

            def top(self):
                '''
                    Return the value of the leftmost element without removing it 
                '''
                if not self.q1:
                    raise IndexError('Empty stack')
                return self.q1[0]

            def empty(self):
                '''
                    Check to see if the stack is empty 
                '''
                return len(self.q1) == 0

        return MyStack()


    @staticmethod 
    def implement_queue_using_stacks():
        '''
            Implement a queue using only stack operations 

            Q) What is the time complexity of queue operations using two stacks?
                a) Enqueue: O(1) -> just push to input stack 
                a) Dequeue: O(1) amortized, each element is moved at most twice 
            Q) What is the key insight for this implementation?
                a) Use two stacks to reverse the order twice, getting FIFO from LIFO 
        '''

        class MyQueue:
            def __init__(self):
                '''
                    Example Walkthrough) Operations: enqueue(1), enqueue(2), dequeue(), enqueue(3), dequeue()
                        1. enqueue(1): input_stack = [1], output_stack = []
                        2. enqueue(2): input_stack = [1, 2], output_stack = []
                        3. dequeue(): 
                           - output_stack empty, transfer from input_stack
                           - Pop from input_stack and push to output_stack: [2] → [], [1] → [], [] → [2], [] → [2, 1]
                           - input_stack = [], output_stack = [2, 1]
                           - Pop from output_stack returns 1 (FIFO achieved!)
                        4. enqueue(3): input_stack = [3], output_stack = [2]
                        5. dequeue(): output_stack not empty, pop returns 2
                '''
                self.input_stack = []
                self.output_stack = []
            
            def enqueue(self, x):
                '''Add element to rear of queue'''
                self.input_stack.append(x)
            
            def dequeue(self):
                '''Remove and return front element'''
                if not self.output_stack:
                    # Transfer all elements from input to output
                    while self.input_stack:
                        self.output_stack.append(self.input_stack.pop())
                
                if not self.output_stack:
                    raise IndexError("dequeue from empty queue")
                
                return self.output_stack.pop()
            
            def front(self):
                '''Return front element without removing'''
                if not self.output_stack:
                    while self.input_stack:
                        self.output_stack.append(self.input_stack.pop())
                
                if not self.output_stack:
                    raise IndexError("front from empty queue")
                
                return self.output_stack[-1]
            
            def empty(self):
                '''Check if queue is empty'''
                return len(self.input_stack) == 0 and len(self.output_stack) == 0
        
        return MyQueue()
    
    @staticmethod 
    def sliding_window_maximum(nums, k):
        '''
            Find the maximum element in each sliding window of size k.

            Args:
                nums: list of integers
                k: window size 

            Returns:
                list of maximum elements in each window 

            Q) What is the time and space complexity?
                a) Time complexity is O(n)
                a) Space complexity is O(k) -> deque stores at most k elements 
            Q) What type of queue do we use and why?
                a) Deque (double ended queue) -> since we need to remove from both ends 
            Q) What do we store in the deque?
                a) Indices in decreasing order of their values 

            Example Walkthrough) nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
                1. result = [], dq = deque()
                2. i = 0, num = 1, dq = [0]
                3. i = 1, num = 3, 3 > 1, remove 1, dq = [1]
                4. i = 2, num = -1, -1 < 3, dq = [1,2], window complete, max = nums[1] = 3
                5. i = 3, num = -3, -3 < -1, dq = [1,2,3], max = nums[1] = 3
                6. i = 4, nums = 5, 5 > all previous, dq = [4], max = nums[4] = 5
                7. i = 5, nums = 3, 3 < 5, dq = [4, 5], max = nums[4] = 5
                8. i = 6, nums = 6, 6 > all previous, dq = [6], max = nums[6] = 6
                9. i = 7, nums = 7, 7 > all previous, dq = [7], max = nums[7] = 7
                10. return [3, 3, 5, 5, 6, 7]
        '''

        if not nums or k == 0:
            return []

        result = []
        dq = deque()

        for i in range(len(nums)):
            # remove indicies otuside current window 
            while dq and dq[0] <= i - k:
                dq.popleft()

            # remove indicies whose values are smaller than current element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # add maximum to result when window is complete 
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result 

    
    @staticmethod
    def first_negative_in_window(nums, k):
        '''
            Find the first negative number in each sliding window of size k.

            Args:
                nums: a list of integers 
                k: window size 
            
            Returns:
                list of first negative numbers in each window, 0 if no negative 

            Q) What is the time and space complexity?
                a) Time complexity is O(n) -> each element is processed once 
                a) Space complexity is O(k) -> store at most k negative numbers 
            
            Example Walkthrough) nums = [12, -1, -7, 8, -15, 30, 16, 28], k = 3
                1. result = [], negatives = deque()
                2. Window [12, -1, 7], negatives = [-1, -7], first = -1 
                3. Window [-1, -7, 8], negatives = [-1, -7], first = -1 
                4. window = [-7, 8, -15], remove -1, negatives = [-7, -15], first = -7 
                5. window = [8, -15, 30], remove -7, negatives = [-15], first = -15
                6. window = [-15, 30, 16], remove 8, negatives = [-15], first = -15 
                7. window = [30, 16, 28], remove -15, negatives = [], first = 0
                8. return [-1, -1, -7, -15, -15, 0]
        '''

        if not nums or k == 0:
            return []

        result = []
        negatives = deque() # store indices of negative numbers 

        for i in range(len(nums)):
            # remove indices outside curent window 
            while negatives and negatives[0] <= i - k:
                negatives.popleft()

            if nums[i] < 0:
                negatives.append(i)

            # add result when window is complete
            if i >= k - 1:
                if negatives:
                    result.append(nums[negatives[0]])
                else:
                    result.append(0)

        return result
