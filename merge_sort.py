def is_sorted_list(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False 
    return True

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Diviser le tableau en deux parties égales
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Tri récursif des sous-tableaux
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # Fusion des sous-tableaux triés
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    # Ajouter les éléments restants
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    
    return result

            
def bubble_sort(arr):
    i = 0
    while not is_sorted_list(arr):
        if i >= len(arr) -1:
            i = 0
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]  
        i += 1
    return arr

arr = [38, 27, 43, 3, 9, 82, 10]
array = [1,2,3,4,5]

print(merge_sort(arr))
print(bubble_sort(arr))