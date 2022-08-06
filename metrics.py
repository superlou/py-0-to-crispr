from timeit import timeit
from fna import read_fna
from suffix_array import naive_sa, naive_sa2, bubble_sort_sa, quicksort_sa
from time import time
from sorts import quicksort
import matplotlib.pyplot as plt
import pandas as pd


def benchmark_sa(alg, text: bytearray, n_list: list):
    name = alg.__name__
    trials = []

    for n in n_list:
        print(f"{name:15} sequence length {n:6}", end="")
        start = time()
        sa = alg(text[:n])
        duration = time() - start
        print(f" {duration:.3f} s")
        trials.append({
            "method": name,
            "len": n,
            "duration": duration,
        })

    return trials


def main():
    seq, _ = read_fna("./gene.fna")
    print(f"Sequence length: {len(seq):,}")

    # t1 = timeit("sa = naive_sa(seq)", number=2, globals=globals())
    # t2 = timeit("sa = naive_sa2(seq)", number=2, globals=globals())

    # print(t1, t2)

    trials = []
    trials += benchmark_sa(bubble_sort_sa, seq,
                           [10, 100, 250, 500, 750, 1000, 2000])
    trials += benchmark_sa(quicksort_sa, seq,
                           [10, 100, 500, 1000, 5000, 10000, 20000, 40000])

    df = pd.DataFrame(trials)

    for method, data in df.groupby("method"):
        plt.plot(data.len, data.duration, label=method)

    plt.semilogx()
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
