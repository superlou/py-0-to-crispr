from sorts import bubble_sort, quicksort


def test_bubble_sort():
    array = [8, 2, 6, 4, 5]

    def cmp(a, b):
        return a > b

    bubble_sort(array, cmp)
    assert [2, 4, 5, 6, 8] == array

    text = b"banana$"
    array = list(range(len(text)))

    def cmp(a, b):
        return text[a:] > text[b:]

    bubble_sort(array, cmp)
    assert [6, 5, 3, 1, 0, 4, 2] == array


def test_quicksort():
    array = [8, 2, 6, 4, 5]

    def cmp(a, b):
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0

    result = quicksort(array, cmp)
    assert [2, 4, 5, 6, 8] == result

    text = b"banana$"
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
    assert [6, 5, 3, 1, 0, 4, 2] == result