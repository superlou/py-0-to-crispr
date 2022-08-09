from suffix_array import naive_sa, naive_sa2, sa_search
from suffix_array import bubble_sort_sa, quicksort_sa, sa_is
from suffix_array import build_sl_types


def test_naive_sa():
    text = b"banana$"
    sa = naive_sa(text)
    assert [6, 5, 3, 1, 0, 4, 2] == sa


def test_naive_sa2():
    text = b"banana$"
    sa = naive_sa2(text)
    assert [6, 5, 3, 1, 0, 4, 2] == sa

    sa = naive_sa(b"gtcccgatgtcatgtcagga$")
    assert [20, 19, 16, 11, 6, 15, 10, 2, 3, 4,
            18, 5, 17, 13, 8, 0, 14, 9, 1, 12, 7] == sa


def test_sa_search():
    text = b"This is some text that has repeated fiscally$"
    sa = naive_sa2(text)
    assert [2, 5, 37] == sa_search(b"is", text, sa)


def test_build_sl_types():
    sl = build_sl_types(b"gtcccgatgtcatgtcagga$")
    assert [c for c in "slssslslsllslsllsllls"] == sl


def test_sa_is():
    sa = sa_is(b"gtcccgatgtcatgtcagga$")
    assert [20, 19, 16, 11, 6, 15, 10, 2, 3, 4,
            18, 5, 17, 13, 8, 0, 14, 9, 1, 12, 7] == sa