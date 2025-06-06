from types import MethodDescriptorType
from typing import List, Set, Tuple, Optional
from collections import defaultdict

class BacktrackingOperations:
    '''
        Comprehensive backtracking algorithms for coding interviews

        Key Backtracking Concepts:
            1. CHOICE: What decisions can we make at each step
            2. CONSTRAINT: What rules must we follow? When do we prune?
            3. GOAL: When we have found a complete solution?

        Common Patterns:
            1. Generate all combinations/permutations
            2. Find paths through constraints
            3. Solve puzzles with rules
            4. Partition problems with conditions

        Permutation Mental Notes:
            1. 'Try Everything' -> the for loop is an exhaustive search that tries every possibilty, ensuring we don't miss any choices
            2. 'Clean Slate' -> After exploring one choice, reset the slate so that each branch of the DT doesn't interfere with others
            3. 'Trust the Recursion' -> Make one choice at a given level, let the recursive call to handle everything below it. Just focus on the current decision
    '''


    @staticmethod
    def generate_permutations(nums):
        '''
            Generate all permutations of given numbers

            Args:
                nums: list of integers

            Returns:
                list of all permutations

            Q) What is the time and space complexity?
                a) Time complexity is O(n! * n) -> n! permutations, each taking O(n) to build
                a) Space complexity is O(n! * n)
            Q) What is the backtracking framework?
                1. Choice: pick any unused number
                2. Constraint: Can't reuse numbers already in current permutation
                3. Goal: Current permutation has same length as input

            Example) nums = [1,2,3]
                Decision Tree:
                        []
                    /    |    \
                 [1]    [2]    [3]
                /  \    /  \   /   \
            [1,2][1,3][2,1][2,3][3,1][3,2]
             |    |    |    |    |    |
          [1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]



            Example) Trace generate_permutations([1,2]) step by step:
                Call 1: backtrack([], [1, 2])
                ├─ i=0: Try number 1
                │  ├─ current_permutation.append(1) → current_permutation = [1]
                │  ├─ new_remaining = [2]
                │  ├─ Call 2: backtrack([1], [2])
                │  │  ├─ i=0: Try number 2
                │  │  │  ├─ current_permutation.append(2) → current_permutation = [1, 2]
                │  │  │  ├─ new_remaining = []
                │  │  │  ├─ Call 3: backtrack([1, 2], [])
                │  │  │  │  └─ GOAL! remaining_nums is empty → add [1, 2] to result
                │  │  │  └─ current_permutation.pop() → current_permutation = [1]
                │  │  └─ Return to Call 2
                │  └─ current_permutation.pop() → current_permutation = []
                ├─ i=1: Try number 2
                │  ├─ current_permutation.append(2) → current_permutation = [2]
                │  ├─ new_remaining = [1]
                │  ├─ Call 4: backtrack([2], [1])
                │  │  ├─ i=0: Try number 1
                │  │  │  ├─ current_permutation.append(1) → current_permutation = [2, 1]
                │  │  │  ├─ new_remaining = []
                │  │  │  ├─ Call 5: backtrack([2, 1], [])
                │  │  │  │  └─ GOAL! remaining_nums is empty → add [2, 1] to result
                │  │  │  └─ current_permutation.pop() → current_permutation = [2]
                │  │  └─ Return to Call 4
                │  └─ current_permutation.pop() → current_permutation = []
                └─ Return final result: [[1, 2], [2, 1]]
        '''

        def backtrack(current_permutation, remaining_nums):
            # GOAL - found complete permutation
            if not remaining_nums:
                result.append(current_permutation[:]) # deep copy -> any changes made to the copy do not affect the original object
                return

            # CHOICE - try each remaining number
            for i in range(len(remaining_nums)):
                # make choice
                current_permutation.append(remaining_nums[i])
                new_remaining = remaining_nums[:i] + remaining_nums[i+1:]

                # recurse -> go deeper into the decision tree with the new updated state, handle all possibilities from the newly established point
                backtrack(current_permutation, new_remaining)

                # undo choice (backtrack) -> restore the state to what it was before the iteration (for example if this iteration went [1, 2, 3], then we pop back to [1] so we can do [1, 3, 2])
                current_permutation.pop()

        result = []
        backtrack([], nums)
        return result

    @staticmethod
    def generate_combinations(n, k):
        '''
            Generate all combinations of k numbers from 1 to n

            Args:
                n: upper bound (inclusive)
                k: combination size

            Returns:
                list of all combinations

            Q) What is the time and space complexity?
                a) Time complexity is O(C(n,k) * k) -> C(n,k) combinations, each taking O(k) to build
                a) Space complexity is O(C(n,k) * k)
            Q) What is the backtracking framework?
                a) CHOICE: Pick next number >= current number
                a) CONSTRAINT: Can only pick numbers > last number picked
                a) GOAL: Current combination has k elements


            Example)
                Decision tree:
                        []
                    /   |   |   \
                 [1]   [2] [3]  [4]
                / | \   |   |
            [1,2][1,3][1,4][2,3][2,4][3,4]

            Example Walkthrough) C(3,2) -> Choose two numbers from {1, 2, 3}

            Call 1: backtrack([], [1, 2, 3])
            ├─ i=0: Try number 1
            │  ├─ current_combination.append(1) → current_combination = [1]
            │  ├─ next_choices = [2, 3] (only numbers > 1)
            │  ├─ Call 2: backtrack([1], [2, 3])
            │  │  ├─ i=0: Try number 2
            │  │  │  ├─ current_combination.append(2) → current_combination = [1, 2]
            │  │  │  ├─ GOAL! len([1, 2]) == 2 → add [1, 2] to result
            │  │  │  └─ current_combination.pop() → current_combination = [1]
            │  │  ├─ i=1: Try number 3
            │  │  │  ├─ current_combination.append(3) → current_combination = [1, 3]
            │  │  │  ├─ GOAL! len([1, 3]) == 2 → add [1, 3] to result
            │  │  │  └─ current_combination.pop() → current_combination = [1]
            │  │  └─ Return to Call 2
            │  └─ current_combination.pop() → current_combination = []
            ├─ i=1: Try number 2
            │  ├─ current_combination.append(2) → current_combination = [2]
            │  ├─ next_choices = [3] (only numbers > 2)
            │  ├─ Call 3: backtrack([2], [3])
            │  │  ├─ i=0: Try number 3
            │  │  │  ├─ current_combination.append(3) → current_combination = [2, 3]
            │  │  │  ├─ GOAL! len([2, 3]) == 2 → add [2, 3] to result
            │  │  │  └─ current_combination.pop() → current_combination = [2]
            │  │  └─ Return to Call 3
            │  └─ current_combination.pop() → current_combination = []
            ├─ i=2: Try number 3
            │  ├─ current_combination.append(3) → current_combination = [3]
            │  ├─ next_choices = [] (no numbers > 3)
            │  ├─ Call 4: backtrack([3], [])
            │  │  └─ No choices available, return immediately
            │  └─ current_combination.pop() → current_combination = []
            └─ Return final result: [[1, 2], [1, 3], [2, 3]]
        '''
        def backtrack(current_combination, start_num):
            #GOAL: found combination of size k
            if len(current_combination) == k:
                result.append(current_combination[:]) # deep copy
                return

            # CHOICE: try numbers from start_num to n
            for num in range(start_num, n + 1):
                # CONSTRAINT: automatically satisfied by using start_num
                current_combination.append(num)

                # recurse with next start number
                backtrack(current_combination, num + 1)

                # undo choice
                current_combination.pop()

        result = []
        backtrack([], 1)
        return result


    @staticmethod
    def generate_subsets(nums):
        '''
            Generate all possible subsets (power sets) of the array

            Args:
                nums: a list of integers

            Returns:
                list of all subsets

            Q) What is the time and space complexity?
                a) Time complexity is O(2^n * n) -> 2^n subsets, each taking O(n) to buiild
                a) Space complexity is O(2^n * n)
            Q) What is the backtracking framework?
                1. CHOICE: Include current element or skip it
                2. CONSTRAINT: Process elements in order, avoiding duplicates
                3. GOAL: Processed all elements

            Example Walkthrough) generate_subsets([1,2])

            Call 1: backtrack(0, []) -- start=0, considering elements from index 0 onwards
            ├─ Store current subset: ans.append([]) → ans = [[]]
            ├─ Loop: for i in range(0, 2) -- i can be 0 or 1
            ├─ i=0: Try adding nums[0] = 1
            │  ├─ tmp.append(1) → tmp = [1]
            │  ├─ Call 2: backtrack(1, [1]) -- start=1, considering elements from index 1 onwards
            │  │  ├─ Store current subset: ans.append([1]) → ans = [[], [1]]
            │  │  ├─ Loop: for i in range(1, 2) -- i can only be 1
            │  │  ├─ i=1: Try adding nums[1] = 2
            │  │  │  ├─ tmp.append(2) → tmp = [1, 2]
            │  │  │  ├─ Call 3: backtrack(2, [1, 2]) -- start=2, considering elements from index 2 onwards
            │  │  │  │  ├─ Store current subset: ans.append([1, 2]) → ans = [[], [1], [1, 2]]
            │  │  │  │  ├─ Loop: for i in range(2, 2) -- empty range, no iterations
            │  │  │  │  └─ Return to Call 3
            │  │  │  └─ tmp.pop() → tmp = [1] (undo adding 2)
            │  │  └─ Return to Call 2 (finished trying all elements from index 1)
            │  └─ tmp.pop() → tmp = [] (undo adding 1)
            ├─ i=1: Try adding nums[1] = 2
            │  ├─ tmp.append(2) → tmp = [2]
            │  ├─ Call 4: backtrack(2, [2]) -- start=2, considering elements from index 2 onwards
            │  │  ├─ Store current subset: ans.append([2]) → ans = [[], [1], [1, 2], [2]]
            │  │  ├─ Loop: for i in range(2, 2) -- empty range, no iterations
            │  │  └─ Return to Call 4
            │  └─ tmp.pop() → tmp = [] (undo adding 2)
            └─ Return final result: [[], [1], [1, 2], [2]]
        '''

        def backtrack(start, end, temp):
            result.append(temp[:]) # with subsets, every state is a valid solution so no need for a goal check

            for i in range(start, end):
                temp.append(nums[i])
                backtrack(i+1, end, temp)
                temp.pop()

        result = []
        backtrack(0, len(nums), [])

        return result


    @staticmethod
    def solve_n_queens(n):
        '''
            Solve the N-queens problem. Plance n queens on an nxn board so that no queens attack each other

            Args:
                n: board size and number of queens

            Returns:
                list of all valid board configurations

            Q) What is the time and space complexity?
                a) Time complexity is O(n!) -> about n! ways to place the queen
                a) Space complexity is O(n^2) -> board representation
            Q) What is the backtracking framework?
                1. CHOICE: Place a queen on any column in the current row
                2. CONSTRAIN: No two queens attack each other (row/col/diag)
                3. GOAL: Place all n queens
            Q) What are the queen attack rules?
                1. Same row: checked by placing one queen per row
                2. Same col: track occupied columns
                3. Same diag: (row - col) and (row + col) are on constant diagonals

            Example: n=4, one solution:
                    . Q . .
                    . . . Q
                    Q . . .
                    . . Q .

            Advanced Walkthrough)

                    Initial State:
                    Board: [['.', '.', '.', '.'],
                            ['.', '.', '.', '.'],
                            ['.', '.', '.', '.'],
                            ['.', '.', '.', '.']]

                    occupied_cols = {}
                    pos_diag = {}  (main diagonal: row - col)
                    neg_diag = {}  (anti-diagonal: row + col)
                    result = []
                    Execution Trace:
                    Call 1: backtrack(0) -- Placing queen in row 0
                    ├─ Try col=0: is_safe(0, 0)?
                    │  ├─ col 0 in occupied_cols? No ✓
                    │  ├─ (0-0=0) in pos_diag? No ✓
                    │  ├─ (0+0=0) in neg_diag? No ✓
                    │  ├─ SAFE! Place queen at (0,0)
                    │  ├─ occupied_cols.add(0) → {0}
                    │  ├─ pos_diag.add(0-0=0) → {0}
                    │  ├─ neg_diag.add(0+0=0) → {0}
                    │  ├─ board[0][0] = 'Q'
                    │  ├─ Board: [['Q', '.', '.', '.'], ['.', '.', '.', '.'], ...]
                    │  ├─ Call 2: backtrack(1) -- Placing queen in row 1
                    │  │  ├─ Try col=0: is_safe(1, 0)?
                    │  │  │  ├─ col 0 in occupied_cols{0}? Yes ❌
                    │  │  │  └─ UNSAFE! Skip col 0
                    │  │  ├─ Try col=1: is_safe(1, 1)?
                    │  │  │  ├─ col 1 in occupied_cols{0}? No ✓
                    │  │  │  ├─ (1-1=0) in pos_diag{0}? Yes ❌ (same main diagonal as (0,0))
                    │  │  │  └─ UNSAFE! Skip col 1
                    │  │  ├─ Try col=2: is_safe(1, 2)?
                    │  │  │  ├─ col 2 in occupied_cols{0}? No ✓
                    │  │  │  ├─ (1-2=-1) in pos_diag{0}? No ✓
                    │  │  │  ├─ (1+2=3) in neg_diag{0}? No ✓
                    │  │  │  ├─ SAFE! Place queen at (1,2)
                    │  │  │  ├─ occupied_cols.add(2) → {0, 2}
                    │  │  │  ├─ pos_diag.add(1-2=-1) → {0, -1}
                    │  │  │  ├─ neg_diag.add(1+2=3) → {0, 3}
                    │  │  │  ├─ board[1][2] = 'Q'
                    │  │  │  ├─ Board: [['Q', '.', '.', '.'], ['.', '.', 'Q', '.'], ...]
                    │  │  │  ├─ Call 3: backtrack(2) -- Placing queen in row 2
                    │  │  │  │  ├─ Try col=0: is_safe(2, 0)?
                    │  │  │  │  │  ├─ col 0 in occupied_cols{0, 2}? Yes ❌
                    │  │  │  │  │  └─ UNSAFE! Skip col 0
                    │  │  │  │  ├─ Try col=1: is_safe(2, 1)?
                    │  │  │  │  │  ├─ col 1 in occupied_cols{0, 2}? No ✓
                    │  │  │  │  │  ├─ (2-1=1) in pos_diag{0, -1}? No ✓
                    │  │  │  │  │  ├─ (2+1=3) in neg_diag{0, 3}? Yes ❌ (same anti-diagonal as (1,2))
                    │  │  │  │  │  └─ UNSAFE! Skip col 1
                    │  │  │  │  ├─ Try col=2: is_safe(2, 2)?
                    │  │  │  │  │  ├─ col 2 in occupied_cols{0, 2}? Yes ❌
                    │  │  │  │  │  └─ UNSAFE! Skip col 2
                    │  │  │  │  ├─ Try col=3: is_safe(2, 3)?
                    │  │  │  │  │  ├─ col 3 in occupied_cols{0, 2}? No ✓
                    │  │  │  │  │  ├─ (2-3=-1) in pos_diag{0, -1}? Yes ❌ (same main diagonal as (1,2))
                    │  │  │  │  │  └─ UNSAFE! Skip col 3
                    │  │  │  │  └─ NO VALID POSITIONS in row 2! Backtrack...
                    │  │  │  ├─ BACKTRACK from Call 3:
                    │  │  │  ├─ occupied_cols.remove(2) → {0}
                    │  │  │  ├─ pos_diag.remove(-1) → {0}
                    │  │  │  ├─ neg_diag.remove(3) → {0}
                    │  │  │  ├─ board[1][2] = '.'
                    │  │  │  └─ Board: [['Q', '.', '.', '.'], ['.', '.', '.', '.'], ...]
                    │  │  ├─ Try col=3: is_safe(1, 3)?
                    │  │  │  ├─ col 3 in occupied_cols{0}? No ✓
                    │  │  │  ├─ (1-3=-2) in pos_diag{0}? No ✓
                    │  │  │  ├─ (1+3=4) in neg_diag{0}? No ✓
                    │  │  │  ├─ SAFE! Place queen at (1,3)
                    │  │  │  ├─ occupied_cols.add(3) → {0, 3}
                    │  │  │  ├─ pos_diag.add(-2) → {0, -2}
                    │  │  │  ├─ neg_diag.add(4) → {0, 4}
                    │  │  │  ├─ Call 4: backtrack(2) -- Placing queen in row 2
                    │  │  │  │  ├─ Try col=0: UNSAFE (same column)
                    │  │  │  │  ├─ Try col=1: is_safe(2, 1)?
                    │  │  │  │  │  ├─ col 1 in occupied_cols{0, 3}? No ✓
                    │  │  │  │  │  ├─ (2-1=1) in pos_diag{0, -2}? No ✓
                    │  │  │  │  │  ├─ (2+1=3) in neg_diag{0, 4}? No ✓
                    │  │  │  │  │  ├─ SAFE! Place queen at (2,1)
                    │  │  │  │  │  ├─ Update sets: cols{0,3,1}, pos_diag{0,-2,1}, neg_diag{0,4,3}
                    │  │  │  │  │  ├─ Call 5: backtrack(3) -- Placing queen in row 3
                    │  │  │  │  │  │  ├─ Try col=0: UNSAFE (same column)
                    │  │  │  │  │  │  ├─ Try col=1: UNSAFE (same column)
                    │  │  │  │  │  │  ├─ Try col=2: is_safe(3, 2)?
                    │  │  │  │  │  │  │  ├─ col 2 in occupied_cols{0,1,3}? No ✓
                    │  │  │  │  │  │  │  ├─ (3-2=1) in pos_diag{0,-2,1}? Yes ❌
                    │  │  │  │  │  │  │  └─ UNSAFE! (same main diagonal as (2,1))
                    │  │  │  │  │  │  ├─ Try col=3: UNSAFE (same column)
                    │  │  │  │  │  │  └─ NO VALID POSITIONS! Backtrack...
                    │  │  │  │  │  └─ BACKTRACK from Call 5... (remove (2,1))
                    │  │  │  │  ├─ Try col=2: UNSAFE
                    │  │  │  │  ├─ Try col=3: UNSAFE (same column)
                    │  │  │  │  └─ NO VALID POSITIONS! Backtrack...
                    │  │  │  └─ BACKTRACK from Call 4... (remove (1,3))
                    │  │  └─ NO MORE COLUMNS in row 1! Backtrack...
                    │  └─ BACKTRACK from Call 2... (remove (0,0))
                    ├─ Try col=1: is_safe(0, 1)?
                    │  ├─ All sets now empty: occupied_cols{}, pos_diag{}, neg_diag{}
                    │  ├─ SAFE! Place queen at (0,1)
                    │  ├─ occupied_cols.add(1) → {1}
                    │  ├─ pos_diag.add(0-1=-1) → {-1}
                    │  ├─ neg_diag.add(0+1=1) → {1}
                    │  ├─ Call 6: backtrack(1) -- Continue exploring...
                    │  │  ├─ Try col=0: SAFE!
                    │  │  ├─ Try col=3: is_safe(1, 3)?
                    │  │  │  ├─ col 3 in occupied_cols{1}? No ✓
                    │  │  │  ├─ (1-3=-2) in pos_diag{-1}? No ✓
                    │  │  │  ├─ (1+3=4) in neg_diag{1}? No ✓
                    │  │  │  ├─ SAFE! Continue with (1,3)...
                    │  │  │  └─ Eventually find first solution: [".Q..", "...Q", "Q...", "..Q."]
                    │  │  └─ Add solution to result!
                    │  └─ Continue exploring other branches...
                    ├─ Try col=2: ... (similar exploration)
                    ├─ Try col=3: ... (similar exploration)
                    └─ FINAL RESULT: 2 solutions found

        '''

        occupied_cols = set()
        pos_diag = set()
        neg_diag = set()

        result = []
        board = [["."] * n for i in range(n)]
        def is_safe(row, col):
            # check if placing the queen at the [row][col] is safe

            # check col
            if col in occupied_cols:
                return False

            # check main diagonal ↘
            if (row + col) in pos_diag:
                return False

            # check anti diagonal ↘
            if (row - col) in neg_diag:
                return False

            return True

        def backtrack(row):
            if row == n:
                copy = [''.join(row) for row in board]
                result.append(copy)
                return

            for col in range(n):
                if not is_safe(row,col):
                    continue

                occupied_cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                board[row][col] = 'Q'

                backtrack(row + 1)

                # if we hit a dead end, we undo all changes (remove queen from board, remove col from occupied cols, remove diagonal values, get completely back to state before choice for col was made in for loop)
                occupied_cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                board[row][col] = '.'

        backtrack(0)
        return result



    @staticmethod
    def solve_sudoku(board):
        '''
            Solve a 9x9 sudoku puzzle

            Args:
                board: 9x9 grid with '.' for empty cells, digits for filled

            Returns:
                True if solvable (modifies board in place), false otherwise


            Q) What is the time and space complexity?
                a) Time complexity is O(9^(empty_cells)) -> worst case is try every possibility
                a) Space complexity is O(1) -> constant extra space
            Q) What is the backtracking framework?
                a) CHOICE: Try digits 1-9 in an empty cell
                a) CONSTRAINT: Must follow sudoku rules
                    - each row contains digits 1-9 exactly once
                    - each col contains digits 1-9 exactly once
                    - each 3x3 box contains digits 1-9 exactly once
                a) GOAL: no empty cells

            Descriptions/Walkthroughs)

                         Box Index Mapping:

                Sudoku Grid:             Box Indices:
                0 1 2 | 3 4 5 | 6 7 8    0 0 0 | 1 1 1 | 2 2 2
                0 1 2 | 3 4 5 | 6 7 8    0 0 0 | 1 1 1 | 2 2 2
                0 1 2 | 3 4 5 | 6 7 8    0 0 0 | 1 1 1 | 2 2 2
                ------+-------+------    ------+-------+------
                0 1 2 | 3 4 5 | 6 7 8    3 3 3 | 4 4 4 | 5 5 5
                0 1 2 | 3 4 5 | 6 7 8    3 3 3 | 4 4 4 | 5 5 5
                0 1 2 | 3 4 5 | 6 7 8    3 3 3 | 4 4 4 | 5 5 5
                ------+-------+------    ------+-------+------
                0 1 2 | 3 4 5 | 6 7 8    6 6 6 | 7 7 7 | 8 8 8
                0 1 2 | 3 4 5 | 6 7 8    6 6 6 | 7 7 7 | 8 8 8
                0 1 2 | 3 4 5 | 6 7 8    6 6 6 | 7 7 7 | 8 8 8

                Formula: box_index = (row // 3) * 3 + (col // 3)


                         Complete Walkthrough: Simple 4x4 Sudoku

                For clarity, let's trace a simplified 4x4 Sudoku (digits 1-4, 2x2 boxes):

                Initial Board:

                            1 . | . 4
                            . 4 | 1 .
                            ----+----
                            . 1 | 4 .
                            4 . | . 1

                            Box Layout:

                            Box 0 | Box 1
                            ------+------
                            Box 2 | Box 3

                Initial Constraint Sets:
                row_sets = [{'1', '4'}, {'4', '1'}, {'1', '4'}, {'4', '1'}]
                col_sets = [{'1', '4'}, {'4', '1'}, {'1', '4'}, {'4', '1'}]
                box_sets = [{'1', '4'}, {'4', '1'}, {'1', '4'}, {'4', '1'}]

                empty_cells = [(0,1), (0,2), (1,0), (1,3), (2,0), (2,3), (3,1), (3,2)]
                Execution Trace:
                Call 1: backtrack(0) -- Processing cell (0,1)
                ├─ Current cell: (0,1), box_index = (0//2)*2 + (1//2) = 0
                ├─ Try digit '1': is_safe(0, 1, '1')?
                │  ├─ '1' in row_sets[0]{'1','4'}? Yes ❌
                │  └─ UNSAFE! Skip
                ├─ Try digit '2': is_safe(0, 1, '2')?
                │  ├─ '2' in row_sets[0]{'1','4'}? No ✓
                │  ├─ '2' in col_sets[1]{'4','1'}? No ✓
                │  ├─ '2' in box_sets[0]{'1','4'}? No ✓
                │  ├─ SAFE! Place '2' at (0,1)
                │  ├─ board[0][1] = '2'
                │  ├─ row_sets[0].add('2') → {'1','4','2'}
                │  ├─ col_sets[1].add('2') → {'4','1','2'}
                │  ├─ box_sets[0].add('2') → {'1','4','2'}
                │  ├─ Board now: [['1','2','.','4'], ['.','4','1','.'], ...]
                │  ├─ Call 2: backtrack(1) -- Processing cell (0,2)
                │  │  ├─ Current cell: (0,2), box_index = (0//2)*2 + (2//2) = 1
                │  │  ├─ Try digit '1': is_safe(0, 2, '1')?
                │  │  │  ├─ '1' in row_sets[0]{'1','4','2'}? Yes ❌
                │  │  │  └─ UNSAFE! Skip
                │  │  ├─ Try digit '2': is_safe(0, 2, '2')?
                │  │  │  ├─ '2' in row_sets[0]{'1','4','2'}? Yes ❌
                │  │  │  └─ UNSAFE! Skip
                │  │  ├─ Try digit '3': is_safe(0, 2, '3')?
                │  │  │  ├─ '3' in row_sets[0]{'1','4','2'}? No ✓
                │  │  │  ├─ '3' in col_sets[2]{'1','4'}? No ✓
                │  │  │  ├─ '3' in box_sets[1]{'4','1'}? No ✓
                │  │  │  ├─ SAFE! Place '3' at (0,2)
                │  │  │  ├─ board[0][2] = '3', update sets
                │  │  │  ├─ Board: [['1','2','3','4'], ['.','4','1','.'], ...]
                │  │  │  ├─ Call 3: backtrack(2) -- Processing cell (1,0)
                │  │  │  │  ├─ Current cell: (1,0), box_index = (1//2)*2 + (0//2) = 0
                │  │  │  │  ├─ Try digit '1':
                │  │  │  │  │  ├─ '1' in row_sets[1]{'4','1'}? Yes ❌
                │  │  │  │  ├─ Try digit '2':
                │  │  │  │  │  ├─ '2' in row_sets[1]{'4','1'}? No ✓
                │  │  │  │  │  ├─ '2' in col_sets[0]{'1','4'}? No ✓
                │  │  │  │  │  ├─ '2' in box_sets[0]{'1','4','2'}? Yes ❌
                │  │  │  │  │  └─ UNSAFE! (Already used '2' in box 0)
                │  │  │  │  ├─ Try digit '3':
                │  │  │  │  │  ├─ '3' in row_sets[1]{'4','1'}? No ✓
                │  │  │  │  │  ├─ '3' in col_sets[0]{'1','4'}? No ✓
                │  │  │  │  │  ├─ '3' in box_sets[0]{'1','4','2','3'}? Yes ❌
                │  │  │  │  │  └─ UNSAFE! (Already used '3' in box 0)
                │  │  │  │  ├─ Try digit '4':
                │  │  │  │  │  ├─ '4' in row_sets[1]{'4','1'}? Yes ❌
                │  │  │  │  │  └─ UNSAFE!
                │  │  │  │  └─ NO VALID DIGITS! Backtrack...
                │  │  │  ├─ BACKTRACK from Call 3:
                │  │  │  ├─ board[0][2] = '.'
                │  │  │  ├─ row_sets[0].remove('3') → {'1','4','2'}
                │  │  │  ├─ col_sets[2].remove('3') → {'1','4'}
                │  │  │  ├─ box_sets[1].remove('3') → {'4','1'}
                │  │  │  └─ Board restored: [['1','2','.','4'], ['.','4','1','.'], ...]
                │  │  ├─ Try digit '4': is_safe(0, 2, '4')?
                │  │  │  ├─ '4' in row_sets[0]{'1','4','2'}? Yes ❌
                │  │  │  └─ UNSAFE! Skip
                │  │  └─ NO MORE DIGITS! Backtrack...
                │  ├─ BACKTRACK from Call 2:
                │  ├─ board[0][1] = '.'
                │  ├─ row_sets[0].remove('2') → {'1','4'}
                │  ├─ col_sets[1].remove('2') → {'4','1'}
                │  ├─ box_sets[0].remove('2') → {'1','4'}
                │  └─ Board restored: [['1','.', '.','4'], ['.','4','1','.'], ...]
                ├─ Try digit '3': is_safe(0, 1, '3')?
                │  ├─ '3' in row_sets[0]{'1','4'}? No ✓
                │  ├─ '3' in col_sets[1]{'4','1'}? No ✓
                │  ├─ '3' in box_sets[0]{'1','4'}? No ✓
                │  ├─ SAFE! Place '3' at (0,1)
                │  ├─ Update sets and continue...
                │  ├─ Call 4: backtrack(1) -- Try (0,2) with '3' at (0,1)
                │  │  ├─ Only digit '2' is valid for (0,2) now
                │  │  ├─ Place '2', continue to next cell...
                │  │  └─ Eventually find complete solution!
                │  └─ SUCCESS! Return True
                └─ SOLUTION FOUND:
                   [['1','3','2','4'],
                    ['2','4','1','3'],
                    ['3','1','4','2'],
                    ['4','2','3','1']]
        '''

        # track which digits are used in each row, column, and 3x3 box
        row_sets = [set() for _ in range(9)] # row_sets[i] = digits used in row i
        col_sets = [set() for _ in range(9)] # col_sets[j] = digits used in col j
        box_sets = [set() for _ in range(9)] # box_sets[k] = digits used in box k


        # collect empty cells
        empty_cells = []

        def get_box_index(row, col):
            ''' convert row,col to a box index (0-8)'''

            return (row // 3) * 3 + (col // 3)
        # initialize constraint set with existing numbers
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    digit = board[row][col]
                    row_sets[row].add(digit)
                    col_sets[col].add(digit)
                    box_sets[get_box_index(row, col)].add(digit)
                else:
                    empty_cells.append((row, col))


        def is_safe(row, col, digit):
            ''' check if placing digit violates constraints'''
            box_idx = get_box_index(row, col)

            if digit in row_sets[row]:
                return False
            if digit in col_sets[col]:
                return False
            if digit in box_sets[box_idx]:
                return False

            return True

        def backtrack(cell_index):
            #GOAL: all empty cells filled
            if cell_index == len(empty_cells):
                return True

            row, col = empty_cells[cell_index]
            box_idx = get_box_index(row, col)

            #CHOICE: try digits 1-9
            potential_digits = '123456789'
            for digit in potential_digits:
                if is_safe(row, col, digit):
                    # make choice: place digit and update constraint sets
                    board[row][col] = digit
                    row_sets[row].add(digit)
                    col_sets[col].add(digit)
                    box_sets[box_idx].add(digit)

                    # recurse back to empty cell
                    if backtrack(cell_index + 1):
                        return True

                    # undo choice by removing digit and restoring sets
                    board[row][col] = '.'
                    row_sets[row].remove(digit)
                    col_sets[col].remove(digit)
                    box_sets[box_idx].remove(digit)

            return False # no valid digit found for this cell

        backtrack(0)


    @staticmethod
    def generate_parentheses(n):
        '''
            Generate all valid combinations of n pairs of parentheses

            Args:
                n: number of parenthesis pairs

            Returns:
                list of all valid parentheses combinations

            Q) What is the time and space complexity?
                a) Time complexity is O(4^n / sqrt(n)) - Catalan number
                a) Space complexity is O(4^n / sqrt(n)) - storing all combinations
            Q) What is the backtracking framework?
                a) CHOICE: add '(' or ')'
                a) CONSTRAINT: open_count <= n, close_count <= open_count
                a) GOAL: Used all n pairs

            Brief Example) n = 3
                1. valid:
                    - ((()))
                    - (()())
                    - ()(())
                    - ()()()
                2. invalid:
                    - ((((too many opens)))
                    - ))) -> close before opens


            Complete Walkthrough: generateParentheses(2)

                Goal: Generate all valid combinations of 2 pairs of parentheses
                Expected Result: ["(())", "()()"]
                Initial State:
                n = 2
                result = []
                current_path = []
                Execution Trace:
                Call 1: backtrack(0, 0) -- open_count=0, close_count=0
                ├─ current_path = [], length = 0 (need 2*2=4 total)
                ├─ Try char='(':
                │  ├─ is_safe('(', 0, 0)? open_count(0) < n(2)? Yes ✓
                │  ├─ Make choice: current_path.append('(') → ['(']
                │  ├─ new_open=1, new_close=0
                │  ├─ Call 2: backtrack(1, 0) -- open_count=1, close_count=0
                │  │  ├─ current_path = ['('], length = 1
                │  │  ├─ Try char='(':
                │  │  │  ├─ is_safe('(', 1, 0)? open_count(1) < n(2)? Yes ✓
                │  │  │  ├─ Make choice: current_path.append('(') → ['(', '(']
                │  │  │  ├─ new_open=2, new_close=0
                │  │  │  ├─ Call 3: backtrack(2, 0) -- open_count=2, close_count=0
                │  │  │  │  ├─ current_path = ['(', '('], length = 2
                │  │  │  │  ├─ Try char='(':
                │  │  │  │  │  ├─ is_safe('(', 2, 0)? open_count(2) < n(2)? No ❌
                │  │  │  │  │  └─ UNSAFE! Skip '('
                │  │  │  │  ├─ Try char=')':
                │  │  │  │  │  ├─ is_safe(')', 2, 0)? close_count(0) < open_count(2)? Yes ✓
                │  │  │  │  │  ├─ Make choice: current_path.append(')') → ['(', '(', ')']
                │  │  │  │  │  ├─ new_open=2, new_close=1
                │  │  │  │  │  ├─ Call 4: backtrack(2, 1) -- open_count=2, close_count=1
                │  │  │  │  │  │  ├─ current_path = ['(', '(', ')'], length = 3
                │  │  │  │  │  │  ├─ Try char='(':
                │  │  │  │  │  │  │  ├─ is_safe('(', 2, 1)? open_count(2) < n(2)? No ❌
                │  │  │  │  │  │  │  └─ UNSAFE! Skip '('
                │  │  │  │  │  │  ├─ Try char=')':
                │  │  │  │  │  │  │  ├─ is_safe(')', 2, 1)? close_count(1) < open_count(2)? Yes ✓
                │  │  │  │  │  │  │  ├─ Make choice: current_path.append(')') → ['(', '(', ')', ')']
                │  │  │  │  │  │  │  ├─ new_open=2, new_close=2
                │  │  │  │  │  │  │  ├─ Call 5: backtrack(2, 2) -- open_count=2, close_count=2
                │  │  │  │  │  │  │  │  ├─ current_path = ['(', '(', ')', ')'], length = 4
                │  │  │  │  │  │  │  │  ├─ GOAL! len(current_path) == 2*n(2) = 4
                │  │  │  │  │  │  │  │  ├─ result.append('(())') → result = ['(())']
                │  │  │  │  │  │  │  │  └─ Return
                │  │  │  │  │  │  │  └─ Undo: current_path.pop() → ['(', '(', ')']
                │  │  │  │  │  │  └─ Return to Call 4
                │  │  │  │  │  └─ Undo: current_path.pop() → ['(', '(']
                │  │  │  │  └─ Return to Call 3
                │  │  │  └─ Undo: current_path.pop() → ['(']
                │  │  ├─ Try char=')':
                │  │  │  ├─ is_safe(')', 1, 0)? close_count(0) < open_count(1)? Yes ✓
                │  │  │  ├─ Make choice: current_path.append(')') → ['(', ')']
                │  │  │  ├─ new_open=1, new_close=1
                │  │  │  ├─ Call 6: backtrack(1, 1) -- open_count=1, close_count=1
                │  │  │  │  ├─ current_path = ['(', ')'], length = 2
                │  │  │  │  ├─ Try char='(':
                │  │  │  │  │  ├─ is_safe('(', 1, 1)? open_count(1) < n(2)? Yes ✓
                │  │  │  │  │  ├─ Make choice: current_path.append('(') → ['(', ')', '(']
                │  │  │  │  │  ├─ new_open=2, new_close=1
                │  │  │  │  │  ├─ Call 7: backtrack(2, 1) -- open_count=2, close_count=1
                │  │  │  │  │  │  ├─ current_path = ['(', ')', '('], length = 3
                │  │  │  │  │  │  ├─ Try char='(':
                │  │  │  │  │  │  │  ├─ is_safe('(', 2, 1)? open_count(2) < n(2)? No ❌
                │  │  │  │  │  │  │  └─ UNSAFE! Skip '('
                │  │  │  │  │  │  ├─ Try char=')':
                │  │  │  │  │  │  │  ├─ is_safe(')', 2, 1)? close_count(1) < open_count(2)? Yes ✓
                │  │  │  │  │  │  │  ├─ Make choice: current_path.append(')') → ['(', ')', '(', ')']
                │  │  │  │  │  │  │  ├─ new_open=2, new_close=2
                │  │  │  │  │  │  │  ├─ Call 8: backtrack(2, 2)
                │  │  │  │  │  │  │  │  ├─ current_path = ['(', ')', '(', ')'], length = 4
                │  │  │  │  │  │  │  │  ├─ GOAL! len(current_path) == 4
                │  │  │  │  │  │  │  │  ├─ result.append('()()') → result = ['(())', '()()']
                │  │  │  │  │  │  │  │  └─ Return
                │  │  │  │  │  │  │  └─ Undo: current_path.pop() → ['(', ')', '(']
                │  │  │  │  │  │  └─ Return to Call 7
                │  │  │  │  │  └─ Undo: current_path.pop() → ['(', ')']
                │  │  │  │  ├─ Try char=')':
                │  │  │  │  │  ├─ is_safe(')', 1, 1)? close_count(1) < open_count(1)? No ❌
                │  │  │  │  │  └─ UNSAFE! (would have equal opens and closes, but still need more)
                │  │  │  │  └─ Return to Call 6
                │  │  │  └─ Undo: current_path.pop() → ['(']
                │  │  └─ Return to Call 2
                │  └─ Undo: current_path.pop() → []
                ├─ Try char=')':
                │  ├─ is_safe(')', 0, 0)? close_count(0) < open_count(0)? No ❌
                │  └─ UNSAFE! (can't start with closing bracket)
                └─ Return final result: ['(())', '()()']
        '''

        result = []
        current_path = [] # build string as list

        def is_safe(char, open_count, close_count):
            ''' check if adding this char violates constraints'''

            if char == '(':
                return open_count < n # can add ( if we haven't used all n opening brackets
            else:
                return close_count < open_count # can add ) if we have unmatched opening brackets

        def backtrack(open_count, close_count):
            #GOAL: use all n pairs (so total length is 2n)
            if len(current_path) == 2 * n:
                result.append(''.join(current_path))
                return

            # CHOICE: try adding ( or )
            for char  in ['(', ')']:
                if is_safe(char, open_count, close_count):
                    current_path.append(char)
                    new_open = open_count + 1 if char == '(' else open_count
                    new_close = close_count + 1 if char == ')' else close_count


                    # recurse
                    backtrack(new_open, new_close)

                    # undo to reset state by removing char
                    current_path.pop()

        backtrack(0,0)
        return result



    @staticmethod
    def letter_combinations(digits):
        '''
            Generate all letter combinations for phone number digits

            Args:
                digits: string of digits 2-9

            Returns:
                list of all possible letter combinations

            Q) What is the time and space complexity?
                a) Time complexity is O(4^n) -> worst case 4 letters per digit
                a) Space complexity is O(4^n) -> storing all combinations
            Q) What is the backtracking framework?
                a) CHOICE: Pick any letter for current digit
                a) CONSTRAINT: Must use digits in order
                a) GOAL: Processed all digits

            Brief Example)
                digits = [2,3] where 2 maps to 'abc' and 3 maps to 'def'
                results = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

            Complete Execution Trace:
                Call 1: backtrack('', 0) -- index=0, processing digit '2'
                ├─ index (0) != len(digits) (2), so continue
                ├─ current_digit = digits[0] = '2'
                ├─ phone_map['2'] = 'abc'
                ├─ Loop: for letter in 'abc' -- try letters 'a', 'b', 'c'
                ├─ letter='a': Try adding 'a'
                │  ├─ Call 2: backtrack('a', 1) -- index=1, processing digit '3'
                │  │  ├─ index (1) != len(digits) (2), so continue
                │  │  ├─ current_digit = digits[1] = '3'
                │  │  ├─ phone_map['3'] = 'def'
                │  │  ├─ Loop: for letter in 'def' -- try letters 'd', 'e', 'f'
                │  │  ├─ letter='d': Try adding 'd'
                │  │  │  ├─ Call 3: backtrack('ad', 2)
                │  │  │  │  ├─ GOAL! index (2) == len(digits) (2)
                │  │  │  │  └─ Add "ad" to result → result = ["ad"]
                │  │  │  └─ Return to Call 2
                │  │  ├─ letter='e': Try adding 'e'
                │  │  │  ├─ Call 4: backtrack('ae', 2)
                │  │  │  │  ├─ GOAL! index (2) == len(digits) (2)
                │  │  │  │  └─ Add "ae" to result → result = ["ad", "ae"]
                │  │  │  └─ Return to Call 2
                │  │  ├─ letter='f': Try adding 'f'
                │  │  │  ├─ Call 5: backtrack('af', 2)
                │  │  │  │  ├─ GOAL! index (2) == len(digits) (2)
                │  │  │  │  └─ Add "af" to result → result = ["ad", "ae", "af"]
                │  │  │  └─ Return to Call 2
                │  │  └─ Return to Call 1 (finished all letters for digit '3')
                │  └─ Continue with next letter in Call 1
                ├─ letter='b': Try adding 'b'
                │  ├─ Call 6: backtrack('b', 1) -- index=1, processing digit '3'
                │  │  ├─ index (1) != len(digits) (2), so continue
                │  │  ├─ current_digit = digits[1] = '3'
                │  │  ├─ phone_map['3'] = 'def'
                │  │  ├─ Loop: for letter in 'def' -- try letters 'd', 'e', 'f'
                │  │  ├─ letter='d': Try adding 'd'
                │  │  │  ├─ Call 7: backtrack('bd', 2)
                │  │  │  │  ├─ GOAL! index (2) == len(digits) (2)
                │  │  │  │  └─ Add "bd" to result → result = ["ad", "ae", "af", "bd"]
                │  │  │  └─ Return to Call 6
                │  │  ├─ letter='e': Try adding 'e'
                │  │  │  ├─ Call 8: backtrack('be', 2)
                │  │  │  │  ├─ GOAL! index (2) == len(digits) (2)
                │  │  │  │  └─ Add "be" to result → result = ["ad", "ae", "af", "bd", "be"]
                │  │  │  └─ Return to Call 6
                │  │  ├─ letter='f': Try adding 'f'
                │  │  │  ├─ Call 9: backtrack('bf', 2)
                │  │  │  │  ├─ GOAL! index (2) == len(digits) (2)
                │  │  │  │  └─ Add "bf" to result → result = ["ad", "ae", "af", "bd", "be", "bf"]
                │  │  │  └─ Return to Call 6
                │  │  └─ Return to Call 1 (finished all letters for digit '3')
                │  └─ Continue with next letter in Call 1
                ├─ letter='c': Try adding 'c'
                │  ├─ Call 10: backtrack('c', 1) -- index=1, processing digit '3'
                │  │  ├─ index (1) != len(digits) (2), so continue
                │  │  ├─ current_digit = digits[1] = '3'
                │  │  ├─ phone_map['3'] = 'def'
                │  │  ├─ Loop: for letter in 'def' -- try letters 'd', 'e', 'f'
                │  │  ├─ letter='d': Try adding 'd'
                │  │  │  ├─ Call 11: backtrack('cd', 2)
                │  │  │  │  ├─ GOAL! index (2) == len(digits) (2)
                │  │  │  │  └─ Add "cd" to result → result = ["ad", "ae", "af", "bd", "be", "bf", "cd"]
                │  │  │  └─ Return to Call 10
                │  │  ├─ letter='e': Try adding 'e'
                │  │  │  ├─ Call 12: backtrack('ce', 2)
                │  │  │  │  ├─ GOAL! index (2) == len(digits) (2)
                │  │  │  │  └─ Add "ce" to result → result = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce"]
                │  │  │  └─ Return to Call 10
                │  │  ├─ letter='f': Try adding 'f'
                │  │  │  ├─ Call 13: backtrack('cf', 2)
                │  │  │  │  ├─ GOAL! index (2) == len(digits) (2)
                │  │  │  │  └─ Add "cf" to result → result = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
                │  │  │  └─ Return to Call 10
                │  │  └─ Return to Call 1 (finished all letters for digit '3')
                │  └─ Finished all letters for digit '2'
                └─ Return final result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

        '''

        if not digits:
            return []

        phone_map = {
                '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'
        }

        def backtrack(index, temp):
            #GOAL: processed all digits
            if index == len(digits):
                result.append(''.join(temp))
                return

            #CHOICE: try each letter for the current digit
            current_digit = digits[index]
            for letter in phone_map[current_digit]:
                temp.append(letter) # make the choice/select the letter
                backtrack(index + 1, temp)
                temp.pop()

        result = []
        backtrack(0, [])
        return result


