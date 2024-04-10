import pygame


from .constants import WHITE, BLACK, WIDTH, HEIGHT



# TODO : Améliorer l'affichage


class BaseSortDisplayer:
    clock = pygame.time.Clock()
    def __init__(self, screen, tab, order, title):
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

    def get_color(self, num):
        color_value = int(255 * (num - self.min) / self.color_range)
        color = (255 - color_value, color_value, 0)  # Rouge à vert
        return color

    @property
    def is_sorted(self):
        if self.order == 'asc':
            return all(self.tab[i] <= self.tab[i + 1] for i in range(len(self.tab) - 1))
        else:
            return all(self.tab[i] >= self.tab[i + 1] for i in range(len(self.tab) - 1))

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
        font = pygame.font.SysFont("", font_size)
        text = font.render(text, True, color)
        text_rect = text.get_rect(center=(x, y))
        self.screen.blit(text, text_rect)

    def clean_screen(self):
        self.screen.fill(WHITE)
        self.draw_title(self.title)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
                self.stop_sorting = True

    def update_screen(self):
        print("Update Screen", self.tab)
        self.clean_screen()
        for i in range(len(self.tab)):
            color = self.get_color(self.tab[i])
            normalized_height = (self.tab[i] / self.max) * (HEIGHT - 100)  # Normaliser la hauteur
            pygame.draw.rect(self.screen, color, (i * WIDTH // len(self.tab), HEIGHT - normalized_height, WIDTH // len(self.tab), normalized_height))#self.draw_text(" ".join(map(str, self.tab)), WIDTH // 2, 150)
        if self.is_sorted:
            self.draw_text("Done", WIDTH // 2, 200, color=BLACK)

        pygame.display.flip()
        self.clock.tick(20)

    def sort(self):
        raise NotImplementedError("Method must be implemented in subclass")


class SelectionSortDisplayer(BaseSortDisplayer):
    def __init__(self, screen, tab, order):
        super().__init__(screen=screen, tab=tab, order=order, title="Selection Sort")
        self.i = 0

    def sort(self):
        for i in range(len(self.tab)):
            self.handle_events()
            if self.stop_sorting or self.is_sorted:
                break
            self.i = i
            print("i = ", self.i)
            if self.order == 'asc':
                # Trouver l'indice du minimum dans la partie non triée de la liste
                min_index = i + self.tab[i:].index(min(self.tab[i:]))
            elif self.order == 'desc':
                # Trouver l'indice du maximum dans la partie non triée de la liste
                min_index = i + self.tab[i:].index(max(self.tab[i:]))
            # Échanger l'élément actuel avec l'élément minimum/maximum trouvé
            self.tab[i], self.tab[min_index] = self.tab[min_index], self.tab[i]
            
            self.update_screen()


class BubbleSortDisplayer(BaseSortDisplayer):
    def __init__(self, screen, tab, order):
        super().__init__(screen=screen, tab=tab, order=order, title="Bubble Sort")
        self.i = 0

    def sort(self):
        while not self.is_sorted:
            self.handle_events()
            if self.stop_sorting:
                break
            if self.i >= len(self.tab) - 1:
                self.i = 0
            print("i = ", self.i)
            if self.order == 'asc':
                if self.tab[self.i] > self.tab[self.i + 1]:
                    self.tab[self.i], self.tab[self.i + 1] = self.tab[self.i + 1], self.tab[self.i]
            elif self.order == 'desc':
                if self.tab[self.i] < self.tab[self.i + 1]:
                    self.tab[self.i], self.tab[self.i + 1] = self.tab[self.i + 1], self.tab[self.i]

            self.i += 1
            
            self.update_screen()



class InsertionSortDisplayer(BaseSortDisplayer):
    def __init__(self, screen, tab, order):
        super().__init__(screen=screen, tab=tab, order=order, title="Insertion Sort")
        self.i = 0
        self.j = 0

    def sort(self):
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
                    print("i = ", self.i, "j = ", self.j)
            elif self.order == 'desc':
                while j > 0 and self.tab[j - 1] < x:
                    self.handle_events()
                    if self.stop_sorting or self.is_sorted:
                        break
                    self.tab[j] = self.tab[j - 1]
                    j -= 1
                    self.j = j
                    print("i = ", self.i, "j = ", self.j)
            self.tab[j] = x
            print("i = ", self.i, "j = ", self.j)
            self.update_screen()



class MergeSortDisplayer(BaseSortDisplayer):
    def __init__(self, screen, tab, order):
        super().__init__(screen=screen, tab=tab, order=order, title="Merge Sort")
        self._is_sorted = False

    @property
    def is_sorted(self):
        return self._is_sorted

    def merge(self, left, right):
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
        self.handle_events()
        if self.stop_sorting or len(tab) <= 1 or self.is_sorted:
            return tab, []  # Retourne la liste et une liste vide des paires de sous-listes à fusionner
        
        middle = len(tab) // 2
        left, left_steps = self.sort_recursive(tab[:middle])
        right, right_steps = self.sort_recursive(tab[middle:])
        steps = left_steps + right_steps + [(left, right)]
        print("steps = ", steps)
        return self.merge(left, right), steps  # Retourne la liste fusionnée et la paire de sous-listes

    def sort(self):
        self.tab, steps = self.sort_recursive(self.tab)
        self.update_screen()
        print("steps len = ", len(steps))
        # TODO : afficher les paires de sous listes à fusionner
        for i, step in enumerate(steps):
            left, right = step
            self.tab = self.merge(left, right)
            self.update_screen()
        self._is_sorted = True
        self.update_screen()



class QuickSortDisplayer(BaseSortDisplayer):
    def __init__(self, screen, tab, order):
        super().__init__(screen=screen, tab=tab, order=order, title="Quick Sort")


    def partition(self, tab, low, high):
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
        print("low = ", low, "high = ", high)
        if low < high:
            pi = self.partition(tab, low, high)
            self.update_screen()
            self.sort_recursive(tab, low, pi - 1)
            self.sort_recursive(tab, pi + 1, high)

    def sort(self):
        self.sort_recursive(self.tab, 0, len(self.tab) - 1)


class HeapSortDisplayer(BaseSortDisplayer):
    def __init__(self, screen, tab, order):
        super().__init__(screen=screen, tab=tab, order=order, title="Heap Sort")

    def heapify(self, tab, i, n):
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
    def __init__(self, screen, tab, order):
        super().__init__(screen=screen, tab=tab, order=order, title="Comb Sort")
        self.shrink_factor = 1.3

    def sort(self):
        gap = len(self.tab)
        sorted = False

        while not sorted:
            self.handle_events()
            if self.stop_sorting:
                return
            
            gap = int(gap / self.shrink_factor)
            if gap <= 1:
                gap = 1
            
            swapped = False  # Drapeau pour suivre les échanges dans cette itération
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


ALGORITHMS_DISPLAYERS = {
    'selection_sort': SelectionSortDisplayer,
    'bubble_sort': BubbleSortDisplayer,
    'insertion_sort': InsertionSortDisplayer,
    'merge_sort': MergeSortDisplayer,
    'quick_sort': QuickSortDisplayer,
    'heap_sort': HeapSortDisplayer,
    'comb_sort': CombSortDisplayer
}
