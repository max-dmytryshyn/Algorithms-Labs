import time
from datetime import timedelta


def heapify_max(array, length, i):
    max_node = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    swaps_counter = 0
    comparisons_counter = 0

    if left_child < length:
        if array[left_child] > array[max_node]:
            max_node = left_child
        comparisons_counter += 1
    comparisons_counter += 1

    if right_child < length:
        if array[right_child] > array[max_node]:
            max_node = right_child
        comparisons_counter += 1
    comparisons_counter += 1

    if max_node != i:
        array[max_node], array[i] = array[i], array[max_node]
        swaps_counter += 1
        swaps_counter_increment, comparisons_counter_increment = heapify_max(array, length, max_node)
        swaps_counter += swaps_counter_increment
        comparisons_counter += comparisons_counter_increment

    return swaps_counter, comparisons_counter


def heapify_min(array, length, i):
    min_node = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    swaps_counter = 0
    comparisons_counter = 0

    if left_child < length:
        if array[left_child] < array[min_node]:
            min_node = left_child
        comparisons_counter += 1
    comparisons_counter += 1

    if right_child < length:
        if array[right_child] < array[min_node]:
            min_node = right_child
        comparisons_counter += 1
    comparisons_counter += 1

    if min_node != i:
        array[min_node], array[i] = array[i], array[min_node]
        swaps_counter += 1
        swaps_counter_increment, comparisons_counter_increment = heapify_min(array, length, min_node)
        swaps_counter += swaps_counter_increment
        comparisons_counter += comparisons_counter_increment

    return swaps_counter, comparisons_counter


def heap_sort(input_array, sort_order="asc"):
    start_time = time.monotonic()
    swaps_counter = 0
    comparisons_counter = 0

    length = len(input_array)
    last_parent_node = length // 2 - 1

    if sort_order == "asc":
        for node in range(last_parent_node, -1, -1):
            swaps_counter_increment, comparisons_counter_increment = heapify_max(input_array, length, node)
            swaps_counter += swaps_counter_increment
            comparisons_counter += comparisons_counter_increment

        for node in range(length - 1, 0, -1):
            input_array[node], input_array[0] = input_array[0], input_array[node]
            swaps_counter += 1
            swaps_counter_increment, comparisons_counter_increment = heapify_max(input_array, node, 0)
            swaps_counter += swaps_counter_increment
            comparisons_counter += comparisons_counter_increment

    elif sort_order == "desc":
        for node in range(last_parent_node, -1, -1):
            swaps_counter_increment, comparisons_counter_increment = heapify_min(input_array, length, node)
            swaps_counter += swaps_counter_increment
            comparisons_counter += comparisons_counter_increment

        for node in range(length - 1, 0, -1):
            input_array[node], input_array[0] = input_array[0], input_array[node]
            swaps_counter += 1
            swaps_counter_increment, comparisons_counter_increment = heapify_min(input_array, node, 0)
            swaps_counter += swaps_counter_increment
            comparisons_counter += comparisons_counter_increment

    else:
        print("Wrong sort order")

    execution_time = timedelta(seconds=time.monotonic() - start_time)
    print("Heap Sort:")
    print("Execution time:", execution_time.microseconds, "μs")
    print("Comparisons:", comparisons_counter)
    print("Swaps:", swaps_counter)
