from pathlib import Path

import pytest

from seqtools import gc_content, read_fasta, reverse_complement

DATA = Path(__file__).parent.parent / "data"


def test_read_fasta():
    sequences = read_fasta(DATA / "example.fasta")
    assert list(sequences) == ["ins_fragment", "gapdh_fragment", "contig_7", "low_gc_region"]
    assert sequences["ins_fragment"].startswith("ATGGCCCTGTGGATGCGC")


def test_reverse_complement():
    assert reverse_complement("ATGC") == "GCAT"
    assert reverse_complement("AAACCC") == "GGGTTT"


def test_reverse_complement_twice_returns_original():
    seq = "ATGGCCCTGTGGATGCGC"
    assert reverse_complement(reverse_complement(seq)) == seq


def test_gc_content():
    assert gc_content("GGCC") == 1.0
    assert gc_content("ATAT") == 0.0
    assert gc_content("ATGC") == pytest.approx(0.5)
