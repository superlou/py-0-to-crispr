from timeit import timeit
from fna import read_fna
from suffix_array import naive_sa, naive_sa2, bubble_sort_sa, quicksort_sa
from time import time
from sorts import quicksort
import matplotlib.pyplot as plt

import pandas as pd

seq, _ = read_fna("./gene.fna")

# t1 = timeit("sa = naive_sa(seq)", number=2, globals=globals())
# t2 = timeit("sa = naive_sa2(seq)", number=2, globals=globals())

# print(t1, t2)

trials = []

for n in [10, 100, 500, 1000, 2000]:
    print(f"Bubble sort with sequence length {n}")
    text = seq[:n]
    start = time()

    sa = bubble_sort_sa(text)

    duration = time() - start
    print(duration)
    trials.append({
        "method": "bubble sort",
        "len": n,
        "duration": duration,
    })

for n in [10, 100, 500, 1000, 5000, 10000, 20000]:
    print(f"Quicksort with sequence length {n}")
    text = seq[:n]
    start = time()
    
    sa = quicksort_sa(text)

    duration = time() - start
    print(duration)
    trials.append({
        "method": "quicksort",
        "len": n,
        "duration": duration,
    })

df = pd.DataFrame(trials)
print(df)

for method, data in df.groupby("method"):
    plt.plot(data.len, data.duration, label=method)

plt.semilogx()
plt.legend()
plt.grid()
plt.show()