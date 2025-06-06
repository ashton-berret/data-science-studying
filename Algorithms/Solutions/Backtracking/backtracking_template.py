class BacktrackingOperations:
    @staticmethod
    def backtrack_template(problem_type="permutations", input_data=None):
        """
        Universal backtracking template that you can practice with different problems

        Args:
            problem_type: str - "permutations", "combinations", "subsets", "nqueens", "parentheses"
            input_data: depends on problem type
                - permutations: list of numbers [1,2,3]
                - combinations: tuple (n, k) like (4, 2)
                - subsets: list of numbers [1,2,3]
                - nqueens: integer n (board size)
                - parentheses: integer n (number of pairs)

        Returns:
            List of all solutions for the given problem

        Example usage:
            BacktrackingOperations.backtrack_template("permutations", [1,2,3])
            BacktrackingOperations.backtrack_template("combinations", (4, 2))
            BacktrackingOperations.backtrack_template("subsets", [1,2])
            BacktrackingOperations.backtrack_template("nqueens", 4)
            BacktrackingOperations.backtrack_template("parentheses", 3)
        """

        if input_data is None:
            return "Error: input_data is required"
        # Initialize result list (closure variable accessible to nested function)
        result = []

        def is_complete_solution(current_state):
            """Check if we have a complete solution (GOAL)"""
            if problem_type == "permutations":
                return len(current_state) == len(input_data)
            elif problem_type == "combinations":
                n, k = input_data
                return len(current_state) == k
            elif problem_type == "subsets":
                return len(current_state) == len(input_data)  # processed all elements
            elif problem_type == "nqueens":
                return len(current_state) == input_data  # placed all queens
            elif problem_type == "parentheses":
                return len(current_state) == 2 * input_data  # used all pairs
            return False

        def is_valid_choice(choice, current_state):
            """Check if choice is valid given current state (CONSTRAINT)"""
            if problem_type == "permutations":
                # Can't reuse numbers already in permutation
                return choice not in current_state
            elif problem_type == "combinations":
                # Must pick numbers in ascending order (avoid duplicates)
                return len(current_state) == 0 or choice > current_state[-1]
            elif problem_type == "subsets":
                # Always valid (we control choices in get_next_choices)
                return True
            elif problem_type == "nqueens":
                row, col = choice
                # Check if queen position conflicts with existing queens
                for existing_row, existing_col in current_state:
                    if (existing_col == col or  # same column
                        existing_row - existing_col == row - col or  # same diagonal
                        existing_row + existing_col == row + col):   # same anti-diagonal
                        return False
                return True
            elif problem_type == "parentheses":
                char = choice
                open_count = current_state.count('(')
                close_count = current_state.count(')')
                if char == '(':
                    return open_count < input_data
                else:  # char == ')'
                    return close_count < open_count
            return True

        def make_choice(choice, current_state):
            """Update state to reflect our choice"""
            if problem_type in ["permutations", "combinations", "nqueens"]:
                current_state.append(choice)
            elif problem_type == "subsets":
                # For subsets, choice is (element, include_flag)
                element, include = choice
                if include:
                    current_state.append(element)
            elif problem_type == "parentheses":
                current_state.append(choice)

        def undo_choice(choice, current_state):
            """Restore state by undoing our choice (BACKTRACK)"""
            if problem_type in ["permutations", "combinations", "nqueens", "parentheses"]:
                current_state.pop()
            elif problem_type == "subsets":
                element, include = choice
                if include and current_state and current_state[-1] == element:
                    current_state.pop()

        def get_next_choices(choice, remaining_choices):
            """Get available choices for next recursive call"""
            if problem_type == "permutations":
                # Remove the chosen element from remaining choices
                return [x for x in remaining_choices if x != choice]
            elif problem_type == "combinations":
                n, k = input_data
                # Only consider numbers greater than current choice
                return [x for x in remaining_choices if x > choice]
            elif problem_type == "subsets":
                # Move to next element (remove first element from remaining)
                return remaining_choices[1:] if remaining_choices else []
            elif problem_type == "nqueens":
                # Move to next row
                row, col = choice
                next_row = row + 1
                return [(next_row, c) for c in range(input_data)] if next_row < input_data else []
            elif problem_type == "parentheses":
                # Always have choice between '(' and ')'
                return ['(', ')']
            return []

        def get_initial_choices():
            """Get the initial set of choices"""
            if problem_type == "permutations":
                return input_data[:]  # copy of input list
            elif problem_type == "combinations":
                n, k = input_data
                return list(range(1, n + 1))
            elif problem_type == "subsets":
                # Choices are (element, include_flag) pairs
                return [(input_data[0], True), (input_data[0], False)] if input_data else []
            elif problem_type == "nqueens":
                # Start with first row, try each column
                return [(0, col) for col in range(input_data)]
            elif problem_type == "parentheses":
                return ['(', ')']
            return []

        def backtrack_recursive(current_state, remaining_choices):
            """The actual backtracking function"""
            # GOAL: Check if we have a complete solution
            if is_complete_solution(current_state):
                # Store a copy of the solution
                if problem_type == "subsets":
                    # For subsets, we store solution at each step
                    result.append(current_state[:])
                    return
                elif problem_type == "nqueens":
                    # Convert queen positions to board representation
                    board = [['.' for _ in range(input_data)] for _ in range(input_data)]
                    for row, col in current_state:
                        board[row][col] = 'Q'
                    result.append([''.join(row) for row in board])
                    return
                else:
                    result.append(current_state[:])
                return

            # For subsets, we also store partial solutions
            if problem_type == "subsets":
                result.append(current_state[:])
                if not remaining_choices:  # no more elements to process
                    return

            # CHOICE: Try each available choice
            for choice in remaining_choices:
                # CONSTRAINT: Check if choice is valid
                if is_valid_choice(choice, current_state):
                    # Make choice (update state)
                    make_choice(choice, current_state)

                    # Recurse with updated state
                    next_choices = get_next_choices(choice, remaining_choices)
                    backtrack_recursive(current_state, next_choices)

                    # Undo choice (restore state)
                    undo_choice(choice, current_state)

        # Validate input
        if input_data is None:
            return "Error: input_data is required"

        # Start the backtracking process
        initial_state = []
        initial_choices = get_initial_choices()

        backtrack_recursive(initial_state, initial_choices)

        return result

    @staticmethod
    def demo_backtrack_template():
        """
        Demonstrate the backtrack_template with different problem types
        """
        print("🎯 BACKTRACKING TEMPLATE DEMO")
        print("=" * 50)

        # Demo 1: Permutations
        print("\n1. PERMUTATIONS of [1,2,3]:")
        result = BacktrackingOperations.backtrack_template("permutations", [1,2,3])
        print(f"   Result: {result}")
        print(f"   Count: {len(result)} (expected: 6)")

        # Demo 2: Combinations
        print("\n2. COMBINATIONS C(4,2):")
        result = BacktrackingOperations.backtrack_template("combinations", (4, 2))
        print(f"   Result: {result}")
        print(f"   Count: {len(result)} (expected: 6)")

        # Demo 3: Subsets
        print("\n3. SUBSETS of [1,2]:")
        result = BacktrackingOperations.backtrack_template("subsets", [1,2])
        print(f"   Result: {result}")
        print(f"   Count: {len(result)} (expected: 4)")

        # Demo 4: N-Queens
        print("\n4. N-QUEENS (n=4):")
        result = BacktrackingOperations.backtrack_template("nqueens", 4)
        print(f"   Solutions found: {len(result)} (expected: 2)")
        if result:
            print("   First solution:")
            for row in result[0]:
                print(f"     {row}")

        # Demo 5: Parentheses
        print("\n5. PARENTHESES (n=3):")
        result = BacktrackingOperations.backtrack_template("parentheses", 3)
        print(f"   Result: {result}")
        print(f"   Count: {len(result)} (expected: 5)")

        print("\n✅ Template demo complete!")
        print("\n💡 PRACTICE TIP:")
        print("   Try modifying the helper functions to understand how each part works!")
        print("   Example: BacktrackingOperations.backtrack_template('permutations', [1,2,3])")

# Example usage for testing
if __name__ == "__main__":
    # This would only run if the file is executed directly
    bt = BacktrackingOperations()
    bt.demo_backtrack_template()
