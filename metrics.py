from timeit import timeit
from fna import read_fna
from suffix_array import naive_sa, naive_sa2
from time import time
from sorts import bubble_sort, quicksort

import pandas as pd

seq, _ = read_fna("./gene.fna")

# t1 = timeit("sa = naive_sa(seq)", number=2, globals=globals())
# t2 = timeit("sa = naive_sa2(seq)", number=2, globals=globals())

# print(t1, t2)

df = pd.DataFrame(columns=["method", "len", "duration"])

for n in [10, 100, 1000]:
    print(f"Bubble sort with sequence length {n}")
    text = seq[:n]
    start = time()

    array = list(range(len(text)))

    def cmp(a, b):
        return text[a:] > text[b:]

    bubble_sort(array, cmp)
    duration = time() - start
    print(duration)
    pd.concat(df, {
        "method": "bubble sort",
        "len": n,
        "duration": duration,
    }, ignore_index=True)

for n in [10, 100, 1000, 10000]:
    print(f"Quicksort with sequence length {n}")
    text = seq[:n]
    start = time()
    
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
    duration = time() - start
    print(duration)
    df.concat({
        "method": "quicksort",
        "len": n,
        "duration": duration,
    }, ignore_index=True)

print(df)