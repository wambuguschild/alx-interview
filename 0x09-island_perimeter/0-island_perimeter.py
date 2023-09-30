#!/usr?bin/python3
"""Function to find the perimeter of and island"""


def island_perimeter(grid):
    """Getting the perimeter of island

    Args:
        grid (_type_): the grid containing
        the island
    """
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
