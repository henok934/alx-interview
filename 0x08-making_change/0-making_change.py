#!/usr/bin/python3
""" 0-making_change.py"""


def makeChange(coins, total):
    # Initialize the array to store the minimum number of coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Iterate over all amounts from 1 to the total
    for amount in range(1, total + 1):
        # Try each coin denomination
        for coin in coins:
            if coin <= amount:
                # Update the minimum number of coins needed
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Check if the total amount can be made using the given coins
    if dp[total] == float('inf'):
        return -1  # Total cannot be met by any number of coins
    else:
        return dp[total]  # Return the minimum number of coins needed
