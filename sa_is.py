# Cloning https://sites.google.com/site/yuta256/sais

mask = bytearray([0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01])

def tset(a, i, b):
    if b == 1:
        a[i // 8] =   mask[i % 8]  | a[i // 8]
    else:
        a[i // 8] = (~mask[i % 8]) & a[i // 8]


def SA_IS(s: bytearray, SA: bytearray, n: int, K: int, cs: int):
    # LS-type array packed into bits
    ls = bytearray([0] * (n // 8 + 1))
    print(ls)

    tset(ls, n - 1, 1)  # Sentinel must be S-type
    tset(ls, n - 2, 0)  # To the left of sentinel must be L-type

    for i in range(n - 3, 0, -1):
        # todo chr macro

    print(ls)



if __name__ == '__main__':
    text = b"gtcccgatgtcatgtcagga$" 
    SA_IS(text, None, len(text), 0, 0)