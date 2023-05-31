def binary_search(input_array, value):
    """
    Assumes the list only has distinct elements,
    meaning there are no repeated values, and
    elements are in a strictly increasing order.
    """
    value_idx = 0
    while len(input_array) > 0:
        mean_idx = len(input_array) // 2
        if input_array[mean_idx] == value:
            value_idx += mean_idx
            return value_idx
        elif input_array[mean_idx] > value:
            input_array = input_array[:mean_idx]
        else:
            value_idx += (mean_idx + 1)
            input_array = input_array[mean_idx + 1:]
    return -1



