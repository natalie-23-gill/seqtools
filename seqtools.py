"""Small tools for working with DNA sequences."""

import sys

COMPLEMENT = {"A": "T", "T": "A", "G": "C", "C": "G"}


def read_fasta(path):
    """Read a FASTA file and return a dict of {name: sequence}."""
    sequences = {}
    name = None
    with open(path) as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                name = line[1:].split()[0]
                sequences[name] = ""
            else:
                sequences[name] += line
    return sequences


def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    return "".join(COMPLEMENT[base] for base in reversed(seq))


def gc_content(seq):
    """Return the fraction of bases in a sequence that are G or C."""
    seq = seq.upper()
    gc = seq.count("G") + seq.count("C")
    return gc / len(seq)


def main():
    if len(sys.argv) != 2:
        print("Usage: python seqtools.py <file.fasta>")
        sys.exit(1)
    sequences = read_fasta(sys.argv[1])
    print("name\tlength\tgc_content")
    for name, seq in sequences.items():
        print(f"{name}\t{len(seq)}\t{gc_content(seq):.3f}")


if __name__ == "__main__":
    main()
