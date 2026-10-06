# seqtools

A small Python script for working with DNA sequences, used in the AI Fluency for Biologists workshop to practice reviewing changes made by a coding agent. Not meant as a real tool.

It reads a FASTA file and reports the length and GC content of each sequence. It uses only the Python standard library.

## Setup

You need Python 3.9 or later and git.

```bash
# Put the folder under version control so you can review every change
cd seqtools
git init
git add .
git commit -m "Starting point"

# Install pytest to run the tests
python3 -m pip install -r requirements.txt
```

Check that everything works:

```bash
python3 seqtools.py data/example.fasta
python3 -m pytest
```

## Files

- `seqtools.py`: the functions `read_fasta`, `reverse_complement`, and `gc_content`, plus a command-line entry point
- `tests/test_seqtools.py`: tests for each function
- `data/example.fasta`: four short sequences
    - `ins_fragment`: the first 90 bases of the human insulin coding sequence (NM_000207.3)
    - `gapdh_fragment`: the first 90 bases of the human GAPDH coding sequence (NM_002046.7), in lowercase
    - `contig_7`: an invented assembly contig that contains runs of N
    - `low_gc_region`: an invented AT-rich sequence

## Tasks to try with a coding agent

Do each task the same way:

1. Commit, so the agent starts from a clean state.
2. Ask the agent to make a plan before it changes anything. Read the plan and correct it.
3. Let the agent make the change.
4. Read the diff in your IDE or with `git diff`. Make sure you understand every line.
5. Run the tests.
6. Commit the change if you accept it. Run `git restore .` to discard it.

### Task 1: Add a translate function

> Add a function that translates a DNA sequence into a protein sequence.

Questions to answer from the plan and the diff:

- Did the agent add a new dependency? Do you want one?
- What happens when the sequence length is not a multiple of 3?
- What happens at a stop codon?
- Did the agent add tests?

### Task 2: Handle lowercase letters and N

> Make reverse_complement work on lowercase sequences and on sequences that contain N.

Try `reverse_complement` on `gapdh_fragment` before you start, to see the current behavior.

- Should the output keep the input's case?
- Which other characters might appear in a real FASTA file?

### Task 3: Check the GC content of contig_7

> The GC content for contig_7 looks too low. Fix it.

- What decision did the agent make about N?
- Did it ask you, or decide on its own?
- Would a colleague in your field make the same decision?

The agent can make the code do what you ask. It cannot tell you whether that is the right choice for your analysis. If you are not sure, learn how the analysis is usually done or ask an expert to review it.
