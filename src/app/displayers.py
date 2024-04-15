"""
displayers.py

This module contains the displayers used in the sorting algorithms pygame app.

It includes the following classes:

- `BaseSortDisplayer`: the base class for the displayers
- `BubbleSortDisplayer`: the class for the bubble sort display
- `SelectionSortDisplayer`: the class for the selection sort display
- `InsertionSortDisplayer`: the class for the insertion sort display
- `ShellSortDisplayer`: the class for the shell sort display
- `MergeSortDisplayer`: the class for the merge sort display
- `QuickSortDisplayer`: the class for the quick sort display
- `HeapSortDisplayer`: the class for the heap sort display
- `CombSortDisplayer`: the class for the comb sort display
"""

import pygame

from .constants import WHITE, BLACK, WIDTH, HEIGHT


class BaseSortDisplayer:
    """
    The base class for the displayers
    
    Class variables:
        - `clock`: the pygame clock

    Attributes:
        - screen (pygame.Surface): the screen
        - tab (list): the list to sort
        - order (str): the order of the list ('asc' or 'desc')
        - title (str): the title of the algorithm
        - stop_sorting (bool): whether to stop the sorting
        - min (int): the minimum value in the list
        - max (int): the maximum value in the list
        - color_range (int): the range of the colors
        
    Methods:
        - get_color(num): get the color of the number
        - draw_title(title): draw the title on the screen
        - draw_text(text, x, y, color=WHITE): draw the text on the screen
        - clean_screen(): clean the screen
        - handle_events(): handle events
        - update_screen(): update the screen
        - sort(): sort the list based on the algorithm and order specified in the constructor (MUST BE IMPLEMENTED IN SUBCLASS)

    Properties:
        - is_sorted: check if the list is sorted
    """
    clock = pygame.time.Clock()

    def __init__(self, screen, tab, order, title):
        """
        Initialize the displayer

        Args:
            screen (pygame.Surface): the screen
            tab (list): the list to sort
            order (str): the order of the list
            title (str): the title of the algorithm
            
        Raises:
            ValueError: if the order is not 'asc' or 'desc'
        """
        if order not in ['asc', 'desc']:
            raise ValueError(f"'{order}' is not a valid order - must be 'asc' or 'desc'")
        self.screen = screen
        self.tab = tab
        self.order = order
        self.title = title
        self.stop_sorting = False
        self.min = min(self.tab)
        self.max = max(self.tab)
        self.color_range = self.max - self.min

    @property
    def is_sorted(self):
        """
        Check if the list is sorted

        Returns:
            bool: whether the list is sorted
        """
        if self.order == 'asc':
            return all(self.tab[i] <= self.tab[i + 1] for i in range(len(self.tab) - 1))
        else:
            return all(self.tab[i] >= self.tab[i + 1] for i in range(len(self.tab) - 1))

    def get_color(self, num):
        """
        Get the color of the number

        Args:
            num (int): the number

        Returns:
            tuple: the color of the number
        """
        color_value = int(255 * (num - self.min) / self.color_range)
        color = (255 - color_value, color_value, 0)  # Red to green
        return color

    def draw_title(self, title):
            """
            Draw the title on the screen

            Args:
                title (str): the title
            """
            font = pygame.font.SysFont("", 50)

            text = font.render(title, True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, 50))
            self.screen.blit(text, text_rect)

    def draw_text(self, text, x, y, color=BLACK, font_size=30):
        """
        Draw the text on the screen

        Args:
            text (str): the text
            x (int): the x coordinate
            y (int): the y coordinate
            color (tuple, optional): the color. Defaults to BLACK.
            font_size (int, optional): the font size. Defaults to 30.
        """
        font = pygame.font.SysFont("", font_size)
        text = font.render(text, True, color)
        text_rect = text.get_rect(center=(x, y))
        self.screen.blit(text, text_rect)

    def clean_screen(self):
        """
        Clean the screen
        """
        self.screen.fill(WHITE)
        self.draw_title(self.title)

    def handle_events(self):
        """
        Handle events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
                self.stop_sorting = True

    def update_screen(self):
        """
        Update the screen
        """
        self.clean_screen()
        for i in range(len(self.tab)):
            color = self.get_color(self.tab[i])
            normalized_height = (self.tab[i] / self.max) * (HEIGHT - 100)  # Normalize height
            pygame.draw.rect(self.screen, color, (i * WIDTH // len(self.tab), HEIGHT - normalized_height, WIDTH // len(self.tab), normalized_height))#self.draw_text(" ".join(map(str, self.tab)), WIDTH // 2, 150)
        if self.is_sorted:
            self.draw_text("Done", WIDTH // 2, 200, color=BLACK)

        pygame.display.flip()
        self.clock.tick(20)

    def sort(self):
        """
        Sort the list based on the algorithm and order specified in the constructor (MUST BE IMPLEMENTED IN SUBCLASS)
        
        Raises:
            NotImplementedError: if the method is not implemented in the subclass
        """
        raise NotImplementedError("Method must be implemented in subclass")


class SelectionSortDisplayer(BaseSortDisplayer):
    """
    Displayer for the Selection Sort algorithm
    
    Attributes:
        Inherited from `BaseSortDisplayer`:
            screen (pygame.Surface): the screen
            tab (list): the list to sort
            order (str): the order of the list
            title (str): the title of the algorithm
            stop_sorting (bool): whether to stop the sorting
            min (int): the minimum value in the list
            max (int): the maximum value in the list
            color_range (int): the range of the colors
        Local:
            i (int): the index of the current element being sorted

    Methods:
        Inherited from `BaseSortDisplayer`:
            get_color(self, num)
            draw_title(self, title)
            draw_text(self, text, x, y, color=BLACK, font_size=30)
            clean_screen(self)
            handle_events(self)
            update_screen(self)
        Override:
            sort(self)

    Properties:
        Inherited from `BaseSortDisplayer`:
            is_sorted (bool): whether the list is sorted
    """

    def __init__(self, screen, tab, order):
        """
        Initialize the displayer

        Args:
            screen (pygame.Surface): the screen
            tab (list): the list to sort
            order (str): the order of the list
        """
        super().__init__(screen=screen, tab=tab, order=order, title="Selection Sort")
        self.i = 0

    def sort(self):
        """
        Sort the list based on the selection sort algorithm and the order specified in the constructor
        """
        for i in range(len(self.tab)):
            self.handle_events()
            if self.stop_sorting or self.is_sorted:
                break
            self.i = i
            if self.order == 'asc':
                # Find the index of the minimum in the unsorted part of the list
                index = i + self.tab[i:].index(min(self.tab[i:]))
            elif self.order == 'desc':
                # Find the index of the maximum in the unsorted part of the list
                index = i + self.tab[i:].index(max(self.tab[i:]))
            # Exchange the current element with the minimum/maximum element found
            self.tab[i], self.tab[index] = self.tab[index], self.tab[i]
            
            self.update_screen()


class BubbleSortDisplayer(BaseSortDisplayer):
    """
    Displayer for the Bubble Sort algorithm

    Attributes:
        Inherited from `BaseSortDisplayer`:
            screen (pygame.Surface): the screen
            tab (list): the list to sort
            order (str): the order of the list
            title (str): the title of the algorithm
            stop_sorting (bool): whether to stop the sorting
            min (int): the minimum value in the list
            max (int): the maximum value in the list
            color_range (int): the range of the colors
        Local:
            i (int): the index of the current element being sorted
    
    Methods:
        Inherited from `BaseSortDisplayer`:
            get_color(self, num)
            draw_title(self, title)
            draw_text(self, text, x, y, color=BLACK, font_size=30)
            clean_screen(self)
            handle_events(self)
            update_screen(self)
        Override:
            sort(self)

    Properties:
        Inherited from `BaseSortDisplayer`:
            is_sorted (bool): whether the list is sorted
    """

    def __init__(self, screen, tab, order):
        """
        Initialize the displayer

        Args:
            screen (pygame.Surface): the screen
            tab (list): the list to sort
            order (str): the order of the list
        """
        super().__init__(screen=screen, tab=tab, order=order, title="Bubble Sort")
        self.i = 0

    def sort(self):
        """
        Sort the list based on the bubble sort algorithm and the order specified in the constructor
        """
        while not self.is_sorted:
            self.handle_events()
            if self.stop_sorting:
                break
            if self.i >= len(self.tab) - 1:
                self.i = 0
            if self.order == 'asc':
                if self.tab[self.i] > self.tab[self.i + 1]:
                    self.tab[self.i], self.tab[self.i + 1] = self.tab[self.i + 1], self.tab[self.i]
            elif self.order == 'desc':
                if self.tab[self.i] < self.tab[self.i + 1]:
                    self.tab[self.i], self.tab[self.i + 1] = self.tab[self.i + 1], self.tab[self.i]

            self.i += 1
            
            self.update_screen()


class InsertionSortDisplayer(BaseSortDisplayer):
    """
    Displayer for the Insertion Sort algorithm

    Attributes:
        Inherited from `BaseSortDisplayer`:
            screen (pygame.Surface): the screen
            tab (list): the list to sort
            order (str): the order of the list
            title (str): the title of the algorithm
            stop_sorting (bool): whether to stop the sorting
            min (int): the minimum value in the list
            max (int): the maximum value in the list
            color_range (int): the range of the colors
        Local:
            i (int): the index of the current element being sorted
            j (int): the index of the previous element being sorted
            
    Methods:
        Inherited from `BaseSortDisplayer`:
            get_color(self, num)
            draw_title(self, title)
            draw_text(self, text, x, y, color=BLACK, font_size=30)
            clean_screen(self)
            handle_events(self)
            update_screen(self)
        Override:
            sort(self)

    Properties:
        Inherited from `BaseSortDisplayer`:
            is_sorted (bool): whether the list is sorted
    """
    def __init__(self, screen, tab, order):
        """
        Initialize the displayer

        Args:
            screen (pygame.Surface): the screen
            tab (list): the list to sort
            order (str): the order of the list
        """
        super().__init__(screen=screen, tab=tab, order=order, title="Insertion Sort")
        self.i = 0
        self.j = 0

    def sort(self):
        """
        Sort the list based on the insertion sort algorithm and the order specified in the constructor
        """
        for i in range(1, len(self.tab)):
            self.handle_events()
            if self.stop_sorting or self.is_sorted:
                break
            x = self.tab[i]
            j = i
            self.i = i
            if self.order == 'asc':
                while j > 0 and self.tab[j - 1] > x:
                    self.tab[j] = self.tab[j - 1]
                    j -= 1
                    self.j = j
            elif self.order == 'desc':
                while j > 0 and self.tab[j - 1] < x:
                    self.handle_events()
                    if self.stop_sorting or self.is_sorted:
                        break
                    self.tab[j] = self.tab[j - 1]
                    j -= 1
                    self.j = j
            self.tab[j] = x
            self.update_screen()


class MergeSortDisplayer(BaseSortDisplayer):
    """
    Displayer for the Merge Sort algorithm

    Attributes:
        Inherited from `BaseSortDisplayer`:
            screen (pygame.Surface): the screen
            tab (list): the list to sort
            order (str): the order of the list
            title (str): the title of the algorithm
            stop_sorting (bool): whether to stop the sorting
            min (int): the minimum value in the list
            max (int): the maximum value in the list
            color_range (int): the range of the colors
        Local:
            _is_sorted (bool): whether the list is sorted
            
    Methods:
        Inherited from `BaseSortDisplayer`:
            get_color(self, num)
            draw_title(self, title)
            draw_text(self, text, x, y, color=BLACK, font_size=30)
            clean_screen(self)
            handle_events(self)
            update_screen(self)
        Override:
            sort(self)
        Local:
            sort_recursive(self, tab)
            merge(self, left, right)

    Properties:
        Override:
            is_sorted (bool): whether the list is sorted
    """
    def __init__(self, screen, tab, order):
        """
        Initialize the displayer

        Args:
            screen (pygame.Surface): the screen
            tab (list): the list to sort
            order (str): the order of the list
        """
        super().__init__(screen=screen, tab=tab, order=order, title="Merge Sort")
        self._is_sorted = False

    @property
    def is_sorted(self):
        """
        Check if the list is sorted
        """
        return self._is_sorted

    def merge(self, left, right):
        """
        Merge two sorted lists

        Args:
            left (list): the left list
            right (list): the right list

        Returns:
            list: the merged list
        """
        left_index, right_index = 0, 0
        result = []
        while left_index < len(left) and right_index < len(right):
            if self.order == 'asc':
                condition = left[left_index] <= right[right_index]
            elif self.order == 'desc':
                condition = left[left_index] >= right[right_index]
            if condition:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result += left[left_index:]
        result += right[right_index:]
        return result

    def sort_recursive(self, tab):
        """
        Sort the list based on the merge sort algorithm and the order specified in the constructor

        Args:
            tab (list): the list to sort

        Returns:
            list: the sorted list
        """
        self.handle_events()
        if self.stop_sorting or len(tab) <= 1 or self.is_sorted:
            return tab  # Returns the list
        
        middle = len(tab) // 2
        left = self.sort_recursive(tab[:middle])
        right = self.sort_recursive(tab[middle:])
        return self.merge(left, right)  # Returns the merged list

    def sort(self):
        """
        Sort the list based on the merge sort algorithm and the order specified in the constructor
        """
        self.update_screen()
        self.clock.tick(1)
        self.tab = self.sort_recursive(self.tab)
        self.update_screen()


class QuickSortDisplayer(BaseSortDisplayer):
    """
    Displayer for the Quick Sort algorithm
    
    Attributes:
        Inherited from `BaseSortDisplayer`:
            screen (pygame.Surface): the screen
            tab (list): the list to sort
            order (str): the order of the list
            title (str): the title of the algorithm
            stop_sorting (bool): whether to stop the sorting
            min (int): the minimum value in the list
            max (int): the maximum value in the list
            color_range (int): the range of the colors
    
    Methods:
        Inherited from `BaseSortDisplayer`:
            get_color(self, num)
            draw_title(self, title)
            draw_text(self, text, x, y, color=BLACK, font_size=30)
            clean_screen(self)
            handle_events(self)
            update_screen(self)
        Override:
            sort(self)
        Local:
            partition(self, tab, low, high)
            sort_recursive(self, tab, low, high)

    Properties:
        Inherited from `BaseSortDisplayer`:
            is_sorted (bool): whether the list is sorted
    """
    def __init__(self, screen, tab, order):
        """
        Initialize the displayer

        Args:
            screen (pygame.Surface): the screen
            tab (list): the list to sort
            order (str): the order of the list
        """
        super().__init__(screen=screen, tab=tab, order=order, title="Quick Sort")

    def partition(self, tab, low, high):
        """
        Partition the list into two parts

        Args:
            tab (list): the list to partition
            low (int): the low index
            high (int): the high index

        Returns:
            int: the pivot index
        """
        pivot = tab[high]
        i = low - 1
        for j in range(low, high):
            if self.order == 'asc':
                if tab[j] < pivot:
                    i += 1
                    tab[i], tab[j] = tab[j], tab[i]
            elif self.order == 'desc':
                if tab[j] > pivot:
                    i += 1
                    tab[i], tab[j] = tab[j], tab[i]
        tab[i + 1], tab[high] = tab[high], tab[i + 1]
        return i + 1

    def sort_recursive(self, tab, low, high):
        """
        Sort the list based on the quick sort algorithm and the order specified in the constructor"""
        if low < high:
            pivot = self.partition(tab, low, high)
            self.update_screen()
            self.sort_recursive(tab, low, pivot - 1)
            self.sort_recursive(tab, pivot + 1, high)

    def sort(self):
        """
        Sort the list based on the quick sort algorithm and the order specified in the constructor
        """
        self.sort_recursive(self.tab, 0, len(self.tab) - 1)


class HeapSortDisplayer(BaseSortDisplayer):
    """
    Displayer for the Heap Sort algorithm

    Attributes:
        Inherited from `BaseSortDisplayer`:
            screen (pygame.Surface): the screen
            tab (list): the list to sort
            order (str): the order of the list
            title (str): the title of the algorithm
            stop_sorting (bool): whether to stop the sorting
            min (int): the minimum value in the list
            max (int): the maximum value in the list
            color_range (int): the range of the colors

    Methods:
        Inherited from `BaseSortDisplayer`:
            get_color(self, num)
            draw_title(self, title)
            draw_text(self, text, x, y, color=BLACK, font_size=30)
            clean_screen(self)
            handle_events(self)
            update_screen(self)
        Override:
            sort(self)
        Local:
            heapify(self, tab, i, n)
            
    Properties:
        Inherited from `BaseSortDisplayer`:
            is_sorted (bool): whether the list is sorted
    """

    def __init__(self, screen, tab, order):
        """
        Initialize the displayer

        Args:
            screen (pygame.Surface): the screen
            tab (list): the list to sort
            order (str): the order of the list
        """
        super().__init__(screen=screen, tab=tab, order=order, title="Heap Sort")

    def heapify(self, tab, i, n):
        """
        Heapify the list
        
        Args:
            tab (list): the list to heapify
            i (int): the index of the root
            n (int): the length of the list
        """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if self.order == 'asc':
            if left < n and tab[i] < tab[left]:
                largest = left
            if right < n and tab[largest] < tab[right]:
                largest = right
        elif self.order == 'desc':
            if left < n and tab[i] > tab[left]:
                largest = left
            if right < n and tab[largest] > tab[right]:
                largest = right

        if largest != i:
            tab[i], tab[largest] = tab[largest], tab[i]
            self.heapify(tab, largest, n)

    def sort(self):
        """
        Sort the list
        """
        for i in range(len(self.tab) // 2 - 1, -1, -1):
            self.handle_events()
            if self.stop_sorting:
                return
            self.i = i
            self.heapify(self.tab, i, len(self.tab))
            self.update_screen()
        for i in range(len(self.tab) - 1, 0, -1):
            self.handle_events()
            if self.stop_sorting:
                return
            self.tab[0], self.tab[i] = self.tab[i], self.tab[0]
            self.heapify(self.tab, 0, i)
            self.update_screen()


class CombSortDisplayer(BaseSortDisplayer):
    """
    Displayer for the Comb Sort algorithm

    Attributes:
        Inherited from `BaseSortDisplayer`:
            screen (pygame.Surface): the screen
            tab (list): the list to sort
            order (str): the order of the list
            title (str): the title of the algorithm
            stop_sorting (bool): whether to stop the sorting
            min (int): the minimum value in the list
            max (int): the maximum value in the list
            color_range (int): the range of the colors
            
    Methods:
        Inherited from `BaseSortDisplayer`:
            get_color(self, num)
            draw_title(self, title)
            draw_text(self, text, x, y, color=BLACK, font_size=30)
            clean_screen(self)
            handle_events(self)
            update_screen(self)
        Override:
            sort(self)
        Local:
            shrink_factor (float): the shrink factor of the gap

    Properties:
        Inherited from `BaseSortDisplayer`:
            is_sorted (bool): whether the list is sorted
    """
    def __init__(self, screen, tab, order):
        """
        Initialize the displayer

        Args:
            screen (pygame.Surface): the screen
            tab (list): the list to sort
            order (str): the order of the list
        """
        super().__init__(screen=screen, tab=tab, order=order, title="Comb Sort")
        self.shrink_factor = 1.3

    def sort(self):
        """
        Sort the list
        """
        gap = len(self.tab)
        sorted = False

        while not sorted:
            self.handle_events()
            if self.stop_sorting:
                return
            
            gap = int(gap / self.shrink_factor)
            if gap <= 1:
                gap = 1
            
            swapped = False  # Flag to follow exchanges in this iteration
            for i in range(len(self.tab) - gap):
                
                self.handle_events()
                if self.stop_sorting:
                    return
                if self.order == 'asc':
                    if self.tab[i] > self.tab[i + gap]:
                        self.tab[i], self.tab[i + gap] = self.tab[i + gap], self.tab[i]
                        swapped = True
                elif self.order == 'desc':
                    if self.tab[i] < self.tab[i + gap]:
                        self.tab[i], self.tab[i + gap] = self.tab[i + gap], self.tab[i]
                        swapped = True

            if swapped:
                self.update_screen()
            elif gap == 1:
                sorted = True


# Dictionnary of algorithms
ALGORITHMS_DISPLAYERS = {
    'selection_sort': SelectionSortDisplayer,
    'bubble_sort': BubbleSortDisplayer,
    'insertion_sort': InsertionSortDisplayer,
    'merge_sort': MergeSortDisplayer,
    'quick_sort': QuickSortDisplayer,
    'heap_sort': HeapSortDisplayer,
    'comb_sort': CombSortDisplayer
}
