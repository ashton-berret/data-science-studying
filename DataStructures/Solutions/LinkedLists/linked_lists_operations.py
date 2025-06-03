class ListNode:
    ''' Standard singly linked list node'''

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

    def __repr__(self):
        return f"ListNode({self.val})"

class DoublyListNode:
    '''Doubly linked list node'''
    
    def __init__(self, val=0, prev=None, next=None):
        self.val = val 
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"DoublyListNode({self.val})"

class LinkedListOperations:
    ''' Common linked list operations and patterns for coding interviews'''

    # ===================== Basic Linked List Implementations =======================

    class SinglyLinkedList:
        ''' Basic singly linked list implementation '''
        
        def __init__(self):
            '''
                Implement an empty singly linked list 

                Q) What is the time and space complexity?
                    a) Time complexity is O(1)
                    a) Space complexity is O(1)
                Q) What is a dummy head and why use it?
                    a) A dummy head is a ghost node at the beginning of a linked list, it doesn't contain any value but serves as a placeholder for the starting point so that we don't have to
                        duplicate code within a while loop to figure out which value should serve as the head. 
                    a) We use it to:
                        1. Simplify edge cases like empty list operations 
                        2. Have consistent handling for insertion/deletion operations on the first node 
                        3. Reduce conditional logic within methods since we don't need any checks, we know exactly what is in the starting node
            '''
            self.dummy_head = ListNode(0)
            self.size = 0

        def get(self, index):
            '''
                Get the value of the node at the given index 

                Args: 
                    index: 0-based index 

                Returns:
                    value at index, or -1 if invalid 

                Q) What is the time and space complexity?
                    a) Time complexity is O(index) since we have to traverse to the position
                    a) Space complexity is O(1)
            '''
            if index < 0 or index >= self.size:
                return -1

            current = self.dummy_head.next
            for _ in range(index):
                current = current.next
            
            return current.val

        def add_at_head(self, val):
            '''
               Add a node at the beginning of the list 

               Args:
                   val: value to add 

                Q) What is the time and space complexity?
                    a) Time complexity is O(1)
                    a) Space complexity is O(1)
            '''
                
            new_node = ListNode(val)
            new_node.next = self.dummy_head.next
            self.dummy_head.next = new_node
            self.size += 1

        def add_at_tail(self, val):  
            '''
               Add a node at the end of the list 

               Args:
                   val: value to add 

                Q) What is the time and space complexity?
                    a) Time complexity is O(n) -> have to traverse to the end of the list 
                    a) Space complexity is O(1)
            '''
            new_node = ListNode(val)
            current = self.dummy_head

            while current.next:
                current = current.next # think of this as just iterating i 

            current.next = new_node 
            self.size += 1
            
        def add_at_index(self, index, val):
            '''
                Add a value at a specified index 

                Args:
                    index: the index to add the value at 
                    val: the value to add 

                Q) What is the time and space complexity?
                    a) Time complexity is O(index)
                    a) Space complexity is O(1)
            '''

            if index > self.size:
                return 

            if index < 0:
                index = 0

            current = self.dummy_head 
            for _ in range(index):
                current = current.next

            new_node = ListNode(val)
            new_node.next = current.next
            current.next = new_node 
            self.size += 1

        def delete_at_index(self, index):
            '''
                Delete a node at a given index

                Args:
                    index: the index of the node to delete 

                Q) What is the time and space complexity?
                    a) Time complexity is O(n)
                    a) Space complexity is O(1)
            '''

            if index < 0 or index >= self.size:
                return

            current = self.dummy_head
            for _ in range(index):
                current = current.next 

            current.next = current.next.next # replace the next node with the node after that, effectively deleting the node  
            self.size -= 1


        def to_list(self):
            '''
                Convert the linked list to a python list 
            '''
            
            result = []
            current = self.dummy_head.next
            while current:
                result.append(current.val)
                current = current.next 

            return result

    class DoublyLinkedList:
        ''' Basic Doubly Linked List Implementation '''

        def __init__(self):
            '''
                Initializes an empty doubly linked list with sentinel nodes (head and tail dummy nodes)

                Q) Why do we use sentinel nodes?
                    a) No need to check for None when accessing prev/next, consistent edge case handling, easier insertion/deletion logic 
            '''
            self.head = DoublyListNode(0)
            self.tail = DoublyListNode(0)
            self.head.next = self.tail
            self.tail.prev = self.head 
            self.size = 0

        
        def _add_between(self, val, before, after):
            '''
                Helper method to add a node between two existing nodes

                Q) What is the key thing we have to remember when adding between two nodes? What has to be updated compared to Singly linked List?
                    a) We have to update two pointers, not just one. The before/predecessor pointer and the after/sucessor node
            '''
            
            new_node = DoublyListNode(val, before, after) 
            before.next = new_node
            after.prev = new_node 
            self.size += 1

        def add_first(self, val):
            '''
                Add an element to the beginning (after dummy head)
            '''
            self._add_between(val, self.head, self.head.next)

        def add_last(self, val):
            '''
                Add an element to the end (before dummy tail)
            '''
            self._add_between(val, self.tail.prev, self.tail)

        def _remove_node(self, node):
            '''
                Helper method to remove a specific node 
            '''
            before = node.prev 
            after = node.next 
            before.next = after
            after.prev = before 
            self.size -= 1
            return node.val

        def remove_first(self):
            '''
                Remove the first element after the dummy head 
            '''
            if self.is_empty():
                raise IndexError('Empty list')
            return self._remove_node(self.head.next)

        def remove_last(self):
            '''
                Remove the last element before tail 
            '''
            if self.is_empty():
                raise IndexError('empty list')
            return self._remove_node(self.tail.prev)
        
        def is_empty(self):
            return self.size == 0

        def to_list(self):
            result = []
            current = self.head.next

            while current != self.tail:
                result.append(current.val)
                current = current.next

            return result


    #====================== Helper methods ================

    @staticmethod
    def create_linked_list(values):
        '''
            Create a linked list from a list of values 

            Args: 
                values: list of values

            Returns: 
                head node of the created list 

            Example Walkthrough) head = create_linked_list([1, 2, 3,]) creates 1->2->3->None 
        '''
        if not values:
            return None

        head = ListNode(values[0])
        current = head 

        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next 

        return head 

    @staticmethod
    def linked_list_to_list(head):
        '''
            Convert linked list to python list 

            Args:
                head: head node of LL 

            Returns:
                list of values
        '''

        result = []
        current = head 
        while current:
            result.append(current.val)
            current = current.next 

        return result 

    @staticmethod
    def print_linked_list(head):
        values = LinkedListOperations.linked_list_to_list(head)
        return " -> ".join(map(str, values)) + " -> None"


    #====================== Core Linked List Operations =======================

    @staticmethod
    def reverse_linked_list(head):
        '''
            Reverse a singly linked list iteratively

            Args:
                head node of LL 

            Returns:
                head of reversed LL 

            Q) What is the time and space complexity?
                a) Time complexity is O(n) -> traverse through the list 
                a) Space complexity is O(1)
            Q) What is the general algorithm for the reversal?
                a) 3 steps:
                    1. Use three pointers: prev, current, next
                    2. For each node, reverse the link direction
                    3. Move pointers forward 
        '''

        prev = None
        current = head 

        while current: 
            next_node = current.next # store the next node before we lose it 
            current.next = prev # reverse the link (pointer, not val)
            prev = current # move prev forward 
            current = next_node # move current forward

        return prev


    @staticmethod
    def reverse_linked_list_recursive(head):
        '''
            Reverse a singly linked list recursively 

            Q) What is the time and space complexity?
                a) Time complexity is O(n)
                a) Space complexity is O(n) due to recursion stack 
        '''

        # best case is an empty list or single node 
        if not head or not head.next:
            return head 

        # recursively reverse the rest of the list
        new_head = LinkedListOperations.reverse_linked_list_recursive(head.next)

        # reverse the current connection
        head.next.next = head 
        head.next = None

        return new_head

    @staticmethod
    def has_cycle(head):
        '''
            Detect if a linked list has a cycle using Floyd's algorithm 

            Args:
                head: head of a linked list

            Returns: 
                true if cycle, false otherwise

            Q) What is the time and space complexity?
                a) Time complexity is O(n)
                a) Space complexity is O(1)

            Example Walkthrough/Algorithm)
                1. Think tortoise and hare 
                2. Use two pointers:
                    - slow moves one step 
                    - fast moves two steps
                3. if theres a cycle, fast will eventually meet slow 
                4. If no cycle, fast will reach None
        '''

        if not head or not head.next:
            return False 

        slow = head
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

            if slow == fast:
                return True 

        return False 

    @staticmethod 
    def find_cycle_start(head):
        '''
            Find the starting node of a cycle in a linked list 

            Algorithm:
                1. Find a cycle via Floyd's algorithm 
                2. Return one pointer to head 
                3. Move both pointers one step until they meet 
                4. Meeting point is the cycle start 
            
            Proof:
                1. let distance from head to cycle start = a 
                2. let distance from cycle start to meeting point = b 
                3. let remaining cycle length = c 
                4. when they meet, slow traveled a + b and fast traveled a + b + c + b 
                5. since fast travels 2x speed of slow, 2(a+b) = a + b + c + b 
                6. simplifying, we get:
                    2a + 2b = a + 2b + c 
                    2a = a + c 
                    a = c 
                7. so, moving from head and meeting point will simultaneously meet at cycle start (lens are same and we are both moving one step at a time)
            
            Example) 
                A -> B -> C -> D -> E -> F 
                          ^              |
                          |______________|

                Where:
                - a = 2 (A -> B -> C) 
                - Meeting happens at E 
                - b = 2 (C -> D -> E)
                - c = 2 ( E -> F -> C)
                - Total cycle = 2 (C -> D -> E -> C)

                Slow -> a + b = 2 + 2 = 4
                Fast -> a + 2b + c = 2 + 4 + 2 = 8
                Checking that 2(a+b) = a + b + c + b 
                    2*4 = 8 --> good to go 
                
                After Floyd's detection:
                    start: A (needs 2 steps to reach C)
                    slow:  E (needs 2 steps to reach C: E -> F -> C)

                    Step 1:
                        start: A -> B 
                        slow:  E -> F
                    Step 2:
                        start: B -> C  ✓ 
                        slow:  F -> C  ✓

                THEY MEET AT C!
        '''

        if not head or not LinkedListOperations.has_cycle(head):
            return None 
        
        # find meeting point 
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast:
                break 

        # find start, slow is starting at the meeting point still  
        start = head 
        while start != slow:
            start = start.next
            slow = slow.next 

        return start 


    @staticmethod
    def merge_two_sorted_lists(list1, list2):
        '''
            Merge two sorted linked lists into one sorted link list. 

            Args:
                list1, list2: heads of sorted linked lists 

            Returns:
                head of merged sorted lists 

            Algorithm:
                1. use dummy head 
                2. compare current nodes from both lists 
                3. add smaller node to result and advance that pointer 
                4. append remaining nodes from non-empty list 

            Q) What is the time and space complexity?
                a) Time complexity is O(m + n)
                a) Space complexity is O(1)
        '''

        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next 
            else:
                current.next = list2 
                list2 = list2.next 

            current = current.next 

        # append remaining nodes
        current.next = list1 or list2 

        return dummy.next

    @staticmethod
    def find_middle_node(head):
        '''
            Find the middle node of a linked list 

            Args: 
                head: head node of linked list 

            Returns:
                middle node (if even, second middle node)

            Algorithm:
                1. use slow and fast pointers 
                2. slow moves 1 step, fast moves two 
                3. when fast reaches end, slow is at the middle 

            Q) What is the time and space complexity?
                a) Time complexity is O(n)
                a) Space complexity is O(1)
        '''

        if not head:
            return None 

        slow = head 
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        return slow


    @staticmethod
    def remove_nth_from_end(head, n):
        '''
            Remove the nth node from the end of the list 

            Args:
                head: the head of the list
                n: the position from the end (1-indexed)

            Returns:
                head of the modified list 

            Algorithm:
                1. use dummy head to handle edge case of removing the first node 
                2. set fast pointer to n+1 steps ahead 
                3. move both pointers until fast reaches the end 
                4. slow.next is the node to remove 

            Q) What is time and space complexity?
                a) Time complexity is O(L) where L is length 
                a) Space complexity is O(1)
        '''

        dummy = ListNode(0)
        dummy.next = head 

        slow = dummy
        fast = dummy 

        for _ in range(n+1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next 

        return dummy.next 
       
    @staticmethod 
    def intersection_of_two_lists(headA, headB):
        '''
            Find the intersection node of two linked lists, where the intersection is when two nodes occupy the same memory (shared node that is instantiated once)

            Args:
                headA, headB: heads of 2 linked lists 

            Returns:
                intersection node, none if no intersection 

            Algorithm:
                1. use two pointers starting at each head 
                2. when a pointer reaches the end, redirect it to the other list's head 
                3. they will meet at intersection 
                    - if the lists intersect, the pointers will travel the same total distance and meet at intersection after at most 2 passes 

            Q) What is the time and space complexity?
                a) Time complexity is O(n + m)
                a) Space complexity is O(1)
        '''

        if not headA or not headB:
            return None 

        pointerA = headA
        pointerB = headB

        while pointerA != pointerB:
            # when we reach the other end, swap to the next list 
            pointerA = pointerA.next if pointerA else headB  
            pointerB = pointerB.next if pointerB else headA 

        return pointerA


    @staticmethod
    def is_palindrome(head):
        '''
            Check if a linked list is a palindrome 

            Args:
                head: head of a linked list 

            Returns:
                true if palindrome, false otherwise 

            Algorithm:
                1. find middle of list using two pointers 
                2. reverse second half of list
                3. if reversed second half matches first half, is palindrome 
                4. restore original list structure 

            Q) What is time and space complexity?
                a) Time complexity is O(n)
                a) Space complexity is O(1)
            Q) Why can't we start at head and tail and meet in the middle, comparing chars on the way?
                a) Singly linked list so no way to use prev. also cant manipulate to increment x amount after tail since tail just points to None, not head. 
        '''
        if not head or not head.next:
            return True
        slow = head 
        fast = head 

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next 

        #middle = slow.next
        
        # reverse the second half of the linked list, using the middle as the "head" 
        prev = None 
        current = slow.next  


        while current:
            next_node = current.next 
            current.next = prev 
            prev = current 
            current = next_node 
        
        # after reversal, previous now points to the head of the second half
        second_half = prev

        # split the list 
        slow.next = None

        # compare halves
        first_half = head 
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True 

    @staticmethod
    def add_two_numbers(l1, l2):
        '''
            Add two numbers represented as link lists

            Args:
                l1, l2: heads of two linked lists

            Returns:
                head of the linked list representing the sum 

            Example) 
                Input
                    l1 = 2 -> 4 -> 3
                    l2 = 5 -> 6 -> 4
                Represents:
                    342 + 465 = 807
                Output:
                    7 -> 0 -> 8 

            Algorithm:
                1. Process digits from least significant (head) to most significant(tail)
                2. keep track of carry from each addition
                3. create new nodes for result 

            Q) What is the time and space complexity?
                a) Time complexity is O(max(m, n))
                a) Space complexity is O(max(m, n))
        '''

        dummy = ListNode(0)
        current = dummy 
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry 
            carry = total // 10 # // is integer division, rounding down to floor... keeps track of the remainder when adding stuff like 8  + 5 = 13, have to keep track of the 1. 
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next 

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


    @staticmethod
    def remove_duplicates_sorted(head):
        '''
            Remove duplicates from a sorted linked list

            Args:
                head: the head of the LL 

            Returns:
                the head of the cleaned LL 

            Q) What is the time and space complexity?
                a) Time complexity is O(n)
                a) Space complexity is O(1)
        '''

        current = head 

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next 
            else:
                current = current.next

        return head


    @staticmethod
    def partition_list(head, x):
        '''
            Partition linked list around value x. All nodes less than x come before nodes greater than or equal to x.

            Args:
                head: head of LL 
                x: value to partition by

            Returns:
                head of partitioned list 

            Algorithm:
                1. create two separate lists, before and after 
                2. traverse the original list, adding to the appropriate list 
                3. connect before list to after list 

            Q) What is the time and space complexity?
                a) Time complexity is O(n)
                a) Space complexity is O(1)
        '''
        
        before_head = ListNode(0)
        after_head = ListNode(0)

        before = before_head
        after = after_head 

        current = head
        while current:
            if current.val < x:
                before.next = current
                before = before.next 
            else:
                after.next = current
                after = after.next 
            current = current.next 

        # connect the two lists
        after.next = None # terminate the after list, ensures the linked list ends with None 
        before.next = after_head.next # connects the end of the before list to the after list, skipping the dummy head (the reason for the .next) 

        return before_head.next

