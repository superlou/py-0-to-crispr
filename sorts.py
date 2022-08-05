# https://realpython.com/sorting-algorithms-python/
from random import randint


def bubble_sort(array, cmp):
    # cmp must return true if the first parameter is larger than the second

    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if cmp(array[j], array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False

        if already_sorted:
            break

def quicksort(array, cmp):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        comparison = cmp(item, pivot)

        if comparison < 0:
            low.append(item)
        elif comparison == 0:
            same.append(item)
        elif comparison > 0:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low, cmp) + same + quicksort(high, cmp)