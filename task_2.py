# Реалізація функції merge_k_lists для злиття k відсортованих списків в один.

import heapq

def merge_k_lists(lists):
    merged_list = []
    min_heap = []

    # Ініціалізація heap з першими елементами кожного списку
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i][0], i, 0))

    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(val)
        
        # Додаємо наступний елемент з цього списку до heap
        if element_idx + 1 < len(lists[list_idx]):
            heapq.heappush(min_heap, (lists[list_idx][element_idx + 1], list_idx, element_idx + 1))
    
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
