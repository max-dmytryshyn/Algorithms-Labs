def heapify_max(array, length, i):
    max_node = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < length and array[left_child] > array[max_node]:
        max_node = left_child

    if right_child < length and array[right_child] > array[max_node]:
        max_node = right_child

    if max_node != i:
        array[max_node], array[i] = array[i], array[max_node]
        heapify_max(array, length, max_node)


def heapify_min(array, length, i):
    min_node = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < length and array[left_child] < array[min_node]:
        min_node = left_child

    if right_child < length and array[right_child] < array[min_node]:
        min_node = right_child

    if min_node != i:
        array[min_node], array[i] = array[i], array[min_node]
        heapify_min(array, length, min_node)


def heap_sort(input_array, sort_order="asc"):
    length = len(input_array)
    last_parent_node = length // 2 - 1

    if sort_order == "asc":
        for node in range(last_parent_node, -1, -1):
            heapify_max(input_array, length, node)

        for node in range(length - 1, 0, -1):
            input_array[node], input_array[0] = input_array[0], input_array[node]
            heapify_max(input_array, node, 0)

    elif sort_order == "desc":
        for node in range(last_parent_node, -1, -1):
            heapify_min(input_array, length, node)

        for node in range(length - 1, 0, -1):
            input_array[node], input_array[0] = input_array[0], input_array[node]
            heapify_min(input_array, node, 0)

    else:
        print("Wrong sort order")
