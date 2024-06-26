"""
src/utils.py

Utils for sorting algorithms

This module contains the utils for sorting algorithms

It includes the following functions:

- `is_sorted`
- `time_sort`
- `OrderError`
"""

from pathlib import Path
from time import time


STATS_DIR = Path(__file__).resolve().parent / 'stats'


class OrderError(Exception):
    """
    Raised when the order is not 'asc' or 'desc'
    
    Parameters
    ----------
    order : str
        The order must be 'asc' or 'desc'
    """
    def __init__(self, order, *args):
        super().__init__(f"'{order}' is not a valid order - must be 'asc' or 'desc'")



def is_sorted(tab, order='asc'):
    """
    Parameters
    ----------
    tab : list
        The list to be sorted
    order : str, optional
        The order of the list. The default is 'asc'. Possible values are 'asc' and 'desc'
    """
    if order == 'asc':
        sorted = all(tab[i] <= tab[i + 1] for i in range(len(tab) - 1))
    else:
        sorted = all(tab[i] >= tab[i + 1] for i in range(len(tab) - 1))
    
    return sorted



def time_sort(tab, name, sort_function, order, verbose=True):
    """
    Views the execution time of the sort function

    Parameters
    ----------
    tab : list
        The list to be sorted
    name : str
        The name of the algorithm
    sort_function : function
        The function to sort the list
    order : str
        The order of the list. Possible values are 'asc' and 'desc'
    verbose : bool, optional
        Whether to print the execution time or not. The default is True
    """
    start = time()
    sorted_tab = sort_function(tab, order)
    end = time()
    runtime = (end - start)
    tab_is_sorted = is_sorted(sorted_tab, order)
    if verbose:
        if tab_is_sorted:
            print(f"{name} - {order} - Sorted in {runtime} s")
        else:
            print(f"{name} - {order} - Unsorted")

    return runtime, tab_is_sorted
