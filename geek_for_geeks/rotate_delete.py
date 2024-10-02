from collections import deque


def last_element(arr):
    """
    Returns the last element left in the array after performing the specified operations.

    :param arr: The input array of integers.
    :return: The last element left in the array.
    """
    sz = len(arr)
    start = 0
    for k in range(1, sz // 2 + 1):

        start = (start - 1) % len(arr)

        delete_index = (start + sz - k) % len(arr)

        arr.pop(delete_index)

        if delete_index <= start:
            start -= 1

        sz -= 1

    return arr[start]


# Example usage:
arr = [1, 2, 3, 4, 5, 6]
result = last_element(arr)
print(result)  # Output: 3