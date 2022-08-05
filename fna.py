from typing import Tuple


def read_fna(filename: str) -> Tuple[bytes, str]:
    metadata = ""
    b = bytearray()

    with open(filename, "rb") as f:
        for i, line in enumerate(f.readlines()):
            if i == 0:
                metadata = line.decode().strip()
            else:
                b += bytearray(line.strip())

    return b, metadata


if __name__ == "__main__":
    seq, info = read_fna("./ncbi_dataset/data/gene.fna")
    print(info)
    print(f"Length: {len(seq):,}")
    print(f"{seq[:100].decode()}...")
