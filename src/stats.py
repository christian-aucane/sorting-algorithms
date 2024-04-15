"""
src/stats.py

Statistics for sorting algorithms

This module contains the statistics for sorting algorithms

It includes the following functions:

- `generate_stats_dict`
- `write_stats_to_file`
- `main`
"""

import json
from pprint import pprint
from random import randint

from sorting import SORT_ALGORITHMS
from utils import STATS_DIR, time_sort


def generate_stats_dict(tab):
    """
    Parameters
    ----------
    tab : list
        The list to be sorted
    """
    stats = {}
    for name, function in SORT_ALGORITHMS.items():
            # if len(tab) <= 1000 or name != "bubble_sort":  # TODO : faire tourner en supprimant cette ligne
            stats[name] = {}
            for order in ['asc', 'desc']:
                runtime, tab_is_sorted = time_sort(tab[:], name, function, order, verbose=False)

                if tab_is_sorted:
                    print(f"{name} - {order} - Sorted in {runtime} s")
                    stats[name][order] = runtime
                else:
                    print(f"{name} - {order} - Unsorted")
                    stats[name][order] = None
    return stats


def write_stats_to_file(stats, filename):
    """
    Parameters
    ----------
    stats : dict
        The statistics to be written
    filename : str
        The name of the file
    """
    with open(filename, 'w') as f:
        json.dump(stats, f, indent=4)


def main():
    """
    Main function for the sorting algorithms statistics
    """
    min = -1000
    max = 1000
    result = {}
    STATS_DIR.mkdir(parents=True, exist_ok=True)
    for N in [10, 100, 1000, 10_000]:
        print(f"N = {N}")
        tab = [randint(min, max) for _ in range(N)]

        stats = generate_stats_dict(tab)
        pprint(stats)
        result[N] = stats
        write_stats_to_file(stats, STATS_DIR / f"{N}.json")

    pprint(result)
    write_stats_to_file(result, STATS_DIR / "stats.json")


if __name__ == "__main__":
    main()
