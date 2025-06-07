from typing import List, Optional
from collections import defaultdict


class DP1Operations:
    '''
        Comprehenensive 1-D Dynamic Programming algorithms for coding interviews

        DYNAMIC PROGRAMMING FUNDAMENTALS
        ================================

            Dynamic programming solves problems by breaking them into overlapping subproblems and storing solutions to avoid recalculation (can think of almost as a lookup table with previously solved indices/values).
            DP works when a problem has:
                1. Optimal substructure: optimal solution contains optimal solutions to sub problems
                2. Overlapping subproblems: same subproblems are solved multiple times

        3 MAIN APPROACHES TO DP:
        ========================
            1. RECURSIVE (Top Down)
                - Start with the original problem and break it down
                - Use recursion to solve smaller problems
                - Often leads to exponential times due to repeated calculations
                - Good for understanding problem structure

                Example) fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
                    - Problem) fibonacci(5) recalculates fibonacci(3) multiple times
                    - Time) O(2^n) -> exponential
                    - Space) O(n) -> recursion call stack

            2. MEMOIZATION (Top Down)
                - Same recursive structure as approach 1, but adding a cache (memo) to store already computed results
                - Check cache before computing, store result after computing
                - Eliminates redundant calculations while keeping recursive structure

                Benefits)
                    - Easy to convert from recursive solution
                    - Only computes subproblems that are actually needed
                    - Natural for problems where not all subproblems are required

                Drawbacks)
                    - Still uses recursion so there is call stack overhead
                    - Can hit recursion limits for large inputs
                    - Cache management can be tricky

                Time and Space)
                    - O(n) time -> each subproblem computed once
                    - O(n) space -> memo cache + O(n) recursion stack = O(n)

            3. TABULATION (Bottom Up)
                - Start with smallest subproblems and build up
                - Uses iteration instead of recursion
                - Fill a table (typically an array) from base cases to final answer
                - No recursion overhead, more space efficient options

                Benefits)
                    - No recursion stack which avoids stack overflow
                    - Often more space efficient (can optimize space usage)
                    - Clearer time/space complexity
                    - Generally faster due to no function call overhead

                Drawbacks)
                    - Must compute all subproblems, even if they aren't needed for the final answer
                    - Sometimes less intuitive
                    - Need to determine the correct order of computation

                Time and Space)
                    - O(n) time -> compute each subproblem once
                    - O(n) space - dp table (can often optimize to O(1))

        WHEN TO USE EACH APPROACH
        =========================
            1. Use RECURSIVE when:
                - understanding the problem structure
                - prototyping/learning phase
                - problem has complex constraints that make memoization more natural

            2. Use MEMOIZATION when:
                - converting from recursive solution
                - not all subproblems are needed
                - recursion depth is manageable
                - complex state representation

            3. Use TABULATION when:
                - final production solution
                - large inputs
                - need space optimization
                - interview coding
                - all subproblems will be computed anyways


        COMMON 1-DP PATTERNS:
        =====================
            1. FIBONACCI STYLE: dp[i] depends on previous few values
                - examples) Fibonacci, climbing stairs, house robber
                - Pattern)
                        dp[i] = f(dp[i-1], dp[i-2], etc...)

            2. MAX/MIN SO FAR: dp[i] represents best solution up to index i
                - examples) Maximum subarray, best time to buy/sell stock
                - Pattern)
                        dp[i] = max/min(dp[i-1] + something, reset_value)

            3. DECISION PROBLEMS: dp[i] represents if something is possible up to index i
                - examples) word break, partition equal sum subset
                - Pattern)
                        dp[i] = dp[j] and some_condition for various j<i

            4. COUNTING PROBLEMS: dp[i] represents the number of ways to reach state i
                - examples) Coin change, decode ways
                - Pattern)
                        dp[i] = sum(dp[j]) for valid transitions from j to i

            5. OPTIMIZATION PROBLEMS: dp[i] represents optimal value ending at position i
                - examples) longest increasing subsequence, jump game
                - Pattern)
                        dp[i] = best(db[j] + cost) for valid j < i


        DP FRAMEWORK (This Standard Approach)
        =====================================
            For every DP problem, ask these three questions:

                1. STATE: What does dp[i] represent?
                    - define what each entry in the dp table means
                    - be specific about what 'optimal solution for subproblem i' means
                2. TRANSITION: How do we build dp[i] from previous states?
                    - what smaller subproblems does dp[i] depend on?
                    - write the recurrence relation: dp[i] = f(dp[j]) for j < i
                3. BASE CASE: What are our starting conditions?
                    - what are the smallest subproblems we can solve directly?
                    - usually, dp[0], dp[1], or specific boundary conditions


    '''

    @staticmethod
    def fibonacci(n):
        '''
            Calculate the nth fibonacci number using dynamic programming

                The fibonacci sequence is defined as:
                    F(0) = 0
                    F(1) = 1
                    F(n) = F(n-1) + F(n-2) for n >= 2

                    Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
                    Each number is the sum of the two preceeding numbers

            Args:
                n: non-negative integer representing the position in the fibonacci sequence

            Returns:
                nth fibonacci number

            Q) What is the DP Framework for this problem?
                a) STATE: dp[i] = the ith fib number
                a) TRANSITION: dp[i] = dp[i-1] + dp[i-2]
                a) BASE CASE: dp[0] = 0, dp[1] = 1

            Q) What are the space and time complexities?
                a) Recursion -> O(2^n) time, O(n) space --> exponential due to overlapping subproblems
                a) Memoization -> O(n) time, O(n) space --> cache eliminates redundant calcualtions
                a) Tabulated --> O(n) time, O(n) space
                a) Space optimized --> O(n) time, O(n) space --> only store previous two values

            Q) Why is this a DP problem?
                a) Optimal substructure: F(n) optimally depends on F(n-1) and F(n-2)
                a) Overlapping subproblems

            Q) Why do we use tabulation over memoization?
                a) We need all fib numbers anyways
                a) No recursion stack overhead for large numbers
                a) Easy to space optimize to O(1)


            Advanced Walkthrough)

                EXECUTION TRACE: fibonacci(5)
                ==============================

                Initial Setup:
                n = 5
                dp = [0, 0, 0, 0, 0, 0]  # Create array of size n+1

                Base Cases:
                dp[0] = 0 → dp = [0, 0, 0, 0, 0, 0]  # F(0) = 0 by definition
                dp[1] = 1 → dp = [0, 1, 0, 0, 0, 0]  # F(1) = 1 by definition

                Bottom-Up Building (i from 2 to n):

                i=2: Calculate dp[2]
                ├─ dp[2] = dp[1] + dp[0] = 1 + 0 = 1
                ├─ Meaning: F(2) = F(1) + F(0) = 1 + 0 = 1
                └─ dp = [0, 1, 1, 0, 0, 0]

                i=3: Calculate dp[3]
                ├─ dp[3] = dp[2] + dp[1] = 1 + 1 = 2
                ├─ Meaning: F(3) = F(2) + F(1) = 1 + 1 = 2
                └─ dp = [0, 1, 1, 2, 0, 0]

                i=4: Calculate dp[4]
                ├─ dp[4] = dp[3] + dp[2] = 2 + 1 = 3
                ├─ Meaning: F(4) = F(3) + F(2) = 2 + 1 = 3
                └─ dp = [0, 1, 1, 2, 3, 0]

                i=5: Calculate dp[5]
                ├─ dp[5] = dp[4] + dp[3] = 3 + 2 = 5
                ├─ Meaning: F(5) = F(4) + F(3) = 3 + 2 = 5
                └─ dp = [0, 1, 1, 2, 3, 5]

                Final Result: return dp[5] = 5

                VERIFICATION:
                Expected Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21...
                ✓ Our result dp = [0, 1, 1, 2, 3, 5] matches perfectly!

        '''

        # handle base cases directly
        if n <= 1:
            return n

        # create DP table to store fib numbers
        dp = [0] * (n + 1)

        # enter first two values manually
        dp[0] = 0
        dp[1] = 1

        # fill the table using transition relation: f(n) = f(n-1) + f(n-2)
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]




    @staticmethod
    def climbing_stairs(n):
        '''
            Calculate the number of distinct ways to climb n stairs (can step 1 or 2 steps at a time)

            Args:
                n: positive integer representing the number of stairs

            Returns:
                number of distinct ways to reach the top


            Q) What is the DP Framework?
                1. STATE: dp[i] = the number of ways to reach step i
                2. TRANSITION: dp[i] = dp[i] = dp[i-1] + dp[i-2] --> arrive from 1 step back or two steps back
                3. BASE CASE: dp[0] = 1, (1 way to stay at ground), dp[1] = 1 (one way to reach step 1)

            Q) What are the time and space complexities?
                _ TABULATED: O(n) time, O(n) space
                - SPACE OPTIMIZED: O(n) time, O(1) space -> only need two previous values


            Advanced Walkthrough)

                EXECUTION TRACE: climbing_stairs(4)
                ===================================

                Initial Setup:
                n = 4
                dp = [0, 0, 0, 0, 0]  # Create array of size n+1

                Base Cases:
                dp[0] = 1 → dp = [1, 0, 0, 0, 0]  # 1 way to stay at ground (do nothing)
                dp[1] = 1 → dp = [1, 1, 0, 0, 0]  # 1 way to reach step 1 (take 1 step)

                Bottom-Up Building (i from 2 to n):

                i=2: Calculate dp[2] (ways to reach step 2)
                ├─ Can arrive from step 1 (take 1 step) OR step 0 (take 2 steps)
                ├─ dp[2] = dp[1] + dp[0] = 1 + 1 = 2
                ├─ Ways: [1,1] or [2]
                └─ dp = [1, 1, 2, 0, 0]

                i=3: Calculate dp[3] (ways to reach step 3)
                ├─ Can arrive from step 2 (take 1 step) OR step 1 (take 2 steps)
                ├─ dp[3] = dp[2] + dp[1] = 2 + 1 = 3
                ├─ Ways: [1,1,1] or [1,2] or [2,1]
                └─ dp = [1, 1, 2, 3, 0]

                i=4: Calculate dp[4] (ways to reach step 4)
                ├─ Can arrive from step 3 (take 1 step) OR step 2 (take 2 steps)
                ├─ dp[4] = dp[3] + dp[2] = 3 + 2 = 5
                ├─ Ways: [1,1,1,1] or [1,1,2] or [1,2,1] or [2,1,1] or [2,2]
                └─ dp = [1, 1, 2, 3, 5]

                Final Result: return dp[4] = 5

                VERIFICATION:
                Manual enumeration of all paths:
                1. [1,1,1,1] - take 1 step four times
                2. [1,1,2] - 1+1+2 steps
                3. [1,2,1] - 1+2+1 steps
                4. [2,1,1] - 2+1+1 steps
                5. [2,2] - take 2 steps twice
                ✓ Total = 5 ways, matches our result!

        '''

        # base case
        if n <= 1:
            return 1

        # create the dp table
        dp = [0] * (n+1)

        # handle first two entries
        dp[0] = 1 # one way to stay at ground --> do nothing
        dp[1] = 1 # one way to get to first step


        for i in range(2, n+1):
            dp[n] = dp[i-1] + dp[i-2] # arrive from one step back or two steps back

        return dp[n]




    @staticmethod
    def house_robber(nums):
        '''
            Find the maximum money that can be robbed without robbing adjacent houses

            Args:
                nums: list of integers representing the amount of money in each house

            Returns:
                maximum amount of money that can be robbed

            Q) What is the DP Framework?
                a) STATE: dp[i] = the maximum amount of money that can be robbed from houses 0 to i
                a) TRANSITION: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
                    - either skip house i (take dp[i-1]) or rob house i and take dp[i-2] + nums[i]
                a) BASE CASE: dp[0] = nums[0], dp[1] = max(nums[0], nums[1])

            Q) What are the time and space complexities?
                - TABULATED: O(n) time, O(n) space - our solution
                - SPACE-OPTIMIZED: O(n) time, O(1) space - only need previous two values

            Q) Why is this a DP problem?
                - OPTIMAL SUBSTRUCTURE: Optimal solution for houses 0..i depends on optimal solutions for smaller ranges
                - OVERLAPPING SUBPROBLEMS: Recursive solution recalculates same subproblems
                - DECISION PATTERN: At each house, decide whether to rob it or not

            Q) Why do we use tabulation here?
                - Linear dependency pattern (each state depends on previous two)
                - All subproblems needed for final answer
                - Easy to space-optimize

            EXECUTION TRACE: house_robber([2,7,9,3,1])
            =============================================

            Initial Setup:
            nums = [2, 7, 9, 3, 1]
            n = 5
            dp = [0, 0, 0, 0, 0]  # Create array of size n

            Base Cases:
            dp[0] = nums[0] = 2 → dp = [2, 0, 0, 0, 0]  # Can only rob house 0
            if n > 1: dp[1] = max(nums[0], nums[1]) = max(2, 7) = 7 → dp = [2, 7, 0, 0, 0]

            Bottom-Up Building (i from 2 to n-1):

            i=2: Decide about house 2 (value=9)
            ├─ Option 1: Skip house 2 → keep dp[1] = 7
            ├─ Option 2: Rob house 2 → dp[0] + nums[2] = 2 + 9 = 11
            ├─ dp[2] = max(7, 11) = 11 (rob houses 0 and 2)
            ├─ Optimal so far: rob houses [0, 2] for total 11
            └─ dp = [2, 7, 11, 0, 0]

            i=3: Decide about house 3 (value=3)
            ├─ Option 1: Skip house 3 → keep dp[2] = 11
            ├─ Option 2: Rob house 3 → dp[1] + nums[3] = 7 + 3 = 10
            ├─ dp[3] = max(11, 10) = 11 (skip house 3, keep previous optimal)
            ├─ Optimal so far: rob houses [0, 2] for total 11
            └─ dp = [2, 7, 11, 11, 0]

            i=4: Decide about house 4 (value=1)
            ├─ Option 1: Skip house 4 → keep dp[3] = 11
            ├─ Option 2: Rob house 4 → dp[2] + nums[4] = 11 + 1 = 12
            ├─ dp[4] = max(11, 12) = 12 (rob house 4 in addition to optimal from dp[2])
            ├─ Optimal final: rob houses [0, 2, 4] for total 12
            └─ dp = [2, 7, 11, 11, 12]

            Final Result: return dp[4] = 12

            VERIFICATION:
            All possible non-adjacent combinations:
            - Rob [0]: 2
            - Rob [1]: 7
            - Rob [2]: 9
            - Rob [3]: 3
            - Rob [4]: 1
            - Rob [0,2]: 2+9=11
            - Rob [0,3]: 2+3=5
            - Rob [0,4]: 2+1=3
            - Rob [1,3]: 7+3=10
            - Rob [1,4]: 7+1=8
            - Rob [2,4]: 9+1=10
            - Rob [0,2,4]: 2+9+1=12 ← Maximum!
            - Rob [1,3]: 7+3=10
            ✓ Maximum is indeed 12!

        '''

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # table to store amount of money robbed up to each house
        n = len(nums)
        dp =  [0] * n

        # handle first two base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # fill the table, for each house decide whether to rob it or not
        for i in range(2, n):

            # option 1 is skip current house, keep the previous max
            skip_current = dp[i-1]

            # option 2 is rob current, add the max from 2 houses ago
            rob_current = dp[i-2] + nums[i]

            dp[i] = max(skip_current, rob_current)

        return dp[n-1]




    @staticmethod
    def coin_change(coins, amount):
        '''
            Find the minimum number of coins needed to make the given amount.

            Args:
                coins: list of integers representing coin denominations (positive integers)
                amount: target amount to make (non-negative integer)

            Returns:
                minimum amount of coins needed or -1 if impossible


            Q) What is the DP Framework for this problem?
                1. STATE: dp[i] = minimum coins needed to make amount i
                2. TRANSITION: dp[i] = min(dp[i-coin] + 1) for all valid coins
                   - For each coin, if we can make (i-coin), then we can make i with 1 more coin
                        |> the dp table essentially acts as a lookup table for future coins
                        |> if we are trying to solve for amount 6 and we currently have a coin 3 (so count is inherently 1), we just need to solve for the minimum number of coins needed for the 'complement' (amount - current_coin.val) = 3
                        |> we've already done this since dp table goes iteratively for each amount 0 to amount

                3. BASE CASE: dp[0] = 0 (need 0 coins to make amount 0)

            Q) What are the time and space complexities?
                - TABULATED: O(amount * len(coins)) time, O(amount) space - our solution
                - We try each coin for each amount from 1 to target amount

            Q) Why is this a DP problem?
                - OPTIMAL SUBSTRUCTURE: Optimal solution for amount i uses optimal solution for amount (i-coin)
                - OVERLAPPING SUBPROBLEMS: Many amounts are recalculated in recursive approach
                - UNBOUNDED KNAPSACK pattern: Can use same coin multiple times

            Q) Why do we use tabulation here?
                - Need to build up from smaller amounts to larger amounts
                - All intermediate amounts are needed
                - Easier to handle "impossible" cases with bottom-up approach

            EXECUTION TRACE: coin_change([1,3,4], 6)
            =========================================

            Initial Setup:
            coins = [1, 3, 4]
            amount = 6
            dp = [inf, inf, inf, inf, inf, inf, inf]  # dp[0] to dp[6], inf means impossible

            Base Case:
            dp[0] = 0 → dp = [0, inf, inf, inf, inf, inf, inf]  # 0 coins needed for amount 0

            Bottom-Up Building (i from 1 to amount):

            i=1: Find min coins for amount 1
            ├─ Try coin 1: dp[1-1] + 1 = dp[0] + 1 = 0 + 1 = 1
            ├─ Try coin 3: 1-3 = -2 < 0, skip
            ├─ Try coin 4: 1-4 = -3 < 0, skip
            ├─ dp[1] = min(inf, 1) = 1
            └─ dp = [0, 1, inf, inf, inf, inf, inf]

            i=2: Find min coins for amount 2
            ├─ Try coin 1: dp[2-1] + 1 = dp[1] + 1 = 1 + 1 = 2
            ├─ Try coin 3: 2-3 = -1 < 0, skip
            ├─ Try coin 4: 2-4 = -2 < 0, skip
            ├─ dp[2] = min(inf, 2) = 2
            └─ dp = [0, 1, 2, inf, inf, inf, inf]

            i=3: Find min coins for amount 3
            ├─ Try coin 1: dp[3-1] + 1 = dp[2] + 1 = 2 + 1 = 3
            ├─ Try coin 3: dp[3-3] + 1 = dp[0] + 1 = 0 + 1 = 1
            ├─ Try coin 4: 3-4 = -1 < 0, skip
            ├─ dp[3] = min(inf, 3, 1) = 1
            └─ dp = [0, 1, 2, 1, inf, inf, inf]

            i=4: Find min coins for amount 4
            ├─ Try coin 1: dp[4-1] + 1 = dp[3] + 1 = 1 + 1 = 2
            ├─ Try coin 3: dp[4-3] + 1 = dp[1] + 1 = 1 + 1 = 2
            ├─ Try coin 4: dp[4-4] + 1 = dp[0] + 1 = 0 + 1 = 1
            ├─ dp[4] = min(inf, 2, 2, 1) = 1
            └─ dp = [0, 1, 2, 1, 1, inf, inf]

            i=5: Find min coins for amount 5
            ├─ Try coin 1: dp[5-1] + 1 = dp[4] + 1 = 1 + 1 = 2
            ├─ Try coin 3: dp[5-3] + 1 = dp[2] + 1 = 2 + 1 = 3
            ├─ Try coin 4: dp[5-4] + 1 = dp[1] + 1 = 1 + 1 = 2
            ├─ dp[5] = min(inf, 2, 3, 2) = 2
            └─ dp = [0, 1, 2, 1, 1, 2, inf]

            i=6: Find min coins for amount 6
            ├─ Try coin 1: dp[6-1] + 1 = dp[5] + 1 = 2 + 1 = 3
            ├─ Try coin 3: dp[6-3] + 1 = dp[3] + 1 = 1 + 1 = 2
            ├─ Try coin 4: dp[6-4] + 1 = dp[2] + 1 = 2 + 1 = 3
            ├─ dp[6] = min(inf, 3, 2, 3) = 2
            └─ dp = [0, 1, 2, 1, 1, 2, 2]

            Final Result: return dp[6] = 2

            VERIFICATION:
            Optimal solution: use coins [3, 3] → total 2 coins for amount 6
            Other options: [1,1,4] → 3 coins, [1,1,1,3] → 4 coins, etc.
            ✓ Minimum is indeed 2 coins!
        '''


        if amount == 0:
            return 0
        if amount < 0 or not coins:
            return -1

        # create the dp table with pos inf values since we are finding minimums. has to be amount + 1 length long since must store the amount (and table is 0 indexed)
        dp = [float('inf')] * (amount + 1)

        # base case --> no coins needed to make 0
        dp[0] = 0

        # fill the table. for each amount, try every coin in coins
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i: # can only use the coin if it doesn't exceed the current amount we are trying to fill
                    # option -> use this coin + the optimal solution for the complement coin value
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        # return result, -1 if impossible, dp[amount] otherwise
        return dp[amount] if dp[amount] else -1



    @staticmethod
    def longest_increasing_subsequence(nums):
        '''
            Find the length of the longest strictly increasing subsequence. A subsequence is derived by deleting some or no elements without changing the order of remaining elements

            Args:
                nums: a ist of integers

            Returns:
                length of the longest increasing subsequence

            NOTE: LIS will stand for longest-increasing-subsequence


            Q) What is the DP Framework?
                a) STATE: dp[i] = length of LIS up to that point in nums (ending at index i)
                a) TRANSITION: dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]
                a) BASE CASE: dp[1] = i for all i (each element forms LIS of length 1 by itself)

            Q) What is the time and space complexity?
                a) TABULATED: O(n^2) time, O(n) space -> check all previous elements
                a) OPTIMIZED: O(n log n) time, O(n) space -> using binary search with patience sorting

            Q) Why is this a DP problem?
                - OPTIMAL SUBSTRUCTURE: LIS ending at i uses LIS ending at some j < i
                - OVERLAPPING SUBPROBLEMS: Same LIS lengths are recalculated
                - OPTIMIZATION PATTERN: Find optimal solution ending at each position

            Q) Why do we use tabulation here?
                - Need to consider all previous positions for each current position
                - All subproblems contribute to finding global maximum
                - Bottom-up naturally builds from smaller to larger indices

            EXECUTION TRACE: longest_increasing_subsequence([10,9,2,5,3,7,101,18])
            ====================================================================

            Initial Setup:
            nums = [10, 9, 2, 5, 3, 7, 101, 18]
            n = 8
            dp = [1, 1, 1, 1, 1, 1, 1, 1]  # Each element can form LIS of length 1

            Bottom-Up Building (i from 1 to n-1):

            i=1: Consider nums[1]=9, find best LIS ending at index 1
            ├─ Check j=0: nums[0]=10 > nums[1]=9, can't extend
            ├─ dp[1] remains 1 (just element 9 by itself)
            └─ dp = [1, 1, 1, 1, 1, 1, 1, 1]

            i=2: Consider nums[2]=2, find best LIS ending at index 2
            ├─ Check j=0: nums[0]=10 > nums[2]=2, can't extend
            ├─ Check j=1: nums[1]=9 > nums[2]=2, can't extend
            ├─ dp[2] remains 1 (just element 2 by itself)
            └─ dp = [1, 1, 1, 1, 1, 1, 1, 1]

            i=3: Consider nums[3]=5, find best LIS ending at index 3
            ├─ Check j=0: nums[0]=10 > nums[3]=5, can't extend
            ├─ Check j=1: nums[1]=9 > nums[3]=5, can't extend
            ├─ Check j=2: nums[2]=2 < nums[3]=5, can extend!
            │  └─ dp[3] = max(dp[3], dp[2] + 1) = max(1, 1 + 1) = 2
            ├─ Best LIS ending at 3: [2, 5] with length 2
            └─ dp = [1, 1, 1, 2, 1, 1, 1, 1]

            i=4: Consider nums[4]=3, find best LIS ending at index 4
            ├─ Check j=0: nums[0]=10 > nums[4]=3, can't extend
            ├─ Check j=1: nums[1]=9 > nums[4]=3, can't extend
            ├─ Check j=2: nums[2]=2 < nums[4]=3, can extend!
            │  └─ dp[4] = max(dp[4], dp[2] + 1) = max(1, 1 + 1) = 2
            ├─ Check j=3: nums[3]=5 > nums[4]=3, can't extend
            ├─ Best LIS ending at 4: [2, 3] with length 2
            └─ dp = [1, 1, 1, 2, 2, 1, 1, 1]

            i=5: Consider nums[5]=7, find best LIS ending at index 5
            ├─ Check j=0: nums[0]=10 > nums[5]=7, can't extend
            ├─ Check j=1: nums[1]=9 > nums[5]=7, can't extend
            ├─ Check j=2: nums[2]=2 < nums[5]=7, can extend!
            │  └─ dp[5] = max(dp[5], dp[2] + 1) = max(1, 1 + 1) = 2
            ├─ Check j=3: nums[3]=5 < nums[5]=7, can extend!
            │  └─ dp[5] = max(dp[5], dp[3] + 1) = max(2, 2 + 1) = 3
            ├─ Check j=4: nums[4]=3 < nums[5]=7, can extend!
            │  └─ dp[5] = max(dp[5], dp[4] + 1) = max(3, 2 + 1) = 3
            ├─ Best LIS ending at 5: [2, 5, 7] with length 3
            └─ dp = [1, 1, 1, 2, 2, 3, 1, 1]

            i=6: Consider nums[6]=101, find best LIS ending at index 6
            ├─ Check all j < 6: nums[j] < 101 for all previous elements
            ├─ Best extension: dp[5] + 1 = 3 + 1 = 4 (from [2,5,7] to [2,5,7,101])
            ├─ dp[6] = 4
            └─ dp = [1, 1, 1, 2, 2, 3, 4, 1]

            i=7: Consider nums[7]=18, find best LIS ending at index 7
            ├─ Check all j < 7: nums[j] < 18 for j ∈ {2,3,4,5} (2,5,3,7 all < 18)
            ├─ Best extension: dp[5] + 1 = 3 + 1 = 4 (from [2,5,7] to [2,5,7,18])
            ├─ dp[7] = 4
            └─ dp = [1, 1, 1, 2, 2, 3, 4, 4]

            Final Result: max(dp) = max([1, 1, 1, 2, 2, 3, 4, 4]) = 4

            VERIFICATION:
            Possible LIS of length 4:
            - [2, 5, 7, 101] (indices 2→3→5→6)
            - [2, 5, 7, 18] (indices 2→3→5→7)
            - [2, 3, 7, 101] (indices 2→4→5→6)
            - [2, 3, 7, 18] (indices 2→4→5→7)
            ✓ Maximum length is indeed 4!
        '''

        if not nums:
            return 0

        n = len(nums)
        # initialize table where each value in dp automatically has a LIS of 1 (that value is a subsequence)
        dp = [1] * n

        # for each position, check all previous positions
        for i in range(1,n):
            for j in range(i):
                # if we can extend the LIS ending at j to include nums[i]
                if nums[j] < nums[i]: # so if the previous number is less than the current number
                    dp[i] = max(dp[i], dp[j] + 1)
                # else we can't add

        return max(dp)



    @staticmethod
    def word_break(s, word_dict):
        '''
            Given a string s and a dictionary of strings word_dict, return True if s can be segmented into space separated words of one or more dictionary words.
            Note that the same word in the dictionary may be used multiple times, but each char in the string can only be used once

            Examples:
            - s="leetcode", word_dict=["leet","code"] → True ("leet" + "code")
            - s="applepenapple", word_dict=["apple","pen"] → True ("apple" + "pen" + "apple")
            - s="catsandog", word_dict=["cats","dog","sand","and","cat"] → False

            Args:
                s: string to segment
                word_dict: list of dictionary words

            Returns:
                True if s can be segmented, False otherwise

            Q) What is the DP Framework for this problem?
                1. STATE: dp[i] = True if s[0:i] can be segmented into dictionary words
                2. TRANSITION: dp[i] = True if dp[j] AND s[j:i] in word_dict for some j < i
                3. BASE CASE: dp[0] = True (empty string can always be segmented)

            Q) What are the time and space complexities?
                - TABULATED: O(n² * m) time, O(n) space where n=len(s), m=avg word length
                - For each position i, check all positions j < i, and check if s[j:i] is in dict

            Q) Why is this a DP problem?
                - OPTIMAL SUBSTRUCTURE: s[0:i] can be segmented if s[0:j] can be segmented AND s[j:i] is a word
                - OVERLAPPING SUBPROBLEMS: Same prefixes are checked multiple times
                - DECISION PATTERN: Boolean DP where we track feasibility

            Q) Why do we use tabulation here?
                - Need to build up from smaller prefixes to larger prefixes
                - All intermediate prefixes needed to determine final answer
                - Natural left-to-right processing of string

            EXECUTION TRACE: word_break("leetcode", ["leet", "code"])
            =============================================================

            Initial Setup:
            s = "leetcode"
            word_dict = ["leet", "code"]
            word_set = {"leet", "code"}  # Convert to set for O(1) lookup
            n = 8
            dp = [False] * 9  # dp[0] to dp[8], representing s[0:0] to s[0:8]

            Base Case:
            dp[0] = True → dp = [True, False, False, False, False, False, False, False, False]
            # dp[0] means empty string s[0:0] = "" can be segmented (trivially true)

            Bottom-Up Building (i from 1 to n):

            i=1: Check if s[0:1] = "l" can be segmented
            ├─ j=0: dp[0]=True AND s[0:1]="l" in word_set? True AND False = False
            ├─ dp[1] = False
            └─ dp = [True, False, False, False, False, False, False, False, False]

            i=2: Check if s[0:2] = "le" can be segmented
            ├─ j=0: dp[0]=True AND s[0:2]="le" in word_set? True AND False = False
            ├─ j=1: dp[1]=False, skip (no point checking further)
            ├─ dp[2] = False
            └─ dp = [True, False, False, False, False, False, False, False, False]

            i=3: Check if s[0:3] = "lee" can be segmented
            ├─ j=0: dp[0]=True AND s[0:3]="lee" in word_set? True AND False = False
            ├─ j=1: dp[1]=False, skip
            ├─ j=2: dp[2]=False, skip
            ├─ dp[3] = False
            └─ dp = [True, False, False, False, False, False, False, False, False]

            i=4: Check if s[0:4] = "leet" can be segmented
            ├─ j=0: dp[0]=True AND s[0:4]="leet" in word_set? True AND True = True
            ├─ Found valid segmentation! dp[4] = True
            └─ dp = [True, False, False, False, True, False, False, False, False]

            i=5: Check if s[0:5] = "leetc" can be segmented
            ├─ j=0: dp[0]=True AND s[0:5]="leetc" in word_set? True AND False = False
            ├─ j=1: dp[1]=False, skip
            ├─ j=2: dp[2]=False, skip
            ├─ j=3: dp[3]=False, skip
            ├─ j=4: dp[4]=True AND s[4:5]="c" in word_set? True AND False = False
            ├─ dp[5] = False
            └─ dp = [True, False, False, False, True, False, False, False, False]

            i=6: Check if s[0:6] = "leetco" can be segmented
            ├─ j=0: dp[0]=True AND s[0:6]="leetco" in word_set? True AND False = False
            ├─ j=1,2,3: dp[j]=False, skip
            ├─ j=4: dp[4]=True AND s[4:6]="co" in word_set? True AND False = False
            ├─ j=5: dp[5]=False, skip
            ├─ dp[6] = False
            └─ dp = [True, False, False, False, True, False, False, False, False]

            i=7: Check if s[0:7] = "leetcod" can be segmented
            ├─ j=0: dp[0]=True AND s[0:7]="leetcod" in word_set? True AND False = False
            ├─ j=1,2,3: dp[j]=False, skip
            ├─ j=4: dp[4]=True AND s[4:7]="cod" in word_set? True AND False = False
            ├─ j=5,6: dp[j]=False, skip
            ├─ dp[7] = False
            └─ dp = [True, False, False, False, True, False, False, False, False]

            i=8: Check if s[0:8] = "leetcode" can be segmented
            ├─ j=0: dp[0]=True AND s[0:8]="leetcode" in word_set? True AND False = False
            ├─ j=1,2,3: dp[j]=False, skip
            ├─ j=4: dp[4]=True AND s[4:8]="code" in word_set? True AND True = True
            ├─ Found valid segmentation! dp[8] = True
            └─ dp = [True, False, False, False, True, False, False, False, True]

            Final Result: return dp[8] = True

            VERIFICATION:
            Valid segmentation found: s[0:4]="leet" (word) + s[4:8]="code" (word)
            ✓ "leetcode" = "leet" + "code", both in dictionary!
        '''

        if not s:
            return True

        # convert the word dict to a set for O(1) lookup
        word_set = set(word_dict)
        n = len(s)

        # dp[i] represents wheter s[0:i] can be segmented
        dp = [False] * (n + 1) # have to store char at end of n
        dp[0] = True # empty string can always be segmented

        # for each position i, try all possible splits
        for i in range(1, n+1):
            for j in range(i):
                # if s[0:j] can be segmeneted AND s[j:i] is a valid word (example where i is 6 and j is 4 -> check if dp[4] is valid AND if 4:6 is valid)
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break # found a valid segment, no need to keep checking

        return dp[n] # returning the last to ensure the last character is part of the word (i.e., can't have dog but not dogs)




    @staticmethod
    def buy_sell_stock1(prices):
        '''
            Find maximum profit from a single buy/sell transaction

            PROBLEM DESCRIPTION:
            You are given an array prices where prices[i] is the price of a stock on day i.
            You want to maximize profit by buying on one day and selling on a later day.
            Return the maximum profit. If no profit possible, return 0.

            Examples:
            - [7,1,5,3,6,4]: Buy on day 1 (price=1), sell on day 4 (price=6) → profit=5
            - [7,6,4,3,1]: Prices only decrease → no profit possible → return 0

            Args:
                prices: list of integers representing stock prices on each day

            Returns:
                maximum profit from single buy/sell transaction

            Q) What is the DP Framework for this problem?
                1. STATE: Two states at each day i:
                   - min_price = minimum price seen so far (best day to buy)
                   - max_profit = maximum profit achievable so far
                2. TRANSITION:
                   - min_price = min(min_price, prices[i])
                   - max_profit = max(max_profit, prices[i] - min_price)
                3. BASE CASE: min_price = prices[0], max_profit = 0

            Q) What are the time and space complexities?
                - TABULATED: O(n) time, O(1) space - our solution (single pass)
                - ALTERNATIVE: O(n) time, O(n) space - could store min_price and max_profit arrays

            Q) Why is this a DP problem?
                - OPTIMAL SUBSTRUCTURE: Best profit at day i depends on best buy price before day i
                - OVERLAPPING SUBPROBLEMS: Would recalculate minimum prices in brute force
                - MAX SO FAR PATTERN: Track running maximum profit and minimum price

            Q) Why do we use space-optimized tabulation?
                - Only need previous minimum price, not entire history
                - Single pass through array is sufficient
                - State can be compressed to two variables

            EXECUTION TRACE: buy_sell_stock1([7,1,5,3,6,4])
            ================================================

            Initial Setup:
            prices = [7, 1, 5, 3, 6, 4]
            min_price = 7  # Initialize with first price
            max_profit = 0  # No profit initially

            Day-by-Day Processing:

            Day 0: prices[0] = 7 (initialization, already handled)
            ├─ min_price = 7 (best buy price so far)
            ├─ max_profit = 0 (no selling possible yet)
            └─ State: min_price=7, max_profit=0

            Day 1: prices[1] = 1
            ├─ Update min_price = min(7, 1) = 1 (found better buy price!)
            ├─ Calculate profit if sell today: 1 - 1 = 0
            ├─ Update max_profit = max(0, 0) = 0
            └─ State: min_price=1, max_profit=0

            Day 2: prices[2] = 5
            ├─ Update min_price = min(1, 5) = 1 (keep previous best buy price)
            ├─ Calculate profit if sell today: 5 - 1 = 4
            ├─ Update max_profit = max(0, 4) = 4 (new best profit!)
            └─ State: min_price=1, max_profit=4

            Day 3: prices[3] = 3
            ├─ Update min_price = min(1, 3) = 1 (keep previous best buy price)
            ├─ Calculate profit if sell today: 3 - 1 = 2
            ├─ Update max_profit = max(4, 2) = 4 (keep previous best profit)
            └─ State: min_price=1, max_profit=4

            Day 4: prices[4] = 6
            ├─ Update min_price = min(1, 6) = 1 (keep previous best buy price)
            ├─ Calculate profit if sell today: 6 - 1 = 5
            ├─ Update max_profit = max(4, 5) = 5 (new best profit!)
            └─ State: min_price=1, max_profit=5

            Day 5: prices[5] = 4
            ├─ Update min_price = min(1, 4) = 1 (keep previous best buy price)
            ├─ Calculate profit if sell today: 4 - 1 = 3
            ├─ Update max_profit = max(5, 3) = 5 (keep previous best profit)
            └─ State: min_price=1, max_profit=5

            Final Result: return max_profit = 5

            VERIFICATION:
            Optimal strategy: Buy on day 1 (price=1), sell on day 4 (price=6)
            Profit = 6 - 1 = 5
            ✓ This matches our result!
        '''

        if not prices or len(prices) < 2:
            return 0

        # best day to buy
        min_price = prices[0]
        max_profit = 0
        n = len(prices)
        # process each day, updating best buy price and profit if sold that day
        for i in range(1, n):
            # update min price if we found a better buy day
            min_price = min(min_price, prices[i])

            # calculate current profit if we sold today
            current_profit = prices[i] - min_price
            max_profit = max(max_profit, current_profit)

        return max_profit




    @staticmethod
    def buy_sell_stock2(prices):
        '''
            Find maximum profit from multiple buy/sell transactions

            PROBLEM DESCRIPTION:
            You are given an array prices where prices[i] is the price of a stock on day i.
            Find the maximum profit you can achieve. You may complete as many transactions
            as you like (buy one and sell one share multiple times).
            Note: You cannot engage in multiple transactions simultaneously (must sell before buying again).

            Examples:
            - [7,1,5,3,6,4]: Buy day 1→sell day 2 (profit=4), buy day 3→sell day 4 (profit=3) → total=7
            - [1,2,3,4,5]: Buy day 0→sell day 4 (profit=4) OR multiple small transactions → total=4

            Args:
                prices: list of integers representing stock prices on each day

            Returns:
                maximum profit from multiple transactions

            Q) What is the DP Framework for this problem?
                1. STATE: Two states at each day i:
                   - hold_profit = max profit when holding stock at end of day i
                   - sold_proft = max profit when not holding stock at end of day i
                2. TRANSITION:
                   - hold = max(hold, sold - prices[i]) # keep holding OR buy today
                   - sold = max(sold, hold + prices[i]) # keep not holding OR sell today
                3. BASE CASE: hold = -prices[0] (bought on day 0), sold = 0 (no transactions)

            Q) What are the time and space complexities?
                - TABULATED: O(n) time, O(1) space - our solution
                - ALTERNATIVE: Greedy O(n) time, O(1) space - buy before every price increase

            Q) Why is this a DP problem?
                - OPTIMAL SUBSTRUCTURE: Best profit at day i depends on best profits at day i-1
                - STATE MACHINE: Track different states (holding vs not holding stock)
                - DECISION PATTERN: At each day, decide whether to buy, sell, or do nothing

            Q) Why do we use state machine DP here?
                - Two distinct states with different transitions
                - Each state depends on both states from previous day
                - Natural representation of the constraint (can't buy when already holding)

            EXECUTION TRACE: buy_sell_stock2([7,1,5,3,6,4])
            ===============================================

            Initial Setup:
            prices = [7, 1, 5, 3, 6, 4]
            hold = -7  # If we buy on day 0, profit = -7
            sold = 0   # If we don't buy on day 0, profit = 0

            Day-by-Day Processing:

            Day 0: prices[0] = 7 (initialization, already handled)
            ├─ hold = -7 (bought stock for 7, so profit is -7)
            ├─ sold = 0 (no transactions, profit is 0)
            └─ State: hold=-7, sold=0

            Day 1: prices[1] = 1
            ├─ New hold = max(old_hold, sold - prices[1]) = max(-7, 0 - 1) = max(-7, -1) = -1
            │  └─ Better to buy today (cost=1) than keep old position (cost=7)
            ├─ New sold = max(old_sold, hold + prices[1]) = max(0, -7 + 1) = max(0, -6) = 0
            │  └─ Better to stay cash than sell at loss
            └─ State: hold=-1, sold=0

            Day 2: prices[2] = 5
            ├─ New hold = max(old_hold, sold - prices[2]) = max(-1, 0 - 5) = max(-1, -5) = -1
            │  └─ Keep current position (bought at 1) rather than buy at 5
            ├─ New sold = max(old_sold, hold + prices[2]) = max(0, -1 + 5) = max(0, 4) = 4
            │  └─ Sell today! Profit = 5 - 1 = 4
            └─ State: hold=-1, sold=4

            Day 3: prices[3] = 3
            ├─ New hold = max(old_hold, sold - prices[3]) = max(-1, 4 - 3) = max(-1, 1) = 1
            │  └─ Buy today! Use previous profit (4) to buy at price 3, net=1
            ├─ New sold = max(old_sold, hold + prices[3]) = max(4, -1 + 3) = max(4, 2) = 4
            │  └─ Don't sell, keep previous profit of 4
            └─ State: hold=1, sold=4

            Day 4: prices[4] = 6
            ├─ New hold = max(old_hold, sold - prices[4]) = max(1, 4 - 6) = max(1, -2) = 1
            │  └─ Keep current position rather than buy at higher price
            ├─ New sold = max(old_sold, hold + prices[4]) = max(4, 1 + 6) = max(4, 7) = 7
            │  └─ Sell today! Total profit = previous 4 + new transaction profit 3 = 7
            └─ State: hold=1, sold=7

            Day 5: prices[5] = 4
            ├─ New hold = max(old_hold, sold - prices[5]) = max(1, 7 - 4) = max(1, 3) = 3
            │  └─ Could buy today, but let's see if we sell instead
            ├─ New sold = max(old_sold, hold + prices[5]) = max(7, 1 + 4) = max(7, 5) = 7
            │  └─ Don't sell at lower price, keep profit of 7
            └─ State: hold=3, sold=7

            Final Result: return sold = 7

            VERIFICATION:
            Optimal transactions:
            1. Buy day 1 (price=1) → Sell day 2 (price=5) → Profit = 4
            2. Buy day 3 (price=3) → Sell day 4 (price=6) → Profit = 3
            Total profit = 4 + 3 = 7 ✓

        '''

        if not prices or len(prices) < 2:
            return 0

        # hold_profit -> max profit when holding stock
        hold_profit = -prices[0] # buy on day 0

        # sold_profit -> max profit when not holding stock
        sold_profit = 0 # no transactions on day 0

        # process each day, updating both states
        for i in range(1, len(prices)):
            # update the hold_profit state... keep holding or buy today (i.e., if hold_profit is -2 (bought at $2), but price today is 1, we get max (-2, (0 - 1)) = max(-2, -1), then better to buy today than to keep hold position)
            # either
            # |> i was already holding stock yesterday, so i don't sell today
            # |> i sold yesterday, so i buy today (profit right after i sold the last stock i owned - what it would cost to buy the new stock)
            new_hold_profit = max(hold_profit, sold_profit - prices[i])

            # update the sold profit state: keep not holding or sell today
            # either
            # |> i was not holding profit yesterday
            # |> i was holding stock yesterday + im going to sell today (profit from right after the time of last purchase + would i would make today)
            new_sold_profit = max(sold_profit, hold_profit + prices[i])

            hold_profit, sold_profit = new_hold_profit, new_sold_profit

        return sold_profit # all transactions completed
