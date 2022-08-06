from typing import List
from fna import read_fna
from sorts import bubble_sort, quicksort


def naive_sa(text: bytearray):
    """
    Very naive suffix array builder that builds a table of
    index-suffix tuples.
    """
    table = [(i, text[i:]) for i in range(len(text))]
    table.sort(key=lambda x: x[1])
    return [x[0] for x in table]


def naive_sa2(text: bytearray):
    """
    Less space naive version that doesn't build a table
    that has a size based on the text length.
    """
    a = list(range(len(text)))
    a.sort(key=lambda x: text[x:])
    return a


def bubble_sort_sa(text: bytearray):
    array = list(range(len(text)))

    def cmp(a, b):
        return text[a:] > text[b:]

    bubble_sort(array, cmp) 

    return array


def quicksort_sa(text: bytearray):
    array = list(range(len(text)))

    def cmp(a, b):
        a = text[a:]
        b = text[b:]

        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0

    result = quicksort(array, cmp)
    return result


def sa_search(query: bytes, text: bytes, sa) -> List[int]:
    def suffix_at(n):
        return text[sa[n]:]

    # Find starting of interval in SA
    left = 0
    right = len(text)

    while left < right:
        mid = (left + right) // 2
        if query > suffix_at(mid):
            left = mid + 1
        else:
            right = mid

    start = left

    # Find end of interval in SA
    # Wikipedia says it should be inclusive, but doesn't appear that way
    right = len(text)

    while left < right:
        mid = (left + right) // 2
        if suffix_at(mid).startswith(query):
            left = mid + 1
        else:
            right = mid

    return [sa[i] for i in range(start, right)]
