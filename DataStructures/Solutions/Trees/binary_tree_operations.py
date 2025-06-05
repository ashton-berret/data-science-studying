class TreeNode:
    ''' Binary tree node definition '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

class BinaryTreeOperations:
    ''' Common binary tree operations and patterns for interviews '''

    @staticmethod
    def inorder_traversal_recursive(root):
        '''
            Perform an inorder traversal of the binary tree recursively (left, root, right)

            Args:
                root: a TreeNode representing the root of the tree

            Returns:
                list of values in inorder sequence

            Q) What is the time and space complexity
                a) Time complexity is O(n), visit each node once
                a) Space complexity is O(n) -> recursion stack depth is equal to tree heigh
            Q) What is the order of operations in inorder traversal?
                a) Left subtree, root, right substree
            Q) Why is inorder traversal special for BSTs?
                a) It visits nodes in sorted order for a valid BST
            Q) What is the best case for the recursion?
                a) When root is None, it returns an empty list.


            Example Walkthrough) Tree:
                    1
                   / \
                  2   3
                 / \
                4   5

                1. Inorder(2): visits 4, then 2 then 5 -> [4, 2, 5]
                2. visit root 1: [4, 2, 5, 1]
                3. inorder(3): [4, 2, 5, 1, 3]
                4. return [4, 2, 5, 1, 3]
        '''

        if not root:
            return []

        result = []
        result.extend(BinaryTreeOperations.inorder_traversal_recursive(root.left))
        result.append(root.val)
        result.extend(BinaryTreeOperations.inorder_traversal_recursive(root.right))

        return result


    @staticmethod
    def inorder_traversal_iterative(root):
        '''
            Perform inorder traversal iteratively using a stack

            Args:
                root: a TreeNode representing the root of the tree

            Returns:
                list of values in inorder sequence

            Q) What is the time and space complexity?
                a) Time complexity is O(n)
                a) Space complexity is O(h)
            Q) How does the iterative approach simulate recursion?
                a) Use explicit stack to track nodes, go left as far as possible, process, go right
            Q) Why do we go left first before adding to result
                a) Inorder requires processing left subtree before current node

            Example Walkthrough) Tree:
                    1
                   / \
                  2   3
                 / \
                4   5

                    1. start at 1, go left to 2, then left to 4, stack = [1,2,4]
                    2. 4 has no left, process 4, result = [4], go right (None)
                    3. pop 2, process 2, result = [4,2], go right to 5,
                    4. 5 has no left, process 5, result = [4, 2, 5]
                    5. pop 1, process 1, result = [4, 2, 5, 1], go right
                    6. 3 has no left, process 3, result = [4,2,5,1,3], 3 has no right
                    7. return [4, 2, 5, 1, 3]
        '''

        if not root:
            return []

        stack = []
        result = []
        current = root

        while stack or current:
            # go left as far as possible
            while current:
                stack.append(current)
                current = current.left

            # process the current node
            current = stack.pop()
            result.append(current.val)

            # move to right subtree
            current = current.right

        return result

    @staticmethod
    def preorder_traversal_recursive(root):
        '''
            Perform preorder tree reversal recursively (root, left, right)

            Args:
                root: TreeNode representing the root of the binary tree

            Returns:
                list of values in preorder sequence

            Q) What is the time and space complexity?
                a) Time complexity is O(n), visit each node once
                a) Space complexity is O(h), recursion stack depth
            Q) What is the order of operations in preorder tree traversal?
                a) root -> left -> right
            Q) What is preorder traversal useful for?
                a) Creating a copy of the tree, prefix expression evaluation

            Example Walkthrough) Tree:
                    1
                   / \
                  2   3
                 / \
                4   5

                1. Visit root 1 -> [1]
                2. preorder(2) -> visit 2 -> [1,2] and then preorder(4) -> [1,2,4], then preorder(5) -> [1,2,4,5]
                3. preorder(3) -> visit 3 -> [1,2,4,5,3]
                4. return [1,2,4,5,3]
        '''

        if not root:
            return []

        result = []
        result.append(root.val)
        result.extend(BinaryTreeOperations.preorder_traversal_recursive(root.left))
        result.extend(BinaryTreeOperations.preorder_traversal_recursive(root.right))

        return result

    @staticmethod
    def preorder_traversal_iterative(root):
        '''
            Perform a preorder traversal iteratively using a stack

            Args:
                root: TreeNode representing the root of the binary tree

            Returns:
                list of values in preorder sequence

            Q) What is the time and space complexity?
                a) Time complexity is O(n)
                a) Space complexity is O(h)
            Q) Why do we add right child before left child to stack?
                a) Stack is LIFO, so we want to process the left child first


            Example Walkthrough) Tree:
                    1
                   / \
                  2   3
                 / \
                4   5

                1. Start with stack = [1]
                2. pop(1), add to result -> [1], push right(3) then left(2), stack = [3,2]
                3. pop(2), add to result -> [1,2], push right(5), then left 4, stack = [3,5,4]
                4. pop(4), add to result -> [1,2,4], no children, stack = [3,5]
                5. pop(5), add to result -> [1,2,4,5], no children, stack = [3]
                6. pop(3), add to result -> [1,2,4,5,3], no children, stack = []
                7. return [1,2,4,5,3]
        '''

        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            current = stack.pop()
            result.append(current.val)

            # add right first, then left since stack is LIFO
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return result


    @staticmethod
    def postorder_traversal_recursive(root):
        '''
            Perform a postorder traversal recursively (left, right, root)

            Args:
                root: TreeNode representing the root of the binary tree

            Returns:
                list of values in preorder sequence

            Q) What is the time and space complexity?
                a) Time complexity is O(n)
                a) Space complexity is O(h)
            Q) What is postorder useful for?
                a) Deleting nodes, calculating directory sizes, postfix expression evaluation.

            Example Walkthrough) Tree:
                    1
                   / \
                  2   3
                 / \
                4   5

                1. Postorder(2): postorder(4) -> [4], -> postorder(5) -> [4,5] visit 2 -> [4,5,2]
                2. postorder(3): visit 3 -> [4,5,2,3]
                3. visit root(1): -> [4,5,2,3,1]
                4. return [4,5,2,3,1]
        '''

        if not root:
            return []

        result = []
        result.extend(BinaryTreeOperations.postorder_traversal_recursive(root.left))
        result.extend(BinaryTreeOperations.postorder_traversal_recursive(root.right))
        result.append(root.val)

        return result

    @staticmethod
    def postorder_traversal_iterative(root):
        '''
            Perform a postorder traversal iteratively (left, right, root)

            Args:
                root: TreeNode representing the root of the binary tree

            Returns:
                list of values in preorder sequence

            Q) What is the time and space complexity?
                a) Time complexity is O(n)
                a) Space complexity is O(h)
            Q) Why do we use two stacks for iterative postorder?
                a) First stack for traversal, second stack to reverse the order to get Left-Right-Root
            Q) How does this approach work?
                a) Use modified preorder (Root-Right-Left) and reverse to get post order

            Walkthrough) Tree:
                    1
                   / \
                  2   3
                 / \
                4   5

                1. stack1 [1], stack2=[]
                2. pop1 from stack1, push to stack2, push left(2), then right(3) to stack1
                    - stack1 = [2,3], stack2 = [1]
                3. pop 3 from stack 1, push to stack2, no children
                    - stack1 = [2], stack2 = [1,3]
                4. pop 2 from stack1, push to stack1, push left(4) then right(5) to stack1
                    - stack1 = [4,5], stack2=[1,3,2]
                5. pop 5 from stack1, push to stack2, no children
                    - stack1 = [4], stack2=[1,3,2,5]
                6. pop 4 from stack1, push to stack2, no children
                    - stack1 = [], stack2=[1,3,2,5,4]
                7. pop from stack2 to return result = [4,5,2,3,1]
        '''

        if not root:
            return []

        traversal_stack = [root]
        to_reorder_stack = []
        result = []

        while traversal_stack:
            current = traversal_stack.pop()
            to_reorder_stack.append(current)

            if current.left:
                traversal_stack.append(current.left)
            if current.right:
                traversal_stack.append(current.right)

        while to_reorder_stack:
            result.append(to_reorder_stack.pop().val)

        return result


    @staticmethod
    def level_order_traversal(root):
        '''
            Perform a level order (breadth first) traversal of the binary tree

            Args:
                root: TreeNode representing the root of the binary tree

            Returns:
                list of lists, where each inner list contains that values at each level

            Q) What is the time and space complexity?
                a) Time complexity is O(n)
                a) Space complexity is O(w) where w is the max width of the tree
            Q) What data structure do we use for level-order traversal?
                a) Queue (FIFO) to process nodes level by level
            Q) How do we separate levels in the output?
                a) Process all nodes at current level before moving to next level

            Example Walkthrough) Tree:
                    3
                   / \
                  9  20
                    /  \
                   15   7


                1. start with queue = [3], result = []
                2. level 0: process 3, add children to queue[9,20], result = [[3]]
                3. level 1: process 9 (no children), process 20(add children to queue), queue = [15,7], result = [[3], [9,20]]
                4. level 2: process 15 (no children), process 7 (no children), queue = [], result = [[3], [9,20], [15,7]]
        '''

        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.pop(0)
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result

    @staticmethod
    def max_depth(root):
        '''
            Find the maxmimum depth (height) of a binary tree.

            Args:
                root: TreeNode representing the root of the binary tree

            Returns:
                integer representing maximum depth

            Q) What is the time and space complexity?
                a) Time complexity is O(n)
                a) Space complexity is O(h)
            Q) What is the difference between depth and height?
                a) Depth is the distance from root to node, height is distance from node to deepest leaf
            Q) What is the best case?
                a) Empty tree has depth 0

            Example Walkthrough) Tree:
                    3
                   / \
                  9  20
                    /  \
                   15   7

                1. max_depth(3): 1 + max(max_depth(9), max_depth(20))
                2. max_depth(9): 1 + max(0,0) = 1
                3. max_depth(20): 1 + max(max_depth(15), max_depth(7))
                4. max_depth(15): 1 + max(0, 0) = 1
                5. max_depth(7): 1 + max(0,0) = 1
                6. max_depth(20): 1 + max(1, 1) = 2
                7. max_depth(3): 1 + max(1,2) = 3
                8. return 3
        '''

        if not root:
            return 0

        left_depth = BinaryTreeOperations.max_depth(root.left)
        right_depth = BinaryTreeOperations.max_depth(root.right)

        return 1 + max(left_depth, right_depth)


    @staticmethod
    def min_depth(root):
        '''
            Find the minimum depth of a binary tree

            Args:
                root: TreeNode representing the root of the binary tree

            Returns:
                integer representing minimum depth

            Q) What is the time and space complexity?
                a) Time complexity is O(n)
                a) Space complexity is O(h)
            Q) How is minimum depth different from maximum depth?
                a) Minimum depth is the shortest path from root to any leaf node
            Q) What special case do we handle for nodes with only one child?
                a) If one child is None, we don't count it as a path to a leaf

            Example Walkthrough) Tree:
                    3
                   / \
                  9  20
                    /  \
                   15   7

                1. min_depth(3): 1 + min(min_depth(9), min_depth(20))
                2. min_depth(9): leaf node, return 1
                3. min_depth(20): 1 + min(min_depth(15), min_depth(7))
                4. min_depth(15): leaf node, return 1
                5. min_depth(7): leaf node, return 1
                6. min_depth(20): 1 + min(1,1) = 2
                7. min_depth(3): 1 + min(1,2) = 2
                8. return 2
        '''

        if not root:
            return 0

        # if this is a leaf node
        if not root.left and not root.right:
            return 1

        # if only the right subtree exists
        if not root.left:
            return 1 + BinaryTreeOperations.min_depth(root.right)

        # if only left subtree exists
        if not root.right:
            return 1 + BinaryTreeOperations.min_depth(root.left)

        # both subtrees exist
        left_depth = BinaryTreeOperations.min_depth(root.left)
        right_depth = BinaryTreeOperations.min_depth(root.right)

        return 1 + min(left_depth, right_depth)


    @staticmethod
    def is_balanced(root):
        '''
            Check if a binary tree is height-balanced

            Args:
                root: TreeNode representing the root of the binary tree
            Returns:
                boolean indicating if the tree is balanced

            Q) What is the time and space complexity?
                a) O(n) time complexity - visit each node once
                a) O(h) space complexity - recursion stack depth
            Q) What makes a tree height-balanced?
                a) For every node, the height difference between left and right subtrees is at most 1
            Q) How do we optimize to avoid recalculating heights?
                a) Return both balance status and height from each recursive call

            Example Walkthrough) Tree:
                    3
                   / \
                  9  20
                    /  \
                   15   7

                1. Check node 3: height difference = |1 - 2| = 1 <= 1 ✓
                2. Check node 9: leaf node, balanced ✓
                3. Check node 20: height difference = |1 - 1| = 0 <= 1 ✓
                4. all nodes balanced, return true
        '''

        def check_balance(node):
            if not node:
                return True, 0 # returns balance status and height

            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0

            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0

            is_current_balanced = abs(left_height - right_height) <= 1
            current_height = 1 + max(left_height, right_height)

            return is_current_balanced, current_height

        balanced, _ = check_balance(root)
        return balanced


    @staticmethod
    def invert_binary_tree(root):
        '''
            Invert a binary tree (swap left and right children of all nodes)

            Args:
                root: TreeNode representing the root of the binary tree
            Returns:
                TreeNode representing the root of the inverted tree

            Q) What is the time and space complexity?
                a) O(n) time complexity - visit each node once
                a) O(h) space complexity - recursion stack depth
            Q) What does "invert" mean for a binary tree?
                a) Swap the left and right children of every node
            Q) Is this operation done in-place?
                a) Yes, we modify the original tree structure

            Example Walkthrough) Tree:
                    4
                   / \
                  2   7
                 / \ / \
                1  3 6  9

                After inversion:
                    4
                   / \
                  7   2
                 / \ / \
                9  6 3  1
        '''

        if not root:
            return None

        root.left, root.right = root.right, root.left

        # recursively invert the binary tree
        BinaryTreeOperations.invert_binary_tree(root.left)
        BinaryTreeOperations.invert_binary_tree(root.right)

        return root


    @staticmethod
    def lowest_common_ancestor(root, p, q):
        '''
            Find the lowest common ancestor of two nodes in a binary tree

            Args:
                root: TreeNode representing the root of the binary tree
                p: TreeNode representing first target node
                q: TreeNode representing second target node
            Returns:
                TreeNode representing the lowest common ancestor

            Q) What is the time and space complexity?
                a) O(n) time complexity - may visit all nodes
                a) O(h) space complexity - recursion stack depth
            Q) What is the lowest common ancestor?
                a) The deepest node that has both p and q as descendants
            Q) What are the base cases?
                a) If root is None, p, or q, return root

            Example Walkthrough) Tree:
                    3
                   / \
                  5   1
                 / \ / \
                6  2 0  8
                  / \
                 7   4

                Find LCA of 5 and 1:
                1. At node 3: left subtree contains 5, right subtree contains 1
                2. Since 3 has descendants in both subtrees, LCA is 3
        '''

        if not root or root == p or root == q:
            return root

        left = BinaryTreeOperations.lowest_common_ancestor(root.left, p, q)
        right = BinaryTreeOperations.lowest_common_ancestor(root.right, p, q)

        # if both left and right are not None, that means the current node is LCA
        if left and right:
            return root

        return left or right


    @staticmethod
    def has_path_sum(root, target_sum):
        '''
            Check if tree has a root-to-leaf path with given sum

            Args:
                root: TreeNode representing the root of the binary tree
                target_sum: integer representing the target sum
            Returns:
                boolean indicating if such a path exists

            Q) What is the time and space complexity?
                a) O(n) time complexity - may visit all nodes
                a) O(h) space complexity - recursion stack depth
            Q) What constitutes a valid path?
                a) A path from root to any leaf node
            Q) How do we handle the base cases?
                a) Empty tree: False; Leaf node: check if value equals remaining sum

            Example Walkthrough) Tree:
                    5
                   / \
                  4   8
                 /   / \
                11  13  4
               / \      \
              7   2      1

                Target sum = 22
                1. Path 5->4->11->2 = 22 ✓
                2. Return True
        '''

        if not root:
            return False

        # if the node is a leaf node, check to see if it equals the target sum
        if not root.left and not root.right:
            return root.val == target_sum

        remaining_sum = target_sum - root.val
        return(
            BinaryTreeOperations.has_path_sum(root.left, remaining_sum)
            or
            BinaryTreeOperations.has_path_sum(root.right, remaining_sum)
        )



    @staticmethod
    def path_sum_all_paths(root, target_sum):
        '''
            Find all root-to-leaf paths with given sum

            Args:
                root: TreeNode representing the root of the binary tree
                target_sum: integer representing the target sum
            Returns:
                list of lists, each containing a valid path

            Q) What is the time and space complexity?
                a) O(n²) time complexity in worst case - copying paths
                a) O(h) space complexity for recursion, O(n) for storing results
            Q) How do we track the current path?
                a) Pass current path as parameter and backtrack after recursive calls
            Q) Why do we need to copy the path when adding to results?
                a) The path list is modified during recursion (backtracking)

            Example Walkthrough) Tree:
                    5
                   / \
                  4   8
                 /   / \
                11  13  4
               / \     / \
              7   2   5   1

                Target sum = 22
                1. Find path 5->4->11->2 = 22
                2. Find path 5->8->4->5 = 22
                3. Return [[5,4,11,2], [5,8,4,5]]
        '''

        def find_paths(node, remaining_sum, current_path, all_paths):
            if not node:
                return

            # add current node to path
            current_path.append(node.val)

            # if this is a leaf node and the sum matches, add the path to results
            if not node.left and not node.right and node.val == remaining_sum:
                all_paths.append(current_path[:])
            else:
                # continue searching in sub trees
                find_paths(node.left, remaining_sum - node.val, current_path, all_paths)
                find_paths(node.right, remaining_sum - node.val, current_path, all_paths)

            # backtrack
            current_path.pop()

        all_paths = []
        find_paths(root, target_sum, [], all_paths)
        return all_paths


    @staticmethod
    def build_tree_from_preorder_inorder(preorder, inorder):
        '''
            Build a binary tree from preorder and inorder traversal arays

            Args:
                preorder: list of values in preorder sequence
                inorder: list of values in inorder sequence

            Returns:
                TreeNode representing the root of constructed tree

            Q) What is the time and space complexity?
                a) Time complexity is O(n) with hashmap for index lookup
                a) Space complexity is O(n) for hashmap and recursion stack
            Q) Why do we need both preorder and inorder?
                a) Preorder gives us the root, inorder helps us separate the left and right trees
            Q) How do we optimize the index lookup in inorder array?
                a) Use a hashmap to store value -> index mapping for 0(1) lookup

            Example Walkthrough)
                preorder = [3,9,20,15,7]
                inorder = [9,3,15,20,7]

                1. root = 3 (first in preorder)
                2. in inorder, 3 is at index 1 so we know 9 is the left subtree, [15,20,7] is the right subtree
                3. left subtree: preorder=[9], inorder=[9], single node
                4. right subtree: preorder = [20,15,7], inorder = [15,20,17] -> root = 20
                5. continue recursively
        '''

        if not preorder or not inorder:
            return None

        # create a hashmap for O(1) index lookup in inorder
        inorder_map = {val: i for i, val in enumerate(inorder)}

        def build_tree(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None

            # root is always the first element in the preorder range
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # find root position in inorder
            root_index = inorder_map[root_val]

            # calculate the left subtree size
            left_size = root_index - in_start

            # build the left and right subtrees
            root.left = build_tree(pre_start + 1, pre_start + left_size, in_start, root_index - 1)
            root.right = build_tree(pre_start + left_size + 1, pre_end, root_index + 1, in_end)

            return root

        return build_tree(0, len(preorder) - 1, 0, len(inorder) -1)



    @staticmethod
    def serialize_tree(root):
        '''
            Serialize a binary tree to a string

            Args:
                root: TreeNode representing the root of the binary tree

            Returns:
                string representation of the string

            Q) What is the time and space complexity?
                a) Time complexity is O(n)
                a) Space complexity is O(n)
            Q) How do we handle None nodes in serialization?
                a) Use a special marker like null or "#"
            Q) What traversal method works best for serialization?
                a) Preorder allows easy reconstruction

            Example Walkthrough)
                    1
                   / \
                  2   3
                     / \
                    4   5

                Serialized: "1, 2, null, null, 3, 4, null, null, 5, null, null"
        '''

        def serialize_helper(node):
            if not node:
                vals.append("null")
                return

            vals.append(str(node.val))
            serialize_helper(node.left)
            serialize_helper(node.right)

        vals = []
        serialize_helper(root)

        return ",".join(vals)



    @staticmethod
    def deserialize_tree(data):
        '''
            Deserialize a string to binary tree

            Args:
                data: string representation of the tree
            Returns:
                TreeNode representing the root of reconstructed tree

            Q) What is the time and space complexity?
                a) O(n) time complexity - process each value once
                a) O(n) space complexity - recursion stack and tree storage
            Q) How do we maintain state during recursive reconstruction?
                a) Use an index or iterator to track current position in data
            Q) Why is preorder traversal ideal for reconstruction?
                a) We can build the tree top-down, creating nodes as we encounter them

            Example Walkthrough)
                data = "1,2,null,null,3,4,null,null,5,null,null"

                1. Create node 1, build left subtree
                2. Create node 2, left child is null, right child is null
                3. Back to node 1, build right subtree
                4. Create node 3, build its subtrees...
        '''
        def deserialize_helper():
            nonlocal index
            if index >= len(vals):
                return None

            val = vals[index]
            index += 1

            if val == "null":
                return None

            node = TreeNode(int(val))
            node.left = deserialize_helper()
            node.right = deserialize_helper()
            return node

        if not data:
            return None

        vals = data.split(",")
        index = 0
        return deserialize_helper()



    @staticmethod
    def is_valid_bst(root):
        '''
            Validate if a binary tree is a valid binary search tree

            Args:
                root: TreeNode representing the root of the binary tree
            Returns:
                boolean indicating if the tree is a valid BST

            Q) What is the time and space complexity?
                a) O(n) time complexity - visit each node once
                a) O(h) space complexity - recursion stack depth
            Q) What are the BST properties we need to check?
                a) For each node, all left descendants < node.val < all right descendants
            Q) Why isn't it enough to just compare with immediate children?
                a) We need to ensure the BST property holds for the entire subtree
            Q) How do we track the valid range for each node?
                a) Pass min and max bounds that tighten as we go down the tree

            Example Walkthrough) Tree:
                    5
                   / \
                  1   4
                     / \
                    3   6

                1. Node 5: valid range (-inf, inf) ✓
                2. Node 1: valid range (-inf, 5) ✓
                3. Node 4: valid range (5, inf) ✗ (4 < 5)
                4. Return False
        '''

        def validate(node, min_val, max_val):
            if not node:
                return True

            if node.val <= min_val or node.val > max_val:
                return False

            return (validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val))

        return validate(root, float('-inf'), float('inf'))



    @staticmethod
    def bst_insert(root, val):
        '''
            Insert a value into a binary search tree

            Args:
                root: TreeNode representing the root of the BST
                val: integer value to insert
            Returns:
                TreeNode representing the root of the modified BST

            Q) What is the time and space complexity?
                a) O(h) time complexity where h is height of tree
                a) O(h) space complexity for recursion stack
            Q) Where do we insert the new node?
                a) At the first empty position following BST property
            Q) What if the value already exists?
                a) Typically ignore duplicates or handle based on requirements

            Example Walkthrough) Insert 4 into:
                    5
                   / \
                  3   7
                 /   / \
                2   6   8

                1. 4 < 5, go left to 3
                2. 4 > 3, go right (empty)
                3. Insert 4 as right child of 3
        '''

        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = BinaryTreeOperations.bst_insert(root.left, val)
        elif val > root.val:
            root.right = BinaryTreeOperations.bst_insert(root.right, val)
        # else if the root.value == value, we don't insert duplicates or we just add a way to handle as required (maybe just tie into one of the if elif cases above)
        return root


    @staticmethod
    def bst_search(root, val):
        '''
            Search for a value in a binary search tree

            Args:
                root: TreeNode representing the root of the BST
                val: integer value to search for
            Returns:
                TreeNode if found, None otherwise

            Q) What is the time and space complexity?
                a) O(h) time complexity where h is height of tree
                a) O(h) space complexity for recursion stack (O(1) for iterative)
            Q) How do we decide which direction to search?
                a) Compare target with current node: go left if smaller, right if larger
            Q) What are the base cases?
                a) Node is None (not found) or node.val == val (found)

            Example Walkthrough) Search for 6 in:
                    5
                   / \
                  3   7
                 /   / \
                2   6   8

                1. 6 > 5, go right to 7
                2. 6 < 7, go left to 6
                3. 6 == 6, found! Return node
        '''

        if not root or root.val == val:
            return root

        if val < root.val:
            return BinaryTreeOperations.bst_search(root.left, val)
        else:
            return BinaryTreeOperations.bst_search(root.right, val)



    @staticmethod
    def bst_delete(root, val):
        '''
            Delete a value from a binary search tree

            Args:
                root: TreeNode representing the root of the BST
                val: integer value to delete
            Returns:
                TreeNode representing the root of the modified BST

            Q) What is the time and space complexity?
                a) O(h) time complexity where h is height of tree
                a) O(h) space complexity for recursion stack
            Q) What are the three cases for deletion?
                a) Node has no children: simply remove
                a) Node has one child: replace with child
                a) Node has two children: replace with inorder successor
            Q) What is the inorder successor?
                a) The smallest node in the right subtree (leftmost node in right subtree)

            Example Walkthrough) Delete 3 from:
                    5
                   / \
                  3   7
                 / \ / \
                2  4 6  8

                1. Node 3 has two children
                2. Find inorder successor: 4 (leftmost in right subtree)
                3. Replace 3's value with 4
                4. Delete the original 4 node
        '''

        if not root:
            return root

        if val < root.val:
            root.left = BinaryTreeOperations.bst_delete(root.left, val)
        elif val > root.val:
            root.right = BinaryTreeOperations.bst_delete(root.right, val)
        else:
            # no node found to be deleted

            # case 1, node has no children or only right child
            if not root.left:
                return root.right

            # case 2, node has only left child
            elif not root.right:
                return root.left

            # case 3, node has two children, have to find in order successor
            successor = root.right
            while successor.left:
                successor = successor.left

            # replace root's value with the sucessors value
            root.val = successor.val

            # delete the successor
            root.right = BinaryTreeOperations.bst_delete(root.right, successor.val)

        return root


    @staticmethod
    def binary_tree_paths(root):
        '''
            Find all root-to-leaf paths in a binary tree

            Args:
                root: TreeNode representing the root of the binary tree
            Returns:
                list of strings, each representing a path from root to leaf

            Q) What is the time and space complexity?
                a) O(n²) time complexity in worst case (copying paths)
                a) O(n) space complexity for storing paths
            Q) How do we represent each path?
                a) As a string with nodes separated by "->"
            Q) When do we add a path to the result?
                a) When we reach a leaf node (no left or right children)

            Example Walkthrough) Tree:
                    1
                   / \
                  2   3
                   \
                    5

                Paths: ["1->2->5", "1->3"]
        '''

        if not root:
            return []

        def find_paths(node, current_path, all_paths):
            if not node:
                return

            # add current node to path
            current_path.append(str(node.val))

            # if this is a leaf, add path to results
            if not node.left and not node.right:
                all_paths.append("->".join(current_path))
            else:
                # continue searching in subtrees
                find_paths(node.left, current_path, all_paths)
                find_paths(node.right, current_path, all_paths)



            # backtrack
            current_path.pop()

        all_paths = []
        find_paths(root, [], all_paths)

        return all_paths



    @staticmethod
    def diameter_of_binary_tree(root):
        '''
            Find the diameter of a binary tree (longest path between any two nodes)

            Args:
                root: TreeNode representing the root of the binary tree
            Returns:
                integer representing the diameter (number of edges)

            Q) What is the time and space complexity?
                a) O(n) time complexity - visit each node once
                a) O(h) space complexity - recursion stack depth
            Q) What is the diameter of a tree?
                a) The longest path between any two nodes (may or may not pass through root)
            Q) How do we handle the case where the longest path doesn't go through root?
                a) For each node, consider the longest path that goes through it
            Q) What does the longest path through a node look like?
                a) Left height + right height of that node

            Example Walkthrough) Tree:
                    1
                   / \
                  2   3
                 / \
                4   5

                1. At node 2: left_height=1, right_height=1, diameter=2
                2. At node 1: left_height=2, right_height=1, diameter=3
                3. Maximum diameter = 3
        '''

        def height_and_diameter(node):
            if not node:
                return 0, 0

            left_height, left_diameter = height_and_diameter(node.left)
            right_height, right_diameter = height_and_diameter(node.right)

            # current node's height
            current_height = 1 + max(left_height, right_height)

            # diameter through the current node
            current_diameter = left_height + right_height

            # max diameter seen so far
            max_diameter = max(left_diameter, right_diameter, current_diameter)

            return current_height, max_diameter

        if not root:
            return 0

        _, diameter = height_and_diameter(root)

        return diameter



    @staticmethod
    def count_nodes(root):
        '''
            Count the total number of nodes in a binary tree

            Args:
                root: TreeNode representing the root of the binary tree
            Returns:
                integer representing the total number of nodes

            Q) What is the time and space complexity?
                a) O(n) time complexity - visit each node once
                a) O(h) space complexity - recursion stack depth
            Q) What is the base case?
                a) Empty tree has 0 nodes
            Q) How do we count nodes recursively?
                a) 1 (current node) + count(left subtree) + count(right subtree)

            Example Walkthrough) Tree:
                    1
                   / \
                  2   3
                 / \
                4   5

                1. count(1) = 1 + count(2) + count(3)
                2. count(2) = 1 + count(4) + count(5) = 1 + 1 + 1 = 3
                3. count(3) = 1 + 0 + 0 = 1
                4. count(1) = 1 + 3 + 1 = 5
        '''

        if not root:
            return 0

        return 1 + BinaryTreeOperations.count_nodes(root.left) + BinaryTreeOperations.count_nodes(root.right)



    @staticmethod
    def is_symmetric(root):
        '''
            Check if a binary tree is symmetric (mirror of itself)

            Args:
                root: TreeNode representing the root of the binary tree
            Returns:
                boolean indicating if the tree is symmetric

            Q) What is the time and space complexity?
                a) O(n) time complexity - visit each node once
                a) O(h) space complexity - recursion stack depth
            Q) What makes a tree symmetric?
                a) Left subtree is a mirror reflection of right subtree
            Q) How do we check if two subtrees are mirrors?
                a) Left.left mirrors Right.right, and Left.right mirrors Right.left

            Example Walkthrough) Tree:
                    1
                   / \
                  2   2
                 / \ / \
                3  4 4  3

                1. Compare left subtree (2,3,4) with right subtree (2,4,3)
                2. Check if structure and values are mirrored
                3. Return True
        '''

        def is_mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return (left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left))

        if not root:
            return True

        return is_mirror(root.left, root.right)

    @staticmethod
    def print_tree_structure(root, level=0, prefix='Root: '):
        '''
            Print tree structure for debugging/visualization

            Args:
                root: TreeNode representing the root of the binary tree
                level: current level in the tree (for indentation)
                prefix: string prefix for the current node
            Returns:
                None (prints to console)

            Q) How does this help with debugging?
                a) Provides visual representation of tree structure
            Q) What do the prefixes indicate?
                a) "Root:" for root, "L---" for left child, "R---" for right child

            Example Output) Tree:
                    1
                   / \
                  2   3
                 / \
                4   5

                Root: 1
                L--- 2
                     L--- 4
                     R--- 5
                R--- 3
        '''

        if root is not None:
            print("   " * level + prefix + str(root.val))
            if root.left is not None or root.right is not None:
                if root.left:
                    BinaryTreeOperations.print_tree_structure(root.left, level + 1, "L--- ")
                else:
                    print("   " * (level + 1) + "L--- None")
                if root.right:
                    BinaryTreeOperations.print_tree_structure(root.right, level + 1, "R--- ")
                else:
                    print("   " * (level + 1) + "R--- None")

            else:
                print("    " * level + prefix + "None")



    @staticmethod
    def build_tree_from_array(arr):
        '''
            Build binary tree from array representation (level-order)

            Args:
                arr: list where arr[i] is the value at index i (None for missing nodes)
            Returns:
                TreeNode representing the root of constructed tree

            Q) What is the time and space complexity?
                a) O(n) time complexity - process each element once
                a) O(n) space complexity - queue and tree storage
            Q) How are array indices related to tree positions?
                a) For node at index i: left child at 2*i+1, right child at 2*i+2
            Q) How do we handle None values in the array?
                a) Skip creating nodes for None values but still track index positions

            Example Walkthrough) arr = [3, 9, 20, None, None, 15, 7]

                Index:  0  1   2    3     4     5   6
                Value:  3  9  20  None  None  15   7

                Tree:   3
                       / \
                      9  20
                        /  \
                       15   7
        '''

        if not arr or arr[0] is None:
            return None

        root = TreeNode(arr[0])
        queue = [root]
        i = 1

        while queue and i < len(arr):
            node = queue.pop()

            # add left child
            if i < len(arr) and arr[i] is not None:
                node.left = TreeNode(arr[i])
                queue.append(node.left)
            i += 1
            # add right child
            if i < len(arr) and arr[i] is not None:
                node.right = TreeNode(arr[i])
                queue.append(node.right)
            i += 1

        return root
