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

# Exemple d'utilisation
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)