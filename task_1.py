import timeit
import random

# Алгоритм сортування вставками
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

# Алгоритм сортування злиттям
def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1
    return lst

# Timsort (вбудований в Python алгоритм сортування)
def tim_sort(lst):
    return sorted(lst)

# Генерація випадкового списку
def generate_random_list(size):
    return [random.randint(0, size) for _ in range(size)]

# Вимірювання часу виконання для кожного алгоритму
def measure_time(sort_func, lst):
    return timeit.timeit(lambda: sort_func(lst.copy()), number=1)

# Основна функція для тестування
def compare_sorting_algorithms():
    sizes = [100, 1000, 10000]  # Різні розміри масивів для тестування
    for size in sizes:
        lst = generate_random_list(size)
        print(f"Розмір масиву: {size}")
        
        time_insertion = measure_time(insertion_sort, lst)
        print(f"Сортування вставками: {time_insertion:.6f} секунд")

        time_merge = measure_time(merge_sort, lst)
        print(f"Сортування злиттям: {time_merge:.6f} секунд")

        time_tim = measure_time(tim_sort, lst)
        print(f"Timsort: {time_tim:.6f} секунд")
        print("")

compare_sorting_algorithms()

# Пояснення
# Сортування вставками (Insertion Sort): Проста реалізація алгоритму сортування вставками.
# Сортування злиттям (Merge Sort): Реалізація рекурсивного алгоритму сортування злиттям.
# Timsort: Використання вбудованої функції sorted в Python, яка реалізує Timsort.
# Генерація випадкових списків: Для тестування алгоритмів сортування на різних наборах даних.
# Вимірювання часу виконання: Використання модуля timeit для вимірювання часу виконання кожного 
# алгоритму на кожному наборі даних.
# Висновок
# Після виконання цих тестів ви побачите, що Timsort зазвичай набагато швидший на практиці 
# завдяки поєднанню сортування злиттям та сортування вставками, особливо на великих наборах 
# даних. Це і є причина, чому вбудовані функції сортування в Python є надзвичайно ефективними.