from typing import List
import numpy as np
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


def build_sl_types(text: bytearray):
    sl_type = [None] * len(text)

    def is_s_type(k):
        # should early return check be if k is last rather than sentinel?
        return text[k] == ord("$") or \
            text[k] < text[k+1] or \
            (text[k] == text[k+1] and sl_type[k+1] == "s")

    def is_l_type(k):
        return text[k] > text[k+1] or \
            (text[k] == text[k+1] and sl_type[k+1] == "l")

    for i in reversed(range(len(text))):
        if is_s_type(i):
            sl_type[i] = "s"
        elif is_l_type(i):
            sl_type[i] = "l"
        else:
            raise Exception("Must be S or L type suffix")

    return sl_type


def lms_from_sl_types(sl_list):
    return [i for i in range(1, len(sl_list))
            if sl_list[i-1] == 'l' and sl_list[i] == 's']


def sa_is(text: bytearray):
    sa = [' '] * len(text)

    print(f"SA-IS start...")
    print(f"Text: {'  '.join(text.decode())}")

    sl = build_sl_types(text)
    print(f"SL:   {'  '.join(sl)}")

    lms_suffixes = lms_from_sl_types(sl)
    
    lms_info = [' '] * len(text)
    for i in lms_suffixes:
        lms_info[i] = "|"
    print(f"LMS:  {'  '.join(lms_info)}")

    # todo Make sorted alphabet generation dynamic
    alphabet = {
        ord("$"): 0,
        ord("a"): 1,
        ord("c"): 2,
        ord("g"): 3,
        ord("t"): 4,
    }

    counts = np.array([0] * len(alphabet))

    for c in text:
        counts[alphabet[c]] += 1

    # Pass 1: Place the LMS suffxies at the end of their buckets
    bucket_ends = np.cumsum(counts) - 1

    for suffix in reversed(lms_suffixes):
        first_char = text[suffix]
        bucket = alphabet[first_char]
        sa[bucket_ends[bucket]] = suffix
        bucket_ends[bucket] -= 1

    print("P1:   " + ''.join([f"{s:<3}" for s in sa]))

    # Pass 2:  Place the L-type suffixes at the fronts of their buckets
    bucket_fronts = np.insert(np.cumsum(counts[:-1]), 0, 0)
    
    for i in range(len(sa)):
        if sa[i] != ' ' and sa[i] > 0 and sl[sa[i] - 1] == 'l':
            first_char = text[sa[i] - 1]
            bucket = alphabet[first_char]
            sa[bucket_fronts[bucket]] = sa[i] - 1
            bucket_fronts[bucket] += 1

    print("P2:   " + ''.join([f"{s:<3}" for s in sa]))

    # Pass 3:  Place the L-type suffixes at the fronts of their buckets
    bucket_ends = np.cumsum(counts) - 1
    
    for i in reversed(range(len(sa))):
        if sa[i] != ' ' and sa[i] > 0 and sl[sa[i] - 1] == 's':
            first_char = text[sa[i] - 1]
            bucket = alphabet[first_char]
            sa[bucket_ends[bucket]] = sa[i] - 1
            bucket_ends[bucket] -= 1

    print("P3:   " + ''.join([f"{s:<3}" for s in sa]))

    # Number the LMS blocks
    lms_blocks_ordered = [s for s in sa if s in lms_suffixes]
    
    print("lms:", lms_suffixes)

    num_blocks = len(lms_blocks_ordered)
    print("ordered:", lms_blocks_ordered)
    
    def lms_block_from_suffix(suffix):
        start = suffix
        end = start
        saw_l = False

        while text[end] != ord('$') and not (sl[end] == 's' and saw_l):
            if sl[end] == 'l':
                saw_l = True

            end += 1

        return text[start:end + 1]


    lms_block_vals = {}  # todo find a way to look these up without a dict or huge array
    i = -1
    prev_lms_block = ""

    for lms_suffix in lms_blocks_ordered:
        lms_block = lms_block_from_suffix(lms_suffix)

        if lms_block != prev_lms_block:
            i += 1

        print(f"{lms_suffix:>2} {i} {lms_block.decode()}")

        lms_block_vals[lms_suffix] = i
        prev_lms_block = lms_block

    # Build reduced string
    reduced = [lms_block_vals[suffix] for suffix in lms_suffixes]
    print("Reduced:", reduced)

    return []


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
