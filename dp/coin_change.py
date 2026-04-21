"""
You are given an integer array _coins_ representing coins of
different denominations and an integer _amount_ representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

E.g.
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

This is a test case that made me realize why we can't use greedy here:
Input: coins = [1, 3, 4], amount = 6
Output: 2
Explanation: 2 = 3 + 3 (greedy would have chosen 4 + 1 + 1)

Therefore, we need to use dynamic programming

Claude told me that we should be using a knapsack style DP which I am trying
to recall from my undergrad class

Think of using DP when:
* You need to try all possibilities (exhaustive search)
* But the same subproblems keep appearing repeatedly
* And you only need the optimal result, not every individual path
"""

def coin_change(coins: list[int], amount: int) -> int:
    # Create a list of size (amount + 1), one slot for every amount from 0 to amount
    # Each slot stores "what is the fewest coins needed to make this amount?"
    # We will fill it with infinity as a placeholder
    dp = [float("inf") * (amount + 1)]
    dp[0] = 0 # base case: 0 coins to make amount 0

    # Work out way up from amount 1 all the way up to our target amount
    for i in range(1, amount + 1):
        # For the current amount i, try every coin we have
        for coin in coins:
            # Only try this coin if its small enough to be used
            if coin <= i:
                # dp[i - coin] is the answer for the amount AFTER using this coin
                # e.g. if i=11 and coin=5, dp[6] is how many coins it took to make 6
                # Adding 1 accounts for the coin we just used
                # We take the min because we want the fewest coins overall
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[amount] is still infinity, no combination of coins could make this amount
    # Otherwise return the answer we built up
    return dp[amount] if dp[amount] != float("inf") else -1