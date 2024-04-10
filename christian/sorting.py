from random import randint
from time import time

from utils import OrderError, is_sorted, time_sort


def selection_sort(tab, order='asc'):
    """
    Selection sort

    Parameters
    ----------
    tab : list
        The list to be sorted
    order : str, optional
        The order of the list. The default is 'asc'. Possible values are 'asc' and 'desc'

    Returns
    -------
    tab : list
        The sorted list
    """
    n = len(tab)
    for i in range(n):
        if order == 'asc':
            # Trouver l'indice du minimum dans la partie non triée de la liste
            min_index = i + tab[i:].index(min(tab[i:]))
        elif order == 'desc':
            # Trouver l'indice du maximum dans la partie non triée de la liste
            min_index = i + tab[i:].index(max(tab[i:]))
        else:
            raise OrderError(order)
        
        # Échanger l'élément actuel avec l'élément minimum/maximum trouvé
        tab[i], tab[min_index] = tab[min_index], tab[i]
        print(tab)  # Optionnel : afficher les étapes intermédiaires du tri
    
    return tab


def bubble_sort(tab, order='asc'):
    """
    Bubble sort

    Parameters
    ----------
    tab : list
        The list to be sorted
    order : str, optional
        The order of the list. The default is 'asc'. Possible values are 'asc' and 'desc'

    Returns
    -------
    tab : list
        The sorted list
    """
    i = 0
    while not is_sorted(tab, order):
        if i >= len(tab) - 1:
            i = 0
        if order == 'asc':
            if tab[i] > tab[i + 1]:
                tab[i], tab[i + 1] = tab[i + 1], tab[i]
        elif order == 'desc':
            if tab[i] < tab[i + 1]:
                tab[i], tab[i + 1] = tab[i + 1], tab[i]
        else:
            raise OrderError(order)
        i += 1

    return tab


def insertion_sort(tab, order='asc'):
    """
    Insertion sort

    Parameters
    ----------
    tab : list
        The list to be sorted
    order : str, optional
        The order of the list. The default is 'asc'. Possible values are 'asc' and 'desc'

    Returns
    -------
    tab : list
        The sorted list
    """
    while not is_sorted(tab, order):
        for i in range(1, len(tab)):
            x = tab[i]
            j = i
            if order == 'asc':
                while j > 0 and tab[j - 1] > x:
                    tab[j] = tab[j - 1]
                    j -= 1
            elif order == 'desc':
                while j > 0 and tab[j - 1] < x:
                    tab[j] = tab[j - 1]
                    j -= 1
            else:
                raise OrderError(order)
            tab[j] = x

    return tab


def merge_sort(tab, order='asc'):
    """
    Merge sort

    Parameters
    ----------
    tab : list
        The list to be sorted
    order : str, optional
        The order of the list. The default is 'asc'. Possible values are 'asc' and 'desc'

    Returns
    -------
    tab : list
        The sorted list
    """
    def merge(left, right, order):
        left_index, right_index = 0, 0
        result = []
        while left_index < len(left) and right_index < len(right):
            if order == 'asc':
                condition = left[left_index] <= right[right_index]
            elif order == 'desc':
                condition = left[left_index] >= right[right_index]
            else:
                raise OrderError(order)
            if condition:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result += left[left_index:]
        result += right[right_index:]
        return result
    
    if len(tab) <= 1:
        if is_sorted(tab, order):
            return tab
    middle = len(tab) // 2
    left = merge_sort(tab[:middle], order)
    right = merge_sort(tab[middle:], order)
    return merge(left, right, order)


def quick_sort(tab, order='asc'):
    """
    Quick sort

    Parameters
    ----------
    tab : list
        The list to be sorted
    order : str, optional
        The order of the list. The default is 'asc'. Possible values are 'asc' and 'desc'
        
    Returns
    -------
    tab : list
        The sorted list
    """
    if len(tab) <= 1:
        return tab
    
    pivot = tab[len(tab) // 2]
    if order == 'asc':
        left = [x for x in tab if x < pivot]
        right = [x for x in tab if x > pivot]
    elif order == 'desc':
        left = [x for x in tab if x > pivot]
        right = [x for x in tab if x < pivot]
    else:
        raise OrderError(order)
    tab = quick_sort(left, order) + [pivot] + quick_sort(right, order)
    return tab


def heap_sort(tab, order='asc'):
    """
    Heap sort

    Parameters
    ----------
    tab : list
        The list to be sorted
    order : str, optional
        The order of the list. The default is 'asc'. Possible values are 'asc' and 'desc'

    Returns
    -------
    tab : list
        The sorted list
    """
    def heapify(tab, i, n, order):
        i_largest = i
        i_left = 2 * i + 1
        i_right = 2 * i + 2

        if order == 'asc':
            if i_left < n and tab[i] < tab[i_left]:
                i_largest = i_left
            if i_right < n and tab[i_largest] < tab[i_right]:
                i_largest = i_right

        elif order == 'desc':
            if i_left < n and tab[i] > tab[i_left]:
                i_largest = i_left
            if i_right < n and tab[i_largest] > tab[i_right]:
                i_largest = i_right

        if i_largest != i:
            tab[i], tab[i_largest] = tab[i_largest], tab[i]
            heapify(tab, i_largest, n, order)
            
    for i in range(len(tab) // 2 - 1, -1, -1):
        heapify(tab, i, len(tab), order)
    for i in range(len(tab) - 1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify(tab, 0, i, order)
    return tab


def comb_sort(tab, order='asc', shrink_factor=1.3):
    """
    Comb sort

    Parameters
    ----------
    tab : list
        The list to be sorted
    order : str, optional
        The order of the list. The default is 'asc'. Possible values are 'asc' and 'desc'
    shrink_factor : float, optional
        The shrink factor. The default is 1.3

    Returns
    -------
    tab : list
        The sorted list
    """
    gap = len(tab)
    sorted = False

    while not sorted:
        gap = int(gap / shrink_factor)
        if gap <= 1:
            gap = 1
        
        swapped = False  # Drapeau pour suivre les échanges dans cette itération
        for i in range(len(tab) - gap):
            if order == 'asc':
                if tab[i] > tab[i + gap]:
                    tab[i], tab[i + gap] = tab[i + gap], tab[i]
                    swapped = True
            elif order == 'desc':
                if tab[i] < tab[i + gap]:
                    tab[i], tab[i + gap] = tab[i + gap], tab[i]
                    swapped = True
            else:
                raise OrderError(order)

        if gap == 1 and not swapped:
            sorted = True

    return tab


SORT_ALGORITHMS = {
    'selection_sort': selection_sort,
    'bubble_sort': bubble_sort,
    'insertion_sort': insertion_sort,
    'merge_sort': merge_sort,
    'quick_sort': quick_sort,
    'heap_sort': heap_sort,
    'comb_sort': comb_sort 
}


if __name__ == '__main__':
    MIN = 0
    MAX = 1000
    N = 10
    # tab = [randint(MIN, MAX) for _ in range(N)]
    tab = [3, 9, 4, 5, 10, 6, 7]
    print("tab", tab)
    time_sort(tab[:], "Selection sort", selection_sort, 'asc')
    time_sort(tab[:], "Selection sort", selection_sort, 'desc')
    # time_sort(tab[:], "Bubble sort", bubble_sort, 'asc')
    # time_sort(tab[:], "Bubble sort", bubble_sort, 'desc')
    time_sort(tab[:], "Insertion sort", insertion_sort, 'asc')
    time_sort(tab[:], "Insertion sort", insertion_sort, 'desc')
    time_sort(tab[:], "Merge sort", merge_sort, 'asc')
    time_sort(tab[:], "Merge sort", merge_sort, 'desc')
    time_sort(tab[:], "Quick sort", quick_sort, 'asc')
    time_sort(tab[:], "Quick sort", quick_sort, 'desc')
    time_sort(tab[:], "Heap sort", heap_sort, 'asc')
    time_sort(tab[:], "Heap sort", heap_sort, 'desc')
    time_sort(tab[:], "Comb sort", comb_sort, 'asc')
    time_sort(tab[:], "Comb s²ort", comb_sort, 'desc')
