def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def binary_search(arr, target):
    first = 0
    last = len(arr) - 1
    result_ok = False

    while first <= last and not result_ok:
        middle = (first + last) // 2

        if arr[middle] == target:
            result_ok = True
        elif arr[middle] < target:
            first = middle + 1
        else:
            last = middle - 1

    if result_ok:
        print(f"Элемент {target} найден на позиции {middle}")
        return middle
    else:
        print(f"Элемент {target} не найден")
        return -1


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Неотсортированный список:", unsorted_list)
sorted_list = bubble_sort(unsorted_list.copy())
print("Отсортированный список:", sorted_list)


binary_search(sorted_list, 64)
