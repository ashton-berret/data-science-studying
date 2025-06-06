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

            # CHOICE - try each remaining number
                # make choice

                # recurse -> go deeper into the decision tree with the new updated state, handle all possibilities from the newly established point

                # undo choice (backtrack) -> restore the state to what it was before the iteration (for example if this iteration went [1, 2, 3], then we pop back to [1] so we can do [1, 3, 2])

            pass
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

            # CHOICE: try numbers from start_num to n
                # CONSTRAINT: automatically satisfied by using start_num

                # recurse with next start number

                # undo choice

            pass

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
            pass

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

        def is_safe(row, col):
            # check if placing the queen at the [row][col] is safe

            # check col

            # check main diagonal ↘

            # check anti diagonal ↘

            pass
        def backtrack(row):

                # if we hit a dead end, we undo all changes (remove queen from board, remove col from occupied cols, remove diagonal values, get completely back to state before choice for col was made in for loop)

            pass


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


        # collect empty cells

        def get_box_index(row, col):
            ''' convert row,col to a box index (0-8)'''

        # initialize constraint set with existing numbers

            pass

        def is_safe(row, col, digit):
            ''' check if placing digit violates constraints'''
            pass

        def backtrack(cell_index):
            #GOAL: all empty cells filled


            #CHOICE: try digits 1-9
                    # make choice: place digit and update constraint sets

                    # recurse back to empty cell

                    # undo choice by removing digit and restoring sets


            pass

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


        def is_safe(char, open_count, close_count):
            ''' check if adding this char violates constraints'''


        def backtrack(open_count, close_count):
            #GOAL: use all n pairs (so total length is 2n)

            # CHOICE: try adding ( or )


                    # recurse

                    # undo to reset state by removing char

            pass


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

        phone_map = {
                '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'
        }

        def backtrack(index, temp):
            #GOAL: processed all digits

            #CHOICE: try each letter for the current digit

            pass

    @staticmethod
    def word_search(board, word):
        '''
            Find if a word exists in the grid using adjacent cells

            Args:
                board: 2D grid of characters
                word: target word to find

            Return:
                true if exists, false otherwise

            Q) What is the time and space complexity?
                a) Time complexity is O(m*n*4^L) -> mxn grid, 4 directions to search, L is length of word
                a) Space complexity is O(L) -> recursion depth
            Q) What is the backtracking framework?
                a) CHOICE: Move to any of the 4 adjacent cells
                b) CONSTRAINT: Stay in bounds, don't revisit cells, characters must match
                c) GOAL: match entire target word

            Advanced Walkthrough)
                Example Setup:
                    Board:
                    [['A', 'B', 'C'],
                     ['S', 'F', 'E'],
                     ['A', 'D', 'G']]
                    Word: "ABCE"
                    Expected: True (path: A→B→C→E)

                Complete Execution Trace:
                    Phase 1: Try starting from (0,0) - 'A'
                    Call 1: backtrack(0, 0, 0, {}) -- row=0, col=0, index=0, looking for 'A'
                    ├─ index (0) != len(word) (4), continue
                    ├─ Check constraints:
                    │  ├─ row=0, col=0 in bounds ✓
                    │  ├─ board[0][0] = 'A' == word[0] = 'A' ✓
                    │  ├─ (0,0) not in visited ✓
                    │  └─ All constraints passed
                    ├─ Make choice: visited.add((0,0)) → visited = {(0,0)}
                    ├─ Try all 4 directions from (0,0):
                    ├─ Direction 1: (0,1) - right to position (0,1)
                    │  ├─ Call 2: backtrack(0, 1, 1, {(0,0)}) -- looking for 'B' at (0,1)
                    │  │  ├─ index (1) != len(word) (4), continue
                    │  │  ├─ Check constraints:
                    │  │  │  ├─ row=0, col=1 in bounds ✓
                    │  │  │  ├─ board[0][1] = 'B' == word[1] = 'B' ✓
                    │  │  │  ├─ (0,1) not in visited ✓
                    │  │  │  └─ All constraints passed
                    │  │  ├─ Make choice: visited.add((0,1)) → visited = {(0,0), (0,1)}
                    │  │  ├─ Try all 4 directions from (0,1):
                    │  │  ├─ Direction 1: (0,2) - right to position (0,2)
                    │  │  │  ├─ Call 3: backtrack(0, 2, 2, {(0,0), (0,1)}) -- looking for 'C' at (0,2)
                    │  │  │  │  ├─ index (2) != len(word) (4), continue
                    │  │  │  │  ├─ Check constraints:
                    │  │  │  │  │  ├─ row=0, col=2 in bounds ✓
                    │  │  │  │  │  ├─ board[0][2] = 'C' == word[2] = 'C' ✓
                    │  │  │  │  │  ├─ (0,2) not in visited ✓
                    │  │  │  │  │  └─ All constraints passed
                    │  │  │  │  ├─ Make choice: visited.add((0,2)) → visited = {(0,0), (0,1), (0,2)}
                    │  │  │  │  ├─ Try all 4 directions from (0,2):
                    │  │  │  │  ├─ Direction 1: (0,3) - right to position (0,3)
                    │  │  │  │  │  ├─ Call 4: backtrack(0, 3, 3, {(0,0), (0,1), (0,2)})
                    │  │  │  │  │  │  ├─ CONSTRAINT FAIL: col=3 >= cols=3 (out of bounds)
                    │  │  │  │  │  │  └─ Return False
                    │  │  │  │  ├─ Direction 2: (0,1) - left to position (0,1)
                    │  │  │  │  │  ├─ Call 5: backtrack(0, 1, 3, {(0,0), (0,1), (0,2)})
                    │  │  │  │  │  │  ├─ CONSTRAINT FAIL: (0,1) already in visited
                    │  │  │  │  │  │  └─ Return False
                    │  │  │  │  ├─ Direction 3: (1,2) - down to position (1,2)
                    │  │  │  │  │  ├─ Call 6: backtrack(1, 2, 3, {(0,0), (0,1), (0,2)}) -- looking for 'E' at (1,2)
                    │  │  │  │  │  │  ├─ index (3) != len(word) (4), continue
                    │  │  │  │  │  │  ├─ Check constraints:
                    │  │  │  │  │  │  │  ├─ row=1, col=2 in bounds ✓
                    │  │  │  │  │  │  │  ├─ board[1][2] = 'E' == word[3] = 'E' ✓
                    │  │  │  │  │  │  │  ├─ (1,2) not in visited ✓
                    │  │  │  │  │  │  │  └─ All constraints passed
                    │  │  │  │  │  │  ├─ Make choice: visited.add((1,2)) → visited = {(0,0), (0,1), (0,2), (1,2)}
                    │  │  │  │  │  │  ├─ Try all 4 directions from (1,2):
                    │  │  │  │  │  │  ├─ Direction 1: (1,3) - right
                    │  │  │  │  │  │  │  ├─ Call 7: backtrack(1, 3, 4, {...})
                    │  │  │  │  │  │  │  │  ├─ GOAL! index (4) == len(word) (4)
                    │  │  │  │  │  │  │  │  └─ Return True ✅
                    │  │  │  │  │  │  │  └─ SUCCESS! Found complete word
                    │  │  │  │  │  │  └─ Return True ✅
                    │  │  │  │  │  └─ Return True ✅
                    │  │  │  │  └─ Return True ✅
                    │  │  │  └─ Return True ✅
                    │  │  └─ Return True ✅
                    │  └─ Return True ✅
                    └─ SUCCESS! Word found starting from (0,0)
                    Final Result: True - Word "ABCE" found with path: (0,0)→(0,1)→(0,2)→(1,2)
        '''

        def backtrack(row, col, index, visited):
            #GOAL: matched entire word

            '''
                CONSTRAINT: check bounds and character match, not in visited
                    - board[row][col] != word[index] example)
                        - say we are trying to find first letter, index = 0, second letter index = 1, etc
            '''

            #CHOICE: mark as visited

            # try all 4 directions

            # undo choice

        # try starting from each cell

            pass

    @staticmethod
    def palindrome_partitioning(s):
        '''
            Partition a string into all possible palindrome strings

            Args:
                s) input string

            Returns:
                list of possible palindrome partitions

            Q) What is the time and space complexity?
                a) Time complexity is O(2^n * n) -> 2^n partitions, O(n) to check palindrome
                a) Space complexity is O(2^n * n)
            Q) What is the backtracking framework?
                a) CHOICE:
                a) CONSTRAINT:
                a) GOAL:

            Advanced Walkthrough)

                String: "aab"
                Expected Result: [["a","a","b"], ["aa","b"]]

                Slice Explanations:
                s[0:1] = "a" (character at index 0)
                s[0:2] = "aa" (characters from index 0 to 1)
                s[1:2] = "a" (character at index 1)
                s[2:3] = "b" (character at index 2)
                string[::-1] reverses the string (e.g., "aab"[::-1] = "baa")


                Complete Execution Trace:
                Call 1: backtrack(0, []) -- start=0, tmp=[], processing from index 0
                ├─ start (0) != len(s) (3), continue
                ├─ Loop: for end in range(0, 3) -- end can be 0, 1, or 2
                ├─ end=0: Try substring s[0:1] = "a"
                │  ├─ substring = s[0:0+1] = s[0:1] = "a"  # slice [0:1] gets character at index 0
                │  ├─ is_palindrome("a"): "a" == "a"[::-1] = "a" ✓
                │  ├─ tmp.append("a") → tmp = ["a"]
                │  ├─ Call 2: backtrack(1, ["a"]) -- start=1, tmp=["a"], processing from index 1
                │  │  ├─ start (1) != len(s) (3), continue
                │  │  ├─ Loop: for end in range(1, 3) -- end can be 1 or 2
                │  │  ├─ end=1: Try substring s[1:2] = "a"
                │  │  │  ├─ substring = s[1:1+1] = s[1:2] = "a"  # slice [1:2] gets character at index 1
                │  │  │  ├─ is_palindrome("a"): "a" == "a"[::-1] = "a" ✓
                │  │  │  ├─ tmp.append("a") → tmp = ["a", "a"]
                │  │  │  ├─ Call 3: backtrack(2, ["a", "a"]) -- start=2, tmp=["a","a"], processing from index 2
                │  │  │  │  ├─ start (2) != len(s) (3), continue
                │  │  │  │  ├─ Loop: for end in range(2, 3) -- end can only be 2
                │  │  │  │  ├─ end=2: Try substring s[2:3] = "b"
                │  │  │  │  │  ├─ substring = s[2:2+1] = s[2:3] = "b"  # slice [2:3] gets character at index 2
                │  │  │  │  │  ├─ is_palindrome("b"): "b" == "b"[::-1] = "b" ✓
                │  │  │  │  │  ├─ tmp.append("b") → tmp = ["a", "a", "b"]
                │  │  │  │  │  ├─ Call 4: backtrack(3, ["a", "a", "b"]) -- start=3, processed entire string
                │  │  │  │  │  │  ├─ GOAL! start (3) == len(s) (3)
                │  │  │  │  │  │  └─ ans.append(["a", "a", "b"]) → ans = [["a", "a", "b"]]
                │  │  │  │  │  └─ tmp.pop() → tmp = ["a", "a"]
                │  │  │  │  └─ Return to Call 3
                │  │  │  └─ tmp.pop() → tmp = ["a"]
                │  │  ├─ end=2: Try substring s[1:3] = "ab"
                │  │  │  ├─ substring = s[1:2+1] = s[1:3] = "ab"  # slice [1:3] gets characters from index 1 to 2
                │  │  │  ├─ is_palindrome("ab"): "ab" == "ab"[::-1] = "ba" ✗
                │  │  │  └─ Skip this choice (not a palindrome)
                │  │  └─ Return to Call 2
                │  └─ tmp.pop() → tmp = []
                ├─ end=1: Try substring s[0:2] = "aa"
                │  ├─ substring = s[0:1+1] = s[0:2] = "aa"  # slice [0:2] gets characters from index 0 to 1
                │  ├─ is_palindrome("aa"): "aa" == "aa"[::-1] = "aa" ✓
                │  ├─ tmp.append("aa") → tmp = ["aa"]
                │  ├─ Call 5: backtrack(2, ["aa"]) -- start=2, tmp=["aa"], processing from index 2
                │  │  ├─ start (2) != len(s) (3), continue
                │  │  ├─ Loop: for end in range(2, 3) -- end can only be 2
                │  │  ├─ end=2: Try substring s[2:3] = "b"
                │  │  │  ├─ substring = s[2:2+1] = s[2:3] = "b"  # slice [2:3] gets character at index 2
                │  │  │  ├─ is_palindrome("b"): "b" == "b"[::-1] = "b" ✓
                │  │  │  ├─ tmp.append("b") → tmp = ["aa", "b"]
                │  │  │  ├─ Call 6: backtrack(3, ["aa", "b"]) -- start=3, processed entire string
                │  │  │  │  ├─ GOAL! start (3) == len(s) (3)
                │  │  │  │  └─ ans.append(["aa", "b"]) → ans = [["a", "a", "b"], ["aa", "b"]]
                │  │  │  └─ tmp.pop() → tmp = ["aa"]
                │  │  └─ Return to Call 5
                │  └─ tmp.pop() → tmp = []
                ├─ end=2: Try substring s[0:3] = "aab"
                │  ├─ substring = s[0:2+1] = s[0:3] = "aab"  # slice [0:3] gets entire string
                │  ├─ is_palindrome("aab"): "aab" == "aab"[::-1] = "baa" ✗
                │  └─ Skip this choice (not a palindrome)
                └─ Return final result: [["a", "a", "b"], ["aa", "b"]]

                🔍 Slice Explanations in Detail:
                String Extraction:
                pythonsubstring = s[start:end + 1]

                s[0:1] → "a" (single character at index0)
                s[0:2] → "aa" (characters from index 0 to 1, end index 2 is exclusive)
                s[1:3] → "ab" (characters from index 1 to 2, end index 3 is exclusive)

                String Reversal:
                pythonstring[::-1]

                "a"[::-1] → "a" (single character reversed is same)
                "aa"[::-1] → "aa" (palindrome reversed is same)
                "ab"[::-1] → "ba" (reversed string)

                Deep Copy:
                pythonans.append(tmp[:])

                tmp[:] creates a shallow copy of the list
                Why needed: Without copy, all results would reference the same list
                Example: tmp = ["a"] → tmp[:] creates ["a"] as separate list

        '''

        def is_palindrome(string):
            pass
        def backtrack(start, temp):
            #GOAL: Processed entire string

            #CHOICE: try ending the current substring at each position
                # extract the substring from start to end (inclusive so + 1)

                #CONSTRAINT: substring must be palindrome
            pass


    @staticmethod
    def combination_sum(candidates, target):
        '''
            Find all the unique combinations that sum to the target (can reuse values)

            Args:
                candidates: list of distinct positive integers
                target: target sum

            Returns:
                list of all combinations

            Q) What is the time and space complexity?
                a) Time complexity is O(2^target) -> 2 is the base bc we are making two decisions?
                a) Space complexity is O(target) -> recursion depth
            Q) What is the backtracking framework?
                a) CHOICE: include current candidate (multiple times) or skip
                a) CONSTRAINT: current sum <= target
                a) GOAL: current sum == target


            Advanced Walkthrough)

                Candidates: [2, 3, 6, 7]
                Target: 7
                Expected Result: [[2, 2, 3], [7]]
                Key Insight: We can reuse the same number multiple times, but we process candidates in order to avoid duplicates.

                Complete Execution Trace:
                Call 1: backtrack(0, [], 0) -- start=0, tmp=[], current_sum=0
                ├─ current_sum (0) != target (7), continue
                ├─ current_sum (0) <= target (7), continue
                ├─ Loop: for i in range(0, 4) -- try candidates at indices 0,1,2,3
                ├─ i=0: Try candidate=2
                │  ├─ tmp.append(2) → tmp = [2]
                │  ├─ Call 2: backtrack(0, [2], 2) -- start=0, tmp=[2], current_sum=2
                │  │  ├─ current_sum (2) != target (7), continue
                │  │  ├─ current_sum (2) <= target (7), continue
                │  │  ├─ Loop: for i in range(0, 4) -- try candidates at indices 0,1,2,3
                │  │  ├─ i=0: Try candidate=2 (reusing same number)
                │  │  │  ├─ tmp.append(2) → tmp = [2, 2]
                │  │  │  ├─ Call 3: backtrack(0, [2, 2], 4) -- start=0, tmp=[2,2], current_sum=4
                │  │  │  │  ├─ current_sum (4) != target (7), continue
                │  │  │  │  ├─ current_sum (4) <= target (7), continue
                │  │  │  │  ├─ Loop: for i in range(0, 4) -- try candidates at indices 0,1,2,3
                │  │  │  │  ├─ i=0: Try candidate=2
                │  │  │  │  │  ├─ tmp.append(2) → tmp = [2, 2, 2]
                │  │  │  │  │  ├─ Call 4: backtrack(0, [2, 2, 2], 6) -- start=0, tmp=[2,2,2], current_sum=6
                │  │  │  │  │  │  ├─ current_sum (6) != target (7), continue
                │  │  │  │  │  │  ├─ current_sum (6) <= target (7), continue
                │  │  │  │  │  │  ├─ Loop: for i in range(0, 4) -- try candidates at indices 0,1,2,3
                │  │  │  │  │  │  ├─ i=0: Try candidate=2
                │  │  │  │  │  │  │  ├─ tmp.append(2) → tmp = [2, 2, 2, 2]
                │  │  │  │  │  │  │  ├─ Call 5: backtrack(0, [2, 2, 2, 2], 8)
                │  │  │  │  │  │  │  │  ├─ CONSTRAINT FAIL: current_sum (8) > target (7)
                │  │  │  │  │  │  │  │  └─ Return (pruning)
                │  │  │  │  │  │  │  └─ tmp.pop() → tmp = [2, 2, 2]
                │  │  │  │  │  │  ├─ i=1: Try candidate=3
                │  │  │  │  │  │  │  ├─ tmp.append(3) → tmp = [2, 2, 2, 3]
                │  │  │  │  │  │  │  ├─ Call 6: backtrack(1, [2, 2, 2, 3], 9)
                │  │  │  │  │  │  │  │  ├─ CONSTRAINT FAIL: current_sum (9) > target (7)
                │  │  │  │  │  │  │  │  └─ Return (pruning)
                │  │  │  │  │  │  │  └─ tmp.pop() → tmp = [2, 2, 2]
                │  │  │  │  │  │  ├─ i=2,3: Similar failures (6+6=12, 6+7=13 > 7)
                │  │  │  │  │  │  └─ Return to Call 4
                │  │  │  │  │  └─ tmp.pop() → tmp = [2, 2]
                │  │  │  │  ├─ i=1: Try candidate=3
                │  │  │  │  │  ├─ tmp.append(3) → tmp = [2, 2, 3]
                │  │  │  │  │  ├─ Call 7: backtrack(1, [2, 2, 3], 7) -- start=1, tmp=[2,2,3], current_sum=7
                │  │  │  │  │  │  ├─ GOAL! current_sum (7) == target (7)
                │  │  │  │  │  │  └─ ans.append([2, 2, 3]) → ans = [[2, 2, 3]]
                │  │  │  │  │  └─ tmp.pop() → tmp = [2, 2]
                │  │  │  │  ├─ i=2: Try candidate=6
                │  │  │  │  │  ├─ tmp.append(6) → tmp = [2, 2, 6]
                │  │  │  │  │  ├─ Call 8: backtrack(2, [2, 2, 6], 10)
                │  │  │  │  │  │  ├─ CONSTRAINT FAIL: current_sum (10) > target (7)
                │  │  │  │  │  │  └─ Return (pruning)
                │  │  │  │  │  └─ tmp.pop() → tmp = [2, 2]
                │  │  │  │  ├─ i=3: Try candidate=7
                │  │  │  │  │  ├─ tmp.append(7) → tmp = [2, 2, 7]
                │  │  │  │  │  ├─ Call 9: backtrack(3, [2, 2, 7], 11)
                │  │  │  │  │  │  ├─ CONSTRAINT FAIL: current_sum (11) > target (7)
                │  │  │  │  │  │  └─ Return (pruning)
                │  │  │  │  │  └─ tmp.pop() → tmp = [2, 2]
                │  │  │  │  └─ Return to Call 3
                │  │  │  └─ tmp.pop() → tmp = [2]
                │  │  ├─ i=1: Try candidate=3
                │  │  │  ├─ tmp.append(3) → tmp = [2, 3]
                │  │  │  ├─ Call 10: backtrack(1, [2, 3], 5) -- start=1, tmp=[2,3], current_sum=5
                │  │  │  │  ├─ current_sum (5) != target (7), continue
                │  │  │  │  ├─ current_sum (5) <= target (7), continue
                │  │  │  │  ├─ Loop: for i in range(1, 4) -- try candidates at indices 1,2,3
                │  │  │  │  ├─ i=1: Try candidate=3
                │  │  │  │  │  ├─ tmp.append(3) → tmp = [2, 3, 3]
                │  │  │  │  │  ├─ Call 11: backtrack(1, [2, 3, 3], 8)
                │  │  │  │  │  │  ├─ CONSTRAINT FAIL: current_sum (8) > target (7)
                │  │  │  │  │  │  └─ Return (pruning)
                │  │  │  │  │  └─ tmp.pop() → tmp = [2, 3]
                │  │  │  │  ├─ i=2,3: Similar failures (5+6=11, 5+7=12 > 7)
                │  │  │  │  └─ Return to Call 10
                │  │  │  └─ tmp.pop() → tmp = [2]
                │  │  ├─ i=2: Try candidate=6
                │  │  │  ├─ tmp.append(6) → tmp = [2, 6]
                │  │  │  ├─ Call 12: backtrack(2, [2, 6], 8)
                │  │  │  │  ├─ CONSTRAINT FAIL: current_sum (8) > target (7)
                │  │  │  │  └─ Return (pruning)
                │  │  │  └─ tmp.pop() → tmp = [2]
                │  │  ├─ i=3: Try candidate=7
                │  │  │  ├─ tmp.append(7) → tmp = [2, 7]
                │  │  │  ├─ Call 13: backtrack(3, [2, 7], 9)
                │  │  │  │  ├─ CONSTRAINT FAIL: current_sum (9) > target (7)
                │  │  │  │  └─ Return (pruning)
                │  │  │  └─ tmp.pop() → tmp = [2]
                │  │  └─ Return to Call 2
                │  └─ tmp.pop() → tmp = []
                ├─ i=1: Try candidate=3
                │  ├─ tmp.append(3) → tmp = [3]
                │  ├─ Call 14: backtrack(1, [3], 3) -- start=1, tmp=[3], current_sum=3
                │  │  ├─ current_sum (3) != target (7), continue
                │  │  ├─ current_sum (3) <= target (7), continue
                │  │  ├─ Loop: for i in range(1, 4) -- try candidates at indices 1,2,3
                │  │  ├─ i=1: Try candidate=3
                │  │  │  ├─ tmp.append(3) → tmp = [3, 3]
                │  │  │  ├─ Call 15: backtrack(1, [3, 3], 6)
                │  │  │  │  ├─ current_sum (6) != target (7), continue
                │  │  │  │  ├─ current_sum (6) <= target (7), continue
                │  │  │  │  ├─ Loop: for i in range(1, 4) -- try candidates at indices 1,2,3
                │  │  │  │  ├─ i=1: Try candidate=3 → sum=9 > 7 (fail)
                │  │  │  │  ├─ i=2: Try candidate=6 → sum=12 > 7 (fail)
                │  │  │  │  ├─ i=3: Try candidate=7 → sum=13 > 7 (fail)
                │  │  │  │  └─ Return to Call 15
                │  │  │  └─ tmp.pop() → tmp = [3]
                │  │  ├─ i=2: Try candidate=6 → sum=9 > 7 (fail)
                │  │  ├─ i=3: Try candidate=7 → sum=10 > 7 (fail)
                │  │  └─ Return to Call 14
                │  └─ tmp.pop() → tmp = []
                ├─ i=2: Try candidate=6
                │  ├─ tmp.append(6) → tmp = [6]
                │  ├─ Call 16: backtrack(2, [6], 6) -- start=2, tmp=[6], current_sum=6
                │  │  ├─ current_sum (6) != target (7), continue
                │  │  ├─ current_sum (6) <= target (7), continue
                │  │  ├─ Loop: for i in range(2, 4) -- try candidates at indices 2,3
                │  │  ├─ i=2: Try candidate=6 → sum=12 > 7 (fail)
                │  │  ├─ i=3: Try candidate=7 → sum=13 > 7 (fail)
                │  │  └─ Return to Call 16
                │  └─ tmp.pop() → tmp = []
                ├─ i=3: Try candidate=7
                │  ├─ tmp.append(7) → tmp = [7]
                │  ├─ Call 17: backtrack(3, [7], 7) -- start=3, tmp=[7], current_sum=7
                │  │  ├─ GOAL! current_sum (7) == target (7)
                │  │  └─ ans.append([7]) → ans = [[2, 2, 3], [7]]
                │  └─ tmp.pop() → tmp = []
                └─ Return final result: [[2, 2, 3], [7]]
        '''

        def backtrack(start, temp, current_sum):
            #GOAL: found target sum

            #CONSTRAINT: current sum < target, prune otherwise

            #CHOICE: try each candidate from start index to end

            pass


    @staticmethod
    def subset_sum_exists(nums, target):
        '''
            Check if any subset sums to a target

            Args:
                nums: list of integers
                target: target sum

            Returns:
                true if subset exists, false otherwise

            Q) What is the time and space complexity?
                a) Time complexity is O(2^n), checking all subsets
                a) Space complexity is O(n)
            Q) What is the backtracking framework?
                a) CHOICE: include the current number or skip it
                a) CONSTRAINT: current sum <= target (if all positive)
                a) GOAL: current sum == target


            Advanced Walkthrough)

                Numbers: [3, 4, 5]
                Target: 9
                Expected Result: True (subset [4, 5] sums to 9)
                Key Insight: For each number, we have exactly 2 choices: include it or skip it.

                Complete Execution Trace:
                Call 1: backtrack(0, 0) -- index=0, current_sum=0, processing nums[0]=3
                ├─ current_sum (0) != target (9), continue
                ├─ index (0) != len(nums) (3), continue
                ├─ current_sum (0) <= target (9), continue (no pruning)
                ├─ CHOICE 1: Include nums[0] = 3
                │  ├─ Call 2: backtrack(1, 3) -- index=1, current_sum=3, processing nums[1]=4
                │  │  ├─ current_sum (3) != target (9), continue
                │  │  ├─ index (1) != len(nums) (3), continue
                │  │  ├─ current_sum (3) <= target (9), continue (no pruning)
                │  │  ├─ CHOICE 1: Include nums[1] = 4
                │  │  │  ├─ Call 3: backtrack(2, 7) -- index=2, current_sum=7, processing nums[2]=5
                │  │  │  │  ├─ current_sum (7) != target (9), continue
                │  │  │  │  ├─ index (2) != len(nums) (3), continue
                │  │  │  │  ├─ current_sum (7) <= target (9), continue (no pruning)
                │  │  │  │  ├─ CHOICE 1: Include nums[2] = 5
                │  │  │  │  │  ├─ Call 4: backtrack(3, 12) -- index=3, current_sum=12, processed all
                │  │  │  │  │  │  ├─ current_sum (12) != target (9), continue
                │  │  │  │  │  │  ├─ BASE CASE: index (3) == len(nums) (3), processed all numbers
                │  │  │  │  │  │  └─ Return False (didn't find target)
                │  │  │  │  │  └─ Return False to Call 3
                │  │  │  │  ├─ CHOICE 2: Skip nums[2] = 5
                │  │  │  │  │  ├─ Call 5: backtrack(3, 7) -- index=3, current_sum=7, processed all
                │  │  │  │  │  │  ├─ current_sum (7) != target (9), continue
                │  │  │  │  │  │  ├─ BASE CASE: index (3) == len(nums) (3), processed all numbers
                │  │  │  │  │  │  └─ Return False (didn't find target)
                │  │  │  │  │  └─ Return False to Call 3
                │  │  │  │  └─ Return False to Call 2 (both choices failed)
                │  │  │  └─ Return False to Call 2
                │  │  ├─ CHOICE 2: Skip nums[1] = 4
                │  │  │  ├─ Call 6: backtrack(2, 3) -- index=2, current_sum=3, processing nums[2]=5
                │  │  │  │  ├─ current_sum (3) != target (9), continue
                │  │  │  │  ├─ index (2) != len(nums) (3), continue
                │  │  │  │  ├─ current_sum (3) <= target (9), continue (no pruning)
                │  │  │  │  ├─ CHOICE 1: Include nums[2] = 5
                │  │  │  │  │  ├─ Call 7: backtrack(3, 8) -- index=3, current_sum=8, processed all
                │  │  │  │  │  │  ├─ current_sum (8) != target (9), continue
                │  │  │  │  │  │  ├─ BASE CASE: index (3) == len(nums) (3), processed all numbers
                │  │  │  │  │  │  └─ Return False (didn't find target)
                │  │  │  │  │  └─ Return False to Call 6
                │  │  │  │  ├─ CHOICE 2: Skip nums[2] = 5
                │  │  │  │  │  ├─ Call 8: backtrack(3, 3) -- index=3, current_sum=3, processed all
                │  │  │  │  │  │  ├─ current_sum (3) != target (9), continue
                │  │  │  │  │  │  ├─ BASE CASE: index (3) == len(nums) (3), processed all numbers
                │  │  │  │  │  │  └─ Return False (didn't find target)
                │  │  │  │  │  └─ Return False to Call 6
                │  │  │  │  └─ Return False to Call 2 (both choices failed)
                │  │  │  └─ Return False to Call 2
                │  │  └─ Return False to Call 1 (both choices failed)
                │  └─ Return False to Call 1
                ├─ CHOICE 2: Skip nums[0] = 3
                │  ├─ Call 9: backtrack(1, 0) -- index=1, current_sum=0, processing nums[1]=4
                │  │  ├─ current_sum (0) != target (9), continue
                │  │  ├─ index (1) != len(nums) (3), continue
                │  │  ├─ current_sum (0) <= target (9), continue (no pruning)
                │  │  ├─ CHOICE 1: Include nums[1] = 4
                │  │  │  ├─ Call 10: backtrack(2, 4) -- index=2, current_sum=4, processing nums[2]=5
                │  │  │  │  ├─ current_sum (4) != target (9), continue
                │  │  │  │  ├─ index (2) != len(nums) (3), continue
                │  │  │  │  ├─ current_sum (4) <= target (9), continue (no pruning)
                │  │  │  │  ├─ CHOICE 1: Include nums[2] = 5
                │  │  │  │  │  ├─ Call 11: backtrack(3, 9) -- index=3, current_sum=9, processed all
                │  │  │  │  │  │  ├─ GOAL! current_sum (9) == target (9)
                │  │  │  │  │  │  └─ Return True ✅ (found target!)
                │  │  │  │  │  └─ Return True to Call 10 ✅
                │  │  │  │  └─ Return True to Call 9 ✅ (found solution, no need to try CHOICE 2)
                │  │  │  └─ Return True to Call 9 ✅
                │  │  └─ Return True to Call 1 ✅ (found solution, no need to try CHOICE 2)
                │  └─ Return True to Call 1 ✅
                └─ SUCCESS! Return True (subset [4, 5] sums to target 9)
                Final Result: True - Subset [4, 5] (skipped 3, included 4, included 5) sums to 9.

        '''

        def backtrack(index, current_sum):
            #GOAL: found target sum

            # base case: processed all numbers and didn't get sum

            # CONSTRAINT: if we are over target sum and all nums left are positive, prune

            #CHOICE 1: add number

            #CHOICE 2: don't add number
            pass


    @staticmethod
    def restore_ip_addresses(s):
        '''
            Restore valid ip addresses from a string of digits
                - A IP Address is valid if:
                    - exactly 4 parts separated by dots
                    - each part is 0 - 255
                    - no leading 0s except 0 itself

            Args:
                s: string containing only digits

            Returns:
                list of all valid ip addresses

            Q) What is the time and space complexity?
                a) Time complexity is O(1), there are always only 3^4 combinations to check at most
                a) Space complexity is O(1)
            Q) What is the backtracking framework?
                a) CHOICE: Split each string at different positions (1-3 positions per part)
                a) CONSTRAINT: Each part valid (0-255, no leading zeros)
                a) GOAL: created exactly 4 parts using entire string

            Advanced Walkthrough)

                String: "25525511135"
                Expected Result: ["255.255.11.135", "255.255.111.35"]
                IP Address Rules:

                Exactly 4 parts separated by dots
                Each part is 0-255
                No leading zeros (except "0" itself)

                Slice Explanations:

                s[0:1] = "2" (1 character starting at index 0)
                s[0:2] = "25" (2 characters starting at index 0)
                s[0:3] = "255" (3 characters starting at index 0)
                '.'.join(['255', '255', '11', '135']) = "255.255.11.135"


                Complete Execution Trace:
                Call 1: backtrack(0, []) -- start=0, tmp=[], processing from index 0
                ├─ len(tmp) (0) != 4, continue
                ├─ Loop: for length in range(1, 4) -- try lengths 1, 2, 3
                ├─ length=1: Try part s[0:1] = "2"
                │  ├─ start + length = 0 + 1 = 1 <= len(s) (11) ✓
                │  ├─ part = s[0:0+1] = s[0:1] = "2"  # slice [0:1] gets character at index 0
                │  ├─ is_valid_part("2"): len=1≤3 ✓, no leading zero ✓, 2≤255 ✓
                │  ├─ tmp.append("2") → tmp = ["2"]
                │  ├─ Call 2: backtrack(1, ["2"]) -- start=1, tmp=["2"], processing from index 1
                │  │  ├─ len(tmp) (1) != 4, continue
                │  │  ├─ Loop: for length in range(1, 4) -- try lengths 1, 2, 3
                │  │  ├─ length=1: Try part s[1:2] = "5"
                │  │  │  ├─ start + length = 1 + 1 = 2 <= len(s) (11) ✓
                │  │  │  ├─ part = s[1:1+1] = s[1:2] = "5"  # slice [1:2] gets character at index 1
                │  │  │  ├─ is_valid_part("5"): valid ✓
                │  │  │  ├─ tmp.append("5") → tmp = ["2", "5"]
                │  │  │  ├─ Call 3: backtrack(2, ["2", "5"]) -- start=2, tmp=["2","5"]
                │  │  │  │  ├─ len(tmp) (2) != 4, continue
                │  │  │  │  ├─ Loop: for length in range(1, 4) -- try lengths 1, 2, 3
                │  │  │  │  ├─ length=1: Try part s[2:3] = "5"
                │  │  │  │  │  ├─ start + length = 2 + 1 = 3 <= len(s) (11) ✓
                │  │  │  │  │  ├─ part = s[2:2+1] = s[2:3] = "5"  # slice [2:3] gets character at index 2
                │  │  │  │  │  ├─ is_valid_part("5"): valid ✓
                │  │  │  │  │  ├─ tmp.append("5") → tmp = ["2", "5", "5"]
                │  │  │  │  │  ├─ Call 4: backtrack(3, ["2", "5", "5"]) -- start=3, tmp=["2","5","5"]
                │  │  │  │  │  │  ├─ len(tmp) (3) != 4, continue
                │  │  │  │  │  │  ├─ Loop: for length in range(1, 4) -- try lengths 1, 2, 3
                │  │  │  │  │  │  ├─ length=1: Try part s[3:4] = "2"
                │  │  │  │  │  │  │  ├─ part = s[3:4] = "2", valid ✓
                │  │  │  │  │  │  │  ├─ tmp.append("2") → tmp = ["2", "5", "5", "2"]
                │  │  │  │  │  │  │  ├─ Call 5: backtrack(4, ["2", "5", "5", "2"])
                │  │  │  │  │  │  │  │  ├─ GOAL CHECK: len(tmp) (4) == 4 ✓
                │  │  │  │  │  │  │  │  ├─ CONSTRAINT CHECK: start (4) != len(s) (11) ✗
                │  │  │  │  │  │  │  │  └─ Return (not using entire string)
                │  │  │  │  │  │  │  └─ tmp.pop() → tmp = ["2", "5", "5"]
                │  │  │  │  │  │  ├─ length=2: Try part s[3:5] = "25", similar failure...
                │  │  │  │  │  │  ├─ length=3: Try part s[3:6] = "255", similar failure...
                │  │  │  │  │  │  └─ Return to Call 4
                │  │  │  │  │  └─ tmp.pop() → tmp = ["2", "5"]
                │  │  │  │  ├─ length=2,3: Similar explorations...
                │  │  │  │  └─ Return to Call 3
                │  │  │  └─ tmp.pop() → tmp = ["2"]
                │  │  ├─ length=2,3: More explorations...
                │  │  └─ Return to Call 2
                │  └─ tmp.pop() → tmp = []
                ├─ length=2: Try part s[0:2] = "25"
                │  ├─ start + length = 0 + 2 = 2 <= len(s) (11) ✓
                │  ├─ part = s[0:0+2] = s[0:2] = "25"  # slice [0:2] gets characters at indices 0,1
                │  ├─ is_valid_part("25"): len=2≤3 ✓, no leading zero ✓, 25≤255 ✓
                │  ├─ tmp.append("25") → tmp = ["25"]
                │  ├─ Call 6: backtrack(2, ["25"]) -- start=2, tmp=["25"]
                │  │  ├─ ... (similar exploration pattern)
                │  │  └─ Eventually finds some valid IPs...
                │  └─ tmp.pop() → tmp = []
                ├─ length=3: Try part s[0:3] = "255"
                │  ├─ start + length = 0 + 3 = 3 <= len(s) (11) ✓
                │  ├─ part = s[0:0+3] = s[0:3] = "255"  # slice [0:3] gets characters at indices 0,1,2
                │  ├─ is_valid_part("255"): len=3≤3 ✓, no leading zero ✓, 255≤255 ✓
                │  ├─ tmp.append("255") → tmp = ["255"]
                │  ├─ Call 7: backtrack(3, ["255"]) -- start=3, tmp=["255"], processing from index 3
                │  │  ├─ len(tmp) (1) != 4, continue
                │  │  ├─ Loop: for length in range(1, 4) -- try lengths 1, 2, 3
                │  │  ├─ length=1: Try part s[3:4] = "2"
                │  │  │  ├─ ... (will eventually fail - not enough parts)
                │  │  ├─ length=2: Try part s[3:5] = "25"
                │  │  │  ├─ ... (will eventually fail - not enough parts)
                │  │  ├─ length=3: Try part s[3:6] = "255"
                │  │  │  ├─ start + length = 3 + 3 = 6 <= len(s) (11) ✓
                │  │  │  ├─ part = s[3:3+3] = s[3:6] = "255"  # slice [3:6] gets chars at indices 3,4,5
                │  │  │  ├─ is_valid_part("255"): valid ✓
                │  │  │  ├─ tmp.append("255") → tmp = ["255", "255"]
                │  │  │  ├─ Call 8: backtrack(6, ["255", "255"]) -- start=6, tmp=["255","255"]
                │  │  │  │  ├─ len(tmp) (2) != 4, continue
                │  │  │  │  ├─ Loop: for length in range(1, 4) -- try lengths 1, 2, 3
                │  │  │  │  ├─ length=1: Try part s[6:7] = "1"
                │  │  │  │  │  ├─ part = s[6:7] = "1", valid ✓
                │  │  │  │  │  ├─ tmp.append("1") → tmp = ["255", "255", "1"]
                │  │  │  │  │  ├─ Call 9: backtrack(7, ["255", "255", "1"])
                │  │  │  │  │  │  ├─ len(tmp) (3) != 4, continue
                │  │  │  │  │  │  ├─ Try remaining string "1135" as final part
                │  │  │  │  │  │  ├─ part = s[7:11] = "1135", len=4 > 3 ✗ (invalid)
                │  │  │  │  │  │  └─ Return to Call 9
                │  │  │  │  │  └─ tmp.pop() → tmp = ["255", "255"]
                │  │  │  │  ├─ length=2: Try part s[6:8] = "11"
                │  │  │  │  │  ├─ part = s[6:8] = "11", valid ✓
                │  │  │  │  │  ├─ tmp.append("11") → tmp = ["255", "255", "11"]
                │  │  │  │  │  ├─ Call 10: backtrack(8, ["255", "255", "11"])
                │  │  │  │  │  │  ├─ len(tmp) (3) != 4, continue
                │  │  │  │  │  │  ├─ Try remaining string "135" as final part
                │  │  │  │  │  │  ├─ length=3: part = s[8:11] = "135"
                │  │  │  │  │  │  ├─ is_valid_part("135"): len=3≤3 ✓, no leading zero ✓, 135≤255 ✓
                │  │  │  │  │  │  ├─ tmp.append("135") → tmp = ["255", "255", "11", "135"]
                │  │  │  │  │  │  ├─ Call 11: backtrack(11, ["255", "255", "11", "135"])
                │  │  │  │  │  │  │  ├─ GOAL CHECK: len(tmp) (4) == 4 ✓
                │  │  │  │  │  │  │  ├─ CONSTRAINT CHECK: start (11) == len(s) (11) ✓
                │  │  │  │  │  │  │  └─ ans.append("255.255.11.135") → ans = ["255.255.11.135"]
                │  │  │  │  │  │  └─ tmp.pop() → tmp = ["255", "255", "11"]
                │  │  │  │  │  └─ tmp.pop() → tmp = ["255", "255"]
                │  │  │  │  ├─ length=3: Try part s[6:9] = "111"
                │  │  │  │  │  ├─ part = s[6:9] = "111", valid ✓
                │  │  │  │  │  ├─ tmp.append("111") → tmp = ["255", "255", "111"]
                │  │  │  │  │  ├─ Call 12: backtrack(9, ["255", "255", "111"])
                │  │  │  │  │  │  ├─ len(tmp) (3) != 4, continue
                │  │  │  │  │  │  ├─ Try remaining string "35" as final part
                │  │  │  │  │  │  ├─ length=2: part = s[9:11] = "35"
                │  │  │  │  │  │  ├─ is_valid_part("35"): valid ✓
                │  │  │  │  │  │  ├─ tmp.append("35") → tmp = ["255", "255", "111", "35"]
                │  │  │  │  │  │  ├─ Call 13: backtrack(11, ["255", "255", "111", "35"])
                │  │  │  │  │  │  │  ├─ GOAL CHECK: len(tmp) (4) == 4 ✓
                │  │  │  │  │  │  │  ├─ CONSTRAINT CHECK: start (11) == len(s) (11) ✓
                │  │  │  │  │  │  │  └─ ans.append("255.255.111.35") → ans = ["255.255.11.135", "255.255.111.35"]
                │  │  │  │  │  │  └─ tmp.pop() → tmp = ["255", "255", "111"]
                │  │  │  │  │  └─ tmp.pop() → tmp = ["255", "255"]
                │  │  │  │  └─ Return to Call 8
                │  │  │  └─ tmp.pop() → tmp = ["255"]
                │  │  └─ Return to Call 7
                │  └─ tmp.pop() → tmp = []
                └─ Return final result: ["255.255.11.135", "255.255.111.35"]

        '''

        def is_valid_part(part):
            # check if the part is a vlid IP component

            # no leading 0s

            # must be 0 <= x <= 255
            pass

        def backtrack(start, temp):
            #GOAL: created 4 parts using entire string

            #CHOICE: Try different part lengths (1-3) digits


                #CONSTRAINT: part must be valid

            pass


    @staticmethod
    def find_all_paths(maze, start, end):
        '''
            Find all paths from start to end in a maze

            Args:
                maze: 2D grid where 0 = empty and 1 = wall
                start: row,col starting pos
                end: row,col ending position

            Returns:
                a list of paths (each path is a list of coordinates)

            Q) What is the time and space complexity?
                a) Time complexity is O(4^(m*n)) -> worst case explore all cells
                a) Space complexity is O(m*n) -> recursion depth and path storage
            Q) What is the backtracking framework?
                a) CHOICE: move in 4 directions
                a) CONSTRAINT: stay in bounds, avoid the walls, don't revisit cells
                a) GOAL: reach end position

            Advanced Walkthrough)

                Maze:
                [[0, 0, 1],
                 [0, 0, 0],
                 [0, 1, 0]]
                Visual Representation:
                0 0 1    (0,0) (0,1) WALL
                0 0 0 →  (1,0) (1,1) (1,2)
                0 1 0    (2,0) WALL  (2,2)
                Start: (0, 0) End: (2, 2)
                Expected Paths:

                [(0,0), (0,1), (1,1), (1,2), (2,2)]
                [(0,0), (1,0), (2,0), (2,1), (2,2)] (if (2,1) exists)

                Wait - there's an error in expected result! Let me check the maze:

                Position (2,1) is a WALL (value = 1), so path 2 should be: [(0,0), (1,0), (1,1), (1,2), (2,2)]


                Complete Execution Trace:
                Call 1: backtrack(0, 0, [], {}) -- row=0, col=0, path=[], visited={}
                ├─ (row, col) = (0, 0) != end (2, 2), continue
                ├─ Check constraints:
                │  ├─ row=0, col=0 in bounds ✓
                │  ├─ maze[0][0] = 0 (not wall) ✓
                │  ├─ (0,0) not in visited ✓
                │  └─ All constraints passed
                ├─ Make choice: visited.add((0,0)) → visited = {(0,0)}
                ├─ Make choice: path.append((0,0)) → path = [(0,0)]
                ├─ Try all 4 directions from (0,0):
                ├─ Direction 1: (0,1) - right to (0,1)
                │  ├─ Call 2: backtrack(0, 1, [(0,0)], {(0,0)}) -- moving to (0,1)
                │  │  ├─ (0, 1) != end (2, 2), continue
                │  │  ├─ Check constraints:
                │  │  │  ├─ row=0, col=1 in bounds ✓
                │  │  │  ├─ maze[0][1] = 0 (not wall) ✓
                │  │  │  ├─ (0,1) not in visited ✓
                │  │  │  └─ All constraints passed
                │  │  ├─ Make choice: visited.add((0,1)) → visited = {(0,0), (0,1)}
                │  │  ├─ Make choice: path.append((0,1)) → path = [(0,0), (0,1)]
                │  │  ├─ Try all 4 directions from (0,1):
                │  │  ├─ Direction 1: (0,2) - right to (0,2)
                │  │  │  ├─ Call 3: backtrack(0, 2, [(0,0), (0,1)], {(0,0), (0,1)})
                │  │  │  │  ├─ (0, 2) != end (2, 2), continue
                │  │  │  │  ├─ Check constraints:
                │  │  │  │  │  ├─ row=0, col=2 in bounds ✓
                │  │  │  │  │  ├─ maze[0][2] = 1 (WALL) ✗
                │  │  │  │  │  └─ CONSTRAINT FAIL: hit wall
                │  │  │  │  └─ Return (cannot proceed)
                │  │  │  └─ Return to Call 2
                │  │  ├─ Direction 2: (0,0) - left to (0,0)
                │  │  │  ├─ Call 4: backtrack(0, 0, [(0,0), (0,1)], {(0,0), (0,1)})
                │  │  │  │  ├─ (0, 0) != end (2, 2), continue
                │  │  │  │  ├─ Check constraints:
                │  │  │  │  │  ├─ row=0, col=0 in bounds ✓
                │  │  │  │  │  ├─ maze[0][0] = 0 (not wall) ✓
                │  │  │  │  │  ├─ (0,0) already in visited ✗
                │  │  │  │  │  └─ CONSTRAINT FAIL: already visited
                │  │  │  │  └─ Return (cannot revisit)
                │  │  │  └─ Return to Call 2
                │  │  ├─ Direction 3: (1,1) - down to (1,1)
                │  │  │  ├─ Call 5: backtrack(1, 1, [(0,0), (0,1)], {(0,0), (0,1)})
                │  │  │  │  ├─ (1, 1) != end (2, 2), continue
                │  │  │  │  ├─ Check constraints:
                │  │  │  │  │  ├─ row=1, col=1 in bounds ✓
                │  │  │  │  │  ├─ maze[1][1] = 0 (not wall) ✓
                │  │  │  │  │  ├─ (1,1) not in visited ✓
                │  │  │  │  │  └─ All constraints passed
                │  │  │  │  ├─ Make choice: visited.add((1,1)) → visited = {(0,0), (0,1), (1,1)}
                │  │  │  │  ├─ Make choice: path.append((1,1)) → path = [(0,0), (0,1), (1,1)]
                │  │  │  │  ├─ Try all 4 directions from (1,1):
                │  │  │  │  ├─ Direction 1: (1,2) - right to (1,2)
                │  │  │  │  │  ├─ Call 6: backtrack(1, 2, [(0,0), (0,1), (1,1)], {(0,0), (0,1), (1,1)})
                │  │  │  │  │  │  ├─ (1, 2) != end (2, 2), continue
                │  │  │  │  │  │  ├─ Check constraints: all pass ✓
                │  │  │  │  │  │  ├─ Make choice: visited.add((1,2)) → visited = {(0,0), (0,1), (1,1), (1,2)}
                │  │  │  │  │  │  ├─ Make choice: path.append((1,2)) → path = [(0,0), (0,1), (1,1), (1,2)]
                │  │  │  │  │  │  ├─ Try all 4 directions from (1,2):
                │  │  │  │  │  │  ├─ Direction 3: (2,2) - down to (2,2)
                │  │  │  │  │  │  │  ├─ Call 7: backtrack(2, 2, [(0,0), (0,1), (1,1), (1,2)], {...})
                │  │  │  │  │  │  │  │  ├─ GOAL! (2, 2) == end (2, 2)
                │  │  │  │  │  │  │  │  └─ ans.append([(0,0), (0,1), (1,1), (1,2), (2,2)])
                │  │  │  │  │  │  │  │      → ans = [[(0,0), (0,1), (1,1), (1,2), (2,2)]]
                │  │  │  │  │  │  │  └─ Return to Call 6
                │  │  │  │  │  │  ├─ (other directions from (1,2) explored...)
                │  │  │  │  │  │  ├─ Undo choice: visited.remove((1,2)) → visited = {(0,0), (0,1), (1,1)}
                │  │  │  │  │  │  └─ Undo choice: path.pop() → path = [(0,0), (0,1), (1,1)]
                │  │  │  │  │  └─ Return to Call 5
                │  │  │  │  ├─ (other directions from (1,1) explored...)
                │  │  │  │  ├─ Undo choice: visited.remove((1,1)) → visited = {(0,0), (0,1)}
                │  │  │  │  └─ Undo choice: path.pop() → path = [(0,0), (0,1)]
                │  │  │  └─ Return to Call 2
                │  │  ├─ Direction 4: (-1,1) - up to (-1,1)
                │  │  │  ├─ Call 8: backtrack(-1, 1, [(0,0), (0,1)], {(0,0), (0,1)})
                │  │  │  │  ├─ (-1, 1) != end (2, 2), continue
                │  │  │  │  ├─ Check constraints:
                │  │  │  │  │  ├─ row=-1 < 0 (out of bounds) ✗
                │  │  │  │  │  └─ CONSTRAINT FAIL: out of bounds
                │  │  │  │  └─ Return (cannot go out of bounds)
                │  │  │  └─ Return to Call 2
                │  │  ├─ Undo choice: visited.remove((0,1)) → visited = {(0,0)}
                │  │  └─ Undo choice: path.pop() → path = [(0,0)]
                │  └─ Return to Call 1
                ├─ Direction 2: (0,-1) - left to (0,-1)
                │  ├─ Call 9: backtrack(0, -1, [(0,0)], {(0,0)})
                │  │  ├─ Check constraints:
                │  │  │  ├─ col=-1 < 0 (out of bounds) ✗
                │  │  │  └─ CONSTRAINT FAIL: out of bounds
                │  │  └─ Return (cannot go out of bounds)
                │  └─ Return to Call 1
                ├─ Direction 3: (1,0) - down to (1,0)
                │  ├─ Call 10: backtrack(1, 0, [(0,0)], {(0,0)})
                │  │  ├─ (1, 0) != end (2, 2), continue
                │  │  ├─ Check constraints: all pass ✓
                │  │  ├─ Make choice: visited.add((1,0)) → visited = {(0,0), (1,0)}
                │  │  ├─ Make choice: path.append((1,0)) → path = [(0,0), (1,0)]
                │  │  ├─ Try all 4 directions from (1,0):
                │  │  ├─ Direction 1: (1,1) - right to (1,1)
                │  │  │  ├─ Call 11: backtrack(1, 1, [(0,0), (1,0)], {(0,0), (1,0)})
                │  │  │  │  ├─ Similar exploration eventually leads to another path to (2,2)...
                │  │  │  │  └─ This would find path: [(0,0), (1,0), (1,1), (1,2), (2,2)]
                │  │  │  └─ Return to Call 10
                │  │  ├─ Direction 3: (2,0) - down to (2,0)
                │  │  │  ├─ Call 12: backtrack(2, 0, [(0,0), (1,0)], {(0,0), (1,0)})
                │  │  │  │  ├─ Constraints pass, but from (2,0) can only go to (2,1) which is WALL
                │  │  │  │  └─ Dead end - no path to (2,2) from here
                │  │  │  └─ Return to Call 10
                │  │  ├─ Undo choice: visited.remove((1,0)) → visited = {(0,0)}
                │  │  └─ Undo choice: path.pop() → path = [(0,0)]
                │  └─ Return to Call 1
                ├─ Direction 4: (-1,0) - up to (-1,0)
                │  ├─ Out of bounds check fails immediately
                │  └─ Return to Call 1
                ├─ Undo choice: visited.remove((0,0)) → visited = {}
                └─ Undo choice: path.pop() → path = []

                Final result: ans = [[(0,0), (0,1), (1,1), (1,2), (2,2)], [(0,0), (1,0), (1,1), (1,2), (2,2)]]

        '''

        def backtrack(row, col, path, visited):
            #CONSTRAINT: check bounds, walls, and visited

            #CHOICES: mark as visited and add to path

            #GOAL: reached end position

            # try all 4 directions

            #undo choices

            pass


    @staticmethod
    def partition_equal_subset_sum(nums):
        '''
            Check if array can be partitioned into two equal sum sets NOTE------> THIS PROBLEM IS BETTER FOR DYNAMIC PROGRAMMING DUE TO TIME CONSTRAINTS, THIS IS JUST FOR PRACTICE

            Args:
                nums: array of positive integers

            Returns:
                true if can be partitioned, false otherwise

            Q) What is the time and space complexity?
                a) Time complexity is
                a) Space complexity is
            Q) What is backtracking framework?
                a) CHOICE:
                a) CONSTRAINT:
                a) GOAL:

            Advanced Walkthrough)

                Numbers: [1, 5, 11, 5]
                Total Sum: 1 + 5 + 11 + 5 = 22
                Target: 22 // 2 = 11 (each subset must sum to 11)
                Expected Result: True

                Subset 1: [1, 5, 5] → sum = 11
                Subset 2: [11] → sum = 11

                Key Insight: We only track one subset - if it sums to target, the remaining numbers automatically sum to target too.

                Complete Execution Trace:
                total_sum = 22, target = 11

                Call 1: backtrack(0, 0) -- index=0, current_sum=0, processing nums[0]=1
                ├─ current_sum (0) != target (11), continue
                ├─ index (0) != len(nums) (4), continue
                ├─ current_sum (0) <= target (11), continue (no pruning)
                ├─ CHOICE 1: Include nums[0] = 1 in first subset
                │  ├─ Call 2: backtrack(1, 1) -- index=1, current_sum=1, processing nums[1]=5
                │  │  ├─ current_sum (1) != target (11), continue
                │  │  ├─ index (1) != len(nums) (4), continue
                │  │  ├─ current_sum (1) <= target (11), continue (no pruning)
                │  │  ├─ CHOICE 1: Include nums[1] = 5 in first subset
                │  │  │  ├─ Call 3: backtrack(2, 6) -- index=2, current_sum=6, processing nums[2]=11
                │  │  │  │  ├─ current_sum (6) != target (11), continue
                │  │  │  │  ├─ index (2) != len(nums) (4), continue
                │  │  │  │  ├─ current_sum (6) <= target (11), continue (no pruning)
                │  │  │  │  ├─ CHOICE 1: Include nums[2] = 11 in first subset
                │  │  │  │  │  ├─ Call 4: backtrack(3, 17) -- index=3, current_sum=17, processing nums[3]=5
                │  │  │  │  │  │  ├─ current_sum (17) != target (11), continue
                │  │  │  │  │  │  ├─ index (3) != len(nums) (4), continue
                │  │  │  │  │  │  ├─ CONSTRAINT FAIL: current_sum (17) > target (11)
                │  │  │  │  │  │  └─ Return False (pruning - too big)
                │  │  │  │  │  └─ Return False to Call 3
                │  │  │  │  ├─ CHOICE 2: Skip nums[2] = 11 (goes to second subset)
                │  │  │  │  │  ├─ Call 5: backtrack(3, 6) -- index=3, current_sum=6, processing nums[3]=5
                │  │  │  │  │  │  ├─ current_sum (6) != target (11), continue
                │  │  │  │  │  │  ├─ index (3) != len(nums) (4), continue
                │  │  │  │  │  │  ├─ current_sum (6) <= target (11), continue (no pruning)
                │  │  │  │  │  │  ├─ CHOICE 1: Include nums[3] = 5 in first subset
                │  │  │  │  │  │  │  ├─ Call 6: backtrack(4, 11) -- index=4, current_sum=11, processed all
                │  │  │  │  │  │  │  │  ├─ GOAL! current_sum (11) == target (11)
                │  │  │  │  │  │  │  │  └─ Return True ✅ (found valid partition!)
                │  │  │  │  │  │  │  └─ Return True to Call 5 ✅
                │  │  │  │  │  │  └─ Return True to Call 3 ✅ (no need to try CHOICE 2)
                │  │  │  │  │  └─ Return True to Call 3 ✅
                │  │  │  │  └─ Return True to Call 2 ✅
                │  │  │  └─ Return True to Call 2 ✅
                │  │  └─ Return True to Call 1 ✅ (no need to try CHOICE 2)
                │  └─ Return True to Call 1 ✅
                └─ SUCCESS! Return True (can partition into equal subsets)

                Found partition:
                - First subset: [1, 5, 5] (sum = 11)
                - Second subset: [11] (sum = 11)
                Final Result: True - Array can be partitioned into two equal-sum subsets.


        '''


        # base case -> total sum can't be odd since each partition's target is total sum / 2


        # sort the nums so we can group duplicates together -> if we decide to skip one later, we can just skip all rather than re exploring

        def backtrack(index, current_sum):
            #GOAL: first partition == second partition

            # base case: processed all numbers without meeting constraints

            #CONSTRAINT: if the sum exceeds the target, we prune

            #CHOICE 1: include the current number in the first partition

            # skip all duplicates when we choose to exclude

            #CHOICE 2: do not include the current number in the first partition, so it implicitly goes to the second set


            pass


    @staticmethod
    def generate_unique_permutations(nums):
        '''
            Generate all unique permutations (handle duplicates in input)

            Args:
                nums: list of ints that may contain duplicates

            Returns:
                list of unique permutation

            Q) What is the time and space complexity?
            Q) What is the backtracking framework?
                a) CHOICE:
                a) CONSTRAINT:
                a) GOAL:
            Q) What is the key insight?
                a)

            Advanced Walkthrough)

                Numbers: [1, 1, 2]
                After Sorting: [1, 1, 2] (already sorted)
                Expected Result: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
                Key Challenge: Avoid duplicate permutations like having [1, 1, 2] appear multiple times due to the two identical 1s.
                Duplicate Handling Rule:

                If nums[i] == nums[i-1] and used[i-1] == False, skip nums[i]
                This ensures we always use duplicates in order: first occurrence before second occurrence


                Complete Execution Trace:
                nums = [1, 1, 2] (sorted)
                indices: 0  1  2

                Call 1: backtrack([], [F, F, F]) -- tmp=[], used=[F,F,F], building position 0
                ├─ len(tmp) (0) != len(nums) (3), continue
                ├─ Loop: for i in range(3) -- try indices 0, 1, 2
                ├─ i=0: Try nums[0] = 1 (first occurrence)
                │  ├─ used[0] = False ✓ (not used)
                │  ├─ Duplicate check: i=0, no previous element, skip check ✓
                │  ├─ Make choice: used[0] = True, tmp.append(1) → tmp=[1], used=[T,F,F]
                │  ├─ Call 2: backtrack([1], [T, F, F]) -- tmp=[1], used=[T,F,F], building position 1
                │  │  ├─ len(tmp) (1) != len(nums) (3), continue
                │  │  ├─ Loop: for i in range(3) -- try indices 0, 1, 2
                │  │  ├─ i=0: Try nums[0] = 1
                │  │  │  ├─ used[0] = True ✗ (already used)
                │  │  │  └─ Continue (skip used element)
                │  │  ├─ i=1: Try nums[1] = 1 (second occurrence)
                │  │  │  ├─ used[1] = False ✓ (not used)
                │  │  │  ├─ Duplicate check: nums[1]=1 == nums[0]=1 ✓ and used[0]=True ✓
                │  │  │  │  └─ Since used[0]=True, we CAN use nums[1] (first 1 already chosen)
                │  │  │  ├─ Make choice: used[1] = True, tmp.append(1) → tmp=[1,1], used=[T,T,F]
                │  │  │  ├─ Call 3: backtrack([1, 1], [T, T, F]) -- tmp=[1,1], used=[T,T,F], building position 2
                │  │  │  │  ├─ len(tmp) (2) != len(nums) (3), continue
                │  │  │  │  ├─ Loop: for i in range(3) -- try indices 0, 1, 2
                │  │  │  │  ├─ i=0: used[0] = True ✗ (skip)
                │  │  │  │  ├─ i=1: used[1] = True ✗ (skip)
                │  │  │  │  ├─ i=2: Try nums[2] = 2
                │  │  │  │  │  ├─ used[2] = False ✓ (not used)
                │  │  │  │  │  ├─ Duplicate check: nums[2]=2 != nums[1]=1 ✓ (no duplicate issue)
                │  │  │  │  │  ├─ Make choice: used[2] = True, tmp.append(2) → tmp=[1,1,2], used=[T,T,T]
                │  │  │  │  │  ├─ Call 4: backtrack([1, 1, 2], [T, T, T]) -- complete permutation
                │  │  │  │  │  │  ├─ GOAL! len(tmp) (3) == len(nums) (3)
                │  │  │  │  │  │  └─ ans.append([1, 1, 2]) → ans = [[1, 1, 2]]
                │  │  │  │  │  ├─ Undo choice: used[2] = False, tmp.pop() → tmp=[1,1], used=[T,T,F]
                │  │  │  │  │  └─ Return to Call 3
                │  │  │  │  └─ Return to Call 2
                │  │  │  ├─ Undo choice: used[1] = False, tmp.pop() → tmp=[1], used=[T,F,F]
                │  │  │  └─ Return to Call 2
                │  │  ├─ i=2: Try nums[2] = 2
                │  │  │  ├─ used[2] = False ✓ (not used)
                │  │  │  ├─ Duplicate check: nums[2]=2 != nums[1]=1 ✓ (no duplicate issue)
                │  │  │  ├─ Make choice: used[2] = True, tmp.append(2) → tmp=[1,2], used=[T,F,T]
                │  │  │  ├─ Call 5: backtrack([1, 2], [T, F, T]) -- tmp=[1,2], used=[T,F,T], building position 2
                │  │  │  │  ├─ len(tmp) (2) != len(nums) (3), continue
                │  │  │  │  ├─ Loop: for i in range(3) -- try indices 0, 1, 2
                │  │  │  │  ├─ i=0: used[0] = True ✗ (skip)
                │  │  │  │  ├─ i=1: Try nums[1] = 1
                │  │  │  │  │  ├─ used[1] = False ✓ (not used)
                │  │  │  │  │  ├─ Duplicate check: nums[1]=1 == nums[0]=1 ✓ and used[0]=True ✓
                │  │  │  │  │  │  └─ Since used[0]=True, we CAN use nums[1]
                │  │  │  │  │  ├─ Make choice: used[1] = True, tmp.append(1) → tmp=[1,2,1], used=[T,T,T]
                │  │  │  │  │  ├─ Call 6: backtrack([1, 2, 1], [T, T, T]) -- complete permutation
                │  │  │  │  │  │  ├─ GOAL! len(tmp) (3) == len(nums) (3)
                │  │  │  │  │  │  └─ ans.append([1, 2, 1]) → ans = [[1, 1, 2], [1, 2, 1]]
                │  │  │  │  │  ├─ Undo choice: used[1] = False, tmp.pop() → tmp=[1,2], used=[T,F,T]
                │  │  │  │  │  └─ Return to Call 5
                │  │  │  │  ├─ i=2: used[2] = True ✗ (skip)
                │  │  │  │  └─ Return to Call 2
                │  │  │  ├─ Undo choice: used[2] = False, tmp.pop() → tmp=[1], used=[T,F,F]
                │  │  │  └─ Return to Call 2
                │  │  └─ Return to Call 1
                │  ├─ Undo choice: used[0] = False, tmp.pop() → tmp=[], used=[F,F,F]
                │  └─ Return to Call 1
                ├─ i=1: Try nums[1] = 1 (second occurrence)
                │  ├─ used[1] = False ✓ (not used)
                │  ├─ Duplicate check: nums[1]=1 == nums[0]=1 ✓ and used[0]=False ✗
                │  │  └─ SKIP! Cannot use second 1 before first 1 (prevents duplicates)
                │  └─ Continue to next iteration
                ├─ i=2: Try nums[2] = 2
                │  ├─ used[2] = False ✓ (not used)
                │  ├─ Duplicate check: nums[2]=2 != nums[1]=1 ✓ (no duplicate issue)
                │  ├─ Make choice: used[2] = True, tmp.append(2) → tmp=[2], used=[F,F,T]
                │  ├─ Call 7: backtrack([2], [F, F, T]) -- tmp=[2], used=[F,F,T], building position 1
                │  │  ├─ len(tmp) (1) != len(nums) (3), continue
                │  │  ├─ Loop: for i in range(3) -- try indices 0, 1, 2
                │  │  ├─ i=0: Try nums[0] = 1 (first occurrence)
                │  │  │  ├─ used[0] = False ✓ (not used)
                │  │  │  ├─ Duplicate check: i=0, no previous element ✓
                │  │  │  ├─ Make choice: used[0] = True, tmp.append(1) → tmp=[2,1], used=[T,F,T]
                │  │  │  ├─ Call 8: backtrack([2, 1], [T, F, T]) -- tmp=[2,1], used=[T,F,T], building position 2
                │  │  │  │  ├─ len(tmp) (2) != len(nums) (3), continue
                │  │  │  │  ├─ Loop: for i in range(3) -- try indices 0, 1, 2
                │  │  │  │  ├─ i=0: used[0] = True ✗ (skip)
                │  │  │  │  ├─ i=1: Try nums[1] = 1 (second occurrence)
                │  │  │  │  │  ├─ used[1] = False ✓ (not used)
                │  │  │  │  │  ├─ Duplicate check: nums[1]=1 == nums[0]=1 ✓ and used[0]=True ✓
                │  │  │  │  │  │  └─ Since used[0]=True, we CAN use nums[1]
                │  │  │  │  │  ├─ Make choice: used[1] = True, tmp.append(1) → tmp=[2,1,1], used=[T,T,T]
                │  │  │  │  │  ├─ Call 9: backtrack([2, 1, 1], [T, T, T]) -- complete permutation
                │  │  │  │  │  │  ├─ GOAL! len(tmp) (3) == len(nums) (3)
                │  │  │  │  │  │  └─ ans.append([2, 1, 1]) → ans = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
                │  │  │  │  │  ├─ Undo choice: used[1] = False, tmp.pop() → tmp=[2,1], used=[T,F,T]
                │  │  │  │  │  └─ Return to Call 8
                │  │  │  │  ├─ i=2: used[2] = True ✗ (skip)
                │  │  │  │  └─ Return to Call 7
                │  │  │  ├─ Undo choice: used[0] = False, tmp.pop() → tmp=[2], used=[F,F,T]
                │  │  │  └─ Return to Call 7
                │  │  ├─ i=1: Try nums[1] = 1 (second occurrence)
                │  │  │  ├─ used[1] = False ✓ (not used)
                │  │  │  ├─ Duplicate check: nums[1]=1 == nums[0]=1 ✓ and used[0]=False ✗
                │  │  │  │  └─ SKIP! Cannot use second 1 before first 1
                │  │  │  └─ Continue to next iteration
                │  │  ├─ i=2: used[2] = True ✗ (skip)
                │  │  └─ Return to Call 1
                │  ├─ Undo choice: used[2] = False, tmp.pop() → tmp=[], used=[F,F,F]
                │  └─ Return to Call 1
                └─ Return final result: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        '''

        # group the duplicates together

        def backtrack(temp, used):
            #GOAL: found complete permutation

            #try each unused number at current position
                # CONSTRAINT 1: skip used numbers

                # CONSTRAINT 2: skip duplicates at same level -> if the current number equals the previous and the previous is not used, we skip it

                # CHOICE: mark as used and add to permutation

                # undo the choice

            pass


    @staticmethod
    def print_backtracking_concepts():
        """
        Print key backtracking concepts for learning
        """
        concepts = """
        🎯 BACKTRACKING CORE CONCEPTS:

        1. TEMPLATE STRUCTURE:
           def backtrack(path, choices):
               if is_goal(path):
                   result.append(path.copy())
                   return

               for choice in choices:
                   if is_valid(choice, path):
                       path.append(choice)      # Make choice
                       backtrack(path, next_choices)  # Recurse
                       path.pop()               # Undo choice (backtrack)

        2. THREE KEY QUESTIONS:
           🔹 CHOICE: What decisions can we make at each step?
           🔹 CONSTRAINT: What rules limit our choices?
           🔹 GOAL: When do we have a complete solution?

        3. COMMON PATTERNS:
           🔸 Generate All: permutations, combinations, subsets
           🔸 Find Path: maze, word search, N-Queens
           🔸 Partition: subset sum, palindrome partitioning
           🔸 Constraint Satisfaction: Sudoku, graph coloring

        4. OPTIMIZATION TECHNIQUES:
           ⚡ Pruning: Stop early when constraints violated
           ⚡ Sorting: Process elements in optimal order
           ⚡ Memoization: Cache results of subproblems
           ⚡ Early termination: Stop when first solution found

        5. TIME COMPLEXITY PATTERNS:
           📊 Permutations: O(n!)
           📊 Combinations: O(2^n)
           📊 Subsets: O(2^n)
           📊 Path problems: O(4^n) for grid traversal
        """
        print(concepts)

# Example usage and testing helper
if __name__ == "__main__":
    # Print concepts for learning
    BacktrackingOperations.print_backtracking_concepts()

