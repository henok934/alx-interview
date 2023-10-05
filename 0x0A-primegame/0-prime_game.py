#!/usr/bin/python3
""" 0-prime_game.py"""


def isWinner(x, nums):
    """is winner method"""
    wins = {'Maria': 0, 'Ben': 0}  # Track the number of wins for each player

    for i in range(x):
        n = nums[i]  # Get the value of n for the current round

        if isMariaWinner(n):  # Check if Maria wins the game for the given n
            wins['Maria'] += 1
        else:
            wins['Ben'] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Ben'] > wins['Maria']:
        return 'Ben'
    else:
        return None


def isMariaWinner(n):
    """helper method"""

    remaining_nums = [True] * (n + 1)
    remaining_nums[0] = remaining_nums[1] = False
    for i in range(2, int(n**0.5) + 1):
        if remaining_nums[i]:
            for j in range(i * i, n + 1, i):
                remaining_nums[j] = False
    return sum(remaining_nums) % 2 != 0
