#!/usr/bin/python3
"""
Task: Change comes from within
Given a pile of coins of different values,
determine the fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
    Return: fewest number of coins needed to meet total
        - If total is 0 or less, return 0
        - If total cannot be met by any number of coins you have, return -1
        - Coins is a list of the values of the coins in your possession
        - The value of a coin will always be an integer greater than 0
        - You can assume you have an infinite number of each denomination of
        coin in the list
    """
    if total < 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for sub_total in range(coin, total + 1):
            dp[sub_total] = min(dp[sub_total], dp[sub_total - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
